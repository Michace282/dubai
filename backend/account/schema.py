import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType
from backend.mixin import DjangoModelFormMutation
from graphql_jwt.decorators import login_required
import graphql_social_auth
import graphql_jwt
from .forms import SubscribeForm, ContactForm, Guest, Profile
from django.contrib.auth.models import User
from django import forms


class UserType(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node,)


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        interfaces = (graphene.relay.Node,)


class GuestType(DjangoObjectType):
    class Meta:
        model = Guest
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    user = graphene.Field(UserType)
    guest_detail = graphene.Field(GuestType, uuid=graphene.String())

    @login_required
    def resolve_user(self, info, **Nodekwargs):
        return info.context.user

    def resolve_guest_detail(self, info, uuid):
        return Guest.objects.filter(uuid=uuid).first()


class GuestCreateMutation(graphene.Mutation):
    guest = graphene.Field(GuestType)

    @classmethod
    def mutate(cls, root, info):
        return GuestCreateMutation(guest=Guest.objects.create())


class SubscribeCreateMutation(DjangoModelFormMutation):
    class Meta:
        form_class = SubscribeForm


class ContactCreateMutation(DjangoModelFormMutation):
    class Meta:
        form_class = ContactForm


class RefreshJSONWebToken(graphql_jwt.Refresh):
    user = graphene.Field(UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        if info.context.user.is_authenticated:
            return cls(user=info.context.user)
        return cls()


class RegistrationForm(forms.ModelForm):
    guest_uuid = forms.UUIDField(required=False)
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    password_repeat = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'password_repeat', 'guest_uuid')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        password_repeat = cleaned_data.get("password_repeat")
        guest_uuid = cleaned_data.get("guest_uuid")

        if password != password_repeat:
            self.add_error('password_repeat', "Пароли не совпадают")

        if User.objects.filter(username=email).exists():
            self.add_error('email', "Такой аккаунт существует")

        if guest_uuid:
            if not Guest.objects.filter(uuid=guest_uuid).exists():
                self.add_error('guest_uuid', "Такого гостя не существует")

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        cleaned_data = dict([(k, v) for k, v in self.cleaned_data.items() if v != ""])
        instance.username = cleaned_data.get('email')
        instance.email = cleaned_data.get('email')
        instance.first_name = cleaned_data.get('name')

        if commit:
            instance.set_password(instance.password)
            instance.save()

            guest_uuid = cleaned_data.get('guest_uuid')

            if guest_uuid:
                guest = Guest.objects.filter(uuid=guest_uuid).first()
                if guest:
                    for productwishlist in guest.productwishlist_set.all():
                        productwishlist.user = instance
                        productwishlist.save()

                    for feedback in guest.feedback_set.all():
                        feedback.user = instance
                        feedback.save()

                    for basket in guest.basket_set.all():
                        basket.user = instance
                        basket.save()

                    guest.delete()

        return instance


class RegistrationMutation(DjangoModelFormMutation):
    user = graphene.Field(UserType)

    class Meta:
        form_class = RegistrationForm


from graphql_jwt.decorators import token_auth


class Test(graphql_jwt.ObtainJSONWebToken):
    user = graphene.Field(UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        user = None
        if info.context.user.is_authenticated:
            user = info.context.user
        return cls(user=user)

    @classmethod
    @token_auth
    def mutate(cls, root, info, **kwargs):
        return cls.resolve(root, info, **kwargs)


class Mutation(graphene.ObjectType):
    guest_create = GuestCreateMutation.Field()
    token_auth = Test.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = RefreshJSONWebToken.Field()
    social_auth = graphql_social_auth.relay.SocialAuthJWT.Field()
    registration = RegistrationMutation.Field()
    # subscribe_create = SubscribeCreateMutation.Field()
    # contact_create = ContactCreateMutation.Field()

import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType
from backend.mixin import DjangoModelFormMutation
from .forms import SubscribeForm, ContactForm, Guest


class GuestType(DjangoObjectType):
    class Meta:
        model = Guest
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    guest_detail = graphene.Field(GuestType, uuid=graphene.String())

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


class Mutation(graphene.ObjectType):
    guest_create = GuestCreateMutation.Field()
    # subscribe_create = SubscribeCreateMutation.Field()
    # contact_create = ContactCreateMutation.Field()

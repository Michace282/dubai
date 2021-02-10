import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django import DjangoConnectionField
from graphene_django.filter import GlobalIDFilter, GlobalIDMultipleChoiceFilter
from graphene_django.types import DjangoObjectType, ErrorType
from graphql_relay.connection.arrayconnection import offset_to_cursor
from graphql_relay import from_global_id
import django_filters
from .models import *
from account.models import Code, UseCode
import math
from django import forms
from backend.mixin import DjangoModelFormMutation, ClientIDMutation
from django.conf import settings
from image_cropping.fields import ImageCropField
from graphene_django.forms.converter import convert_form_field
from graphene_django.converter import convert_django_field
from graphene_file_upload.scalars import Upload
from django.db import models


class FileUploadField(forms.FileField):
    pass


@convert_form_field.register(FileUploadField)
def convert_form_field_to_upload(field):
    return Upload()


class FileUploadsField(forms.FileField):
    pass


@convert_form_field.register(FileUploadsField)
def convert_form_field_to_uploads(field):
    return graphene.List(Upload)


class ImageGraphene(graphene.Scalar):
    @staticmethod
    def coerce_float(value):
        try:
            return settings.BACKEND_URL + 'media/' + str(value)
        except ValueError:
            return None

    serialize = coerce_float
    parse_value = coerce_float

    @staticmethod
    def parse_literal(ast):
        return ast.value


@convert_django_field.register(ImageCropField)
@convert_django_field.register(models.ImageField)
@convert_django_field.register(models.FileField)
@convert_django_field.register(models.FilePathField)
def convert_image_to_full_image(field, registry=None):
    return ImageGraphene(description=field.help_text, required=not field.null)


class PagesCursor(graphene.ObjectType):
    start_cursor = graphene.String()
    end_cursor = graphene.String()
    cursor = graphene.String()


class ProductImageType(DjangoObjectType):
    class Meta:
        model = ProductImage
        interfaces = (relay.Node,)


class SizeType(DjangoObjectType):
    class Meta:
        model = Size
        interfaces = (relay.Node,)


class SizeChartType(DjangoObjectType):
    class Meta:
        model = SizeChart
        interfaces = (relay.Node,)


class ColorType(DjangoObjectType):
    class Meta:
        model = Color
        interfaces = (relay.Node,)


class ProductSizeColorType(DjangoObjectType):
    class Meta:
        model = ProductSizeColor
        interfaces = (relay.Node,)


class ProductSizeColorType(DjangoObjectType):
    class Meta:
        model = ProductSizeColor
        interfaces = (relay.Node,)


class ProductConnection(graphene.Connection):
    class Meta:
        abstract = True

    colors_available = graphene.List(ColorType)
    sizes_available = graphene.List(SizeType)

    total_count = graphene.Int()
    edge_count = graphene.Int()

    pages_cursor = graphene.List(PagesCursor)
    pages_cursor_count = graphene.Int()

    def resolve_colors_available(self, info, **kwargs):
        params = info.variable_values
        product_type = params.get('product_type', None)
        ladies_type = params.get('ladies_type', None)
        mens_type = params.get('mens_type', None)
        accessories_type = params.get('accessories_type', None)
        dance_shoes_type = params.get('dance_shoes_type', None)

        options = {}

        if product_type:
            options['productsizecolor__product__product_type'] = product_type

        if ladies_type:
            options['productsizecolor__product__ladies_type'] = ladies_type

        if mens_type:
            options['productsizecolor__product__mens_type'] = mens_type

        if accessories_type:
            options['productsizecolor__product__accessories_type'] = accessories_type

        if dance_shoes_type:
            options['productsizecolor__product__dance_shoes_type'] = dance_shoes_type

        return Color.objects.filter(**options).distinct()

    def resolve_sizes_available(self, info, **kwargs):
        params = info.variable_values
        product_type = params.get('product_type', None)
        ladies_type = params.get('ladies_type', None)
        mens_type = params.get('mens_type', None)
        accessories_type = params.get('accessories_type', None)
        dance_shoes_type = params.get('dance_shoes_type', None)

        options = {}

        if product_type:
            options['productsizecolor__product__product_type'] = product_type

        if ladies_type:
            options['productsizecolor__product__ladies_type'] = ladies_type

        if mens_type:
            options['productsizecolor__product__mens_type'] = mens_type

        if accessories_type:
            options['productsizecolor__product__accessories_type'] = accessories_type

        if dance_shoes_type:
            options['productsizecolor__product__dance_shoes_type'] = dance_shoes_type

        return Size.objects.filter(**options).distinct()

    def resolve_pages_cursor(self, info, **kwargs):
        params = info.variable_values
        first = params.get('first', 100)
        count_page = math.ceil(self.length / first)

        pages_cursor = []

        for i in range(count_page):
            cursor = i * first - 1
            if cursor < 0:
                cursor = 0
            pages_cursor.append(
                PagesCursor(start_cursor=offset_to_cursor(i * first),
                            end_cursor=offset_to_cursor((i + 1) * first - 1),
                            cursor=offset_to_cursor(cursor)))

        return pages_cursor

    def resolve_pages_cursor_count(self, info, **kwargs):
        params = info.variable_values
        first = params.get('first', 100)
        count_page = math.ceil(self.length / first)
        return count_page

    def resolve_total_count(self, info, **kwargs):
        return self.length

    def resolve_edge_count(self, info, **kwargs):
        return len(self.edges)


class ProductType(DjangoObjectType):
    is_wishlist = graphene.Boolean()
    avg_feedback = graphene.Float()
    count_feedback_star1 = graphene.Int()
    count_feedback_star2 = graphene.Int()
    count_feedback_star3 = graphene.Int()
    count_feedback_star4 = graphene.Int()
    count_feedback_star5 = graphene.Int()
    count_feedback = graphene.Int()

    def resolve_is_wishlist(self, info):
        user = info.context.user
        if user.is_authenticated:
            return ProductWishlist.objects.filter(product=self, user=user).exists()
        else:
            params = info.variable_values
            guest_uuid = params.get('guestUuid', None)
            if guest_uuid:
                return ProductWishlist.objects.filter(product=self, guest__uuid=guest_uuid).exists()
        return False

    def resolve_avg_feedback(self, info):
        star = self.feedback_set.filter(status=Feedback.StatusType.published).aggregate(
            models.Avg('star'))
        avg_star = star.get('star__avg', 0)
        return avg_star if avg_star is not None else 0

    def resolve_count_feedback_star1(self, info):
        return self.feedback_set.filter(status=Feedback.StatusType.published, star=Feedback.StarType.star1).count()

    def resolve_count_feedback_star2(self, info):
        return self.feedback_set.filter(status=Feedback.StatusType.published, star=Feedback.StarType.star2).count()

    def resolve_count_feedback_star3(self, info):
        return self.feedback_set.filter(status=Feedback.StatusType.published, star=Feedback.StarType.star3).count()

    def resolve_count_feedback_star4(self, info):
        return self.feedback_set.filter(status=Feedback.StatusType.published, star=Feedback.StarType.star4).count()

    def resolve_count_feedback_star5(self, info):
        return self.feedback_set.filter(status=Feedback.StatusType.published, star=Feedback.StarType.star5).count()

    def resolve_count_feedback(self, info):
        return self.feedback_set.filter(status=Feedback.StatusType.published).count()

    class Meta:
        model = Product
        interfaces = (relay.Node,)
        connection_class = ProductConnection


class ProductFilter(django_filters.FilterSet):
    price__gte = django_filters.NumberFilter(label='После цены', method='price__gte_filter')
    price__lte = django_filters.NumberFilter(label='До цены', method='price__lte_filter')

    colors = GlobalIDMultipleChoiceFilter(method='colors_filter')
    sizes = GlobalIDMultipleChoiceFilter(method='sizes_filter')

    guest_uuid = django_filters.UUIDFilter(method='guest_uuid_filter')

    ids = GlobalIDMultipleChoiceFilter(method='ids_filter')
    exclude_id = GlobalIDFilter(method='exclude_id_filter')

    def price__gte_filter(self, queryset, name, value):
        return queryset.filter(price__gte=value)

    def price__lte_filter(self, queryset, name, value):
        return queryset.filter(price__lte=value)

    def colors_filter(self, queryset, name, value):
        ids = []
        for v in value:
            ids.append(from_global_id(v)[1])

        return queryset.filter(productsizecolor__color__in=ids)

    def sizes_filter(self, queryset, name, value):
        ids = []
        for v in value:
            ids.append(from_global_id(v)[1])

        return queryset.filter(productsizecolor__sizes__in=ids)

    def guest_uuid_filter(self, queryset, name, value):
        return queryset

    def exclude_id_filter(self, queryset, name, value):
        return queryset.exclude(id=from_global_id(value)[1])

    def ids_filter(self, queryset, name, value):
        ids = []
        for v in value:
            ids.append(from_global_id(v)[1])

        return queryset.filter(id__in=ids)

    class Meta:
        model = Product
        fields = ['price__gte', 'price__lte', 'product_type', 'ladies_type', 'mens_type', 'accessories_type',
                  'dance_shoes_type', 'colors', 'sizes']

    @property
    def qs(self):
        return super().qs.filter(status=Product.StatusType.published,
                                 productsizecolor__is_available=True).distinct()


class ProductWishlistConnection(graphene.Connection):
    class Meta:
        abstract = True

    total_count = graphene.Int()
    edge_count = graphene.Int()

    pages_cursor = graphene.List(PagesCursor)
    pages_cursor_count = graphene.Int()

    def resolve_pages_cursor(self, info, **kwargs):
        params = info.variable_values
        first = params.get('first', 100)
        count_page = math.ceil(self.length / first)

        pages_cursor = []

        for i in range(count_page):
            cursor = i * first - 1
            if cursor < 0:
                cursor = 0
            pages_cursor.append(
                PagesCursor(start_cursor=offset_to_cursor(i * first),
                            end_cursor=offset_to_cursor((i + 1) * first - 1),
                            cursor=offset_to_cursor(cursor)))

        return pages_cursor

    def resolve_pages_cursor_count(self, info, **kwargs):
        params = info.variable_values
        first = params.get('first', 100)
        count_page = math.ceil(self.length / first)
        return count_page

    def resolve_total_count(self, info, **kwargs):
        return self.length

    def resolve_edge_count(self, info, **kwargs):
        return len(self.edges)


class ProductWishlistType(DjangoObjectType):
    class Meta:
        model = ProductWishlist
        interfaces = (relay.Node,)
        connection_class = ProductWishlistConnection


class ProductWishlistFilter(django_filters.FilterSet):
    guest_uuid = django_filters.UUIDFilter(method='guest_uuid_filter')

    def guest_uuid_filter(self, queryset, name, value):
        return queryset.filter(guest__uuid=value)

    class Meta:
        model = ProductWishlist
        fields = ['guest_uuid']


class FeedbackType(DjangoObjectType):
    class Meta:
        model = Feedback
        interfaces = (relay.Node,)


class FeedbackFilter(django_filters.FilterSet):
    class Meta:
        model = Feedback
        fields = ['product']

    @property
    def qs(self):
        return super().qs.filter(status=Feedback.StatusType.published).distinct()


class FeedbackImageType(DjangoObjectType):
    class Meta:
        model = FeedbackImage
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    product_list = DjangoFilterConnectionField(ProductType, filterset_class=ProductFilter)
    product_detail = graphene.relay.Node.Field(ProductType, id=graphene.ID())

    product_wishlist_list = DjangoFilterConnectionField(ProductWishlistType, filterset_class=ProductWishlistFilter)

    feedback_list = DjangoFilterConnectionField(FeedbackType, filterset_class=FeedbackFilter)

    def resolve_product_wishlist_list(self, info, **kwargs):
        if 'guest_uuid' in kwargs:
            return ProductWishlistFilter(kwargs).qs
        else:
            user = info.context.user
            if user.is_authenticated:
                return ProductWishlistFilter(kwargs).qs.filter(user=user)
        return []


class ProductWishlistCreateForm(forms.ModelForm):
    guest_uuid = forms.UUIDField(required=False)

    class Meta:
        model = ProductWishlist
        fields = ('guest_uuid', 'product',)

    def clean(self):
        cleaned_data = super().clean()
        guest_uuid = cleaned_data.get("guest_uuid")

        if guest_uuid:
            if not Guest.objects.filter(uuid=guest_uuid).exists():
                self.add_error('guest_uuid', "Такого гостя не существует")

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        return instance


class ProductWishlistCreateMutation(DjangoModelFormMutation):
    @classmethod
    def perform_mutate(cls, form, info):
        kwargs = {}
        errors = []
        user = info.context.user
        obj = form.save(commit=False)
        guest_uuid = form.cleaned_data.get('guest_uuid')

        if user.is_authenticated:
            if ProductWishlist.objects.filter(product=obj.product, user=user).exists():
                errors.append(ErrorType(field='product', messages=['Этот продукт уже добавлен в избранное']))
            else:
                obj.user = user
                obj.save()
                kwargs = {cls._meta.return_field_name: obj}
        else:
            if guest_uuid:
                guest = Guest.objects.filter(uuid=guest_uuid).first()
                if guest:
                    if ProductWishlist.objects.filter(product=obj.product, guest=guest).exists():
                        errors.append(ErrorType(field='product', messages=['Этот продукт уже добавлен в избранное']))
                    else:
                        obj.guest = guest
                        obj.save()
                        kwargs = {cls._meta.return_field_name: obj}
                else:
                    errors.append(ErrorType(field='user', messages=['Такого гостя не существует']))
            else:
                errors.append(ErrorType(field='user', messages=['Вы не авторизованы']))

        return cls(errors=errors, **kwargs)

    class Meta:
        form_class = ProductWishlistCreateForm


class ProductWishlistDeleteMutation(ClientIDMutation):
    class Input:
        product = graphene.GlobalID(required=True)
        guest_uuid = graphene.UUID(required=False)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        guest_uuid = input.get('guest_uuid')
        product_id = input.get('product')

        errors = []
        user = info.context.user

        if product_id:
            product = Product.objects.filter(id=from_global_id(product_id)[1]).first()

            if product:
                if user.is_authenticated:
                    if not ProductWishlist.objects.filter(product=product, user=user).exists():
                        errors.append(ErrorType(field='product', messages=['Такого продукта нет в избранном']))
                    else:
                        ProductWishlist.objects.filter(product=product, user=user).delete()
                else:
                    if guest_uuid:
                        guest = Guest.objects.filter(uuid=guest_uuid).first()
                        if guest:
                            if not ProductWishlist.objects.filter(product=product, guest=guest).exists():
                                errors.append(ErrorType(field='product', messages=['Такого продукта нет в избранном']))
                            else:
                                ProductWishlist.objects.filter(product=product, guest=guest).delete()
                        else:
                            errors.append(ErrorType(field='user', messages=['Такого гостя не существует']))
                    else:
                        errors.append(ErrorType(field='user', messages=['Вы не авторизованы']))
            else:
                errors.append(ErrorType(field='id', messages=['Такого продукта не существует']))

        return ProductWishlistDeleteMutation(errors=errors)


class FeedbackCreateForm(forms.ModelForm):
    images = FileUploadsField(required=False)

    def save(self, commit=True):
        instance = super().save(commit=False)
        cleaned_data = dict([(k, v) for k, v in self.cleaned_data.items() if v != ""])
        return instance

    class Meta:
        model = Feedback
        fields = ('star', 'product', 'size', 'color', 'text')


class FeedbackCreateMutation(DjangoModelFormMutation):
    @classmethod
    def perform_mutate(cls, form, info):
        kwargs = {}
        errors = []
        user = info.context.user
        obj = form.save(commit=False)

        if user.is_authenticated:
            print(info.context.FILES)

            obj.user = user
            obj.save()
            kwargs = {cls._meta.return_field_name: obj}
        else:
            errors.append(ErrorType(field='user', messages=['Вы не авторизованы']))

        return cls(errors=errors, **kwargs)

    class Meta:
        form_class = FeedbackCreateForm


class ProductsBasketCreateInput(graphene.InputObjectType):
    product = graphene.GlobalID()
    color = graphene.GlobalID()
    size = graphene.GlobalID()
    count = graphene.Int()


class BasketCreateMutation(ClientIDMutation):
    class Input:
        code = graphene.String(required=False)
        guest_uuid = graphene.UUID(required=False)
        products_basket = graphene.List(ProductsBasketCreateInput)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):

        guest_uuid = input.get('guest_uuid')
        products_basket = input.get('products_basket')
        code = input.get('code')

        errors = []
        user = info.context.user
        guest = None

        if not user.is_authenticated:
            if guest_uuid:
                guest = Guest.objects.filter(uuid=guest_uuid).first()
                if not guest:
                    errors.append(ErrorType(field='user', messages=['Такого гостя не существует']))
            else:
                errors.append(ErrorType(field='user', messages=['Вы не авторизованы']))

        if not products_basket or len(products_basket) == 0:
            errors.append(ErrorType(field='products_basket', messages=['Вы ничего не выбрали']))
        else:
            total_price = 0
            for product_basket in products_basket:
                product = Product.objects.filter(id=from_global_id(product_basket.product)[1]).first()

                if product:
                    total_price += product_basket.count * product.price

        if code:
            c = Code.objects.filter(code=code, status=Code.StatusType.published).first()
            if c:
                if c.count <= c.count_use_code():
                    errors.append(ErrorType(field='code', messages=['Количество кодов кончилось']))
                else:
                    if c.min_price > total_price:
                        errors.append(ErrorType(field='code', messages=[
                            'Для акцтивации кода нужно набрать на ' + str(
                                c.min_price) + ' AED или больше. Сейчас у вас на ' + str(total_price) + ' AED']))

            else:
                errors.append(ErrorType(field='code', messages=['Такого кода нет']))

        if len(errors) == 0:
            basket = Basket()

            c = Code.objects.filter(code=code, status=Code.StatusType.published).first()

            if c:
                basket.code = c
                basket.discount = c.discount

                use_code = UseCode()
                use_code.code = c

                if guest:
                    use_code.guest = guest

                if user.is_authenticated:
                    use_code.user = user

                use_code.save()

            if guest:
                basket.guest = guest

            if user.is_authenticated:
                basket.user = user

            basket.save()

            for product_basket in products_basket:
                product = Product.objects.filter(id=from_global_id(product_basket.product)[1]).first()
                color = Color.objects.filter(id=from_global_id(product_basket.color)[1]).first()
                size = Size.objects.filter(id=from_global_id(product_basket.size)[1]).first()
                if product and color and size and product_basket.count > 0:
                    ProductBasket.objects.create(basket=basket,
                                                 product=product,
                                                 size=size,
                                                 color=color,
                                                 price=product.price,
                                                 count=product_basket.count)

        return BasketCreateMutation(errors=errors)


class Mutation(graphene.ObjectType):
    product_wishlist_create = ProductWishlistCreateMutation.Field()
    product_wishlist_delete = ProductWishlistDeleteMutation.Field()

    feedback_create = FeedbackCreateMutation.Field()

    basket_create = BasketCreateMutation.Field()

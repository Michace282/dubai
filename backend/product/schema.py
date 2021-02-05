import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django import DjangoConnectionField
from graphene_django.filter import GlobalIDFilter, GlobalIDMultipleChoiceFilter
from graphene_django.types import DjangoObjectType
from graphql_relay.connection.arrayconnection import offset_to_cursor
from graphql_relay import from_global_id
import django_filters
from .models import *
import math

from django.conf import settings
from image_cropping.fields import ImageCropField
from graphene_django.converter import convert_django_field
from django.db import models


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
    class Meta:
        model = Product
        interfaces = (relay.Node,)
        connection_class = ProductConnection


class ProductFilter(django_filters.FilterSet):
    price__gte = django_filters.NumberFilter(label='После цены', method='price__gte_filter')
    price__lte = django_filters.NumberFilter(label='До цены', method='price__lte_filter')

    colors = GlobalIDMultipleChoiceFilter(method='colors_filter')
    sizes = GlobalIDMultipleChoiceFilter(method='sizes_filter')

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

    class Meta:
        model = Product
        fields = ['price__gte', 'price__lte', 'product_type', 'ladies_type', 'mens_type', 'accessories_type',
                  'dance_shoes_type', 'colors', 'sizes']

    @property
    def qs(self):
        return super().qs.filter(status=Product.StatusType.published,
                                 productsizecolor__is_available=True).distinct()


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

    feedback_list = DjangoFilterConnectionField(FeedbackType, filterset_class=FeedbackFilter)

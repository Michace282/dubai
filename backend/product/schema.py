import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.filter import GlobalIDFilter, GlobalIDMultipleChoiceFilter
from graphene_django.types import DjangoObjectType
from graphql_relay.connection.arrayconnection import offset_to_cursor
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


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        interfaces = (relay.Node,)
        connection_class = ProductConnection


class ProductFilter(django_filters.FilterSet):
    colors = GlobalIDMultipleChoiceFilter(method='colors_filter')
    sizes = GlobalIDMultipleChoiceFilter(method='sizes_filter')

    def colors_filter(self, queryset, name, value):
        ids = []
        for v in value:
            ids.append(from_global_id(v)[1])

        return queryset.filter(pk__in=ids)

    def sizes_filter(self, queryset, name, value):
        ids = []
        for v in value:
            ids.append(from_global_id(v)[1])

        return queryset.filter(pk__in=ids)

    class Meta:
        model = Product
        fields = ['product_type', 'ladies_type', 'mens_type', 'accessories_type', 'dance_shoes_type', 'colors', 'sizes']

    @property
    def qs(self):
        return super().qs.filter(status=Product.StatusType.published,
                                 productsizecolor__is_available=True).distinct()


class Query(graphene.ObjectType):
    product_list = DjangoFilterConnectionField(ProductType, filterset_class=ProductFilter)

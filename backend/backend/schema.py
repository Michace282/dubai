import graphene
from graphene_django.debug import DjangoDebug
from product.schema import Query as ProductQuery
from stock.schema import Query as StockQuery
from page.schema import Query as PageQuery


#
#
# class Subscription(
#     graphene.ObjectType):
#     debug = graphene.Field(DjangoDebug, name="_debug")
#
#
# class Mutations(
#     graphene.ObjectType):
#     debug = graphene.Field(DjangoDebug, name="_debug")
#
#
class Query(
    ProductQuery,
    PageQuery,
    StockQuery,
    graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="_debug")


#
schema = graphene.Schema(query=Query)
# schema = graphene.Schema(query=Query, mutation=Mutations, subscription=Subscription)

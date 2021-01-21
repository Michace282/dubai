# import graphene
# from graphene_django.debug import DjangoDebug
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
# class Query(
#     graphene.ObjectType):
#     debug = graphene.Field(DjangoDebug, name="_debug")
#
#
schema = graphene.Schema()
# schema = graphene.Schema(query=Query, mutation=Mutations, subscription=Subscription)

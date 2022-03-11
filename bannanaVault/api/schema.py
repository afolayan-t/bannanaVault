import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType, DjangoListField
from graphene_django.debug import DjangoDebug
# from graphql import GraphQLError

from django.conf import settings

# Schemas
from users.schema import UserQuery, UserProfileQuery
from passwords.schema import PasswordEntryQuery

# Mutations
from passwords.schema import PasswordEntryMutation

class Query(UserQuery, UserProfileQuery, PasswordEntryQuery):
    if settings.DEBUG:
        # Debug output - see
         # http://docs.graphene-python.org/projects/django/en/latest/debug/
        debug = graphene.Field(DjangoDebug, name='__debug')

class Mutation(PasswordEntryMutation):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)



    
import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType, DjangoListField
from graphql import GraphQLError
from django.contrib.auth.models import User
from users.models import UserProfile

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"


class UserQuery(ObjectType):
    all_users = graphene.List(UserType)
    user = graphene.Field(UserType, user_id=graphene.Int())

    def resolve_all_users(self, info):
        return User.objects.all()
    
    def resolve_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except:
            return GraphQLError('There is no User matching that ID')


class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile
        fields = "__all__"


class UserProfileQuery(ObjectType):
    all_profiles = graphene.List(UserProfileType)
    profile = graphene.Field(UserProfileType, user_id=graphene.Int())

    def resolve_all_profiles(self, info, *args, **kwargs):
        return UserProfile.objects.all()
    
    def resolve_profile(self, info, user_id):
        try:
            return UserProfile.objects.get(user__id=user_id)
        except:
            return GraphQLError('There is no User Profile matching that ID')


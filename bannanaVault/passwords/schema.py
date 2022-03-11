import graphene
from graphene_django import DjangoObjectType, DjangoListField
from graphql import GraphQLError
from passwords.models import PasswordEntry


class PasswordEntryType(DjangoObjectType):
    class Meta:
        model = PasswordEntry
        fields = "__all__"

class PasswordEntryQuery(graphene.ObjectType):
    all_password_entries = graphene.List(PasswordEntryType, vault_id=graphene.Int())
    password_entry = graphene.Field(PasswordEntryType, user_id=graphene.Int(), pass_id=graphene.Int())

    def resolve_all_password_entries(self, info, vault_id):
        return PasswordEntry.objects.filter(vault__id=vault_id)
    
    def resolve_password_entry(self, info, vault_id, pass_id):
        return PasswordEntry.objects.get(id=pass_id, vault__id=vault_id)

class PasswordEntryInput(graphene.InputObjectType):
    id = graphene.ID()
    site_name = graphene.String()
    site_url = graphene.String()
    auth_id = graphene.String()
    password = graphene.String()
    
class CreatePasswordEntry(graphene.Mutation):
    class Arguments:
        pass_data = PasswordEntryInput()

    password_entry = graphene.Field(PasswordEntryType)

    @staticmethod
    def mutate(root, info, pass_data=None):
        pass_instance = PasswordEntry.objects.create(
            site_name = pass_data.site_name,
            site_url = pass_data.site_url,
            auth_id = pass_data.auth_id,
            password = pass_data.password,
        )
        pass_instance.save()
        return CreatePasswordEntry(password_entry=pass_instance)

class UpdatePasswordEntry(graphene.Mutation):
    class Arguments:
        pass_data = PasswordEntryInput()

    password_entry = graphene.Field(PasswordEntryType)

    @staticmethod
    def mutate(root, info, pass_data=None):

        try:
            if pass_instance := PasswordEntry.objects.get(pk=pass_data.id):
                pass_instance.site_name = pass_data.site_name
                pass_instance.site_url = pass_data.site_url
                pass_instance.auth_id = pass_data.auth_id
                pass_instance.password = pass_data.password
                pass_instance.save()

                return UpdatePasswordEntry(password_entry=pass_instance)
        except:
            return UpdatePasswordEntry(password_entry=None)

class DeletePasswordEntry(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    password_entry = graphene.Field(PasswordEntryType)

    @staticmethod
    def mutate(root, info, id):
        try:
            if pass_instance := PasswordEntry.objects.get(pk=id):
                pass_instance.delete()
                return None
        except:
            return GraphQLError('There is no Password Entry that matches that ID')

class PasswordEntryMutation(graphene.ObjectType):
    create_password_entry = CreatePasswordEntry.Field()
    update_password_entry = UpdatePasswordEntry.Field()
    delete_password_entry = DeletePasswordEntry.Field()
    
from graphene_django import DjangoObjectType
import graphene
from accounts.models import UserModel

class User(DjangoObjectType):
    class Meta:
        model = UserModel

class Query(graphene.ObjectType):
    all_users = graphene.List(User)

    user = graphene.Field(User,id=graphene.Int(), name=graphene.String())

    def resolve_all_users(self, info):
        return UserModel.objects.all()

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        
        if id is not None:
            return UserModel.objects.get(pk=id)

        if name is not None:
            return UserModel.objects.get(name=name)

        return None


schema = graphene.Schema(query=Query)
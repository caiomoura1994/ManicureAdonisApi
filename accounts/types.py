import graphene
from graphene_django import DjangoObjectType
from .models import UserModel

class AccountType(graphene.ObjectType):
    gender = graphene.String() 
    profile_type = graphene.Int()
    biography = graphene.String()
    state = graphene.String()
    city = graphene.String()
    name = graphene.String()
    last_name = graphene.String()
    phone = graphene.String()

class UserType(DjangoObjectType):
    class Meta:
        model = UserModel
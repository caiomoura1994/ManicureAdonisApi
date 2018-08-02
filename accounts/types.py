import graphene
from graphene_django import DjangoObjectType
from .models import UserModel

class UserType(DjangoObjectType):
    class Meta:
        model = UserModel
from graphene_django import DjangoObjectType
import graphene
from .models import ServiceRegister,Service, Category, SubCategory

class category(DjangoObjectType):
    class Meta:
        model = Category

all_categories = graphene.List(category)
category = graphene.Field(category,id=graphene.Int(), name=graphene.String())
def resolve_all_categories(self, info):
    return Category.objects.all()

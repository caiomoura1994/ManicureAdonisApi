from graphene_django import DjangoObjectType
from .models import Category, SubCategory, Service
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class ServiceType(DjangoObjectType):
    class Meta:
        model = Service

class SubCategoryType(DjangoObjectType):
    class Meta:
        model = SubCategory

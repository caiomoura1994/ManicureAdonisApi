from graphene_django import DjangoObjectType
from .models import Category, SubCategory, Service, ServiceRegister
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class ServiceType(DjangoObjectType):
    class Meta:
        model = Service

class ServiceRegisterType(DjangoObjectType):
    class Meta:
        model = ServiceRegister

class SubCategoryType(DjangoObjectType):
    class Meta:
        model = SubCategory

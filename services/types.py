import graphene
from graphene_django import DjangoObjectType
from .models import Category, SubCategory, Service, ServiceRegister
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class ServiceType(DjangoObjectType):
    class Meta:
        model = Service

class ServicePaginatedType(graphene.ObjectType):
    page = graphene.Int()
    pages = graphene.Int()
    has_next = graphene.Boolean()
    has_prev = graphene.Boolean()
    objects = graphene.List(ServiceType)

class ServiceRegisterType(DjangoObjectType):
    class Meta:
        model = ServiceRegister

class ServiceRegisterPaginatedType(graphene.ObjectType):
    page = graphene.Int()
    pages = graphene.Int()
    has_next = graphene.Boolean()
    has_prev = graphene.Boolean()
    objects = graphene.List(ServiceRegisterType)

class SubCategoryType(DjangoObjectType):
    class Meta:
        model = SubCategory

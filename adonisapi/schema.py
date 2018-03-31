from graphene_django import DjangoObjectType
import graphene
from accounts.models import UserModel

from services.models import ServiceRegister,Service, Category, SubCategory

class UserType(DjangoObjectType):
    class Meta:
        model = UserModel

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class SubCategoryType(DjangoObjectType):
    class Meta:
        model = SubCategory

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_categories = graphene.List(CategoryType)
    all_sub_categories = graphene.List(SubCategoryType)
    
    user = graphene.Field(UserType,id=graphene.Int(), name=graphene.String())
    sub_category = graphene.Field(SubCategoryType,id=graphene.Int(), name=graphene.String(), category=graphene.Int())
    
    def resolve_all_categories(self, info):
        return Category.objects.all()

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
    def resolve_sub_category(self, info, **kwargs):
        id = kwargs.get('id')
        category = kwargs.get('category')
        name = kwargs.get('name')
        
        if id is not None:
            return SubCategory.objects.get(pk=id)

        if category is not None:
            return SubCategory.objects.get(category=category)

        if name is not None:
            return SubCategory.objects.get(name=name)

        return None


schema = graphene.Schema(query=Query)
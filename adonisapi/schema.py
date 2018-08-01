from graphene_django import DjangoObjectType
import graphene
from accounts.models import UserModel

from services.models import Service, Category, SubCategory
from services.models import ServiceRegister as ServiceRegisterModel

from accounts.mutations import CreateAccount, Login
from services.mutations import ServiceRegister, CreateService
from accounts.types import UserType
from services.types import CategoryType, ServiceType, SubCategoryType, ServiceRegisterType
        
class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    def resolve_all_users(self, info):
        return UserModel.objects.all()
        
    service = graphene.List(ServiceType)
    def resolve_service(self, info):
        return Service.objects.all()
        
    all_categories = graphene.List(CategoryType)
    def resolve_all_categories(self, info):
        return Category.objects.all()
    
    search_category = graphene.Field(CategoryType,id=graphene.Int(), name=graphene.String())
    def resolve_search_category(self, info, **kwargs):
        id = kwargs.get('id')
        
        name = kwargs.get('name')
        
        if id is not None:
            return Category.objects.get(pk=id)

        if name is not None:
            return Category.objects.get(name=name)

        return None
        
    
    search_service = graphene.List(ServiceType,sub_category=graphene.Int())
    def resolve_search_service(self, info, **kwargs):
        sub_category = kwargs.get('sub_category')
        if sub_category is not None:
            return Service.objects.filter(sub_category=sub_category)
        return None
    
    search_service_register = graphene.List(ServiceRegisterType, professional_id=graphene.Int())
    def resolve_search_service_register(self, info, **kwargs):
        professional_id = kwargs.get('professional_id')
        if professional_id is not None:
            return ServiceRegisterModel.objects.filter(client=professional_id)
        return None
    
    user = graphene.Field(UserType,id=graphene.Int(), name=graphene.String())
    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        
        if id is not None:
            return UserModel.objects.get(pk=id)

        if name is not None:
            return UserModel.objects.get(name=name)

        return None

    all_sub_categories = graphene.List(SubCategoryType)

    sub_category = graphene.Field(SubCategoryType,id=graphene.Int(), name=graphene.String(), category=graphene.Int())
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

class MyMutations(graphene.ObjectType):
    create_service = CreateService.Field()
    create_service_regiter = ServiceRegister.Field()
    create_account = CreateAccount.Field()
    login = Login.Field()

schema = graphene.Schema(query=Query, mutation=MyMutations)
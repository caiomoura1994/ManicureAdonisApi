from graphene_django import DjangoObjectType
import graphene
from accounts.models import UserModel

from services.models import Service, Category, SubCategory
from services.models import ServiceRegister as ServiceRegisterModel

from graphene_django.rest_framework.mutation import SerializerMutation

from django.utils import timezone
from django.core import serializers

class ServiceRegisterInput(graphene.InputObjectType):
    address_attendance = graphene.String()
    client = graphene.Int()
    payment = graphene.String()
    payed = graphene.Boolean()
    status = graphene.String()
    service = graphene.Int()
    user_id = graphene.Int()


# Create a service order
class CreateServiceRegister(graphene.Mutation):
    class Arguments:
        new_service = ServiceRegisterInput(required=True)
    
    count = graphene.Int()
    new_service = graphene.Field(lambda: ServiceRegisterType)
    def mutate(self, info, new_service ):
        
        user_object=UserModel.objects.get(pk=new_service.user_id).user
        service_object= Service.objects.get(pk=new_service.service)
        
        new_service = ServiceRegisterModel(
            date=timezone.now(),
            service=service_object,
            address_attendance=new_service.address_attendance, 
            client=user_object,
            payed=new_service.payed, 
            payment=new_service.payment, 
            status=new_service.status
            )

        new_service.save()

        count = ServiceRegisterModel.objects.count()
        
        
        return CreateServiceRegister(new_service=new_service, count=count)

class UserType(DjangoObjectType):
    class Meta:
        model = UserModel

class ServiceRegisterType(graphene.ObjectType):
    date = graphene.String()
    address_attendance = graphene.String()
    payment = graphene.String()
    payed = graphene.Boolean()
    status = graphene.String()
    pk = graphene.Int()
    
    # client = graphene.Field(UserType)
    
    client = graphene.Field(graphene.types.json.JSONString)
    def resolve_client(self, info):
        user= UserModel.objects.get(pk=self.client.pk)
        data_json = serializers.serialize("json", [user, ])
        print(data_json)
        return data_json

    # pk = graphene.Int()
    # def mutate(self, info):
    #     pk = 1
    #     return ServiceRegisterType(pk=pk)
    # mutation{createServiceRegiter(newService:{
    #   addressAttendance:"aaa",
    #   client:1,
    #   payment:"1",
    #   payed:true,
    #   status:"1",
    #   service:1,
    #   userId:1
    # }) {
    #   pk
    #   count
    #   newService {
    #     client{
    #       id
    #     }
    #     addressAttendance
    #     payment
    #     payed
    #     status
    #   }
    # }}
class MyMutations(graphene.ObjectType):
    create_service_regiter = CreateServiceRegister.Field()


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class ServiceType(DjangoObjectType):
    class Meta:
        model = Service

class SubCategoryType(DjangoObjectType):
    class Meta:
        model = SubCategory
        
class Query(graphene.ObjectType):
    # new_service = graphene.Field(ServiceRegisterType)

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


schema = graphene.Schema(query=Query, mutation=MyMutations)
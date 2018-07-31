import graphene
from django.utils import timezone
from django.core import serializers

from accounts.models import UserModel
from django.contrib.auth.models import User

from services.models import Service, SubCategory
from services.models import ServiceRegister as ServiceRegisterModel
from graphene_django import DjangoObjectType

class ServiceRegisterType(graphene.ObjectType):
    date = graphene.String()
    address_attendance = graphene.String()
    payment = graphene.String()
    payed = graphene.Boolean()
    status = graphene.String()
    pk = graphene.Int()
    client = graphene.Field(graphene.types.json.JSONString)
    def resolve_client(self, info):
        user= UserModel.objects.get(pk=self.client.pk)
        data_json = serializers.serialize("json", [user, ])
        return data_json

class ServiceRegisterInput(graphene.InputObjectType):
    address_attendance = graphene.String()
    client = graphene.Int()
    payment = graphene.String()
    payed = graphene.Boolean()
    status = graphene.String()
    service = graphene.Int()
    user_id = graphene.Int()


# Create a service order
class ServiceRegister(graphene.Mutation):
    class Arguments:
        new_service_order = ServiceRegisterInput(required=True)
    count = graphene.Int()
    new_service_order = graphene.Field(lambda: ServiceRegisterType)
    def mutate(self, info, new_service_order ):
        user_object=UserModel.objects.get(pk=new_service_order.user_id).user
        service_object= Service.objects.get(pk=new_service_order.service)
        new_service_order = ServiceRegisterModel(
            date=timezone.now(),
            service=service_object,
            address_attendance=new_service_order.address_attendance, 
            client=user_object,
            payed=new_service_order.payed, 
            payment=new_service_order.payment, 
            status=new_service_order.status
            )
        new_service_order.save()
        count = ServiceRegisterModel.objects.count()
        return ServiceRegister(new_service_order=new_service_order, count=count)

class ServiceInput(graphene.InputObjectType):
    description = graphene.String()
    price = graphene.Int()
    sub_category = graphene.Int()
    user_id = graphene.Int()

class ServiceUserType(DjangoObjectType):
    class Meta:
        model = UserModel

class ServiceSubCategoryType(DjangoObjectType):
    class Meta:
        model = SubCategory

class ServiceCreatedType(graphene.ObjectType):
    description = graphene.String()
    price = graphene.Int()
    sub_category = graphene.Field(ServiceSubCategoryType)
    user_id = graphene.Field(ServiceUserType)

# Create a service
class CreateService(graphene.Mutation):
    class Arguments:
        new_service = ServiceInput(required=True)
    new_service = graphene.Field(lambda: ServiceCreatedType)
    def mutate(self, info, new_service ):
        user_object = UserModel.objects.get(pk=new_service.user_id)
        sub_category = SubCategory.objects.get(pk = new_service.sub_category)

        new_service = Service(
            pub_date=timezone.now(),
            sub_category = sub_category,
            description = new_service.description,
            price = new_service.price,
            professional_owner = user_object
            )
        new_service.save()

        return CreateService(new_service = new_service)
import graphene
from django.utils import timezone
from django.core import serializers

from accounts.models import UserModel
from django.contrib.auth.models import User

from services.models import Service
from services.models import ServiceRegister as ServiceRegisterModel

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

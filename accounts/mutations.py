import graphene
from django.utils import timezone
from django.core import serializers

from accounts.models import UserModel
from django.contrib.auth.models import User


class AccountInput(graphene.InputObjectType):
    gender = graphene.String() 
    profile_type = graphene.Int()
    biography = graphene.String()
    state = graphene.String()
    city = graphene.String()
    name = graphene.String()
    last_name = graphene.String()
    phone = graphene.String()
    email = graphene.String()
    password = graphene.String()

class AccountType(graphene.ObjectType):
    gender = graphene.String() 
    profile_type = graphene.Int()
    biography = graphene.String()
    state = graphene.String()
    city = graphene.String()
    name = graphene.String()
    last_name = graphene.String()
    phone = graphene.String()
    
# Create a account
class CreateAccount(graphene.Mutation):
    class Arguments:
        new_account = AccountInput(required=True)
    
    count = graphene.Int()
    new_account = graphene.Field(lambda: AccountType)
    def mutate(self, info, new_account ):
        user = User.objects.create_user(new_account.email, new_account.email, new_account.password)
        if user is not None:
            user.last_name = new_account.last_name
            user.first_name = new_account.name
            user.save()

        new_account = UserModel(
            gender = new_account.gender,
            profile_type = new_account.profile_type,
            user = user,
            biography = new_account.biography,
            state = new_account.state,
            city = new_account.city,
            name = new_account.name,
            last_name = new_account.last_name,
            phone = new_account.phone,
            )

        new_account.save()

        count = UserModel.objects.count()
        
        
        return CreateAccount(new_account=new_account, count=count)

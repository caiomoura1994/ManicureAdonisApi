import graphene
from django.utils import timezone
from django.core import serializers
from accounts.models import UserModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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

class LoginInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    password = graphene.String(required=True)

class UserField(graphene.ObjectType):
    avatar = graphene.String()
    biography = graphene.String()
    id = graphene.String()
    city = graphene.String()
    last_name = graphene.String()
    state = graphene.String()
    name = graphene.String()
    online = graphene.Boolean()
    phone = graphene.String()
    user_id = graphene.Int()
    pk = graphene.Int()
    gender = graphene.String()
    profile_type = graphene.String()

class Login(graphene.Mutation):
    class Arguments:
        login_input = LoginInput(required=True)
    
    Output = UserField
    def mutate(self, info, login_input ):
        username = login_input.username
        password = login_input.password
        user = authenticate( None, username = username, password = password )
        if user is not None:
            profile = UserModel.objects.get(user=user)
            if profile is not None:
                return UserField(
                    avatar=profile.avatar,
                    biography=profile.biography,
                    id=profile.id,
                    city=profile.city,
                    last_name=profile.last_name,
                    state=profile.state,
                    name=profile.name,
                    online=profile.online,
                    phone=profile.phone,
                    user_id=profile.user_id,
                    pk=profile.pk,
                    gender=profile.gender,
                    profile_type=profile.profile_type,
                    )
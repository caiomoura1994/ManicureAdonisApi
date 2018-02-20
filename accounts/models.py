from django.db import models
from django.conf import settings

GENDER = (
        ('f', 'Feminino'),
        ('M', 'Masculino'),
        ('O', 'Outros'),
)
states = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
)
class UserModel(models.Model):
    PROFILE_TYPES = (
        (0, 'ServiceProviderProfile'),
        (1, 'ClientProfile'),
        
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER,
        null=True,
        blank=True
    )
    profile_type = models.IntegerField(
        choices=PROFILE_TYPES,
        default=PROFILE_TYPES[0][0]
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    online = models.BooleanField(default=False)
    biography = models.CharField(max_length=420, blank=True, null=True, default='')
    state = models.CharField(choices=states, max_length=2, default='BA')
    city = models.CharField(max_length=254, default='')
    name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=100, default='')
    avatar = models.ImageField(upload_to='images/profiles/', null=True, blank=True)

    def __str__(self):
        return ('%s' % self.user)

    @property
    def user_detail(self):
        return self.user

class ProfileManager(models.Manager):
    profile_type = None
    def get_queryset(self):
        return super(ProfileManager, self).get_queryset().filter(profile_type=self.profile_type)
    class Meta:
        abstract = True


class ServiceProviderProfileManager(ProfileManager):
    profile_type = 0

class ServiceProviderProfile(UserModel):
    objects = ServiceProviderProfileManager()
    class Meta:
        proxy = True

class ClientProfileProfileManager(ProfileManager):
    profile_type = 1

class ClientProfileProfile(UserModel):
    objects = ClientProfileProfileManager()
    class Meta:
        proxy = True


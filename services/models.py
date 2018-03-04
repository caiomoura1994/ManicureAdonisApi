from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=0)    
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Service(models.Model):
    # STATUS_CHOICES = (
    #     ('1','Em andamento'),
    #     ('2','Finalizado')
    # )
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=0)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    price = models.IntegerField(default=0)
    # status = models.CharField(max_length=1,choices=STATUS_CHOICES, default='1')
    professional_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.description

class ServiceRegister(models.Model):
    PAYMENT_CHOICES = (
        ('1','Cartão'),
        ('2','Dinheiro'),
        ('3','PayPal'),
        ('4','PagSeguro')
    )

    STATUS_CHOICES = (
        ('1','Em andamento'),
        ('2','Finalizado')
    )

    service = models.ForeignKey(Service, on_delete=models.CASCADE, default=0)
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField('Registro de data e hora do serviço')
    address_attendance = models.CharField(max_length=200)    
    payment = models.CharField(max_length=1,choices=PAYMENT_CHOICES, default='2')
    payed = models.BooleanField(default=False)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES, default='1')

    def __str__(self):
        return self.client
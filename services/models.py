from django.db import models
from django.conf import settings

class Categorie(models.Model):
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    def __str__(self):
        return self.name
        

class Service(models.Model):
    STATUS_CHOICES = (
        ('1','Em andamento'),
        ('2','Finalizado')
    )
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    price = models.IntegerField(default=0)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES, default='1')
    professional = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.description
        
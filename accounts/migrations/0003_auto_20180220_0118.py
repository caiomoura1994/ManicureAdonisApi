# Generated by Django 2.0.2 on 2018-02-20 01:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20180210_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProfileProfile',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('accounts.usermodel',),
        ),
        migrations.CreateModel(
            name='ServiceProviderProfile',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('accounts.usermodel',),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='biography',
            field=models.CharField(blank=True, default='', max_length=420, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='city',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='online',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='profile_type',
            field=models.IntegerField(choices=[(0, 'ServiceProviderProfile'), (1, 'ClientProfile')], default=0),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='state',
            field=models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='BA', max_length=2),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]

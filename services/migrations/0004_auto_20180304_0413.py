# Generated by Django 2.0.2 on 2018-03-04 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0003_auto_20180304_0231'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Registro de data e hora do serviço')),
                ('address_attendance', models.CharField(max_length=200)),
                ('payment', models.CharField(choices=[('1', 'Cartão'), ('2', 'Dinheiro'), ('3', 'PayPal'), ('4', 'PagSeguro')], default='2', max_length=1)),
                ('payed', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('1', 'Em andamento'), ('2', 'Finalizado')], default='1', max_length=1)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='subcategorie',
            name='categorie',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='professional',
            new_name='professional_owner',
        ),
        migrations.RemoveField(
            model_name='service',
            name='status',
        ),
        migrations.RemoveField(
            model_name='service',
            name='sub_categorie',
        ),
        migrations.RenameModel(
            old_name='Categorie',
            new_name='Category',
        ),
        migrations.DeleteModel(
            name='SubCategorie',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='services.Category'),
        ),
        migrations.AddField(
            model_name='serviceregister',
            name='service',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='services.Service'),
        ),
        migrations.AddField(
            model_name='service',
            name='sub_category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='services.SubCategory'),
        ),
    ]

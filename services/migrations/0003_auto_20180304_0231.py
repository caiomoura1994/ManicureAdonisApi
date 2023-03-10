# Generated by Django 2.0.2 on 2018-03-04 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20180220_0118'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('categorie', models.ManyToManyField(to='services.Categorie')),
            ],
        ),
        migrations.RemoveField(
            model_name='service',
            name='categorie',
        ),
        migrations.AddField(
            model_name='service',
            name='sub_categorie',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='services.SubCategorie'),
        ),
    ]

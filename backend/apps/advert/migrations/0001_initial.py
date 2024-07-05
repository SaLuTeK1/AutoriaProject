# Generated by Django 5.0.6 on 2024-07-05 12:07

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0003_remove_carmodel_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(10)])),
                ('info', models.TextField(validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(180)])),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('pending', 'Pending')], default='pending', max_length=10)),
                ('edit_attempts', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('region', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)])),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='advert', to='cars.carmodel')),
            ],
            options={
                'db_table': 'advert',
            },
        ),
    ]

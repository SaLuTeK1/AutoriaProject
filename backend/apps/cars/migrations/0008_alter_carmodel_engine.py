# Generated by Django 5.0.6 on 2024-07-06 23:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_carmodel_drive_alter_carmodel_fuel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='engine',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)]),
        ),
    ]

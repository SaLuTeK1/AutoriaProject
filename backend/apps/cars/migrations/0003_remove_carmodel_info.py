# Generated by Django 5.0.6 on 2024-07-05 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_carmodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='info',
        ),
    ]

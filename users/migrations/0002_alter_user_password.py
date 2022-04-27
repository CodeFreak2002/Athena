# Generated by Django 4.0.4 on 2022-04-27 11:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=1000, validators=[
                                   django.core.validators.MinLengthValidator(10)]),
        ),
    ]

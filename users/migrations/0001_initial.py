# Generated by Django 4.0.4 on 2022-04-17 03:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
                ('rating', models.PositiveIntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('about', models.CharField(max_length=500)),
                ('role', models.BooleanField(default=False)),
                ('profile_pic', models.ImageField(height_field=300, upload_to='', width_field=300)),
            ],
        ),
        migrations.CreateModel(
            name='UserEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
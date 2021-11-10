# Generated by Django 3.2.9 on 2021-11-10 02:17

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20211110_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('m', 'мужской'), ('f', 'женский')], default='', max_length=1, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=50, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Логин'),
        ),
    ]

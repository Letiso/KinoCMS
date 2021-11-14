# Generated by Django 3.2.9 on 2021-11-13 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_customuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('m', 'Мужской'), ('f', 'Женский')], max_length=1, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='language',
            field=models.CharField(choices=[('ru', 'Русский'), ('ua', 'Українська'), ('en', 'English')], max_length=2, verbose_name='Язык'),
        ),
    ]

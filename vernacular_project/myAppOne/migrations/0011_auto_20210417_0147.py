# Generated by Django 3.2 on 2021-04-16 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAppOne', '0010_auto_20210416_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agerecordinput',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='roomrecordinput',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

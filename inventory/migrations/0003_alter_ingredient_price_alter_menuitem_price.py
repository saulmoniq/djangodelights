# Generated by Django 4.1 on 2022-08-08 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_ingredient_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]

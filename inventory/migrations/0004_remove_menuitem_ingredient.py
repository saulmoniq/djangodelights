# Generated by Django 4.1 on 2022-08-08 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_ingredient_price_alter_menuitem_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='ingredient',
        ),
    ]

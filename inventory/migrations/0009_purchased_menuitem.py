# Generated by Django 4.1 on 2022-08-15 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_delete_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchased',
            name='menuItem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.menuitem'),
        ),
    ]

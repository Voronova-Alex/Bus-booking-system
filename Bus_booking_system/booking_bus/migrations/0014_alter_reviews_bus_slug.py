# Generated by Django 3.2.8 on 2021-11-26 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_bus', '0013_auto_20211125_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='bus_slug',
            field=models.CharField(max_length=100, verbose_name='Автобус'),
        ),
    ]

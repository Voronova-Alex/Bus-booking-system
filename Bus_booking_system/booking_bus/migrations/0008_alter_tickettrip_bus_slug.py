# Generated by Django 3.2.8 on 2021-11-21 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_bus', '0007_tickettrip_bus_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickettrip',
            name='bus_slug',
            field=models.CharField(default=None, max_length=100, verbose_name='Ссылка на автобус'),
        ),
    ]
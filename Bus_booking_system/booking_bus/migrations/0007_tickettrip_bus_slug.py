# Generated by Django 3.2.8 on 2021-11-21 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_bus', '0006_alter_tickettrip_trip'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickettrip',
            name='bus_slug',
            field=models.CharField(default=None, max_length=255, verbose_name='Ссылка на автобус'),
        ),
    ]
# Generated by Django 3.2.8 on 2021-11-16 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_bus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newtrip',
            name='rout_trip',
            field=models.CharField(max_length=50, verbose_name='Направление'),
        ),
    ]
# Generated by Django 3.2.8 on 2021-11-24 17:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0002_remove_rout_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busdetails',
            name='number_sites',
            field=models.PositiveIntegerField(default=15, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(15)], verbose_name='Количество мест'),
        ),
    ]
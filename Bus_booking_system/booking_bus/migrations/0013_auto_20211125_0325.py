# Generated by Django 3.2.8 on 2021-11-25 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking_bus', '0012_auto_20211124_2055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'ordering': ('-created',), 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterField(
            model_name='reviews',
            name='trip',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booking_bus.newtrip', verbose_name='Поезка'),
        ),
    ]

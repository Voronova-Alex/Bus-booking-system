from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.urls import reverse
from datetime import time


class BusDetails(models.Model):
    CHOICES = (
        ('Красный', 'Красный'),
        ('Белый', 'Белый'),
        ('Черный', 'Черный'),
        ('Зеленый', 'Зеленый'),
        ('Синий', 'Синий'),
        ('Желтый', 'Желтый'),
        ('Серый', 'Серый'),
        ('Оранжевый', 'Оранжевый'),
        ('Голубой', 'Голубой'),
    )
    bus_model = models.CharField(max_length=25, verbose_name='Марка авобуса')
    bus_number = models.DecimalField(max_digits=4, decimal_places=0, verbose_name='Номер автобуса')
    slug = models.SlugField(max_length=25, unique=True, verbose_name='SLUG')
    bus_colour = models.CharField(max_length=25, choices=CHOICES, verbose_name='Цвет автобуса')
    bus_photo = models.ImageField(upload_to='media/bus/', verbose_name='Фотография автобуса')
    number_sites = models.PositiveIntegerField(
        default=4,
        validators=[
            MaxValueValidator(50),
            MinValueValidator(15)
        ],
        verbose_name='Количество мест'
    )
    bus_rating = models.PositiveIntegerField(
        default=5,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ],
        verbose_name='Рейтинг'
    )

    class Meta:
        ordering = ('-bus_rating',)
        verbose_name = 'Автобус'
        verbose_name_plural = 'Автобусы'

    def __str__(self):
        return f'{self.bus_model}-{self.bus_number}-{self.bus_colour}'

    def get_absolute_url(self):
        return reverse('bus_detail', kwargs={'slug': self.slug})

class BusStop(models.Model):
    bus_stop = models.CharField(max_length=25, verbose_name='Остановка')
    delta_time = models.TimeField(default=time(00, 00), verbose_name='Время в пути')


    def __str__(self):
        return f'{self.bus_stop}'

    class Meta:
        verbose_name = 'Остановка'
        verbose_name_plural = 'Остановки'




class Rout(models.Model):
    name_start = models.CharField(max_length=25, verbose_name='Начало маршрута')
    name_finish = models.CharField(max_length=25, verbose_name='Конец маршрута')
    slug = models.SlugField(max_length=25, unique=True, verbose_name='SLUG')
    bus_stops = models.ManyToManyField(BusStop, verbose_name='Остановка')


    def __str__(self):
        return f'{self.name_start}-{self.name_finish}'

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'

    def get_absolute_url(self):
        return reverse('rout_detail', kwargs={'slug': self.slug})


class BookingPrice(models.Model):
    price_adult = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Полная стоимость')
    price_child = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Льготная стоимость')
    price_baggage = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Стоимость провоза багажа')
    price_rout = models.ForeignKey(Rout, on_delete=models.CASCADE, verbose_name='Стоимость')

    def __str__(self):
        return f'{self.price_rout}-{self.price_adult}'

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'


class RoutesTravelDatesTimes(models.Model):

    rout = models.ForeignKey(Rout, on_delete=models.CASCADE)
    bus = models.ForeignKey(BusDetails, on_delete=models.CASCADE)
    travel_date = models.DateField(default=timezone.now, verbose_name='Дата отправления')
    travel_time = models.TimeField(default=timezone.now, verbose_name='Время отправления')

    class Meta:
        ordering = ('-travel_date',)
        verbose_name = 'Отправление'
        verbose_name_plural = 'Отправления'

    def __str__(self):
        return f'дата {self.travel_date} время {self.travel_time}'

from django.db import models
from booking_app.models import RoutesTravelDatesTimes, Rout, BusStop
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class NewTrip(models.Model):
    BOOKED = 'Забронировать'
    CONFIRMED = 'Подтвердить'

    TICKET_STATUSES = ((BOOKED, 'Забронировать'),
                       (CONFIRMED, 'Подтвердить'),)

    PAID_BY_CARD = 'По карте'
    PAID_BY_CASH = 'Наличными'

    PAID_STATUSES = ((PAID_BY_CARD, 'По карте'),
                     (PAID_BY_CASH, 'Наличными'),)

    user = models.CharField(max_length=50, verbose_name="Имя", default="User")
    phone = models.CharField(max_length=50, verbose_name="Контактный телефон")
    rout_trip = models.CharField(max_length=50, verbose_name="Направление")
    rout_data_time = models.ForeignKey(RoutesTravelDatesTimes, verbose_name="Дата-Время поездки",
                                       on_delete=models.CASCADE, )
    bus_stop = models.ForeignKey(BusStop, verbose_name="Остановка посадки", on_delete=models.CASCADE,
                                 null=True,
                                 blank=True)
    quantity_adult = models.PositiveIntegerField(
        default=1,
        validators=[
            MaxValueValidator(3),
            MinValueValidator(1)
        ],
        verbose_name="Количество взрослых"
    )
    quantity_child = models.PositiveIntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ],
        verbose_name="Количество детей"
    )
    quantity_baggage = models.PositiveIntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ],
        verbose_name="Количество мест для багажа"
    )
    price_adult = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Стоимость полного билета")
    price_child = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Стоимость льготного билета")
    price_baggage = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Стоимость провоза багажа")
    comment = models.TextField(verbose_name='Комментарий к поездке', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, verbose_name="Статус", max_length=50)
    paid = models.CharField(choices=PAID_STATUSES, default=PAID_BY_CASH, verbose_name="Оплата", max_length=50)
    status_trip = models.BooleanField(default=False, verbose_name="Явка")

    class Meta:
        ordering = ('-user',)
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'

    def __str__(self):
        return 'NewTrip {}'.format(self.id)


class TicketTrip(models.Model):
    trip = models.OneToOneField(NewTrip, verbose_name="Поезка", on_delete=models.CASCADE)
    rout_data_time = models.CharField(max_length=50, verbose_name="Дата поезки")
    bus_stop = models.CharField(max_length=50, verbose_name="Остановка посадки")
    time_stop = models.TimeField('Время посадки', default=timezone.now)
    total_cost = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Общая стоиомсть')
    bus_info = models.CharField(max_length=50, verbose_name="Инфрмация о автобусе")
    bus_slug = models.CharField(max_length=100, verbose_name="Ссылка на автобус")

    class Meta:
        ordering = ('-rout_data_time',)
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'


class TripsUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    quantity_delete_booked_trip = models.PositiveIntegerField(default=0, verbose_name='Количество удаленых броней')
    quantity_autodelete_trip = models.PositiveIntegerField(default=0,
                                                           verbose_name='Количество автоматически удаленных броней')
    quantity_default_trip = models.PositiveIntegerField(default=0, verbose_name='Количество не явок')

    class Meta:
        ordering = ('-user',)
        verbose_name = 'Статиска поездок'
        verbose_name_plural = 'Статиски поездок'

    def __str__(self):
        return f'{self.user}'


class Reviews(models.Model):
    user = models.CharField(max_length=50, verbose_name="Имя", default="User")
    created = models.DateTimeField(auto_now_add=True)
    trip = models.OneToOneField(NewTrip, verbose_name="Поезка", on_delete=models.CASCADE)
    bus_slug = models.CharField(max_length=100, verbose_name="Автобус")
    comment = models.TextField(verbose_name='Комментарий к поездке', null=True, blank=True)
    bus_rating = models.PositiveIntegerField(
        default=5,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ],
        verbose_name='Оценка'
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.bus_slug} оценка {self.bus_rating}'

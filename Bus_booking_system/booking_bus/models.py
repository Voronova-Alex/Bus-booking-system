from django.db import models
from booking_app.models import RoutesTravelDatesTimes, Rout, BusStop
from django.contrib.auth.models import User
from datetime import timedelta, datetime


class NewTrip(models.Model):
    BOOKED = 'Booked'
    CONFIRMED = 'Сonfirmed'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CONFIRMED, 'Сonfirmed'),)

    PAID_BY_CARD = 'Card'
    PAID_BY_CASH = 'Cash'

    PAID_STATUSES = ((PAID_BY_CARD, 'Card'),
                     (PAID_BY_CASH, 'Cash'),)


    user = models.ForeignKey(User,  verbose_name="Имя", on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=50, verbose_name="Контактный телефон")
    rout_trip = models.ForeignKey(Rout, verbose_name="Направление", on_delete=models.CASCADE)
    rout_data_time = models.ForeignKey(RoutesTravelDatesTimes, verbose_name="Дата-Время поездки",  related_name='items', on_delete=models.CASCADE, )
    bus_stop = models.ForeignKey(BusStop, verbose_name="Остановка посадки", on_delete=models.CASCADE, null=True, blank=True)
    quantity_adult = models.PositiveIntegerField(default=0)
    quantity_child = models.PositiveIntegerField(default=0)
    quantity_baggage = models.PositiveIntegerField(default=0)
    price_adult = models.DecimalField(max_digits=4, decimal_places=2)
    price_child = models.DecimalField(max_digits=4, decimal_places=2)
    price_baggage = models.DecimalField(max_digits=4, decimal_places=2)
    comment = models.TextField(verbose_name='Комментарий к поездке', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, verbose_name="Статус", max_length=50)
    paid = models.CharField(choices=PAID_STATUSES, default=PAID_BY_CASH,  verbose_name="Оплата", max_length=50)
    total_cost = models.DecimalField(max_digits=4, decimal_places=2)
    status_trip = models.BooleanField(default=False, verbose_name="Явка")

    class Meta:
        ordering = ('-user',)
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'

    def __str__(self):
        return 'NewTrip {}'.format(self.id)

    def status_trip_upgrade(self):
        if (self.created - timedelta(days=1)) < datetime.combine(self.items.travel_date, self.items.travel_time):
            self.status = 'Сonfirmed'



class TripsUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    quantity_booked_trip = models.PositiveIntegerField(default=0)
    quantity_cancel_trip = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('-user',)
        verbose_name = 'Статиска поездок'
        verbose_name_plural = 'Статиски поездок'


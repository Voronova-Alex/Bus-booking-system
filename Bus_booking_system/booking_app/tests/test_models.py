from django.test import TestCase
from booking_app.models import BusDetails, BusStop, Rout, BookingPrice, RoutesTravelDatesTimes
from datetime import time, date
from django.core.files.uploadedfile import SimpleUploadedFile


class BusDetailsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        BusDetails.objects.create(
            bus_model='B',
            bus_number=1111,
            slug='b-1111',
            bus_colour='Синий',
            bus_photo=SimpleUploadedFile('test_image.jpg', content=b'\test'),
            number_sites=15, bus_rating=5
        )

    def test_string_method(self):
        bus = BusDetails.objects.get(slug='b-1111')
        expected_string = f'{bus.bus_model}-{bus.bus_number}-{bus.bus_colour}'
        self.assertEqual(str(bus), expected_string)

    def test_get_absolute_url(self):
        bus = BusDetails.objects.get(slug='b-1111')
        self.assertEqual(bus.get_absolute_url(), '/bus/b-1111')

    def test_bus_model(self):
        bus = BusDetails.objects.first()
        self.assertEqual(bus.bus_model, 'B')

    def test_bus_number(self):
        bus = BusDetails.objects.first()

        self.assertEqual(bus.bus_number, 1111)

    def test_slug(self):
        bus = BusDetails.objects.first()
        self.assertEqual(bus.slug, 'b-1111')

    def test_bus_colour(self):
        bus = BusDetails.objects.first()
        self.assertEqual(bus.bus_colour, 'Синий')

    def test_bus_number_sites(self):
        bus = BusDetails.objects.first()
        self.assertEqual(bus.number_sites, 15)

    def test_bus_bus_rating(self):
        bus = BusDetails.objects.first()
        self.assertEqual(bus.number_sites, 5)

    def test_bus_bus_rating(self):
        bus = BusDetails.objects.first()
        self.assertEqual(bus.bus_photo, 'media/bus/test_image.jpg')


class BusStopTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        BusStop.objects.create(
            bus_stop='Один',
            delta_time=time(hour=1, minute=1)
        )

    def test_string_method(self):
        stop = BusStop.objects.get(id=1)
        expected_string = f'{stop.bus_stop}'
        self.assertEqual(str(stop), expected_string)

    def test_stop_bus_stop(self):
        stop = BusStop.objects.first()
        self.assertEqual(stop.bus_stop, 'Один')

    def test_stop_delta_time(self):
        stop = BusStop.objects.first()
        self.assertEqual(stop.delta_time, time(hour=1, minute=1))


class RoutTest(TestCase):
    @classmethod
    def setUpTestData(clc):
        rout = Rout.objects.create(
            name_start='start',
            name_finish='finish',
            slug='start-finish'
        )

        rout.bus_stops.create(bus_stop='Один', delta_time=time(hour=1, minute=1))

    def test_string_method(self):
        rout = Rout.objects.get(slug='start-finish')
        expected_string = f'{rout.name_start}-{rout.name_finish}'
        self.assertEqual(str(rout), expected_string)

    def test_get_absolute_url(self):
        rout = Rout.objects.get(slug='start-finish')
        self.assertEqual(rout.get_absolute_url(), '/rout/start-finish')

    def test_rout_name_start(self):
        rout = Rout.objects.first()
        self.assertEqual(rout.name_start, 'start')

    def test_rout_name_finish(self):
        rout = Rout.objects.first()
        self.assertEqual(rout.name_finish, 'finish')

    def test_rout_slug(self):
        rout = Rout.objects.first()
        self.assertEqual(rout.slug, 'start-finish')

    def test_bus_stops(self):
        rout = Rout.objects.first()
        self.assertTrue(rout.bus_stops.exists())


class BookingPriceTest(TestCase):

    @classmethod
    def setUpTestData(self) -> None:
        self.rout = Rout.objects.create(
            name_start='start',
            name_finish='finish',
            slug='start-finish'
        )

        self.rout.bus_stops.create(bus_stop='Один', delta_time=time(hour=1, minute=1))

        self.price = BookingPrice.objects.create(
            price_adult=10,
            price_child=10,
            price_baggage=10,
            price_rout=self.rout
        )

    def test_price_adult(self):
        self.price = BookingPrice.objects.first()
        self.assertEqual(self.price.price_adult, 10)

    def test_price_child(self):
        self.price = BookingPrice.objects.first()
        self.assertEqual(self.price.price_child, 10)

    def test_price_baggage(self):
        self.price = BookingPrice.objects.first()
        self.assertEqual(self.price.price_baggage, 10)

    def test_bus_stops(self):
        self.price = BookingPrice.objects.first()
        self.assertEqual(self.price.price_rout, self.rout)


class BookingPriceTest(TestCase):

    @classmethod
    def setUpTestData(self) -> None:
        self.rout = Rout.objects.create(
            name_start='start',
            name_finish='finish',
            slug='start-finish'
        )

        self.rout.bus_stops.create(bus_stop='Один', delta_time=time(hour=1, minute=1))

        self.bus = BusDetails.objects.create(
            bus_model='B',
            bus_number=1111,
            slug='b-1111',
            bus_colour='Синий',
            bus_photo=SimpleUploadedFile('test_image_2.jpg', content=b'\test'),
            number_sites=15, bus_rating=5
        )

        RoutesTravelDatesTimes.objects.create(
            rout=self.rout,
            bus=self.bus,
            travel_date=date(day=1, month=1, year=2000),
            travel_time=time(hour=1, minute=1)
        )

    def test_rout(self):
        self.travel = RoutesTravelDatesTimes.objects.first()
        self.assertEqual(self.travel.rout, self.rout)

    def test_bus(self):
        self.travel = RoutesTravelDatesTimes.objects.first()
        self.assertEqual(self.bus, self.bus)

    def test_travel_date(self):
        self.travel = RoutesTravelDatesTimes.objects.first()
        self.assertEqual(self.travel.travel_date, date(day=1, month=1, year=2000))

    def test_travel_time(self):
        self.travel = RoutesTravelDatesTimes.objects.first()
        self.assertEqual(self.travel.travel_time, time(hour=1, minute=1))

    def test_string_method(self):
        self.travel = RoutesTravelDatesTimes.objects.first()
        expected_string = f'дата {self.travel.travel_date} время {self.travel.travel_time}'
        self.assertEqual(str(self.travel), expected_string)

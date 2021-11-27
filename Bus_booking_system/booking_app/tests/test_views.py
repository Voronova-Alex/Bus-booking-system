from django.test import TestCase, Client
from django.urls import reverse
from datetime import time
from booking_app.models import BusDetails, BusStop, Rout, BookingPrice, RoutesTravelDatesTimes
from django.core.files.uploadedfile import SimpleUploadedFile


class HomeTest(TestCase):

    def test_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home-page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class RoutListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_routs = 3
        for rout_slug in range(number_of_routs):
            rout = Rout.objects.create(
                name_start=f'start{rout_slug}',
                name_finish=f'finish{rout_slug}',
                slug=f'start-finish{rout_slug}'
            )

            rout.bus_stops.create(bus_stop='Один', delta_time=time(hour=1, minute=1))

    def test_url_exists(self):
        response = self.client.get('/rout/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('rout_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'routes_list.html')


class BusListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_buses = 3
        for bus_slug in range(number_of_buses):
            BusDetails.objects.create(
                bus_model=f'B{bus_slug}',
                bus_number=1111,
                slug=f'b{bus_slug}-1111',
                bus_colour='Синий',
                bus_photo=SimpleUploadedFile(f'test_image{bus_slug}.jpg', content=b'\test'),
                number_sites=15, bus_rating=5
            )

    def test_url_exists(self):
        response = self.client.get('/bus/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bus_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bus_list.html')


class RoutDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(self) -> None:
        self.client = Client()
        self.rout = Rout.objects.create(
            name_start='start',
            name_finish='finish',
            slug='start-finish'
        )
        self.rout.bus_stops.create(bus_stop='Один', delta_time=time(hour=1, minute=1))

        self.url = reverse('rout_detail', args=['start-finish'])

    def test_url_exists(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'routes_detail.html')


class BusDetailsViewTest(TestCase):
    @classmethod
    def setUpTestData(self) -> None:
        BusDetails.objects.create(
            bus_model='B',
            bus_number=2222,
            slug='b-2222',
            bus_colour='Синий',
            bus_photo=SimpleUploadedFile('test_image3.jpg', content=b'\test'),
            number_sites=15, bus_rating=5
        )

        self.url = reverse('bus_detail', args=['b-2222'])

    def test_url_exists(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'bus_detail.html')

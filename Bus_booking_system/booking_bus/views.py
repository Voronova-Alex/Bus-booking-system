import datetime

from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView, DeleteView, UpdateView)
from .models import NewTrip, TicketTrip, TripsUser
from .forms import NewTripForm
from booking_app.models import Rout, BookingPrice, BusStop, RoutesTravelDatesTimes, BusDetails
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from datetime import timedelta, datetime


class ChoiceTripListView(LoginRequiredMixin, ListView):
    model = Rout
    template_name = 'choice_trip.html'


class NewTripCreateView(LoginRequiredMixin, CreateView):
    form_class = NewTripForm
    template_name = 'booking_detail.html'


    def get_form_kwargs(self):
        kwargs = super(NewTripCreateView, self).get_form_kwargs()
        kwargs['slug'] = self.request.build_absolute_uri().split('/')[-2]
        kwargs['rout'] = Rout.objects.get(slug=kwargs['slug'])
        print(kwargs)
        return kwargs

    def get_success_url(self):
        return reverse('home-page')

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user
        slug = self.request.build_absolute_uri().split('/')[-2]
        rout = Rout.objects.get(slug=slug)
        initial['rout_trip'] = Rout.objects.get(slug=slug)
        initial['price_adult'] = BookingPrice.objects.get(price_rout=rout).price_adult
        initial['price_child'] = BookingPrice.objects.get(price_rout=rout).price_child
        initial['price_baggage'] = BookingPrice.objects.get(price_rout=rout).price_baggage
        return initial

    def get_absolute_url(self):
        return reverse('booking_info', args=[str(self.id)])

    def get_slug(self):
        return self.request.build_absolute_uri().split('/')[-2]


    def form_valid(self, form):
        self.object = form.save(commit=False)
        slug = self.request.build_absolute_uri().split('/')[-2]
        rout = Rout.objects.get(slug=slug)
        self.object.user = self.request.user
        self.object.price_adult = BookingPrice.objects.get(price_rout=rout).price_adult
        self.object.price_child = BookingPrice.objects.get(price_rout=rout).price_child
        self.object.price_baggage = BookingPrice.objects.get(price_rout=rout).price_baggage
        if (datetime.now()-timedelta(days=1)) < datetime.combine(self.object.rout_data_time.travel_date, self.object.rout_data_time.travel_time):
            self.object.status = 'Сonfirmed'
        return super().form_valid(form)

class TicketTripView(LoginRequiredMixin, DetailView):
    model = TicketTrip
    template_name = 'order_info.html'

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return TicketTrip.objects.get(trip_id=pk_)




class NewTripView(LoginRequiredMixin, ListView):
    model = NewTrip

    template_name = 'booking_list.html'

    def get_queryset(self):
        return NewTrip.objects.filter(user=self.request.user,  status_trip=False)


class OldTripView(LoginRequiredMixin, ListView):
    model = NewTrip

    template_name = 'booking_list_old.html'

    def get_queryset(self):
        return NewTrip.objects.filter(user=self.request.user, status_trip=True)


class NewTripInfoView(LoginRequiredMixin, DetailView):
    model = NewTrip

    template_name = 'booking_info.html'

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        ticket = NewTrip.objects.get(id=pk_)
        time_start_list = (str(ticket.rout_data_time).split(' ')[-1]).split(':')
        time_start = datetime(year=2000, month=1, day=1, hour=int(time_start_list[0]), minute=int(time_start_list[1]), second=int(time_start_list[2]))
        time_on_stop = BusStop.objects.get(bus_stop=ticket.bus_stop).delta_time
        delta_time = timedelta(days=1, hours=time_on_stop.hour, minutes=time_on_stop.minute, seconds=time_on_stop.second)
        bus_info = ticket.rout_data_time.bus
        bus_slug = ticket.rout_data_time.bus.slug
        if TicketTrip.objects.filter(trip_id=pk_).exists():
            ticket_trip = TicketTrip.objects.get(trip_id=pk_)
            ticket_trip.rout_data_time = str(ticket.rout_data_time).split(' ')[1]
            ticket_trip.bus_stop = str(ticket.bus_stop)
            ticket_trip.time_stop = time_start + delta_time
            ticket_trip.total_cost = ticket.price_adult * ticket.quantity_adult + ticket.price_child * ticket.quantity_child + ticket.price_baggage * ticket.quantity_baggage
            ticket_trip.bus_info = str(bus_info)
            ticket_trip.bus_slug = bus_slug
            ticket_trip.save()
        else:
            ticket_trip = TicketTrip(trip=ticket, rout_data_time=str(ticket.rout_data_time).split(' ')[1],
                                     bus_stop=ticket.bus_stop, time_stop=(time_start + delta_time),
                                     total_cost=ticket.price_adult * ticket.quantity_adult + ticket.price_child * ticket.quantity_child + ticket.price_baggage * ticket.quantity_baggage,
                                     bus_info=bus_info, bus_slug=bus_slug)
            ticket_trip.save()
        return NewTrip.objects.get(id=pk_)

class NewTripUpdateView(LoginRequiredMixin, UpdateView):

    Model = NewTrip

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return NewTrip.objects.get(id=pk_)




    template_name = 'booking_detail.html'
    fields = ['phone', 'quantity_adult', 'quantity_child', 'quantity_baggage', 'comment', 'status', 'paid']
    exclude = ['many_to_many_field']

    success_url = reverse_lazy('booking_list')




class NewTripDeleteView(LoginRequiredMixin, DeleteView):
    model = NewTrip

    success_url = reverse_lazy('booking_list')
    template_name = 'booking_delete.html'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить бронь'
        trip = NewTrip.objects.get(pk=self.kwargs.get('pk'))
        if trip.status == 'Сonfirmed':
            context['status'] = 'Сonfirmed'
            context['message'] = f'Подтвержденную поездку удалить нельзя'
            context['cancel_url'] = 'booking_list'
        else:
            context['message'] = f'Поездка {trip.rout_trip}\n' \
                             f'{trip.rout_data_time}'
            context['cancel_url'] = 'booking_list'
            user_id = self.request.user.id
            if TripsUser.objects.filter(user_id=user_id).exists():
                trip_user = TripsUser.objects.get(user_id=user_id)
                trip_user.quantity_delete_booked_trip += 1
                trip_user.save()
            else:
                trip_user = TripsUser(user_id=user_id, quantity_delete_booked_trip=1, quantity_autodelete_trip=0,
                                      quantity_default_trip=0)
                trip_user.save()
        return context


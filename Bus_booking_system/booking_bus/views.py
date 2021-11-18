from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView, DeleteView, UpdateView)
from .models import NewTrip
from .forms import NewTripForm
from booking_app.models import Rout, BookingPrice, BusStop, RoutesTravelDatesTimes, BusDetails
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


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
        print(self.request.build_absolute_uri().split('/')[-2])
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
"""
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.rout_trip = self.initial['rout_trip']
        self.object.price_adult = self.initial['price_adult']
        self.object.price_child = self.initial['price_child']
        self.object.price_baggage = self.initial['price_baggage']
        # bus = RoutesTravelDatesTimes.object.get(rout=self.object.rout_trip).bus
        # bus_change = BusDetails.get(bus=self.object.rout_trip)
        self.object.save()"""




class NewTripView(LoginRequiredMixin, ListView):
    model = NewTrip

    template_name = 'booking_list.html'

    def get_queryset(self):
        return NewTrip.objects.filter(user=self.request.user,  status_trip=False)

class NewTripInfoView(LoginRequiredMixin, DetailView):
    model = NewTrip

    template_name = 'booking_info.html'
    success_url = reverse_lazy('booking_list')



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
        context['message'] = f'Поездка {trip.rout_trip}\n' \
                             f'{trip.rout_data_time}'
        context['cancel_url'] = 'booking_list'
        return context

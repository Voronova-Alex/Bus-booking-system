from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView, DeleteView, UpdateView)
from .models import NewTrip
from .forms import NewTripForm
from booking_app.models import Rout, BookingPrice
from django.contrib.auth.mixins import LoginRequiredMixin


class NewTripCreateView(LoginRequiredMixin, CreateView):
    form_class = NewTripForm
    template_name = 'booking_detail.html'

    def get_success_url(self):
        return reverse('home-page')

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user


        return initial



class NewTripView(LoginRequiredMixin, ListView):
    model = NewTrip

    template_name = 'booking_list.html'

    def get_queryset(self):
        return NewTrip.objects.filter(user=self.request.user)




class NewTripUpdateView(LoginRequiredMixin, UpdateView):
    model = NewTrip
    fields = '__all__'
    template_name = 'booking_detail.html'

class NewTripDeleteView(LoginRequiredMixin, DeleteView):
    model = NewTrip

    success_url = 'booking_list'
    template_name = 'booking_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить бронь'
        trip = NewTrip.objects.get(pk=self.kwargs.get('pk'))
        context['message'] = f'Поездка {trip.rout_trip}\n' \
                             f'{trip.rout_data_time}'
        context['cancel_url'] = 'booking_list'
        return context


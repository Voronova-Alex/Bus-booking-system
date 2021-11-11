from django.shortcuts import render, reverse
from django.views.generic import (ListView, DetailView, CreateView, DeleteView, UpdateView)
from .models import Rout, RoutesTravelDatesTimes, BookingPrice, BusDetails, BusStop

def home(request):
    return render(request, 'index.html')


class RoutListView(ListView):
    model = Rout
    template_name = 'routes_list.html'


class RoutDetailView(DetailView):
    model = Rout
    template_name = 'routes_detail.html'

class BusListView(ListView):
    model = BusDetails
    template_name = 'bus_list.html'


class BusDetailsView(DetailView):
    model = BusDetails
    template_name = 'bus_detail.html'





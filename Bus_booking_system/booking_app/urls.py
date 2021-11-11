from django.urls import path

from .views import RoutDetailView, RoutListView, home, BusListView, BusDetailsView



urlpatterns = [
    path('', home, name='home-page'),
    path('rout', RoutListView.as_view(), name='rout_list'),
    path('rout/<slug:slug>', RoutDetailView.as_view(), name='rout_detail'),
    path('bus', BusListView.as_view(), name='bus_list'),
    path('bus/<slug:slug>', BusDetailsView.as_view(), name='bus_detail'),

]

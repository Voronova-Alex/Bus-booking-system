from django.contrib import admin
from .models import BusDetails,  Rout, BusStop, BookingPrice, RoutesTravelDatesTimes

@admin.register(BusDetails)
class BusDetailsAdmin(admin.ModelAdmin):
    list_display = 'bus_model', 'bus_number', 'bus_colour', 'number_sites', 'bus_rating', 'slug'
    prepopulated_fields = {'slug': ('bus_model', 'bus_number',)}

@admin.register(Rout)
class RoutAdmin(admin.ModelAdmin):
    list_display = ('name_start', 'name_finish', 'slug',  )
    prepopulated_fields = {'slug': ('name_start', 'name_finish',)}

@admin.register(BusStop)
class BusStopAdmin(admin.ModelAdmin):
    list_display = ('bus_stop', 'delta_time')

@admin.register(BookingPrice)
class BookingPriceAdmin(admin.ModelAdmin):
    list_display = ('price_rout', 'price_adult', 'price_child', 'price_baggage', )
    list_editable = ('price_adult', 'price_child', 'price_baggage',)

@admin.register(RoutesTravelDatesTimes)
class RoutesTravelDatesTimesAdmin(admin.ModelAdmin):
    list_display = ('rout', 'bus', 'travel_date', 'travel_time')
    list_editable = ('bus', 'travel_date', 'travel_time')

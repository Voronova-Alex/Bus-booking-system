from .models import NewTrip, Reviews
from booking_app.models import Rout, RoutesTravelDatesTimes, BookingPrice, BusStop
from django import forms
from datetime import datetime



class NewTripForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        slug = kwargs.pop('slug')
        rout = kwargs.pop('rout')
        super().__init__(*args, **kwargs)
        super(NewTripForm, self).__init__(*args, **kwargs)
        self.fields['bus_stop'].queryset = BusStop.objects.filter(rout__slug__contains=slug)
        self.fields['rout_data_time'].queryset = RoutesTravelDatesTimes.objects.filter(rout=rout, travel_date__gte=datetime.now().date()).exclude(rout=rout, travel_date=datetime.now().date(), travel_time__lt=datetime.now().time())

    class Meta:
        model = NewTrip
        fields = ['user', 'phone', 'rout_trip', 'rout_data_time', 'bus_stop', 'quantity_adult',
                  'quantity_child', 'quantity_baggage', 'price_adult',
                  'price_child', 'price_baggage', 'comment', 'status', 'paid']


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['bus_rating', 'comment']
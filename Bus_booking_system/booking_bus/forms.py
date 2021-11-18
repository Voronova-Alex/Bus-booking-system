from .models import NewTrip
from booking_app.models import Rout, RoutesTravelDatesTimes, BookingPrice, BusStop
from django import forms


class NewTripForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        slug = kwargs.pop('slug')
        rout = kwargs.pop('rout')
        super().__init__(*args, **kwargs)
        super(NewTripForm, self).__init__(*args, **kwargs)
        self.fields['bus_stop'].queryset = BusStop.objects.filter(rout__slug__contains=slug)
        self.fields['rout_data_time'].queryset = RoutesTravelDatesTimes.objects.filter(rout=rout)

    class Meta:
        model = NewTrip
        fields = ['user', 'phone', 'rout_trip', 'rout_data_time', 'bus_stop', 'quantity_adult',
                  'quantity_child', 'quantity_baggage', 'price_adult',
                  'price_child', 'price_baggage', 'comment', 'status', 'paid']

"""

class UpdateTripForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        name_start = kwargs.pop('rout').split('-')[0]
        super().__init__(*args, **kwargs)
        super(UpdateTripForm, self).__init__(*args, **kwargs)
        self.fields['bus_stop'].queryset = BusStop.objects.filter(name_start__slug__contains=name_start)

    class Meta:
        model = NewTrip
        fields = ['phone', 'rout_trip', 'bus_stop', 'quantity_adult',
                  'quantity_child', 'quantity_baggage', 'comment', 'status', 'paid']

"""
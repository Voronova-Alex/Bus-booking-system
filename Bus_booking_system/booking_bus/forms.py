from .models import NewTrip
from booking_app.models import Rout, RoutesTravelDatesTimes, BookingPrice, BusStop
from django import forms




class NewTripForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        slug = kwargs.pop('slug')
        rout = kwargs.pop('rout')
        super().__init__(*args, **kwargs)
        super(NewTripForm, self).__init__(*args, **kwargs)
        self.fields['bus_stop'].queryset = Rout.objects.filter(slug=slug).distinct().values_list('bus_stops', flat=True)
        self.fields['rout_data_time'].queryset = RoutesTravelDatesTimes.objects.filter(rout=rout)






    class Meta:
        model = NewTrip
        fields = ['user', 'phone', 'rout_trip', 'rout_data_time', 'bus_stop', 'quantity_adult',
                  'quantity_child', 'quantity_baggage', 'price_adult',
                  'price_child', 'price_baggage', 'comment', 'status', 'paid']


from .models import NewTrip
from booking_app.models import Rout, RoutesTravelDatesTimes, BookingPrice, BusStop
from django import forms
from .fields import GroupedModelChoiceField



class NewTripForm(forms.ModelForm):

    class Meta:
        model = NewTrip
        fields = ['user', 'phone', 'rout_trip', 'rout_data_time', 'bus_stop', 'quantity_adult',
                  'quantity_child', 'quantity_baggage', 'price_adult',
                  'price_child', 'price_baggage', 'total_cost', 'comment', 'status', 'paid']





'''    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'rout_trip' in self.data:
            try:
                rout_trip_id = int(self.data.get('rout_trip'))
                self.fields['rout_data_time'].queryset = RoutesTravelDatesTimes.objects.filter(id=rout_trip_id)
                self.fields['bus_stop'].queryset = BusStop.objects.filter(id=rout_trip_id)
                self.fields['price_adult'].queryset = BookingPrice.filter(id=rout_trip_id)
                self.fields['price_child'].queryset = BookingPrice.filter(id=rout_trip_id)
                self.fields['price_baggage'].queryset = BookingPrice.filter(id=rout_trip_id)
            except (ValueError, TypeError):
                return HttpResponse('Идиотка')

        elif self.instance.pk:
            self.fields['rout_data_time'].queryset = self.instance.rout_trip.routestraveldatestimes_set
            self.fields['bus_stop'].queryset = self.instance.rout_trip.busstop_set
            self.fields['price_adult'].queryset = self.instance.rout_trip.bookingprice_set
            self.fields['price_child'].queryset = self.instance.rout_trip.bookingprice_set
            self.fields['price_baggage'].queryset = self.instance.rout_trip.bookingprice_set

'''


'''  def __init__(self, rout_trip, *args, **kwargs):
        super(NewTripForm, self).__init__(*args, **kwargs)
        self.fields['rout_data_time'].queryset = RoutesTravelDatesTimes.objects.filter(rout=rout_trip)'''

'''
    price_adult = GroupedModelChoiceField(
        queryset=BookingPrice.objects.values_list('price_adult', 'price_rout'),
        choices_groupby='price_rout'
    )
'''
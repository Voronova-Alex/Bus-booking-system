from django.core.management.base import BaseCommand
from booking_bus.models import NewTrip, TripsUser, TicketTrip
from booking_app.models import RoutesTravelDatesTimes
from datetime import datetime, timedelta

DAYS_B = timedelta(days=1)


class Command(BaseCommand):

    def add_argument(self):
        pass

    def handle(self, *args, **options):
        rout_data_time_query = list(RoutesTravelDatesTimes.objects.filter(travel_date=(datetime.now() + DAYS_B)))
        rout_data_time_list = []
        user_list = []
        for i in range(len(rout_data_time_query)):
            if rout_data_time_query[i] in rout_data_time_list:
                pass
            else:
                rout_data_time_list.append(rout_data_time_query[i])

        for i in rout_data_time_list:
            user_query = NewTrip.objects.filter(rout_data_time=i, status='Забронировать')
            print(user_query)
            for i in user_query:
                user_list.append(i.user)
            print(user_list)
        for i in rout_data_time_list:
            NewTrip.objects.filter(rout_data_time=i, status='Забронировать').delete()
        for user in user_list:
            new_trip = TripsUser.objects.get(user__username=user)
            new_trip.quantity_autodelete_trip += 1
            new_trip.save()

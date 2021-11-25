from django.contrib import admin
from .models import NewTrip, TripsUser, TicketTrip, Reviews


admin.site.register(NewTrip)

admin.site.register(TripsUser)

admin.site.register(TicketTrip)

admin.site.register(Reviews)
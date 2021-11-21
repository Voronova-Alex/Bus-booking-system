from django.urls import path

from .views import NewTripView, NewTripCreateView, NewTripDeleteView, NewTripUpdateView, ChoiceTripListView, \
    NewTripInfoView, TicketTripView

urlpatterns = [
    path('booking', NewTripView.as_view(), name='booking_list'),
    path('booking/choice/', ChoiceTripListView.as_view(), name='choice_trip'),
    path('booking/choice/<slug:slug>/', NewTripCreateView.as_view(), name='new_booking'),
    path('booking/choice/<int:pk>/delete/', NewTripDeleteView.as_view(), name='booking_delete'),
    path('booking/choice/<int:pk>/update/', NewTripUpdateView.as_view(), name='booking_update'),
    path('booking/choice/<int:pk>/info/', NewTripInfoView.as_view(), name='booking_info'),
    path('booking/choice/<int:pk>/order/', TicketTripView.as_view(), name='order'),

]

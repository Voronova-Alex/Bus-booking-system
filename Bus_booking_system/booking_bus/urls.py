from django.urls import path


from .views import NewTripView, NewTripCreateView, NewTripDeleteView, NewTripUpdateView


urlpatterns = [
    path('booking', NewTripView.as_view(), name='booking_list'),
    path('booking/new', NewTripCreateView.as_view(), name='new_booking'),
    path('booking/<int:pk>/delete/', NewTripDeleteView.as_view(), name='booking_delete'),
    path('booking/<int:pk>/update/', NewTripUpdateView.as_view(), name='booking_update'),

]


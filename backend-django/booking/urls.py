from django.urls import path
from .views import BookingCreateView, BookingListView, BookingDetailView

urlpatterns = [
    path('api/bookings/', BookingCreateView.as_view(), name='booking-create'),       
    path('api/bookings/list/', BookingListView.as_view(), name='booking-list'),
    path('api/bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
]
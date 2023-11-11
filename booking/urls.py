from django.urls import path
from . import views
from .views import booking, make_booking, booking_confirmation

urlpatterns = [
    path('booking/', views.booking, name='booking'),
    path('make_booking/', views.make_booking, name='make_booking'),
    path('booking_confirmation/', views.booking_confirmation, name='booking_confirmation'),
]


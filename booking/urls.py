from django.urls import path
from . import views
from .views import booking, make_booking, booking_confirmation, edit_booking, delete_booking

urlpatterns = [
    path('booking/', views.booking, name='booking'),
    path('make_booking/', views.make_booking, name='make_booking'),
    path('booking_confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
]


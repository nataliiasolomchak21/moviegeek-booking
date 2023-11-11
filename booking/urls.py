from django.urls import path
from . import views
from .views import booking, make_booking

urlpatterns = [
    path('booking/', views.booking, name='booking'),
    path('make_booking/', views.make_booking, name='make_booking'),
]


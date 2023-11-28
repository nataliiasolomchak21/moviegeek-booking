from django.urls import path
from . import views
from .views import (
    booking,
    make_booking,
    booking_confirmation,
    edit_booking,
    delete_booking,
)

urlpatterns = [
    path("booking/", booking, name="booking"),
    path("make_booking/", make_booking, name="make_booking"),
    path("booking_confirmation/", booking_confirmation, name="booking_confirmation"),
    path("edit_booking/<int:booking_id>/", edit_booking, name="edit_booking"),
    path("delete_booking/<int:booking_id>/", delete_booking, name="delete_booking"),
]

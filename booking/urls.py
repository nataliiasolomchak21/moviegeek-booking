from .views import booking, occupiedSeats

app_name='moviegeek'

urlpatterns = [
    path('booking/', booking, name="booking"),
    path('occupied/', occupiedSeats, name="occupied_seat")
]
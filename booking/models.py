from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    title=models.CharField(max_length=255)
    price=models.IntegerField()
    date=models.DateField(default='2024-01-01')
    time=models.TimeField(default='00:00')
    booked_seats=models.ManyToManyField('Seat', blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title} (${self.price}) - {self.date} {self.time} "


class Seat(models.Model):
    seat_num=models.IntegerField()
    booking_username=models.CharField(max_length=255)
    booking_email=models.EmailField(max_length=555)
    booking_time=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.booking_username} seat_num {self.seat_num}"
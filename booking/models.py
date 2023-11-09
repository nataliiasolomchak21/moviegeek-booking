from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    title=models.CharField(max_length=255)
    price=models.IntegerField()
    booked_seats=models.ManyToManyField('Seat', null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title} (${self.price})"
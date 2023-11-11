from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=12.00)

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    num_seats = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

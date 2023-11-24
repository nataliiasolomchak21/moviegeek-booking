from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    rating = models.CharField(max_length=5, default='PG')
    genre = models.CharField(max_length=50, default='Default genre')
    year = models.PositiveIntegerField(default=2023)
    trailer_url = models.URLField(default='https://www.example.com/default_trailer')
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField(default='Some default description')
    
    def __str__(self):
        return f"{self.title}"

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    num_seats = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.movie.title} - {self.date} {self.time}"

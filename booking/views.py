from django.shortcuts import render
from .models import Booking

def index(request):
    return render(request, 'index.html')

def booking(request):
    movies=Movie.objects.all
    return render(request, 'booking.html', {
        "movies": movies
    })
from django.shortcuts import render
from .models import Booking

def index(request):
    return render(request, 'index.html')

def booking(request):

  movies = Booking.objects.all()

  dates = ['2024-01-24', '2024-01-26', '2024-01-28']
  times = ['12:00', '15:00', '18:00']

  context = {
    'movies': movies,
    'dates': dates, 
    'times': times
  }

  return render(request, 'booking.html', context)
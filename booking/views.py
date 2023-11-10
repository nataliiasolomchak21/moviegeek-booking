from django.shortcuts import render
from django.http import JsonResponse
from .models import Booking

import json

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


def occupiedSeats(request):
  data=json.loads(request.body)

  movie=Booking.object.get(title=data["movie_title"])
  occupied=movie.booked_seats.all()
  occupied_seats=list(map(lambda seat : seat.seat_num -1, occupied))

  return JsonResponse({
    "occupied_seats": occupied_seat,
    "movie": str(movies)
  })
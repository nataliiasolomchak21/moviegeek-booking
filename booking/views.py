from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Movie, Booking
from datetime import date, time
from django.contrib import messages


def index(request):
    return render(request, "index.html")

def booking(request):
    movies = Movie.objects.all()
    dates = ['2024-01-24', '2024-01-26', '2024-01-30']
    times = ['12:00', '15:00', '19:00']

    context = {
        'movies': movies,
        'dates': dates,
        'times': times,
    }

    return render(request, 'booking.html', context)

def make_booking(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie')
        num_seats = request.POST.get('seats')
        date = request.POST.get('date')
        time = request.POST.get('time')

        movie = Movie.objects.get(pk=movie_id)
        total_price = int(num_seats) * movie.price

        booking = Booking.objects.create(
            movie=movie,
            num_seats=num_seats,
            date=date,
            time=time,
            total_price=total_price
        )

        return redirect('booking')  # Redirect to the booking page or any other page

    return redirect('booking')  # Redirect to the booking page in case of a GET request

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Movie, Booking
from datetime import date, time
from django.contrib import messages
from .forms import BookingForm


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

        return redirect('booking_confirmation')  # Redirect to the booking page or any other page

    return redirect('booking')  # Redirect to the booking page in case of a GET request


def profile(request):
    # Retrieve all bookings for the user 
    bookings = Booking.objects.all()  

    booking_info_list = []

    for booking in bookings:
        booking_info = {
            'id': booking.id, 
            'movie_title': booking.movie.title,
            'date': booking.date,
            'time': booking.time,
            'seats': booking.num_seats,
            'total_price': booking.total_price,
        }
        booking_info_list.append(booking_info)

    context = {
        'booking_info_list': booking_info_list,
    }

    return render(request, "profile.html", context)


def booking_confirmation(request):
    return render(request, 'booking_confirmation.html')

def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_confirmation')

    else:
        form = BookingForm(instance=booking)

    movies = Movie.objects.all()
    dates = ['2024-01-24', '2024-01-26', '2024-01-30']
    times = ['12:00', '15:00', '19:00']

    context = {
        'form': form,
        'booking_id': booking_id,
        'movies': movies,
        'dates': dates,
        'times': times,
    }

    return render(request, 'edit_booking.html', context)



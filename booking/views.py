from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Movie, Booking
from django.contrib import messages
from .forms import BookingForm


def index(request):
    """
    Renders the index page with a list of all movies.
    """
    movies = Movie.objects.all()
    return render(request, "index.html", {"movies": movies})


def booking(request):
    """
    Renders the booking page with a list of movies, dates, and times.
    """
    movies = Movie.objects.all()
    dates = ["2024-01-24", "2024-01-26", "2024-01-30"]
    times = ["12:00", "15:00", "19:00"]

    context = {
        "movies": movies,
        "dates": dates,
        "times": times,
    }

    return render(request, "booking.html", context)


@login_required
def make_booking(request):
    """
    Handles the creation of a new booking.
    Redirects to the user's profile page on successful edit,
    or renders the edit booking page with the form if the request
    method is not POST.
    """
    if request.method == "POST":
        movie_id = request.POST.get("movie")
        num_seats = request.POST.get("seats")
        date = request.POST.get("date")
        time = request.POST.get("time")

        movie = Movie.objects.get(pk=movie_id)
        total_price = int(num_seats) * movie.price

        user = request.user
        booking = Booking.objects.create(
            user=user,
            movie=movie,
            num_seats=num_seats,
            date=date,
            time=time,
            total_price=total_price,
        )

        return redirect("booking_confirmation")

    return redirect("booking")


def profile(request):
    """
    Renders the user's profile page with a list of their bookings.
    Returns rendered HTML template with the user's booking information.
    """
    bookings = Booking.objects.filter(user=request.user).order_by("-id")

    booking_info_list = []

    movie_images_dict = {
        "Barbie": "images/barbie-booking.jpg",
        "Oppenheimer": "images/oppenheimer-booking.jpg",
        "Mission Impossible: Dead Reckoning Part One": "images/mi-booking.jpg",
        "Spider-Man: Across The Spiderverse": "images/spiderman-booking.jpg",
    }

    for booking in bookings:
        booking_info = {
            "id": booking.id,
            "movie_title": booking.movie.title,
            "date": booking.date,
            "time": booking.time,
            "seats": booking.num_seats,
            "total_price": booking.total_price,
            "movie_image": movie_images_dict.get(
                booking.movie.title, "images/spiderman-booking.jpg"
            ),
        }
        booking_info_list.append(booking_info)

    context = {
        "booking_info_list": booking_info_list,
    }

    return render(request, "profile.html", context)


def booking_confirmation(request):
    """
    Renders the booking confirmation page.
    """
    return render(request, "booking_confirmation.html")


def edit_booking(request, booking_id):
    """
    Handles editing of a booking.
    Redirects to the user's profile page on successful edit,
    or renders the edit booking page with the form
    if the request method is not POST.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.user != booking.user:
        return HttpResponseForbidden(render(request, "404.html"))

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            movie_price = form.cleaned_data["movie"].price
            num_seats = form.cleaned_data["num_seats"]
            total_price = movie_price * num_seats

            form.instance.total_price = total_price
            form.save()

            messages.success(request, "Booking updated successfully.")
            return redirect("profile")
        else:
            messages.error(
                request, "Error updating booking. Please check the form."
            )
    else:
        form = BookingForm(instance=booking)

    movies = Movie.objects.all()
    dates = ["2024-01-24", "2024-01-26", "2024-01-30"]
    times = ["12:00", "15:00", "19:00"]

    context = {
        "form": form,
        "booking_id": booking_id,
        "movies": movies,
        "dates": dates,
        "times": times,
    }

    return render(request, "edit_booking.html", context)


def delete_booking(request, booking_id):
    """
    Handles the deletion of a booking.
    Redirects to the user's profile page on successful deletion.
    """
    booking = get_object_or_404(Booking, id=booking_id)

    if request.user != booking.user:
        return HttpResponseForbidden(render(request, "404.html"))

    booking.delete()

    messages.success(request, "Booking deleled successfully.")
    return redirect("profile")

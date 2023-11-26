from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Booking


class TestModels(TestCase):

    def setUp(self):
        Movie.objects.create(
            title="Test Movie",
            price=10.99,
            rating="PG",
            genre="Action",
            year=2023,
            trailer_url="https://www.example.com/test_trailer",
            image="test_image.jpg",
            description="Test description",
        )

    def test_movie_str_method(self):
        movie = Movie.objects.get(title="Test Movie")
        self.assertEqual(str(movie), "Test Movie")

class BookingModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser", password="testpass")
        movie = Movie.objects.create(
            title="Test Movie",
            price=10.99,
            rating="PG",
            genre="Action",
            year=2023,
            trailer_url="https://www.example.com/test_trailer",
            image="test_image.jpg",
            description="Test description",
        )
        Booking.objects.create(
            user=user,
            movie=movie,
            num_seats=2,
            date="2024-01-24",
            time="12:00",
            total_price=20.0,
        )

    def test_booking_str_method(self):
        booking = Booking.objects.get(date="2024-01-24")
        expected_str = "Test Movie - 2024-01-24 12:00:00"
        self.assertEqual(str(booking), expected_str)



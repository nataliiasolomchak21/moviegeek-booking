from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Booking
from .forms import BookingForm


class TestForms(TestCase):
    """
    Test cases for forms in the application.
    """

    def setUp(self):
        """
        Set up necessary data for testing.
        """
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

        # Create a test movie
        self.movie = Movie.objects.create(
            title="Test Movie",
            price=10.0,
            rating="PG",
            genre="Action",
            year=2023,
            trailer_url="https://www.example.com/test_trailer",
            description="Test Description",
        )

    def test_valid_booking_form(self):
        """
        Test the BookingForm with valid data.
        """
        data = {
            "movie": self.movie.id,
            "num_seats": 2,
            "date": "2024-01-24",
            "time": "12:00",
        }
        form = BookingForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_booking_form(self):
        """
        Test the BookingForm with invalid data.
        """
        data = {}
        form = BookingForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("movie", form.errors)
        self.assertIn("num_seats", form.errors)
        self.assertIn("date", form.errors)
        self.assertIn("time", form.errors)

    def test_form_initialization(self):
        """
        Test the initialization of BookingForm
        with a Booking instance.
        """
        booking = Booking(
            user=self.user,
            movie=self.movie,
            num_seats=2,
            date="2024-01-24",
            time="12:00",
            total_price=20.0,
        )
        form = BookingForm(instance=booking)
        self.assertEqual(form.initial["movie"], self.movie.id)
        self.assertEqual(form.initial["num_seats"], 2)
        self.assertEqual(form.initial["date"], "2024-01-24")
        self.assertEqual(form.initial["time"], "12:00")

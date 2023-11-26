from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Movie, Booking


class TestViews(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create test movies
        self.movie = Movie.objects.create(title='Test Movie', price=10.0)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_booking_view(self):
        response = self.client.get(reverse('booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')

    def test_make_booking_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Simulate a POST request to make a booking
        response = self.client.post(reverse('make_booking'), {
            'movie': self.movie.id,
            'seats': 2,
            'date': '2024-01-24',
            'time': '12:00',
        })

        # Check if the booking is created and user is redirected
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Booking.objects.count(), 1)

    def test_profile_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_booking_confirmation_view(self):
        response = self.client.get(reverse('booking_confirmation'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking_confirmation.html')

    def test_edit_booking_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Create a test booking
        booking = Booking.objects.create(
            user=self.user,
            movie=self.movie,
            num_seats=2,
            date='2024-01-24',
            time='12:00',
            total_price=20.0,
        )

        response = self.client.get(reverse('edit_booking', args=[booking.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_booking.html')

    def test_delete_booking_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Create a test booking
        booking = Booking.objects.create(
            user=self.user,
            movie=self.movie,
            num_seats=2,
            date='2024-01-24',
            time='12:00',
            total_price=20.0,
        )

        response = self.client.post(reverse('delete_booking', args=[booking.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Booking.objects.count(), 0)


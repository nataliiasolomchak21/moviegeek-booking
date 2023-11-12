from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['movie', 'num_seats', 'date', 'time']

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
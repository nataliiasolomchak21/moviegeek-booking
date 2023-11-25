from django import forms
from .models import Booking
from django.contrib.auth.forms import UserCreationForm

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['movie', 'num_seats', 'date', 'time']

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    
    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
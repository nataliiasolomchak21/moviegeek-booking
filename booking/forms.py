from django import forms
from .models import Booking
from django.contrib.auth.forms import UserCreationForm

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['movie', 'num_seats', 'date', 'time']

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)

class MySignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        pass
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

from django import forms
from django.contrib.auth.models import User
from .models import Event , Booking

class UserSignup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }
#widgets

class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class EventCreateForm(forms.ModelForm):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    class Meta:
        model = Event
        exclude = ['organizer']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['user','event']

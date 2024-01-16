# booking/forms.py
from django import forms

class BookingForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    num_guests = forms.IntegerField(min_value=1, required=True)
    booking_date = forms.DateField(required=True)
    apartment_id = forms.IntegerField(widget=forms.HiddenInput(), required=True)

# booking/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Apartment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    address = models.CharField(max_length=255, default='')
    lat = models.FloatField(default=0, null=True, blank=True, help_text='Latitude')
    long = models.FloatField(default=0, null=True, blank=True, help_text='Longitude')
    max_guest_allowed = models.PositiveIntegerField(default=0, help_text='Maximum guests allowed')
    image = models.ImageField(upload_to='apartment_images/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    
class Booking(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    num_guests = models.IntegerField(default=0) 
    def __str__(self):
        return f"{self.apartment.name} booked on {self.date}"    
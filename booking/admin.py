from django.contrib import admin
from .models import Apartment,Booking
from django.urls import reverse
from django.utils.html import format_html
# Register your models here.

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price_per_night', 'address', 'image')
   
    def book_now_button(self, obj):
        url = reverse('book_now', args=[obj.id])  # Assuming you have a URL pattern named 'book_now'
        return format_html('<a class="button" href="{}">Book Now</a>', url)

    book_now_button.short_description = 'Book Now'


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('apartment_id', 'date', 'user')  # Customize the displayed fields
    list_filter = ('date',)  # Add filters for the date field
    search_fields = ('apartment_id__name', 'admin')      
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Apartment, Booking
from django.core.mail import send_mail
from django.conf import settings
from .forms import BookingForm

class ApartmentListView(View):
    template_name = 'booking/apartment_list.html'

    def get(self, request):
        apartments = Apartment.objects.all()
        return render(request, self.template_name, {'apartments': apartments})

class BookNowView(View):
    template_name = 'booking/book_now.html'

    def get(self, request, apartment_id):
        return render(request, self.template_name, {'apartment_id': apartment_id})

class ConfirmBookingView(View):
    template_name = 'booking/confirm_booking.html'

    def send_welcome_email(self, user_email, apartment_id, booking_date, num_guests):
        subject = 'Booking Confirmation'
        message = f'Thank you for booking Apartment {apartment_id} on {booking_date} for {num_guests} guests.'
        from_email = 'noufalmhd112@gmail.com' 
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)

    def post(self, request):
        form = BookingForm(request.POST)

        if form.is_valid():
            apartment_id = form.cleaned_data['apartment_id']
            booking_date = form.cleaned_data['booking_date']
            num_guests = form.cleaned_data['num_guests']
            user_email = form.cleaned_data['email']

            
            if Booking.objects.filter(apartment_id=apartment_id, date=booking_date).exists():
                error_message = f"Apartment {apartment_id} is not available on {booking_date}. Please select another date."
                messages.error(request, error_message)
                return render(request, self.template_name, {'error_message': error_message})

            
            try:
                default_user = User.objects.get(username='admin')
            except User.DoesNotExist:
                default_user = User.objects.create_user(username='admin', password='1234')  

           
            apartment = Apartment.objects.get(pk=apartment_id)

            
            if num_guests > apartment.max_guest_allowed:
                error_message = f"Number of guests ({num_guests}) exceeds the maximum allowed ({apartment.max_guest_allowed})."
                messages.error(request, error_message)
                return render(request, self.template_name, {'error_message': error_message})

            Booking.objects.create(apartment_id=apartment_id, date=booking_date, num_guests=num_guests, user=default_user)

            confirmation_message = f"Booking confirmed for Apartment {apartment_id} on {booking_date} for {num_guests} guests."
            messages.success(request, confirmation_message)

            
            user_subject = 'Booking Confirmation'
            user_message = f'Thank you for booking Apartment {apartment_id} on {booking_date} for {num_guests} guests.'
            send_mail(user_subject, user_message, settings.EMAIL_HOST_USER, [user_email])

            
            admin_subject = 'New Booking'
            admin_message = f'New booking for Apartment {apartment_id} on {booking_date} for {num_guests} guests.'
            send_mail(admin_subject, admin_message, settings.EMAIL_HOST_USER, ['noufalmhd112@example.com'])  

            return render(request, self.template_name, {'confirmation_message': confirmation_message, 'booking_date': booking_date, 'num_guests': num_guests})
          
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        form = BookingForm()
        return render(request, self.template_name, {'form': form})

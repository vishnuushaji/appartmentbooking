from django.urls import path
from .views import ApartmentListView, BookNowView, ConfirmBookingView

urlpatterns = [
    path('', ApartmentListView.as_view(), name='apartment_list'),
    path('book-now/<int:apartment_id>/', BookNowView.as_view(), name='book_now'),
    path('confirm-booking/', ConfirmBookingView.as_view(), name='confirm_booking'),
    
]

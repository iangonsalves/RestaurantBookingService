"""
Forms for the restaurant app.

This module contains form classes for handling restaurant-related data input and validation.
"""

from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    """
    Form for handling restaurant table bookings.
    
    This form manages the creation and validation of table reservations,
    including duplicate booking checks and required field validation.
    """
    
    class Meta:
        model = Booking
        fields = ["first_name", "reservation_date", "reservation_slot"]

    def clean(self):
        """
        Validate the form data.
        
        Performs the following validations:
        - Checks if all required fields are filled
        - Verifies no duplicate bookings exist for the same date and time slot
        
        Returns:
            dict: The cleaned form data
            
        Raises:
            forms.ValidationError: If any validation fails
        """
        cleaned_data = super().clean()

        # Validate fields
        if not cleaned_data.get("first_name"):
            raise forms.ValidationError("Name is required")
        if not cleaned_data.get("reservation_date"):
            raise forms.ValidationError("Reservation date is required")
        if not cleaned_data.get("reservation_slot"):
            raise forms.ValidationError("Reservation time is required")

        # Retrieve reservation date and slot from cleaned_data
        reservation_date = cleaned_data.get("reservation_date")
        reservation_slot = cleaned_data.get("reservation_slot")

        # Check for duplicate slot booking on the same date
        if Booking.objects.filter(reservation_date=reservation_date, reservation_slot=reservation_slot).exists():
            raise forms.ValidationError("This time slot is already booked. Please choose another time.")

        return cleaned_data

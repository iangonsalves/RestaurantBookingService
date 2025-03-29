from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["first_name", "reservation_date", "reservation_slot"]

    def clean(self):
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

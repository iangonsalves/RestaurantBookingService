from django.db import models


# Create your models here.
class Booking(models.Model):
    """
    Model representing a restaurant booking/reservation.
    
    This model stores information about customer reservations including their name,
    the date of the reservation, and the time slot.
    
    Attributes:
        first_name (CharField): The customer's first name
        reservation_date (DateField): The date of the reservation
        reservation_slot (SmallIntegerField): The time slot number for the reservation (default: 10)
    """
    first_name = models.CharField(max_length=200, blank=False, null=False)  # Required
    reservation_date = models.DateField(blank=False, null=False)  # Required
    reservation_slot = models.SmallIntegerField(default=10, blank=False, null=False)  # Required

    class Meta:
        unique_together = ('reservation_date', 'reservation_slot')  # Prevent duplicate bookings

    def __str__(self): 
        return f"{self.first_name} - {self.reservation_date} - {self.reservation_slot}"


# Add code to create Menu model
class Menu(models.Model):
    """
    Model representing a menu item in the restaurant.
    
    This model stores information about menu items including their name, price,
    description, and an optional image filename.
    
    Attributes:
        name (CharField): The name of the menu item
        price (IntegerField): The price of the menu item
        menu_item_description (TextField): A detailed description of the menu item
        image_filename (CharField): The filename of the menu item's image (optional)
    """
    name = models.CharField(max_length=200) 
    price = models.IntegerField(null=False) 
    menu_item_description = models.TextField(max_length=1000, default='')
    image_filename = models.CharField(max_length=255, blank=True, null=True) 

    def __str__(self):
        return self.name
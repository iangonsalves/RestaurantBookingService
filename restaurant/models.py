from django.db import models


# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200, blank=False, null=False)  # Required
    reservation_date = models.DateField(blank=False, null=False)  # Required
    reservation_slot = models.SmallIntegerField(default=10, blank=False, null=False)  # Required

    class Meta:
        unique_together = ('reservation_date', 'reservation_slot')  # Prevent duplicate bookings

    def __str__(self): 
        return f"{self.first_name} - {self.reservation_date} - {self.reservation_slot}"


# Add code to create Menu model
class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='')
   image_filename = models.CharField(max_length=255, blank=True, null=True) 

   def __str__(self):
      return self.name
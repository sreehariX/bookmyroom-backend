from django.db import models

class Hostel(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    HOSTEL_TYPE_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    total_rooms = models.IntegerField(default=0)
    price_per_booking = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Add this line
    hostel_type = models.CharField(
        max_length=6, 
        choices=HOSTEL_TYPE_CHOICES, 
        default=MALE
    )

    def __str__(self):
        return f"{self.name} ({self.hostel_type})"
 
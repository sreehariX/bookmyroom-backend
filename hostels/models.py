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
    total_rooms = models.IntegerField()
    hostel_type = models.CharField(
        max_length=6, 
        choices=HOSTEL_TYPE_CHOICES, 
        default=MALE
    )

    def __str__(self):
        return f"{self.name} ({self.hostel_type})"
 
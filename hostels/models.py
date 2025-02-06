from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    hostel_type = models.CharField(
        max_length=6, 
        choices=HOSTEL_TYPE_CHOICES, 
        default=MALE
    )

    def __str__(self):
        return f"{self.name} ({self.hostel_type})"
 
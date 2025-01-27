from django.db import models
from hostels.models import Hostel

class Room(models.Model):
    HOSTEL_TYPE_CHOICES = [
        ('available', 'Available'),
        ('booked', 'Booked'),
    ]
    
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()  # Number of people that can stay in the room

    # Event-specific booking details
    people_booked_moodIndigo = models.IntegerField(default=0)
    people_booked_techFest = models.IntegerField(default=0)
    
    availability_status_moodIndigo = models.CharField(
        max_length=20,
        choices=HOSTEL_TYPE_CHOICES,
        default='available'
    )
    availability_status_techFest = models.CharField(
        max_length=20,
        choices=HOSTEL_TYPE_CHOICES,
        default='available'
    )

    def __str__(self):
        return f"{self.room_number} - {self.hostel.name} (MI: {self.availability_status_moodIndigo} ({self.capacity-self.people_booked_moodIndigo}), TF: {self.availability_status_techFest} ({self.capacity-self.people_booked_techFest}))"
 
from django.db import models
from hostels.models import Hostel
from django.db.models.signals import pre_delete
from django.dispatch import receiver

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
 
def update_hostel_on_room_delete(sender, instance, **kwargs):
    hostel = instance.hostel
    if hostel.total_rooms > 0:
        hostel.total_rooms -= 1
        hostel.save()

@receiver(pre_delete, sender='bookings.Booking')
def update_room_on_booking_delete(sender, instance, **kwargs):
    room = instance.room
    event = instance.event
    
    if event == 'Mood Indigo' and room.people_booked_moodIndigo > 0:
        room.people_booked_moodIndigo -= 1
        if room.people_booked_moodIndigo < room.capacity:
            room.availability_status_moodIndigo = 'available'
        room.save()
    elif event == 'Techfest' and room.people_booked_techFest > 0:
        room.people_booked_techFest -= 1
        if room.people_booked_techFest < room.capacity:
            room.availability_status_techFest = 'available'
        room.save()
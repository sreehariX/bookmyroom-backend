from django.db import models
from users.models import User
from rooms.models import Room
from django.core.exceptions import ValidationError

class Booking(models.Model):
    EVENT_CHOICES = [
        ('Mood Indigo', 'Mood Indigo'),
        ('Techfest', 'Techfest')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    event = models.CharField(max_length=20, choices=EVENT_CHOICES, default='Mood Indigo')
    resident_name = models.CharField(max_length=100, help_text="Name of the person staying in the room")

    def save(self, *args, **kwargs):
        if self.event == 'Mood Indigo':
            if self.room.people_booked_moodIndigo >= self.room.capacity:
                raise ValidationError("This room has reached its capacity for Mood Indigo.")
            
            self.room.people_booked_moodIndigo += 1
            if self.room.people_booked_moodIndigo >= self.room.capacity:
                self.room.availability_status_moodIndigo = 'booked'

        elif self.event == 'Techfest':
            if self.room.people_booked_techFest >= self.room.capacity:
                raise ValidationError("This room has reached its capacity for Techfest.")
            
            self.room.people_booked_techFest += 1
            if self.room.people_booked_techFest >= self.room.capacity:
                self.room.availability_status_techFest = 'booked'

        self.room.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.event == 'Mood Indigo':
            if self.room.people_booked_moodIndigo > 0:
                self.room.people_booked_moodIndigo -= 1
                self.room.availability_status_moodIndigo = 'available'
                # self.room.save()

        elif self.event == 'Techfest':
            if self.room.people_booked_techFest > 0:
                self.room.people_booked_techFest -= 1
                self.room.availability_status_techFest = 'available'
                # self.room.save()
        self.room.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.room.room_number} during {self.event} (Resident: {self.resident_name})"
 
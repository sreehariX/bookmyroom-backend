from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

# Custom User model
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)  # Extra field to distinguish admin users
    # Override groups and user_permissions with unique related_name
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )


# Hostel model
class Hostel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    total_rooms = models.IntegerField()

    def __str__(self):
        return self.name

# Room model
class Room(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()  # Number of people that can stay in the room

    def __str__(self):
        return f"{self.room_number} - {self.hostel.name}"

# Booking model
class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Booking by {self.user.username} for {self.room}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['room', 'start_date', 'end_date'],
                name='unique_booking_per_room_per_date'
            ),
        ]
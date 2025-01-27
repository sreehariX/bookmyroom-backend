from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)  # Extra field to distinguish admin users
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # New phone number field
    
    EVENT_CHOICES = [
        ('Mood Indigo', 'Mood Indigo'),
        ('Techfest', 'Techfest'),
    ]
    event = models.CharField(max_length=20, choices=EVENT_CHOICES, default='Mood Indigo')    
    
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

    def __str__(self):
        return self.username
 
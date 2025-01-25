from django.contrib import admin
from .models import User, Hostel, Room, Booking

admin.site.register(User)
admin.site.register(Hostel)
admin.site.register(Room)
admin.site.register(Booking)
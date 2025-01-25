# filepath: /Users/vihaan/Programming/DEVCOM/RoomBooking/newproj/api/serializers.py
from rest_framework import serializers
from .models import User, Hostel, Room, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_admin']

class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = ['id', 'name', 'location', 'total_rooms']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'hostel', 'room_number', 'capacity']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'room', 'start_date', 'end_date', 'status']
from rest_framework import serializers
from .models import Booking
from users.serializers import UserSerializer
from rooms.models import Room
from hostels.models import Hostel  # Assuming a Hostel model exists

class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    room = serializers.PrimaryKeyRelatedField(read_only=True)
    hostel_name = serializers.CharField(write_only=True)
    room_number = serializers.CharField(write_only=True)

    class Meta:
        model = Booking
        fields = ['event', 'resident_name', 'hostel_name', 'room_number', 'room', 'user']

    def create(self, validated_data):
        hostel_name = validated_data.pop('hostel_name')  # Use `name` instead of `number`
        room_number = validated_data.pop('room_number')

        try:
            room = Room.objects.get(hostel__name=hostel_name, room_number=room_number)
        except Room.DoesNotExist:
            raise serializers.ValidationError("Room not found in the specified hostel.")

        validated_data['room'] = room
        return super().create(validated_data)

from rest_framework import serializers
from .models import Booking
from users.serializers import UserSerializer
from rooms.serializers import RoomSerializer

class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    room = RoomSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        """Ensure room availability before booking."""
        room = data.get('room')
        event = data.get('event')

        if event == 'Mood Indigo' and room.people_booked_moodIndigo >= room.capacity:
            raise serializers.ValidationError("This room has reached its capacity for Mood Indigo.")
        
        if event == 'Techfest' and room.people_booked_techFest >= room.capacity:
            raise serializers.ValidationError("This room has reached its capacity for Techfest.")
        
        return data

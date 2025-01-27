from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    available_capacity_moodIndigo = serializers.SerializerMethodField()
    available_capacity_techFest = serializers.SerializerMethodField()
    hostel_name = serializers.ReadOnlyField(source='hostel.name')

    class Meta:
        model = Room
        fields = '__all__'

    def get_available_capacity_moodIndigo(self, obj):
        return obj.capacity - obj.people_booked_moodIndigo

    def get_available_capacity_techFest(self, obj):
        return obj.capacity - obj.people_booked_techFest

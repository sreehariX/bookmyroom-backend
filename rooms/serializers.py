from rest_framework import serializers
from .models import Room
from hostels.models import Hostel

class RoomSerializer(serializers.ModelSerializer):
    available_capacity_moodIndigo = serializers.SerializerMethodField()
    available_capacity_techFest = serializers.SerializerMethodField()
    hostel_name = serializers.CharField(write_only=True)
    hostel = serializers.PrimaryKeyRelatedField(read_only=True)
    hostel_name_display = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ['id','hostel_name_display', 'room_number', 'capacity', 'people_booked_moodIndigo', 
                 'people_booked_techFest', 'availability_status_moodIndigo',
                'available_capacity_moodIndigo','availability_status_techFest',
                 'available_capacity_techFest', 'hostel', 'hostel_name']

    def get_available_capacity_moodIndigo(self, obj):
        return obj.capacity - obj.people_booked_moodIndigo

    def get_available_capacity_techFest(self, obj):
        return obj.capacity - obj.people_booked_techFest

    def get_hostel_name_display(self, obj):
        return obj.hostel.name

    def create(self, validated_data):
        hostel_name = validated_data.pop('hostel_name')
        try:
            hostel = Hostel.objects.get(name=hostel_name)
        except Hostel.DoesNotExist:
            raise serializers.ValidationError({"hostel_name": "Hostel not found"})
        
        validated_data['hostel'] = hostel
        return super().create(validated_data)
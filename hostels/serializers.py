from rest_framework import serializers
from .models import Hostel

class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = ['id', 'name', 'location', 'hostel_type', 'total_rooms']
        read_only_fields = ['total_rooms']

    def get_total_available_rooms(self, obj):
        return obj.rooms.filter(
            availability_status_moodIndigo='available'
        ).count() + obj.rooms.filter(
            availability_status_techFest='available'
        ).count()

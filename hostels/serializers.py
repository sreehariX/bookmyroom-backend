from rest_framework import serializers
from .models import Hostel

class HostelSerializer(serializers.ModelSerializer):
    total_available_rooms = serializers.SerializerMethodField()

    class Meta:
        model = Hostel
        fields = '__all__'

    def get_total_available_rooms(self, obj):
        return obj.rooms.filter(
            availability_status_moodIndigo='available'
        ).count() + obj.rooms.filter(
            availability_status_techFest='available'
        ).count()

from rest_framework import viewsets
from .models import Room
from .serializers import RoomSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

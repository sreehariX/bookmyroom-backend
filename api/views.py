from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets
from .models import User, Hostel, Room, Booking
from .serializers import UserSerializer, HostelSerializer, RoomSerializer, BookingSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class HostelViewSet(viewsets.ModelViewSet):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def get_room_by_number(request,room_number):
    room = Room.objects.get(room_number=room_number)  
    serializer = RoomSerializer(room)
    return JsonResponse(serializer.data)
def example(request):
    return JsonResponse({'key': 'value'})
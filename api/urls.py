# filepath: /Users/vihaan/Programming/DEVCOM/RoomBooking/newproj/api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, HostelViewSet, RoomViewSet, BookingViewSet, get_room_by_number,example

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'hostels', HostelViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('room/<str:room_number>/', get_room_by_number, name='get_room_by_number'),
    path('example/', example, name='example'),
]
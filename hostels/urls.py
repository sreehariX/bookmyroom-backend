from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HostelViewSet

router = DefaultRouter()
router.register(r'hostels', HostelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

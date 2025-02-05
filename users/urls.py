from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, register_user, logout_user, LoginView

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, login_user

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/', include('django.contrib.auth.urls')),
    path('login/', login_user, name='login'),
]

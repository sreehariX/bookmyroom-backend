from django.shortcuts import render
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, login_user, logout_user, register_user

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/', include('django.contrib.auth.urls')),
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
    path('logout/', logout_user, name='logout'),
    path('logout_page/', lambda request: render(request, 'logout.html'), name='logout_page'),

]

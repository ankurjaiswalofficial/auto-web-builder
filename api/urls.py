
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', home),
    path('login', login_view),
    path('register', register),
    path('update-profile', profile_setup),
    path('forgot-password', forgot_password),
]

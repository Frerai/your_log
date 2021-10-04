"""Defines URL patterns for users."""

from django.urls import path, include

from . import views  # importing "views" module from "users"

app_name = 'users'  # to distinguish these URLS from URLS belonging to other apps
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name='register'),
]

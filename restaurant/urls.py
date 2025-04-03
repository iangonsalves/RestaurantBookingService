"""
URL configuration for the restaurant app.

This module defines the URL patterns for the restaurant application,
mapping URLs to their corresponding view functions.
"""

from django.urls import path
from . import views


urlpatterns = [
    # Home page
    path('', views.home, name="home"),
    
    # About page
    path('about/', views.about, name="about"),
    
    # Booking pages
    path('book/', views.book, name="book"),
    path('reservations/', views.all_reservations, name="reservations"),
    path('bookings', views.bookings, name='bookings'),
    
    # Menu pages
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  # Individual menu item view
]
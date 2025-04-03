"""
Django application configuration for the restaurant app.

This module defines the configuration class for the restaurant application,
including settings like the default auto field and application name.
"""

from django.apps import AppConfig


class RestaurantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restaurant'


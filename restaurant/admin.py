"""
Django admin configuration for the restaurant app.

This module registers models to be managed through the Django admin interface.
"""

from django.contrib import admin

# Register your models here.
from .models import Menu


admin.site.register(Menu)
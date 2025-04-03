"""
Django admin configuration for the restaurant app.

This module registers models to be managed through the Django admin interface.
"""

from django.contrib import admin

# Register your models here.
from .models import Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'menu_item_description')
    list_filter = ('category',)
    search_fields = ('name', 'menu_item_description')
    ordering = ('category', 'name')
    
    # Optimize the queryset to reduce database queries
    def get_queryset(self, request):
        return super().get_queryset(request).defer('menu_item_description')
    
    # Cache the admin index page
    def get_admin_index_page(self):
        return super().get_admin_index_page()
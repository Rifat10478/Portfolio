from django.contrib import admin
from .models import ContactMessage
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display, list_filter, search_fields = ("name", "email", "project_type", "status", "created_at"), ("status",), ("name", "email")

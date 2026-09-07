from django.contrib import admin
from .models import Project
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display, prepopulated_fields = ("title", "category", "featured"), {"slug": ("title",)}

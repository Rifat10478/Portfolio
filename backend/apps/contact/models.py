from django.db import models
class ContactMessage(models.Model):
    class Status(models.TextChoices): NEW = "new", "New"; READ = "read", "Read"; ARCHIVED = "archived", "Archived"
    name = models.CharField(max_length=100)
    email = models.EmailField()
    project_type = models.CharField(max_length=100)
    message = models.TextField(max_length=3000)
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return f"{self.name} — {self.project_type}"

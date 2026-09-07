from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=80)
    short_description = models.CharField(max_length=240)
    description = models.TextField(blank=True)
    technologies = models.JSONField(default=list)
    features = models.JSONField(default=list)
    image = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-featured", "-created_at"]

    def __str__(self): return self.title

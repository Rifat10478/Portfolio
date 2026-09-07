# Generated manually for the initial portfolio schema.
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [migrations.CreateModel(
        name="Project",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("title", models.CharField(max_length=120)), ("slug", models.SlugField(unique=True)),
            ("category", models.CharField(max_length=80)), ("short_description", models.CharField(max_length=240)),
            ("description", models.TextField(blank=True)), ("technologies", models.JSONField(default=list)),
            ("features", models.JSONField(default=list)), ("image", models.URLField(blank=True)),
            ("github_url", models.URLField(blank=True)), ("live_url", models.URLField(blank=True)),
            ("featured", models.BooleanField(default=True)), ("created_at", models.DateTimeField(auto_now_add=True)),
        ], options={"ordering": ["-featured", "-created_at"]},
    )]

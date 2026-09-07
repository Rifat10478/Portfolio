from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [migrations.CreateModel(
        name="ContactMessage",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(max_length=100)), ("email", models.EmailField(max_length=254)),
            ("project_type", models.CharField(max_length=100)), ("message", models.TextField(max_length=3000)),
            ("status", models.CharField(choices=[("new", "New"), ("read", "Read"), ("archived", "Archived")], default="new", max_length=12)),
            ("created_at", models.DateTimeField(auto_now_add=True)), ("updated_at", models.DateTimeField(auto_now=True)),
        ],
    )]

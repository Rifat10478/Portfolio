from django.contrib import admin
from django.urls import include, path

urlpatterns = [path("admin/", admin.site.urls), path("api/projects/", include("apps.projects.urls")), path("api/contact/", include("apps.contact.urls"))]

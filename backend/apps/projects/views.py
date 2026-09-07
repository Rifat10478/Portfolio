from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Project
from .serializers import ProjectSerializer
class ProjectListView(ListAPIView):
    queryset, serializer_class = Project.objects.filter(featured=True), ProjectSerializer
class ProjectDetailView(RetrieveAPIView):
    queryset, serializer_class, lookup_field = Project.objects.all(), ProjectSerializer, "slug"

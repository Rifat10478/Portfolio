from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .models import ContactMessage
from .serializers import ContactMessageSerializer
class ContactMessageView(CreateAPIView):
    queryset, serializer_class, permission_classes = ContactMessage.objects.all(), ContactMessageSerializer, [AllowAny]

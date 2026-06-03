from rest_framework import viewsets
from tools.models import Tool
from .serializers import ToolSerializer

class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
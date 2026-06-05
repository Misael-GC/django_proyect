from rest_framework import viewsets
from ..models import Herramienta
from .serializers import HerramientaSerializer

class HerramientaViewSet(viewsets.ModelViewSet):
    queryset = Herramienta.objects.all()
    serializer_class = HerramientaSerializer
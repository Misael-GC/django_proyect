# usuarios/views.py
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    ViewSet que maneja la lógica de negocio para la exposición
    y gestión del modelo de Usuarios por defecto.
    """
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
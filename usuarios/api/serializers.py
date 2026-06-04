# usuarios/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Exponemos campos seguros y necesarios para el consumo de la API
        fields = ['id', 'username', 'email', 'is_staff', 'is_active']
from rest_framework import serializers
from ..models import Herramienta


class HerramientaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Herramienta
        fields = ['nombre', 'descripcion'] #puede ser '_all__' si quieres incluir todos los campos
        
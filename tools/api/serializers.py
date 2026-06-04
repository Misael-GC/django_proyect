from rest_framework import serializers
from tools.models import Tool


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ['name', 'description'] #puede ser '_all__' si quieres incluir todos los campos
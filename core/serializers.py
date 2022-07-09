from rest_framework import serializers
from .models import usuarios

class UsuariosSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = usuarios
        fields = ['usuario','nombre']
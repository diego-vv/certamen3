from rest_framework import serializers
from myapp.models import Evento

class EventoSerializer(serializers.ModelSerializer):
    tipo_nombre=serializers.CharField(source='tipo.nombre',read_only=True)
    segmento_nombre=serializers.CharField(source='segmento.nombre',read_only=True)
    class Meta:
        model = Evento
        fields = ['id', 'fecha_inicio', 'fecha_termino', 'titulo', 'descripcion', 'tipo', 'tipo_nombre', 'segmento', 'segmento_nombre']
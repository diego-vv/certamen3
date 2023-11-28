from django.shortcuts import render
from rest_framework import viewsets
from myapp.models import Evento 
from .serializer import EventoSerializer
from django_filters.rest_framework import DjangoFilterBackend


class EventoList (viewsets.ModelViewSet):
    queryset=Evento.objects.all()
    serializer_class =EventoSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields=['fecha_inicio', 'fecha_termino', 'tipo__nombre', 'segmento__nombre']


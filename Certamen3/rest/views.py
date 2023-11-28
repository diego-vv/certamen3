from django.shortcuts import render
from rest_framework import generics
from.models import Evento 
from .serializer import EventoSerializer

class EventoList (generics.ListCreateAPIView):
    queryset=Evento.objects.alll
    serializer_calss =EventoSerializer
# Create your views here.

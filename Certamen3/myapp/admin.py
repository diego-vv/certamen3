from django.contrib import admin
from .models import Tipo,Segmento,Evento
admin.user.register(Tipo)
admin.user.register(Segmento)
admin.user.register(Evento)
# Register your models here.

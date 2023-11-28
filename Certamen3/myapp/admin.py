from django.contrib import admin
from .models import Tipo, Segmento, UserProfile
# Register your models here.




# Permite registrar usuarios con determinados rol y demás

#añadimos el registro
admin.site.register(Tipo)
admin.site.register(Segmento)
admin.site.register(UserProfile)
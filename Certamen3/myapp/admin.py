from django.contrib import admin
<<<<<<< HEAD
from .models import Tipo, Segmento, UserProfile
=======
from .models import Tipo,Segmento,Evento

admin.site.register(Tipo)
admin.site.register(Segmento)
admin.site.register(Evento)
>>>>>>> d807a358e5174107db9d24b782f401c2d6b6e82e
# Register your models here.




# Permite registrar usuarios con determinados rol y demás

#añadimos el registro
admin.site.register(Tipo)
admin.site.register(Segmento)
admin.site.register(UserProfile)
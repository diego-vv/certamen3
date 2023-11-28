from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import UserProfile, Segmento, Tipo

def index (request):

    segmentos = Segmento.objects.all()
    tipos = Tipo.objects.all()

    return render(request,'myapp/index.html',{
        "Segmentos": segmentos,
        "Tipos":tipos
    })


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from myapp.models import UserProfile  # Asegúrate de importar tu modelo UserProfile

def login_view(request):
    #Verifica si la solicitud enviada es de método POST
    if request.method == 'POST':
        #Obtiene el valor del formulario en las variables username y password mediante el método POST
        username = request.POST.get('username')
        password = request.POST.get('password')

        #Autentica al usuario desde la base de datos existente en el admin con authenticate
        user = authenticate(request, username=username, password=password)

        #Si el usuario se autentica correctamente
        if user is not None:
            #Inicia sesión mediante la función login implementada por Django, que envía el request y el objeto "user"
            login(request, user)

            try:
                #obtenemos el UserProfile asociado al usuario autenticado
                user_profile = UserProfile.objects.get(user=user)

                # Verifica el rol del usuario a través del UserProfile
                if user_profile.rol.nombre == 'Profesor' or user_profile.rol.nombre == 'Jefe de carrera':
                
                    return redirect('/SU') #re-direccionamos a la página correspondiente por usuario
                else:
    
                    return redirect('/Home') #re-direccionamos a la página correspondiente por usuario
                
            except UserProfile.DoesNotExist:
                # Maneja el caso en el que no se encuentre un UserProfile asociado al usuario y permite que no se genere un error con el pass.
                pass

    return render(request, 'myapp/login.html')

def sus (request):

    return render(request,'myapp/SU.html')

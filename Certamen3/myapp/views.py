from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    titulo= "home"
    datos={
        
    }

    return render (request,'myapp/index.html')
# Create your views here.

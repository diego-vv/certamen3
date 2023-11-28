from django.urls import path, include 
from .views import EventoList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('eventoos',EventoList)

urlpatterns = [
    path('', include(router.urls)),
    
]

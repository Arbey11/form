from django.urls import path
from App10_GestionPedidos.views import contacto

urlpatterns = [
    path('contacto/', contacto),
]
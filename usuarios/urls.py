from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('historial/', views.historial_movimientos, name='historial_movimientos'),
]

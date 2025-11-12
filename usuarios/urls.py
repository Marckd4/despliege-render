from django.urls import path
from . import views
from .views import usuarios_en_linea

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('historial/', views.historial_movimientos, name='historial_movimientos'),
    path('en-linea/', usuarios_en_linea, name='usuarios_en_linea'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('historial/exportar_excel/', views.exportar_excel, name='exportar_excel'),
    path('historial/eliminar_todo/', views.eliminar_todo_historial, name='eliminar_todo_historial'),
    path('historial/', views.historial, name='historial'),
     
    
    
    
]

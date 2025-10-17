from django.urls import path
from . import views

urlpatterns = [
    path('', views.resumen_view, name='resumen_view'),
    path('data/', views.resumen_cod_dun, name='resumen_data'),
    path('exportar_excel/', views.exportar_resumen_excel, name='exportar_resumen_excel'),
    
]

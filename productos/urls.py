from django.urls import path
from . import views

# /productos/.....

app_name = 'productos'
urlpatterns = [
    path('', views.index, name='index'),
    path('editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('<int:producto_id>', views.detalle, name='detalle'),
    path('formulario', views.formulario, name='formulario'),
    path('exportar_excel/', views.exportar_excel, name='exportar_excel'),
    
   
    
]

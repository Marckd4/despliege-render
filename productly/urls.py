"""
URL configuration for productly project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import historial_movimientos

urlpatterns = [
    path('', views.inicio, name="inicio" ),
    path('admin/', admin.site.urls),
    path('productos/' ,include('productos.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('resumen/', include('resumen.urls')),
    path('', include('usuarios.urls')),
    #path('auditoria/historial/', views.auditoria_historial, name='auditoria_historial'),
    #path('historial/', views.historial_movimientos, name='historial_movimientos'),
    
 
    
    
    
]


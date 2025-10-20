from django.shortcuts import render 


def inicio(request):
    return render(
        request,
        'inicio.html',
    )
    
from django.shortcuts import render

def auditoria_historial(request):
    # tu lógica aquí
    return render(request, 'historial.html')


def historial_movimientos(request):
    return render(request, 'auditoria/historial.html')

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroUsuarioForm
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado correctamente. Inicia sesión.')
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('/productos')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

#03
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import MovimientoUsuario

@login_required
def historial_movimientos(request):
    movimientos = MovimientoUsuario.objects.select_related('usuario').order_by('-fecha')
    return render(request, 'usuarios/historial.html', {'movimientos': movimientos})




# 04
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import MovimientoUsuario

@login_required
def historial_movimientos(request):
    movimientos = MovimientoUsuario.objects.select_related('usuario').order_by('-fecha')

    # Filtros opcionales
    usuario_id = request.GET.get('usuario')
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    # Solo filtrar si usuario_id es un número válido
    if usuario_id and usuario_id.isdigit():
        movimientos = movimientos.filter(usuario_id=int(usuario_id))

    if fecha_inicio:
        movimientos = movimientos.filter(fecha__gte=fecha_inicio)
    if fecha_fin:
        movimientos = movimientos.filter(fecha__lte=fecha_fin)

    # Paginación
    paginator = Paginator(movimientos, 1000)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    usuarios = User.objects.all()

    return render(request, 'usuarios/historial.html', {
        'page_obj': page_obj,
        'usuarios': usuarios,
        'usuario_id': usuario_id,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
    })




from django.shortcuts import render
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

def usuarios_en_linea(request):
    ahora = timezone.now()
    hace_5_min = ahora - datetime.timedelta(minutes=5)
    en_linea = User.objects.filter(last_login__gte=hace_5_min)
    return render(request, 'usuarios/en_linea.html', {'usuarios': en_linea})

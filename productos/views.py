from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from productos.forms import ProductoForm
from .models import Producto
from django.contrib.auth.decorators import login_required

# Create your views here.

# productos/
@login_required
def index(request):
    productos = Producto.objects.all()
    
    return render(
        
        request, 
        'index.html',
        context={'productos': productos }
    )
    
    
def detalle(request, producto_id):
    try:
        producto = Producto.objects.get(id=producto_id)
        return render(
            request, 
            'detalle.html', 
            context={'producto': producto})  
    except Producto.DoesNotExist:
        raise Http404()


def formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
        
    else:
            form = ProductoForm()
    
    return render(request,'producto_form.html',{'form': form})



import openpyxl
from django.http import HttpResponse


def exportar_excel(request):
    # Crear un nuevo libro de trabajo y hoja
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Inventario"

    # Encabezados de columnas (según tu tabla)
    columnas = [
        "Categoría", "Empresa", "Ubicación", "Cod EAN", "Cod DUN", "Cod Sistema",
        "Descripción", "Unidad", "Pack", "FactorX", "Cajas", "Saldo", "Stock Físico",
        "Observación", "Fecha Venc", "Fecha Imp", "Contenedor", "Fecha Inv",
        "Encargado", "Acciones"
    ]
    ws.append(columnas)

    # Agregar datos desde la base (ajusta los nombres de campo según tu modelo)
    for item in Producto.objects.all():
        ws.append([
            getattr(item, 'categoria', ''),
            getattr(item, 'empresa', ''),
            getattr(item, 'ubicacion', ''),
            getattr(item, 'cod_ean', ''),
            getattr(item, 'cod_dun', ''),
            getattr(item, 'cod_sistema', ''),
            getattr(item, 'descripcion', ''),
            getattr(item, 'unidad', ''),
            getattr(item, 'pack', ''),
            getattr(item, 'factorx', ''),
            getattr(item, 'cajas', ''),
            getattr(item, 'saldo', ''),
            getattr(item, 'stock_fisico', ''),
            getattr(item, 'observacion', ''),
            getattr(item, 'fecha_venc', ''),
            getattr(item, 'fecha_imp', ''),
            getattr(item, 'contenedor', ''),
            getattr(item, 'fecha_inv', ''),
            getattr(item, 'encargado', ''),
            "Ver / Editar / Eliminar",  # Texto fijo para acciones
        ])

    # Estilo: ajustar ancho de columnas automáticamente
    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        ws.column_dimensions[column].width = max_length + 2

    # Crear la respuesta HTTP con el archivo Excel
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="inventario_completo.xlsx"'

    wb.save(response)
    return response

from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos:index')  # Cambia a la URL correcta
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar.html', {'form': form})

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos:index')  # Usa el nombre correcto
    return render(request, 'eliminar.html', {'producto': producto})

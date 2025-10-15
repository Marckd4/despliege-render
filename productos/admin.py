from django.contrib import admin
from .models import Categoria, Producto

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id','categoria')
    
class ProductoaAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'empresa', 'ubicacion', 'cod_ean', 'cod_dun', 'cod_sistema',
        'descripcion', 'unidad', 'pack', 'factorx', 'cajas', 'saldo',
        'stock_fisico', 'observacion', 'fecha_inv', 'encargado',
        'fecha_imp', 'numero_contenedor')

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto,ProductoaAdmin )

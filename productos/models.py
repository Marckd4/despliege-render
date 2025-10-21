from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)
    
    def __str__(self):
        return self.categoria


class Producto(models.Model):
    categoria = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100, blank=True, null=True)
    ubicacion = models.CharField(max_length=100, blank=True, null=True)
    cod_ean = models.CharField(max_length=50, blank=True, null=True)
    cod_dun = models.CharField(max_length=50, blank=True, null=True)
    cod_sistema = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(max_length=350, blank=True, null=True)
    unidad = models.CharField(max_length=20, blank=True, null=True)
    pack = models.IntegerField(blank=True, null=True)
    factorx = models.FloatField(blank=True, null=True)
    cajas = models.IntegerField(blank=True, null=True)
    saldo = models.IntegerField(blank=True, null=True)
    stock_fisico = models.IntegerField(blank=True, null=True)
    observacion = models.TextField(max_length=350, blank=True, null=True)
    fecha_inv = models.DateField(blank=True, null=True)
    encargado = models.CharField(max_length=100, blank=True, null=True)
    fecha_imp = models.DateField(blank=True, null=True)
    numero_contenedor = models.CharField(max_length=100, blank=True, null=True)
    Data_base = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.categoria

    
from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)
    
    def __str__(self):
        return self.categoria


class Producto(models.Model):
    categoria = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    cod_ean = models.CharField(max_length=50)
    cod_dun = models.CharField(max_length=50)
    cod_sistema = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=350)
    unidad = models.CharField(max_length=20)
    pack = models.IntegerField()
    factorx = models.FloatField()
    cajas = models.IntegerField()
    saldo = models.IntegerField()
    stock_fisico = models.IntegerField()
    observacion = models.TextField(max_length=350,blank=True, null=True)
    fecha_inv = models.DateField()
    encargado = models.CharField(max_length=100)
    fecha_imp = models.DateField(blank=True, null=True)
    numero_contenedor = models.CharField(max_length=100, blank=True, null=True)
    Data_base =models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.categoria

    
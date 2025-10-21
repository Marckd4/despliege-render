from . import models
from django.forms import ModelForm

class ProductoForm(ModelForm):
    class Meta:
        model = models.Producto
        fields ='__all__' #Incluye todos los campos del modelo


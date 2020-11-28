from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo               = models.AutoField(db_column='codigo', primary_key=True)
    nombre_producto      = models.CharField(max_length=30, blank=True, null=True)
    descripcion_producto = models.CharField(max_length=100, blank=True, null=True)
    precio               = models.IntegerField(blank=True, null=True)
    stock                = models.IntegerField(blank=True, null=True)
    foto_producto        = models.ImageField(upload_to='fotos', blank=True, null=True)
from django.db import models

# Create your models here.


#crear tabla ventas
class ventas(models.Model):
    fecha_venta = models.DateField(_("fecha_venta"), auto_now=True)
    sabor = models.CharField(_("sabor"), max_length = 255)
    cantidad = models.IntegerField(_("cantidad"))
    gramos = models.IntegerField(_("gramos"))
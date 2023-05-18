from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class ventas (models.Model):
    id = models.AutoField(_('id'), primary_key=True)
    fecha_venta = models.DateField(_("fecha_venta"),auto_now = True)
    sabor_helado = models.CharField(_("sabor_helado"),max_length=255)
    cantidad = models.IntegerField(_("cantidad"))
    gramos_unidad = models.IntegerField(_("gramos_unidad"))
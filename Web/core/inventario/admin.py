from django.contrib import admin

from core.inventario.models.producto.models import vt_producto_web, StProductoDetalle
from core.inventario.models.prueba.model import TmpImagen

admin.site.register(vt_producto_web)
admin.site.register(StProductoDetalle)

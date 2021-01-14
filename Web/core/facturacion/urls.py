from django.urls import  path

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
from core.facturacion.views.comprobante.views import ImagenComprobanteView
from core.facturacion.views.proforma.views import GrabaProformaTem, proformaImagen
from core.facturacion.views.sale.views import SaleCreateView

app_name = 'fac'

urlpatterns = [
    path('facturacion/', GrabaProformaTem, name = 'grabaProforma'),
    path('imagenesProforma/', proformaImagen.as_view(), name = 'imagenesProforma'),
    path('ImagenComprobante/', ImagenComprobanteView.as_view(), name = 'ImagenComprobante'),

    path('sale/', SaleCreateView.as_view(), name = 'sale_create'),
]
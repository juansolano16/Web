from django.urls import include, path
from rest_framework import routers

from core.inventario.views.BodegaVirtual.views import reservaBodegaV, ventasBodegaViewSet
from core.inventario.views.ProductoWeb import views
from core.inventario.views.inventario.views import inventarioFinAnio, inventarioAuditoriaResultado

app_name = 'productoWeb'

routerP = routers.DefaultRouter()
routerP.register(r'ApiProductosMM', views.ProductoViewSet, 'ApiProductosMM')
routerP.register(r'ApiProductosAuvi', views.ProductoAuviViewSet, 'ApiProductosAuvi')

routerBodegaV = routers.DefaultRouter()
routerBodegaV.register(r'ventasInmot', ventasBodegaViewSet, 'ventasInmot')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(routerP.urls)),

    ## Edicion Detalles Productos ###
    path('listDetalleProductoWeb/', views.listProductoDetalleWeb.as_view(), name='listDetalleProductoWeb'),

    ## Bodegas Virtuales ###
    path('listReservaBodegaV/', reservaBodegaV.as_view(), name='listReservaBodegaV'),
    path('ventasBodegaV/', include(routerBodegaV.urls)),

    ## Inventario de Fin de Año ##
    path('inventarioFinAnio/', inventarioFinAnio.as_view(), name='inventarioFinAnio'),
    path('inventarioAuditoriaResultado/', inventarioAuditoriaResultado.as_view(), name='inventarioAuditoriaResultado'),

    path('prueba2/', views.prueba2),
]

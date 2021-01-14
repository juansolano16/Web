from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import connections
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from rest_framework import viewsets

## PARA VISUALIZAR REST API
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from core.clases_general.mixins import GroupRequiredMixin2
from core.inventario.forms.ProductoWeb.forms import DetalleProductoWebFormEdit, DetalleProductoWebFormAdd
from core.inventario.schedules.bodegaV import *
from core.inventario.models.producto.models import vt_producto_web, StProductoDetalle, VtProductoDetalle, \
    vt_producto_web_auvi, StProductoSerie, StProductoSerieAuvi
from core.inventario.serializers.Producto.serializers import ProductoSerializerMM, ProductoSerializerAuvi

from django.db.models import Max, Prefetch


########################## API REST ########################################
class ProductoViewSet(viewsets.ViewSet):
    def list(self, request):
        ## EJECUTA PROCEDIMIENTOS ALMACENADOS ###
        with connections['default'].cursor() as cur:
           cur.callproc('stock.ks_proforma_web.ACTUALIZA_COLOR_PROD', [2,])
        # queryset = vt_producto_web.objects.prefetch_related('detalles', 'series', 'precio').filter(
        #     grupo='MASTERMOTO').order_by('linea', 'tipo', 'categoria', 'subcategoria')

        queryset = vt_producto_web.objects.prefetch_related(Prefetch('series', queryset=StProductoSerie.objects.all())).filter(
            grupo='MASTERMOTO').order_by('linea', 'tipo', 'categoria', 'subcategoria')

        # serializer_class = ProductoSerializer
        serializer = ProductoSerializerMM(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # queryset = vt_producto_web.objects.prefetch_related('detalles', 'series', 'precio').filter(
        #     grupo='MASTERMOTO').order_by('linea', 'tipo', 'categoria','subcategoria')
        queryset = vt_producto_web.objects.prefetch_related(
            Prefetch('series', queryset=StProductoSerie.objects.all())).filter(
            grupo='MASTERMOTO').order_by('linea', 'tipo', 'categoria', 'subcategoria')

        prod = get_object_or_404(queryset, pk=pk)
        serializer = ProductoSerializerMM(prod)
        return Response(serializer.data)


class ProductoAuviViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = vt_producto_web_auvi.objects.prefetch_related('detalles', 'series', 'precio').filter(
            grupo='AUVI').order_by('linea', 'sublinea', 'categoria', 'segmento', 'subsegmento')

        # serializer_class = ProductoSerializerAuvi
        serializer = ProductoSerializerAuvi(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = vt_producto_web_auvi.objects.prefetch_related('detalles', 'series', 'precio').filter(
            grupo='AUVI').order_by('linea', 'sublinea', 'categoria', 'segmento', 'subsegmento')

        prod = get_object_or_404(queryset, pk=pk)
        serializer = ProductoSerializerAuvi(prod)
        return Response(serializer.data)


############################################################################
class listProductoDetalleWeb(LoginRequiredMixin, GroupRequiredMixin2, ListView):
    model = VtProductoDetalle
    template_name = 'ProductoWeb/listProductoWebDetalles.html'
    permission_required = 'view_stproductodetalle'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = [i.toJSON() for i in self.model.objects.all()]
            elif action == 'updata_det':
                StProductoDetalle.objects.filter(cod_producto=request.POST['cod_producto'], secuencia=request.POST['secuencia']).update(detalle=request.POST['detalle'])
                data = {'ok': 'Registro Grabado'}
            elif action == 'add_det':
                b = StProductoDetalle.objects.filter(cod_producto_id=request.POST['cod_producto'], caracteristicas=request.POST['caracteristica'])
                if not b:
                    sec = StProductoDetalle.objects.filter(cod_producto_id=request.POST['cod_producto']).aggregate(Max('secuencia'))
                    StProductoDetalle.objects.create(empresa=2,
                                                     cod_producto_id=request.POST['cod_producto'],
                                                     secuencia= 1 if not sec['secuencia__max'] else sec['secuencia__max'] + 1,
                                                     caracteristicas=request.POST['caracteristica'],
                                                     detalle=request.POST['detalle'],)
                    data = {'ok': 'Registro Grabado'}
                else:
                    data = {'error': 'Registro ya existe'}
            else:
                data = {'error': 'Ha ocurrido un error'}
        except Exception as e:
            data = {'error': str(e)}
            print(data)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle Productos Web'
        context['form_update_det'] = DetalleProductoWebFormEdit()
        context['form_add_det'] = DetalleProductoWebFormAdd()
        return context


############################################################################
# Create your views here.
def query_db(query, args=(), one=False):
    with connections['oracle'].cursor() as cur:
        cur.execute(query, args)
        r = [dict((cur.description[i][0], value) \
                  for i, value in enumerate(row)) for row in cur.fetchall()]
    return (r[0] if r else None) if one else r


def prueba2(request):
    # reg = readB(nom = '/MASSLINE/prueba_prov.txt', path = 1)
    reg = genRep()
    if type(reg) == dict:
        return JsonResponse(reg, safe=False)
    else:
        return HttpResponse(reg)

from django.db import connections
from django.db.models import Q
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.inventario.models.bodegas.models import StReservaProducto, VtReservaBv
from core.inventario.serializers.BodegaVirtual.serializers import VentaBodegaVitualSerializer

########################## API REST ########################################
###############  API PARA LA BODEGA BAJAC ##################################
class ventasBodegaViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = VtReservaBv.objects.filter(proveedor='0190365751001',
                                           fecha_aprobacion__range=((datetime.now() - timedelta(days=15)).strftime('%Y-%m-%d'),
                                                                    datetime.now().strftime('%Y-%m-%d'))
                                           )
        serializer = VentaBodegaVitualSerializer(queryset, many=True)
        return Response(serializer.data)



###################  APROBAR RESERVAS DE LA BODEGA VIRTUAL ##################
class reservaBodegaV(TemplateView):
    template_name = 'BodegaVirtual/listBodegaReserva.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            action = request.POST['action']
            if action == 'prod_reservados':
                data = [i.toJSON() for i in StReservaProducto.objects.filter(aprobador_por__isnull=True, es_anulado='N')]
            elif action == 'prod_aprobados':
                data = [i.toJSON() for i in StReservaProducto.objects.filter(Q(aprobador_por__isnull=False)|
                                                                             Q(es_anulado__in=['S', 'N']))]
            elif action == 'Aprobar':
                ## EJECUTA PROCEDIMIENTOS ALMACENADOS ###
                with connections['default'].cursor() as cur:
                    pempresa = request.POST['empresa']
                    ptipo_comprobante = request.POST['tipo_comprobante']
                    pcomprobante = request.POST['cod_comprobante']
                    pusuario = request.user.username
                    cur.callproc('stock.ks_bodega_virtual.ApruebaReserva', [pempresa, ptipo_comprobante, pcomprobante, pusuario])
                data = {'ok': 'Reserva Aprobada'}
            elif action == 'Negar':
                ## EJECUTA PROCEDIMIENTOS ALMACENADOS ###
                with connections['default'].cursor() as cur:
                    pempresa = request.POST['empresa']
                    ptipo_comprobante = request.POST['tipo_comprobante']
                    pcomprobante = request.POST['cod_comprobante']
                    pusuario = request.user.username
                    cur.callproc('stock.ks_bodega_virtual.NegarReserva',
                                 [pempresa, ptipo_comprobante, pcomprobante, pusuario])
                data = {'ok': 'Reserva Rechazada'}
            else:
                data = {'error': 'Ha ocurrido un error'}
        except Exception as e:
            data = {'error': str(e)}
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Bodega Virtual'
        # context['form_update_emp'] = turnosEmpleadoForm()
        return context

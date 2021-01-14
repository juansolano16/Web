import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import connections, transaction
from django.http import JsonResponse, HttpResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from core.clases_general.Utilities import resize_image
from core.clases_general.mixins import GroupRequiredMixin2
from core.facturacion.forms.proforma.forms import StClientesImgDocForm
from core.facturacion.modelos.proforma.models import StProformaCabeceraTmp, StProformaDetalleTmp, VtImagenProforma, \
    VtProforma


# @transaction.atomic
@method_decorator(csrf_exempt)
def GrabaProformaTem(request):
    ## Declaracion de variables para ventas con TCR
    id_transaccion_ = banco_ = nom_tarjeta_ = cuotas_ = autorizacion_tcr_ = propietario_tcr_ = tipo_fp_tcr_ = ''

    if request.method == 'POST':
        try:
            ##### CODIGO COMPROBANTE ######
            cod_comprobante_ = ''
            query = 'select genera_comprobante_web from dual'
            with connections['default'].cursor() as cur:
                cur.execute(query)
                cod_comprobante_ = cur.fetchone()[0]

            ##### DATOS DE CABECERA ######
            json_data = json.loads(request.body)

            empresa_ = 2
            tipo_comprobante_ = 'PR'
            cod_agencia_ = 0  # sto domingo 3
            cedula = json_data['cod_persona']
            cod_persona_ = cedula[0:9] + '-' + cedula[9:] if len(cedula) == 10 else cedula
            nombre_ = json_data['nombre_']
            apellido_ = json_data['apellido_']
            cod_forma_pago_ = json_data['cod_forma_pago_']
            cod_tipo_identificacion_ = 1
            cod_tipo_identificacion_gar_ = 1
            num_cuotas_ = 0
            entrada_ = 0  # revisar
            valor_ = json_data['valor']  # revisar
            base_imponible_ = float(valor_) / 1.12
            iva_ = base_imponible_ * 0.12  # revisar
            financiamiento_ = 0
            cod_politica_ = 1 if cod_forma_pago_ == 'EFE' else 4

            if cod_forma_pago_ == 'TCR':
                id_transaccion_ = json_data['id_transaccion']
                autorizacion_tcr_ = json_data['autorizacion']
                propietario_tcr_ = json_data['tar_habiente']
                tipo_fp_tcr_ = json_data['tipo_credito']
                banco_ = json_data['banco']
                nom_tarjeta_ = json_data['nom_tarjeta']
                cuotas_ = json_data['cuotas']


            with transaction.atomic():
                regC = StProformaCabeceraTmp(empresa=empresa_,
                                             tipo_comprobante=tipo_comprobante_,
                                             cod_comprobante=cod_comprobante_,
                                             cod_agencia=cod_agencia_,
                                             cod_forma_pago=cod_forma_pago_,
                                             cod_tipo_identificacion=cod_tipo_identificacion_,
                                             cod_persona=cod_persona_,
                                             nombre_persona=nombre_,
                                             apellido_persona=apellido_,
                                             cod_tipo_identificacion_gar=cod_tipo_identificacion_gar_,
                                             num_cuotas=num_cuotas_,
                                             entrada=entrada_,
                                             iva=iva_,
                                             financiamiento=financiamiento_,
                                             valor=valor_,
                                             cod_politica=cod_politica_,
                                             base_imponible=base_imponible_,

                                             #### datos tarjeta credito ###
                                             id_transaccion_tcr=id_transaccion_,
                                             banco = banco_,
                                             nom_tarjeta = nom_tarjeta_,
                                             cuotas_tcr = cuotas_,
                                             autorizacion_tcr = autorizacion_tcr_,
                                             propietario_tcr = propietario_tcr_,
                                             fp_tcr = tipo_fp_tcr_,
                                             )
                regC.save()

                ##### DATOS DE DETALLE ######
                i = 1
                for det in json_data['detalles']:
                    cod_producto_ = det['cod_producto']
                    cantidad_ = det['cantidad']
                    precio_ = det['precio']

                    regD = StProformaDetalleTmp(empresa=empresa_,
                                                tipo_comprobante=tipo_comprobante_,
                                                cod_comprobante=cod_comprobante_,
                                                secuencia=i,
                                                cod_producto=cod_producto_,
                                                cantidad=cantidad_,
                                                precio=precio_,
                                                iva='S' if iva_ > 0 else 'N',
                                                )
                    i = i + 1
                    regD.save()

                ## EJECUTA PROCEDIMIENTOS ALMACENADOS ###
                with connections['default'].cursor() as cur:
                    cur.callproc('stock.ks_proforma.graba_fercho', [2, 'PR', cod_comprobante_])
                    cur.callproc('stock.ks_proforma_web.actualiza_precio', [2, 'PR', cod_comprobante_])
            data = {'ok': 'Facturacion Exitosa'}
        except Exception as e:
            data = {'error': str(e)}
        return JsonResponse(data, safe=False)
    return HttpResponse('ok get')


####################################################
################# Imagen Proforma  ###############
class proformaImagen(LoginRequiredMixin, GroupRequiredMixin2, TemplateView):
    template_name = 'proforma/proforma_imagen.html'
    permission_required = 'view_stclientesimagenesdocumento'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        try:
            action = request.POST['action']
            if action == 'search_cliente':
                data = []
                prof = VtImagenProforma.objects.values('empresa', 'cod_comprobante', 'fecha', 'agencia', 'cod_persona', 'persona').distinct()
                # prof = VtProforma.objects.all()
                for i in prof.filter(cod_persona__icontains=request.POST['term'])[0:5]:
                    item = i
                    # item = i.toJSON()
                    item ['value'] = i['persona'] + ' : ' + i['cod_comprobante']
                    # item ['value'] = i.nom_cliente + ' : ' + i.cod_comprobante
                    item ['user'] = request.user.username.upper()
                    data.append(item)

            elif action == 'search_img':
                # prof = VtImagenProforma.objects.filter(cod_comprobante = request.POST['comprobante'])
                prof = VtImagenProforma.objects.filter(cod_persona=request.POST['cod_persona'])
                data = [i.toJSON() for i in prof]

            elif action == 'subirImg':
                # img = resize_image(request.FILES)
                form = StClientesImgDocForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    data = {'ok': 'Registro Grabado'}
                else:
                    data = {'error': form.errors}

            else:
                data = {'error': 'Ha ocurrido un error'}
        except Exception as e:
            print(e)
            data = {'error': str(e)}
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Imagenes Proforma'
        context['formImgC'] = StClientesImgDocForm
        context['lista'] = [{'id':'1', 'nom': 'SOL. DE CREDITO'},
                            {'id':'2', 'nom': 'CROQUIS CLIENTE'},
                            {'id':'3', 'nom': 'CEDULA FRONTAL'},
                            {'id':'4', 'nom': 'VERIF. DATOS'},
                            {'id':'5', 'nom': 'SERV.BÁSICO'},
                            {'id':'6', 'nom': 'SUST. INGRESOS'},
                            {'id':'8', 'nom': 'FOTO CLIENTE'},
                            {'id':'9', 'nom': 'CED. POSTERIOR'},
                            {'id':'10', 'nom': 'CERT. VOTACION'},]
        return context

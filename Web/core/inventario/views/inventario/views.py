from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import connections, transaction
from django.http.response import JsonResponse, FileResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.db.models import Q


############ TOMA DE INVENTARIO 2020 ###############################
from core.clases_general import reportes
from core.clases_general.mixins import GroupRequiredMixin2
from core.inventario.forms.inventario.forms import formTgAgencia, formStIventarioDMoto, formMarcaProducto, \
    formStIventarioDRep, formStIventarioDAuvi, formVtReporteAuditoriaGeneral
from core.inventario.models.inventario.models import VtReporteInventarioFinal, StInventarioResultado, \
    StInventarioResultadoD, VtReporteRepuestos, VtReporteInvAuvi, VtResultadoAudMoto, VtResultadoAudAuvi, \
    VtResultadoAudRep, VtProdSerie, VtReporteAuditoriaGeneral
import config.settings as setting


class inventarioFinAnio(LoginRequiredMixin, GroupRequiredMixin2, TemplateView):
    template_name = 'inventario/listProdutoAuditoria.html'
    permission_required = ['add_vtreporteinventariofinal', 'add_vtreporterepuestos', 'add_vtreporteinvauvi',
                           'view_vtresultadoaudmoto', 'view_vtresultadoaudrep', 'view_vtresultadoaudauvi']

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            action = request.POST['action']
            if action == 'searchInvantarioFinal' or action =='searchInvantarioRep' or action =='searchInvantarioAuvi':
                id_agencia = request.POST['agencia']

                if not StInventarioResultado.objects.filter(cod_agencia=id_agencia).exists() and id_agencia != '1':
                    with connections['default'].cursor() as cur:
                        cur.callproc('STOCK.GENERA_CABECERA_INV', [2,id_agencia, request.user.username])

                if id_agencia != '1':
                    inv = StInventarioResultado.objects.get(cod_agencia=id_agencia)
                    comprobante = inv.cod_comprobante
                    cerrado = inv.cerrado
                    tmp = [i.toJSON() for i in self.get_model_inv(action).objects.filter(cod_agencia=id_agencia,)]
                else:
                    cerrado = '-'
                    comprobante = '---'
                    tmp = []

                data = {'comprobante':  comprobante, 'cerrado': cerrado, 'data': tmp}

            elif action == 'grabarEstadoInv': data = self.saveInventario(request.POST, request.user.username)

            elif action == 'search_producto':
                data = []
                prod = VtProdSerie.objects.all()
                for i in prod.filter(Q(serie__icontains=request.POST['term']) |
                                     Q(cod_producto__icontains=request.POST['term']) |
                                     Q(nombre__icontains=request.POST['term']) )[0:5]:
                    item = i.toJSON()
                    item ['value'] = i.nombre + ': ' + i.cod_producto + ': ' + i.serie
                    data.append(item)

            elif action == 'cerrarCabecera':
                id_agencia = request.POST['agencia']
                id_comprobante = request.POST['comprobante']
                if StInventarioResultado.objects.filter(cod_agencia=id_agencia, cod_comprobante=id_comprobante).exists() and id_agencia != '1':
                    reg = StInventarioResultado.objects.get(cod_comprobante = id_comprobante, cod_agencia=id_agencia)
                    if reg.cerrado == 'N':
                        reg.cerrado = 'S'
                        reg.save()
                        data = {'ok': 'Registro grabado'}
                    else: data = {'error': 'Cabecera ya cerrada'}
                else: data = {'error': 'No existe cabecera'}

            else: data = {'error': 'Ha ocurrido un error'}

        except Exception as e:
            data = {'error': str(e)}
        return JsonResponse(data, safe=False)

    def get_bool_item(self, data, id):
        try: return ('S' if data[id] else 'N')
        except: return 'N'

    def get_model_inv(self, action):
        if action == 'searchInvantarioFinal': return VtReporteInventarioFinal
        if action == 'searchInvantarioRep': return VtReporteRepuestos
        else: return VtReporteInvAuvi

    def saveInventario(self, datos, username):
        ind = 1
        if datos['categoriaInv'] == 'Moto':
            det = {'estado': self.get_bool_item(datos, 'estado'),
               'kit': self.get_bool_item(datos, 'kit'),
               'observacion1': datos['observacion1'],
               'observacion2': datos['observacion2']
            }
            cantidad_ = 1
            if datos['sobrante'] == 'S': sobrante_ = 'S'
            elif datos['sobrante']!='S' and self.get_bool_item(datos, 'estado')=='N': sobrante_ = 'N'
            else: sobrante_ = '-'
            tipo_ = '-'

        elif datos['categoriaInv'] == 'Repuesto':
            det = {
                'rayon': datos['cantidad_rayon'] if self.get_bool_item(datos, 'rayon') == 'S' else 0,
                'transferencia': datos['cantidad_trans'] if self.get_bool_item(datos, 'transferencia') == 'S' else 0,
                'observacion1': datos['observacion1'],
                'observacion2': datos['observacion2'],
                'cantidad_reg': datos['cantidad_reg'],
            }
            cantidad_ = datos['cantidad']
            if datos['sobrante'] == 'S': sobrante_ = 'S'
            elif datos['sobrante'] != 'S' and datos['cantidad'] == datos['cantidad_reg'] \
                    and datos['cantidad_rayon'] == '0' and datos['cantidad_rayon'] == '0':
                sobrante_ = '-'
            else: sobrante_ = 'N'
            tipo_=datos['tipo']

        else:
            det = {
                'estado': 'S' if datos['sobrante'] == 'S' else self.get_bool_item(datos, 'estado_prod'),
                'desperfecto': self.get_bool_item(datos, 'desperfecto'),
                'promocional': self.get_bool_item(datos, 'promocional'),
                'garantia': self.get_bool_item(datos, 'garantia'),
                'PorRecibir': 1 if self.get_bool_item(datos, 'transferencia1')=='S' else 0,
                'observacion1': datos['observacion1'],
                'observacion2': datos['observacion2'],
            }
            if datos['sobrante'] == 'S': sobrante_ = 'S'
            elif datos['sobrante'] == 'N' and self.get_bool_item(datos, 'transferencia1') == 'S': sobrante_ = 'N'
            elif datos['sobrante'] == 'N' and self.get_bool_item(datos, 'estado_prod') == 'N': sobrante_ = 'N'
            else: sobrante_ = '-'
            cantidad_ = 1
            tipo_ = '-'

        if StInventarioResultadoD.objects.filter(empresa=2,
                                                 tipo_comprobante_id=datos['tipo_comprobante'],
                                                 cod_comprobante_id=datos['cod_comprobante'],
                                                 cod_producto=datos['cod_producto'],
                                                 serie=datos['serie'],
                                                 ingreso_manual_serie= datos['ingreso_manual'],
                                                 tipo=tipo_
                                                 ).exists(): update = '1'
        else: update = '0'

        if update == '0':
            with transaction.atomic():
                for i in det:
                    StInventarioResultadoD.objects.create(empresa=2,
                                                          tipo_comprobante_id=datos['tipo_comprobante'],
                                                          cod_comprobante_id=datos['cod_comprobante'],
                                                          secuencia=ind,
                                                          cod_producto=datos['cod_producto'],
                                                          serie=datos['serie'],
                                                          sobrante=sobrante_,
                                                          ingreso_manual_serie= datos['ingreso_manual'],
                                                          categoria=datos['categoriaInv'],
                                                          detalle=i,
                                                          valor_detalle= self.toUpper(det[i]),
                                                          cantidad=cantidad_,
                                                          cod_usuario=username.upper(),
                                                          tipo=tipo_)
                    ind += 1
        else:
            with transaction.atomic():
                for i in det:
                    StInventarioResultadoD.objects.filter(empresa=2,
                                                          tipo_comprobante_id=datos['tipo_comprobante'],
                                                          cod_comprobante_id=datos['cod_comprobante'],
                                                          secuencia=ind,
                                                          cod_producto=datos['cod_producto'],
                                                          serie=datos['serie'],
                                                          # sobrante=sobrante_,
                                                          ingreso_manual_serie=datos['ingreso_manual'],
                                                          tipo=tipo_
                    ).update(
                        sobrante=sobrante_,
                        # ingreso_manual_serie=datos['sobrante'],
                        categoria=datos['categoriaInv'],
                        detalle=i,
                        valor_detalle=self.toUpper(det[i]),
                        cantidad = cantidad_,
                        cod_usuario=username.upper()
                    )
                    ind += 1
        return {'ok': 'Registro Grabado'}

    def toUpper(self, string):
        try: return string.upper()
        except: return string

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inventario'
        context['formTgAgencia'] = formTgAgencia()
        context['formMarcaProducto'] = formMarcaProducto()
        context['formStIventarioDMoto'] = formStIventarioDMoto()
        context['formStIventarioDRep'] = formStIventarioDRep()
        context['formStIventarioDAuvi'] = formStIventarioDAuvi()
        context['tabs'] = [{'id': 'tab-1', 'nom': 'Motos/Bicicletas', 'id_tabla': 'data1'},
                           {'id': 'tab-2', 'nom': 'Repuestos/Promocionales', 'id_tabla': 'tablaRep'},
                           {'id': 'tab-3', 'nom': 'Auvi/Electrodomésticos', 'id_tabla': 'tablaAuvi'}, ]
        return context


class inventarioAuditoriaResultado(LoginRequiredMixin, GroupRequiredMixin2, TemplateView):
    template_name = 'inventario/listProdAuditoriaResultado.html'
    permission_required = ['add_vtreporteinventariofinal', 'add_vtreporterepuestos', 'add_vtreporteinvauvi',
                           'view_vtresultadoaudmoto', 'view_vtresultadoaudrep', 'view_vtresultadoaudauvi']

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        try:
            action = request.POST['action']
            if action == 'searchInventarioFinal' or action =='searchInventarioRep' or action =='searchInventarioAuvi':
                tmp = [i.toJSON() for i in self.get_model_inv(action).objects.all()]
                data = {'comprobante':  '', 'data': tmp}

            elif action == 'searchResultadoGrabado':
                tmp = [i.toJSON() for i in self.get_model_resultado(request.POST)]
                data = {'comprobante': '', 'data': tmp}

            elif action == 'generarReporte':
                file_path = self.gen_reporte(request.POST['cod_agencia'])
                return FileResponse(open(file_path, 'rb'))

            else: data = {'error': 'Ha ocurrido un error'}

        except Exception as e:
            data = {'error': str(e)}
        return JsonResponse(data, safe=False)


    def gen_reporte(self, cod_agencia):
        try:
            path = setting.BASE_DIR + '/core/inventario/reportes/jasper/AuditoriaInventario'
            # output = setting.BASE_DIR + '/core/TmpReportes/Rol_' + cedula
            img_dir = setting.BASE_DIR + '/static/img'
            base = 'UNNOPARTSDB'
            parametros = {"PEMPRESA": '2', "PCOD_AGENCIA": cod_agencia,
                          # "PFECHA": periodo,
                          "IMAGE_DIR": img_dir,
                          "SUBREPORT_DIR": path}
            rep = reportes.ReporteJasper(path, base)
            file_path = rep.generarReporte('ActaInventario', parametros, extencion='pdf')
            return file_path

        except Exception as e:
            print(str(e))
            return ('error: ' + str(e))


    def get_model_inv(self, action):
        if action == 'searchInventarioFinal': return VtResultadoAudMoto
        if action == 'searchInventarioRep': return VtResultadoAudRep
        else: return VtResultadoAudAuvi


    def get_model_resultado(self, data):
        agencia = data['cod_agencia']
        if data['categoria'] == 'Motos/Bicicletas': categoria = 'Moto'
        elif data['categoria'] == 'Repuestos/Promocionales': categoria = 'Repuesto'
        else: categoria = 'Auvi'

        return VtReporteAuditoriaGeneral.objects.filter(cod_agencia = agencia, categoria=categoria)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Resultado Inventario'
        context['tabs'] = [{'id':'tab-1', 'nom': 'Motos/Bicicletas', 'id_tabla': 'data1'},
                           {'id':'tab-2', 'nom': 'Repuestos/Promocionales', 'id_tabla': 'tablaRep'},
                           {'id':'tab-3', 'nom': 'Auvi/Electrodomésticos', 'id_tabla': 'tablaAuvi'},]
        return context
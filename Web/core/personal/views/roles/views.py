from django.contrib import messages
from django.http.response import JsonResponse, HttpResponseServerError
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.db import connections
from django.http import FileResponse, HttpResponseBadRequest

from django.contrib.auth.mixins import LoginRequiredMixin

import config.settings as setting
from core.clases_general import reportes
from core.personal.forms.rol_empleado.forms import *

from core.personal.models.personal.models import RhPersonal, RhComprobante, VtRolesDescarga
from core.clases_general.mixins import GroupRequiredMixin


####################################################
################# ROLES DE EMPLEADOS ###############
class rolEmpleado2(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    group_required = ['Rh_empleado', 'Rh_admin']
    model = RhPersonal
    template_name = 'roles/rolEmpleado.html'
    ced = None
    campos = {}

    def get_object(self, queryset=None):
        try:
            self.ced = self.request.user.cod_personal
            ob = self.model.objects.get(cod_personal=self.ced)
            self.set_campos(ob)
            return ob
        except Exception as e:
            messages.error(self.request, 'Usuario No Encontrado')
            return None

    def set_campos(self, ob):
        self.campos['USUARIO'] = ob.cod_personal
        self.campos['NOMBRE EMPLEADO'] = ob.get_empleado()

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            cedula = request.POST['USUARIO']
            periodo = request.POST['periodo']
            file_path = self.gen_reporte(cedula, periodo)
            return FileResponse(open(file_path, 'rb'))
        except Exception as e:
            return HttpResponseBadRequest('Error: ' + str(e))

    def gen_reporte(self, cedula, periodo):
        try:
            path = setting.BASE_DIR + '/core/personal/reportes/jasper/rolEmpleado'
            output = setting.BASE_DIR + '/core/TmpReportes/Rol_' + cedula
            img_dir = setting.BASE_DIR + '/static/img'
            base = 'UNNOPARTSDB'
            parametros = {"PEMPRESA": '2', "PCOD_PERSONA": cedula,
                          "PFECHA": periodo, "IMAGE_DIR": img_dir,
                          "SUBREPORT_DIR": path, 'PUSUARIO': 'JUAN'}
            rep = reportes.ReporteJasper(path, base)
            file_path = rep.generarReporte('RP_ROLPAGOS', parametros, extencion='pdf', output_=output)
            return file_path
        except Exception as e:
            print(str(e))
            return ('error: ' + str(e))

    def get_periodo(self, ced_):
        query = """ select to_char(a.FECHA, 'yyyy-mm') anio from jaher.rh_comprobante a \
                  where a.COD_PERSONA = '""" + ced_ + """' and a.ESTADO_CONTABILIZADO = 'S' \
                  and a.empresa = 2 and a.TIPO_COMPROBANTE = 'RH' order by a.COD_COMPROBANTE desc"""
        with connections['default'].cursor() as cur:
            cur.execute(query)
            periodo = cur.fetchall()
        return [p[0] for p in periodo]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Roles Empleado'
        context['title_rep'] = 'GENERACION DE ROL DE PAGOS EMPLEADOS !!!'
        context['periodos'] = self.get_periodo(self.ced)
        context['campos'] = self.campos
        context['nombre_reporte'] = 'RolEmpleado.pdf'
        return context


class rolEmpleado(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = 'roles/rolEmpleado.html'
    group_required = ['Rh_empleado', 'Rh_admin']

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            action = request.POST['action']
            if action == 'search_periodo_id':
                data = [{'id': '', 'text': '------------'}]
                for i in RhComprobante.objects.filter(cod_persona=request.POST['id']):
                    data.append({'id': i.get_periodo(), 'text': i.get_periodo()})
            elif action == 'genReporte':
                file_path = self.gen_reporte(request.POST['empleado'], request.POST['periodo'], request.user.username)
                return FileResponse(open(file_path, 'rb'))
            else:
                data = {'error': 'Ha ocurrido un error'}
            return JsonResponse(data, safe=False)
        except Exception as e:
            data = {'error': str(e)}
        return JsonResponse(data, safe=False)

    def gen_reporte(self, cedula, periodo, usuario):
        try:
            path = setting.BASE_DIR + '/core/personal/reportes/jasper/rolEmpleado'
            output = setting.BASE_DIR + '/core/TmpReportes/Rol_' + cedula
            img_dir = setting.BASE_DIR + '/static/img'
            base = 'UNNOPARTSDB'
            parametros = {"PEMPRESA": '2', "PCOD_PERSONA": cedula,
                          "PFECHA": periodo, "IMAGE_DIR": img_dir,
                          "SUBREPORT_DIR": path, 'PUSUARIO': usuario}
            rep = reportes.ReporteJasper(path, base)
            file_path = rep.generarReporte('RP_ROLPAGOS', parametros, extencion='pdf', output_=output)

            ## EJECUTA PROCEDIMIENTOS ALMACENADOS ###
            with connections['default'].cursor() as cur:
                cur.callproc('JAHER.PK_RH_ROLES.GRABA_ROL_DESCARGA', [periodo, cedula, usuario])
            return file_path
        except Exception as e:
            print(str(e))
            return ('error: ' + str(e))

    def get_form(self, request):
        if not request.user.is_administrativo():
            form = formRolEmpleado(initial={'cod_persona': request.user.cod_personal})
            form.fields['cod_persona'].disabled = True
        else:
            form = formRolEmpleado()
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Roles Empleado'
        context['title_rep'] = 'GENERACION DE ROL DE PAGOS EMPLEADOS !!!'
        context['form'] = self.get_form(self.request)
        context['nombre_reporte'] = 'RolEmpleado.pdf'
        context['action'] = 'search_periodo_id'
        return context


class listRolesDescargados(LoginRequiredMixin, GroupRequiredMixin, ListView):
    model = VtRolesDescarga
    template_name = 'roles/listDescargaRol.html'
    group_required = [u'Rh_admin', ]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = [i.toJSON() for i in self.model.objects.all()]
            else:
                data = {'error': 'Ha ocurrido un error'}
        except Exception as e:
            data = {'error': str(e)}
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Historial de Roles'
        return context


############################################################
################# ROL DE BENEFICIOS SOCILAES ###############
class rolDecimo(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = 'roles/rolBeneficio.html'
    group_required = ['Rh_admin']

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            action = request.POST['action']
            if action == 'genReporte':
                if (request.POST['beneficio'] == 'D3'):
                    file_path = self.gen_reporte(request.POST['beneficio'], request.POST['periodo'])
                else:
                    file_path = self.gen_reporte(request.POST['beneficio'], request.POST['periodo'],
                                                 request.POST['region'])
                return FileResponse(open(file_path, 'rb'))
            else:
                data = {'error': 'Ha ocurrido un error'}
            return JsonResponse(data, safe=False)
        except Exception as e:
            data = {'error': str(e)}
        return JsonResponse(data, safe=False)

    def gen_reporte(self, beneficio, periodo, region = None):
        try:
            path = setting.BASE_DIR + '/core/personal/reportes/jasper/rolBeneficios'
            img_dir = setting.BASE_DIR + '/static/img'
            base = 'UNNOPARTSDB'
            if beneficio == 'D3':
                nom_rep = 'RBeneficiosD3'
                parametros = {"IMAGE_DIR": img_dir, 'PERIODO': periodo}
            else:
                nom_rep = 'RBeneficiosD4'
                parametros = {"IMAGE_DIR": img_dir, 'PERIODO': periodo, 'REGION': region}
            rep = reportes.ReporteJasper(path, base)
            return rep.generarReporte(nom_rep, parametros, extencion='xlsx')
        except Exception as e:
            return ('error: ' + str(e))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Descarga Rol de Beneficio'
        context['title_rep'] = 'GENERACION DE ROLES DE BENEFICIO SOCIAL !!!'
        context['form'] = formRolBeneficio()
        context['nombre_reporte'] = 'RolBeneficio.xlsx'
        return context

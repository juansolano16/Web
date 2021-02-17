from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import connections
from django.http.response import FileResponse, JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, CreateView, UpdateView

from core.clases_general import reportes
from core.clases_general.mixins import GroupRequiredMixin

import config.settings as setting
from core.personal.forms.empleado.forms import formRhPersonal, formPersonalActivo
from core.personal.models.personal.models import VtPersonal, RhPersonal, RhPersonalD, RhPersonalInstruccion


class listEmpleados(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = 'empleado/listEmpleados.html'
    group_required = [u'Rh_admin', ]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            action = request.POST['action']
            if action == 'searchdata':
                activo = request.POST['activos']
                empresa = request.POST['empresa']
                data = [i.toJSON() for i in VtPersonal.objects.all().filter(activo__in=activo, empresa = empresa)]
            else:
                data = {'error': 'Ha ocurrido un error'}
        except Exception as e:
            data = {'error': str(e)}
        return JsonResponse(data, safe=False)

    def gen_reporte(self, cedula):
        try:
            path = setting.BASE_DIR + '/core/personal/reportes/jasper/liqEmpleado'
            output = setting.BASE_DIR + '/core/TmpReportes/liq_' + cedula
            img_dir = setting.BASE_DIR + '/static/img'
            base = 'UNNOPARTSDB'
            parametros = { "PCOD_PERSONA": cedula, "IMAGE_DIR": img_dir, "SUBREPORT_DIR": path}
            rep = reportes.ReporteJasper(path, base)
            return rep.generarReporte('liqHaberes', parametros, extencion='xlsx', output_=output)
        except Exception as e:
            print(str(e))
            return ('error: ' + str(e))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Empleados'
        context['formActivo'] = formPersonalActivo()
        return context


class rhPersonalCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    template_name = 'empleado/createRhPersonal.html'
    model = RhPersonal
    form_class = formRhPersonal
    group_required = [u'Rh_admin', ]
    success_url = reverse_lazy('personal:listEmpleados')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Empleado'
        context['entity'] = 'Listado Empleado'
        context['list_url'] = self.success_url
        context['formActivo'] = formPersonalActivo()
        return context


class rhPersonalUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = RhPersonal
    form_class = formRhPersonal
    template_name = 'empleado/createRhPersonal.html'
    group_required = [u'Rh_admin', ]
    success_url = reverse_lazy('personal:listEmpleados')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            action = request.POST['action']
            if action == 'searchCargos':
                per = request.POST['cod_personal']
                data = [i.toJSON() for i in RhPersonalD.objects.filter(cod_personal=per)]

            elif action == 'searchEstudios':
                per = request.POST['cod_personal']
                data = [i.toJSON() for i in RhPersonalInstruccion.objects.filter(cod_personal=per)]

            else:
                data = {'error': 'Ha ocurrido un error ' + action}
        except Exception as e:
            data = {'error': str(e)}
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Datos Empleado'
        context['entity'] = 'Listado Empleado'
        context['list_url'] = self.success_url
        return context


class liqEmpleado(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = 'empleado/liqEmpleadoList.html'
    group_required = [u'Rh_admin', ]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = [i.toJSON() for i in VtPersonal.objects.all().filter(activo = 'S')]
            elif action == 'genReporte':
                file_path = self.gen_reporte(request.POST['cedula'])
                return FileResponse(open(file_path, 'rb'))
            elif action == 'genLiq':
                ## EJECUTA PROCEDIMIENTOS ALMACENADOS ###
                with connections['default'].cursor() as cur:
                    cur.callproc('JAHER.PK_RH_ROLES.LIQ_HABERES', [2, request.POST['cedula']])
                data = {'ok': 'Se ha generado valores de liquidacion'}
            else:
                data = {'error': 'Ha ocurrido un error'}
        except Exception as e:
            data = {'error': str(e)}
        return JsonResponse(data, safe=False)

    def gen_reporte(self, cedula):
        try:
            path = setting.BASE_DIR + '/core/personal/reportes/jasper/liqEmpleado'
            output = setting.BASE_DIR + '/core/TmpReportes/liq_' + cedula
            img_dir = setting.BASE_DIR + '/static/img'
            base = 'UNNOPARTSDB'
            parametros = { "PCOD_PERSONA": cedula, "IMAGE_DIR": img_dir, "SUBREPORT_DIR": path}
            rep = reportes.ReporteJasper(path, base)
            return rep.generarReporte('liqHaberes', parametros, extencion='xlsx', output_=output)
        except Exception as e:
            print(str(e))
            return ('error: ' + str(e))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Liquidacion Empleado'
        return context
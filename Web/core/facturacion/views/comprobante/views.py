####################################################
################# Imagen Proforma  ###############
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from core.clases_general.mixins import GroupRequiredMixin2
from core.facturacion.forms.comprobante.forms import StImagenesPagareForm
from core.facturacion.modelos.comprobante.models import VtComprobanteWeb, StImagenesPagare, VtComprobante


class ImagenComprobanteView(LoginRequiredMixin, GroupRequiredMixin2, TemplateView):
    template_name = 'comprobante/imagen_comp.html'
    permission_required = 'view_stimagenespagare'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        try:
            action = request.POST['action']
            if action == 'search_comprobante':
                data = []
                # prof = VtComprobanteWeb.objects.all()
                prof = VtComprobante.objects.all()
                for i in prof.filter(cod_comprobante__icontains=request.POST['term'])[0:5]:
                    item = i.toJSON()
                    item ['value'] = i.cod_comprobante + ' - ' + i.nom_cliente #i.nombre_persona
                    data.append(item)

            elif action == 'search_img':
                prof = StImagenesPagare.objects.filter(cod_comprobante = request.POST['comprobante'])
                data = [i.toJSON() for i in prof]

            elif action == 'subirImg':
                form = StImagenesPagareForm(request.POST, request.FILES)
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
        context['title'] = 'Imagenes Comprobante'
        context['form_img'] = StImagenesPagareForm
        context['lista'] = [{'id':'14', 'nom': 'PAGARE FRONT'},
                            {'id':'15', 'nom': 'PAGARE POST'},
                            {'id':'16', 'nom': 'CLIENTE FIRMANDO'},
                            {'id':'17', 'nom': 'CED CLI FRONT'},
                            {'id':'18', 'nom': 'CEC CLI POST'},
                            {'id':'19', 'nom': 'CERT VOTACIÓN'},
                            {'id':'20', 'nom': 'GARANTE FIRM'},
                            {'id':'21', 'nom': 'CED GART FRONT'},
                            {'id':'22', 'nom': 'CED GART POST'},
                            {'id':'23', 'nom': 'CERT GAR VOT.'},]
        return context
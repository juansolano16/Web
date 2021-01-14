################# PROFORMAS IMAGENES CLIENTE ###############
from django.forms import ModelForm
from django import forms

from core.facturacion.modelos.proforma.models import StClientesImagenesDocumento


class StClientesImgDocForm(ModelForm):
    class Meta:
        model = StClientesImagenesDocumento
        # fields = '__all__'
        fields = ['fecha_transaccion', 'cod_cliente', 'empresa', 'codigo_tipo_imagen_documento', 'adicionado_por', 'anulado', 'path_dir']
        widgets = {'fecha_transaccion': forms.HiddenInput(),
                   'cod_cliente': forms.HiddenInput(),
                   'empresa': forms.HiddenInput(),
                   'codigo_tipo_imagen_documento': forms.HiddenInput(),
                   'adicionado_por': forms.HiddenInput(),
                   'anulado': forms.HiddenInput(),
                   }


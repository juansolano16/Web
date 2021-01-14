from django import forms
from django.forms.models import ModelForm

from core.facturacion.modelos.comprobante.models import StImagenesPagare


class StImagenesPagareForm(ModelForm):
    class Meta:
        model = StImagenesPagare
        fields = '__all__'
        widgets = {'empresa': forms.HiddenInput(),
                   'tipo_comprobante': forms.HiddenInput(),
                   'cod_comprobante': forms.HiddenInput(),
                   'cod_tipo_documento': forms.HiddenInput(),
                   'fecha_adicion': forms.HiddenInput(),
                   }

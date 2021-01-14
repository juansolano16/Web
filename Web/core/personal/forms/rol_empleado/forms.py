# from django.forms import *
from django.forms import ModelChoiceField, Form, ChoiceField
from django.forms.widgets import Select

from core.personal.models.personal.models import VtPersonal, RhComprobante, RhPeriodoDecimos


####################################################
################# ROLES DE EMPLEADOS ###############
class formRolEmpleado(Form):
    cod_persona = ModelChoiceField(queryset=VtPersonal.objects.all(), widget=Select(attrs={
        'class': 'form-control select2',
    }))
    periodo = ModelChoiceField(queryset=RhComprobante.objects.none(), widget=Select(attrs={
        'class': 'form-control select2'
    }))


############################################################
################# ROL DE BENEFICIOS SOCILAES ###############
class formRolBeneficio(Form):
    # iterable
    BEN_CHOICES = [("D4", "Decimo Cuarto"),
                   ("D3", "Decimo Tercero"),]

    REG_CHOICES = [("COSTA", "Costa"),
                   ("SIERRA", "Sierra y Oriente"),]

    beneficio = ChoiceField(choices=BEN_CHOICES, widget=Select(attrs={
        'class': 'form-control select2',
    }))
    region = ChoiceField(choices=REG_CHOICES, widget=Select(attrs={
        'class': 'form-control select2'
    }))
    periodo = ModelChoiceField(queryset=RhPeriodoDecimos.objects.filter(tipo='D4', pregion='SIERRA'),
                               widget=Select(attrs={
                                   'class': 'form-control select2'
                               }))

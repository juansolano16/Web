
from django import forms
from django.forms.widgets import Select, TextInput, Textarea

from core.inventario.models.inventario.models import StInventarioObservacion, VtReporteAuditoriaGeneral
from core.inventario.models.producto.models import Marca
from core.personal.models.personal.models import TgAgencia

TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)


################# INVENTARIO FIN DE ANIO ###############
class formTgAgencia(forms.Form):
    nombre = forms.ModelChoiceField(queryset=TgAgencia.objects.filter(activo='S', empresa =2), widget=Select(attrs={
        'class': 'form-control select2', 'id': 'cod_agencia'
    }))


class formMarcaProducto(forms.Form):
    nombre = forms.ModelChoiceField(queryset=Marca.objects.filter(empresa=2),
        widget=Select(attrs={'class': 'form-control select2', 'id':'cat_producto'}),
        initial='MOTOS',
    )


class formStIventarioDMoto(forms.Form):
    ###### campos visibles #####
    factura = forms.CharField(label='Factura/Cliente', widget=TextInput(attrs={
        'readonly': True,
        'placeholder': 'Ingrese el codigo del producto',
        'id': 'factura_moto'
    }))
    cod_producto = forms.CharField(widget=TextInput(attrs={
        'readonly': True,
        'placeholder': 'Ingrese el codigo del producto',
        'id': 'cod_producto_moto'
    }))

    serie = forms.CharField(label='Serie/Motor', widget=TextInput(attrs={
        'readonly': True,
        'placeholder': 'Ingrese el codigo de serie',
        'id': 'serie_moto'
    }))
    chasis = forms.CharField(widget=TextInput(attrs={
        'readonly': True,
        'placeholder': 'Codigo de Chasis',
        'id': 'chasis_moto'
    }))
    estado = forms.BooleanField(label='¿Se encuentra físicamente? (Señale solo "SI" el producto tiene en la agencia)', required=False,)
    kit = forms.BooleanField(label='¿Tiene kit? (Solo "SI" dispone del kit)', required=False)
    observacion1 = forms.ModelChoiceField(queryset=StInventarioObservacion.objects.filter(empresa=2,categoria=1),
        widget=Select(attrs={
            'class': 'form-control select2',
            'id': 'observacion1'
    }))
    observacion2 = forms.CharField(label='Obsevación Detallada', max_length=1000, required=False, widget=Textarea(attrs={
        'placeholder': 'Ingrese una observación',
        'rows' : 3,
        'cols': 3,
        'id':'obsevacion2'
    }))
    ###### campos ocultos #####
    tipo_comprobante = forms.CharField(initial='IV', widget=forms.HiddenInput(attrs={'id': 'tipo_comprobante_moto'}))
    cod_comprobante = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'cod_comprobante_moto'}))
    categoriaInv = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'categoriaInv_moto'}))
    ingreso_manual = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'update_moto'}))
    sobrante = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'sobrante_moto'}))


class formStIventarioDRep(forms.Form):
    ###### campos visibles #####
    cod_producto = forms.CharField(widget=TextInput(attrs={
        'readonly': False,
        'placeholder': 'Ingrese el codigo del producto',
        'id': 'cod_producto_rep'
    }))
    cantidad = forms.IntegerField(label='Cantidad Existente', initial=1)
    rayon = forms.BooleanField(label='¿Tiene rayón/desperfecto/es usado? (Seleccione solo "SI" el producto tiene esta novedad)', required=False)
    cantidad_rayon = forms.IntegerField(label='Ingrese Cantidad', initial=1)
    transferencia = forms.BooleanField(label='¿Está por recibir? (Solo "SI" el producto está en transferencia)', required=False)
    cantidad_trans = forms.IntegerField(label='Ingrese Cantidad', initial=1)
    observacion1 = forms.ModelChoiceField(label='Obsevación', queryset=StInventarioObservacion.objects.filter(empresa=2,categoria=2),
        widget=Select(attrs={
            'class': 'form-control select2',
            'id': 'observacion1_rep'
    }))
    observacion2 = forms.CharField(label='Obsevación Detallada', max_length=1000, required=False, widget=Textarea(attrs={
        'placeholder': 'Ingrese una observación',
        'rows' : 3,
        'cols': 3,
        'id': 'observacion2_rep'
    }))
    ###### campos ocultos #####
    tipo_comprobante = forms.CharField(initial='IV', widget=forms.HiddenInput(attrs={'id': 'tipo_comprobante_rep'}))
    cod_comprobante = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'cod_comprobante_rep'}))
    serie = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'serie_rep'}))
    categoriaInv = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'categoriaInv_rep'}))
    ingreso_manual = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'update_rep'}))
    sobrante = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'cobrante_rep'}))
    cantidad_reg = forms.IntegerField(widget=forms.HiddenInput(attrs={'id': 'cantidad_reg'}))
    tipo = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'tipo_rep'}))


class formStIventarioDAuvi(forms.Form):
    ###### campos visibles #####
    cod_producto = forms.CharField(widget=TextInput(attrs={
        'readonly': False,
        'placeholder': 'Ingrese el codigo del producto',
        'id': 'cod_producto_auvi'
    }))
    serie = forms.CharField(widget=TextInput(attrs={
        'readonly': True,
        'placeholder': 'Ingrese el codigo de serie',
        'id': 'serie_auvi'
    }))
    estado_prod = forms.BooleanField(label='¿Se encuentra físicamente? (Señale solo "SI" el producto tiene en la agencia)',
                                required=False, )
    desperfecto = forms.BooleanField(label='¿Tiene rayón o desperfecto? (Seleccione solo "SI" el producto tiene esta novedad)', required=False)
    promocional = forms.BooleanField(label='¿Falta promocionales? (Seleccione solo "SI" el producto tiene esta novedad)', required=False)
    garantia = forms.BooleanField(label='¿Garantia/Tramites? (Seleccione solo "SI" el producto tiene esta novedad)', required=False)
    transferencia1 = forms.BooleanField(label='¿Está por recibir? (Seleccione solo "SI" el producto tiene esta novedad)', required=False)
    # cantidad_trans1 = forms.IntegerField(label='Ingrese Cantidad', initial=1)
    observacion1 = forms.ModelChoiceField(label='Obsevación', queryset=StInventarioObservacion.objects.filter(empresa=2,categoria=3),
        widget=Select(attrs={
            'class': 'form-control select2',
            'id': 'observacion1_auvi'
    }))
    observacion2 = forms.CharField(label='Obsevación Detallada', max_length=1000, required=False, widget=Textarea(attrs={
        'placeholder': 'Ingrese una observación',
        'rows' : 3,
        'cols': 3,
        'id': 'observacion2_auvi'
    }))
    ###### campos ocultos #####
    tipo_comprobante = forms.CharField(initial='IV', widget=forms.HiddenInput(attrs={'id': 'tipo_comprobante_auvi'}))
    cod_comprobante = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'cod_comprobante_auvi'}))
    categoriaInv = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'categoriaInv_auvi'}))
    ingreso_manual = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'update_auvi'}))
    sobrante = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'cobrante_auvi'}))


class formVtReporteAuditoriaGeneral(forms.ModelForm):
    class Meta:
        model = VtReporteAuditoriaGeneral
        fields = '__all__'





from django.forms import ModelForm, TextInput, Select, Form, ModelChoiceField, CharField

from core.inventario.models.producto.models import StProductoDetalle, vt_producto_web2, VtCaracteristicasProd


class DetalleProductoWebFormEdit(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['cod_turno'].widget.attrs['autofocus'] = True

    class Meta:
        model = StProductoDetalle
        #fields = '__all__'
        fields = ['secuencia', 'cod_producto', 'caracteristicas', 'detalle']
        widgets = {
            'cod_producto': TextInput(
                attrs={
                    'placeholder': 'Ingrese agencia', 'readonly': True,
                }
            ),
            'secuencia': TextInput(
                attrs={
                    'placeholder': 'Ingrese agencia', 'readonly':True,
                }
            ),
            'caracteristicas': TextInput(
                attrs={
                    'placeholder': 'Ingrese agencia', 'readonly': True,
                }
            ),
        }

class DetalleProductoWebFormAdd(Form):
    cod_producto = ModelChoiceField(queryset=vt_producto_web2.objects.distinct(), widget=Select(
        attrs={'class': 'form-control select2'}
    ))
    caracteristica = ModelChoiceField(queryset=VtCaracteristicasProd.objects.all(), widget=Select(
        attrs={'class': 'form-control select2'}
    ))
    #carateritica2 = CharField(label='Caracteristica', max_length=50)
    detalle = CharField(label='Detalle', max_length=4000)
from django.forms import ModelForm, TextInput, Textarea, Select

from core.personal.models.encuesta.models import RhResultadosEncuesta, VtPersonalTurnos


class EncuestaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['observacion'].widget.attrs['autofocus'] = True

    class Meta:
        model = RhResultadosEncuesta
        #fields = '__all__'
        fields = ['id_encuesta','cod_persona', 'condicion', 'observacion', 'ficha', 'num_sintomas_positivo', 'cita_medica', 'observacion_medica', 'reposom_fdesde','reposom_fhasta','alta']
        labels = {
            'id_encuesta': 'Encuesta', 'reposom_fdesde': 'Reposo Medico Desde','reposom_fhasta': 'Reposo Medico Hasta'
        }
        widgets = {
            'id_encuesta': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'cod_persona': Textarea(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'rows': 1,
                    #'cols': 3
                }
            ),
            'reposom_fdesde': TextInput(
                attrs={
                    'placeholder': 'Ingrese una fecha',
                    'rows': 1,
                    'type': 'date'
                }
            ),
            'reposom_fhasta': TextInput(
                attrs={
                    'placeholder': 'Ingrese una fecha',
                    'rows': 1,
                    'type': 'date'
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


############ GESTION DE TURNOS ###############################
class turnosEmpleadoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cod_turno'].widget.attrs['autofocus'] = True

    class Meta:
        model = VtPersonalTurnos
        fields = ['cedula','empleado', 'agencia', 'cargo', 'cod_turno',]
        widgets = {
            'cedula': TextInput(
                attrs={
                    'placeholder': 'Ingrese la cedula', 'readonly':True,
                }
            ),
            'empleado': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre', 'readonly':True,
                }
            ),
            'agencia': TextInput(
                attrs={
                    'placeholder': 'Ingrese agencia', 'readonly':True,
                }
            ),
            'cargo': TextInput(
                attrs={
                    'placeholder': 'Ingrese un cargo', 'readonly':True,
                }
            ),
            'cod_turno': Select()
        }



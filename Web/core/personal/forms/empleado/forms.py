################# LIQUIDACION DE EMPLEADOS ###############
from crispy_forms.bootstrap import TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Field
from django.forms import Form, ModelChoiceField, ModelForm
from django.forms.widgets import Select

from core.personal.models.personal.models import VtPersonal, RhPersonal


class formRhPersonal(ModelForm):

    class Meta:
        model = RhPersonal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs.update({'class': 'form-control form-control-sm'})

        self.helper = FormHelper()
        # self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Field('empresa', type="hidden", value=2),
            Field('cod_tipo_persona', type="hidden", value='EMP'),
            Row(
                Column('cod_personal', css_class='form-group col-md-2 mb-0'),
                Column('nombre', css_class='form-group col-md-2 mb-0'),
                Column('apellido', css_class='form-group col-md-2 mb-0'),
                Column('sexo', css_class='form-group col-md-1 mb-0'),
                Column('nacionalidad', css_class='form-group col-md-1 mb-0'),
                Column('estado_civil', css_class='form-group col-md-1 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('codigo_cargo__descripcion', css_class='form-group col-md-2 mb-0'),
                Column('cod_departamento', css_class='form-group col-md-2 mb-0'),
                Column('cod_agencia', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('telefono', css_class='form-group col-md-2 mb-0'),
                Column('telefono1', css_class='form-group col-md-2 mb-0'),
                Column('nacimiento', css_class='form-group col-md-2 mb-0'),
                Column('e_mail', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            TabHolder(
                Tab('First Tab',
                    'field_name_1',
                    ),
                Tab('Second Tab',
                    Field('field_name_3', css_class="extra")
                    )
            ),
            # 'check_me_out',
            # Submit('submit', 'Sign in')
        )


class formLiqEmpleado(Form):
    cod_persona = ModelChoiceField(queryset=VtPersonal.objects.all(), widget=Select(attrs={
        'class': 'form-control select2',
    }))
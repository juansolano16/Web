################# LIQUIDACION DE EMPLEADOS ###############
from crispy_forms.bootstrap import TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Field, HTML
from crispy_forms.utils import TEMPLATE_PACK
from django.forms import Form, ModelChoiceField, ModelForm, ChoiceField
from django.forms.widgets import Select

from core.clases_general.Utilities import choiseActivo
from core.personal.models.personal.models import VtPersonal, RhPersonal


class formPersonalActivo(Form):
    activo = ChoiceField(choices=choiseActivo, label='Personal Activo:', initial=choiseActivo[2])


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
            TabHolder(
                Tab('Datos personales',
                    Row(
                        Column(
                            'cod_personal',
                            Row(Column('nombre', css_class='form-group col-md-6 mb-0'),
                                Column('apellido', css_class='form-group col-md-6 mb-0'),
                                ),
                            Row(Column('nacionalidad', css_class='form-group col-md-6 mb-0'),
                                Column('sexo', css_class='form-group col-md-3 mb-0'),
                                Column('estado_civil', css_class='form-group col-md-3 mb-0'),
                                ),
                            Row(
                                Column('fecha_ingreso', css_class='form-group col-md-3 mb-0'),
                                Column('ingreso_por', css_class='form-group col-md-3 mb-0'),
                                Column('discapacidad', css_class='form-group col-md-3 mb-0'),
                                Column('porcentaje_discap', css_class='form-group col-md-3 mb-0'),
                            ),
                            css_class='form-group col-md-8 mb-0'
                        ),
                        Column(
                            HTML(
                                """<div class="row" id="div_img2" data-src="/static/img/persona.png" style="justify-content: center"> 
                                      <img class="scale-on-hover img_img" id="img2" src="/static/img/persona.png" alt="Card Image" width="250" height="300"> 
                                   </div>""",
                            ),
                            css_class='form-group col-md-4 mb-0'
                        ),
                    ),
                    Row(
                        Column('cod_agencia', css_class='form-group col-md-4 mb-0'),
                        Column('cod_departamento', css_class='form-group col-md-4 mb-0'),
                        Column('codigo_cargo', css_class='form-group col-md-4 mb-0'),
                        css_class='form-row'
                    ),
                    Row(
                        Column('fecha_egreso', css_class='form-group col-md-2 mb-0'),
                        Column('motivo_salida', css_class='form-group col-md-2 mb-0'),
                        css_class='form-row'
                    ),
                ),
                Tab('Estudios Realizados',
                     HTML('''  {% load embed %}
                               {% embed 'datatable.html' with idtable='tblEstudios' %}
                                    {% block columns %}
                                        <tr>
                                            <th scope="col" style="width: 20%;">Nivel Instruccion:</th>
                                            <th scope="col" style="width: 20%;">Institucion:</th>
                                            <th scope="col" style="width: 20%;">Observacion</th>
                                        </tr>
                                    {% endblock %}
                               {% endembed %}''')
                ),
                Tab('Historial Cargos',
                     HTML( ''' {% load embed %}
                               {% embed 'datatable.html' with idtable='tblCargos' %}
                                    {% block columns %}
                                        <tr>
                                            <th scope="col" style="width: 15%;">Ingreso por:</th>
                                            <th scope="col" style="width: 20%;">Descripción Cargo</th>
                                            <th scope="col" style="width: 5%;">F.Desde</th>
                                            <th scope="col" style="width: 5%;">F.Hasta</th>
                                            <th scope="col" style="width: 20%;">Agencia</th>
                                            <th scope="col" style="width: 5%;">F.Ingreso</th>
                                            <th scope="col" style="width: 5%;">F.Egreso</th>
                                            <th scope="col" style="width: 20%;">Motivo Salida</th>
                                        </tr>
                                    {% endblock %}
                               {% endembed %}''')
                ),
                Tab('Parametros Empresa',
                    Row(
                        Column('tipo_contrato', css_class='form-group col-md-2 mb-0'),
                        Column('empleo_juvenil', css_class='form-group col-md-2 mb-0'),
                        Column('tiempo_parcial', css_class='form-group col-md-2 mb-0'),
                        Column('banco', css_class='form-group col-md-2 mb-0'),
                        Column('cuenta_corriente', css_class='form-group col-md-2 mb-0'),
                        Column('cuenta_ahorros', css_class='form-group col-md-2 mb-0'),
                        css_class='form-row'
                    ),
                ),
            ),
            # 'check_me_out',
            # Submit('submit', 'Sign in')
        )


class formLiqEmpleado(Form):
    cod_persona = ModelChoiceField(queryset=VtPersonal.objects.all(), widget=Select(attrs={
        'class': 'form-control select2',
    }))

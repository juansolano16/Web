from django.db import models
from django.forms import model_to_dict
from django.db.models import Q

from core.personal.models.personal.models import RhPersonal, TgAgencia, RhCargos

ORDER_COLUMN_CHOICES_RE = [
    {"data": "id_encuesta"},
    {"data": "agencia"},
    {"data": "cod_persona"},
    {"data": "empleado"},
    {"data": "telefono"},
    {"data": "cargo"},
    {"data": "ficha"},
    {"data": "condicion"},
    {"data": "observacion"},
    {"data": "num_sintomas_positivo"},
    {"data": "num_sintomas_positivo"},
]


turnos_choices = (
    ('T1','T1'),
    ('T2','T2'),
    ('T3','T3'),
    ('T4','T4'),
    ('T5','T5'),
)

############ ADMINISTRACION ENCUESTAS COVID #################
class RhPersonalEncuesta(models.Model):
    # empresa = models.OneToOneField(RhPersonal, models.DO_NOTHING, db_column='empresa', primary_key=True)
    empresa = models.IntegerField(primary_key=True)
    id_encuesta = models.CharField(max_length=9)
    # cod_tipo_persona = models.ForeignKey(RhPersonal, models.DO_NOTHING, db_column='cod_tipo_persona', related_name='tipo_persona')
    cod_tipo_persona = models.CharField(max_length=3)
    cod_persona = models.ForeignKey(RhPersonal, models.DO_NOTHING, db_column='cod_persona', related_name='cod_persona')
    ciudad_reg = models.CharField(max_length=40, blank=True, null=True)
    agencia_reg = models.CharField(max_length=50, blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    pregunta = models.CharField(max_length=500)
    respuesta = models.CharField(max_length=1000, blank=True, null=True)
    fecha_registro = models.DateTimeField()
    fecha_aud = models.DateField(blank=True, null=True)

    # fecha_tmp = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rh_personal_encuesta'
        unique_together = (('empresa', 'id_encuesta', 'cod_tipo_persona', 'cod_persona', 'pregunta', 'fecha_registro'),)


class RhResultadosEncuesta(models.Model):
    empresa = models.IntegerField()
    id_encuesta = models.CharField(max_length=20)
    cod_tipo_persona = models.CharField(max_length=3)
    cod_persona = models.CharField(max_length=15)
    observacion = models.CharField(max_length=500, blank=True, null=True)
    ficha = models.CharField(max_length=50)
    num_sintomas_positivo = models.IntegerField(blank=True, null=True)
    cita_medica = models.CharField(max_length=50, blank=True, null=True)
    observacion_medica = models.CharField(max_length=500, blank=True, null=True)
    alta = models.CharField(max_length=100, blank=True, null=True)
    num_sintomas_negativo = models.IntegerField(blank=True, null=True)
    condicion = models.CharField(max_length=500, blank=True, null=True)
    reposom_fdesde = models.DateField(blank=True, null=True)
    reposom_fhasta = models.DateField(blank=True, null=True)

    def toJSON(self):
        p = RhPersonal.objects.get(cod_personal=self.cod_persona)
        a = TgAgencia.objects.get(cod_agencia=p.cod_agencia, empresa=p.empresa)
        c = RhCargos.objects.get(codigo_empresa=p.empresa, codigo_cargo=p.codigo_cargo.codigo_cargo)
        item = model_to_dict(self)
        item['empleado'] = p.apellido + ' ' + p.nombre
        item['agencia'] = a.nombre
        item['cargo'] = c.descripcion
        return item

    class Meta:
        managed = False
        db_table = 'rh_resultados_encuesta'
        unique_together = (('empresa', 'id_encuesta', 'cod_tipo_persona', 'cod_persona', 'ficha'),)


class VtRhResultadosEncuesta(models.Model):
    empresa = models.IntegerField(primary_key=True)
    id_encuesta = models.CharField(max_length=20)
    fecha_enc = models.DateTimeField()
    agencia = models.CharField(max_length=50)
    cod_tipo_persona = models.CharField(max_length=3)
    cod_persona = models.CharField(max_length=15)
    condicion = models.CharField(max_length=500, blank=True, null=True)
    empleado = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    cargo = models.CharField(max_length=50)
    ficha = models.CharField(max_length=50)
    observacion = models.CharField(max_length=500, blank=True, null=True)
    num_sintomas_positivo = models.IntegerField(blank=True, null=True)
    num_sintomas_negativo = models.IntegerField(blank=True, null=True)
    cita_medica = models.CharField(max_length=50, blank=True, null=True)
    observacion_medica = models.CharField(max_length=500, blank=True, null=True)
    alta = models.CharField(max_length=100, blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'vt_rh_resultado_encuesta'
        # ordering = ['-fecha_enc']


def query_resultadosEncuesta_by_args(**kwargs):
    draw = int(kwargs.get('draw', None)[0])
    length = int(kwargs.get('length', None)[0])
    start = int(kwargs.get('start', None)[0])
    search_value = kwargs.get('search[value]', None)[0]
    order_column = kwargs.get('order[0][column]', None)[0]
    order = kwargs.get('order[0][dir]', None)[0]

    order_column = ORDER_COLUMN_CHOICES_RE[int(order_column)]['data']
    # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column

    queryset = VtRhResultadosEncuesta.objects.all()
    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(id_encuesta__icontains=search_value) |
                                   Q(agencia__icontains=search_value) |
                                   Q(cod_persona__icontains=search_value) |
                                   Q(empleado__icontains=search_value) |
                                   Q(telefono__icontains=search_value) |
                                   Q(cargo__icontains=search_value) |
                                   Q(ficha__icontains=search_value) |
                                   Q(condicion__icontains=search_value) |
                                   Q(observacion__icontains=search_value))
    count = queryset.count()
    if order_column.find('id_encuesta') == -1:
        queryset = queryset.order_by(order_column)[start:start + length]
    else:
        queryset = queryset[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }


############ GESTION DE TURNOS ###############################
class VtTurnos(models.Model):
    empresa = models.IntegerField()
    modalidad = models.CharField(max_length=20, primary_key=True)
    t1 = models.CharField(max_length=50, blank=True, null=True)
    t2 = models.CharField(max_length=50, blank=True, null=True)
    t3 = models.CharField(max_length=50, blank=True, null=True)
    t4 = models.CharField(max_length=50, blank=True, null=True)
    t5 = models.CharField(max_length=50, blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vt_turnos'


class VtPersonalTurnos(models.Model):
    empresa = models.IntegerField()
    cedula = models.CharField(max_length=14, primary_key=True)
    empleado = models.CharField(max_length=101, blank=True, null=True)
    agencia = models.CharField(max_length=50)
    cargo = models.CharField(max_length=200)
    cod_turno = models.CharField(max_length=6, choices=turnos_choices, default='T1')

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vt_personal_turnos'


class RhPersonalTurnos(models.Model):
    empresa = models.OneToOneField('RhPersonal', models.DO_NOTHING, db_column='empresa', related_name='empresa_rh_per_turno')
    cod_tipo_persona = models.ForeignKey('RhPersonal', models.DO_NOTHING, db_column='cod_tipo_persona', related_name='cod_tip_rh_per_turno')
    #cod_persona = models.ForeignKey('RhPersonal', models.DO_NOTHING, db_column='cod_persona', primary_key=True, related_name='cod_personal_per')
    cod_persona = models.OneToOneField('RhPersonal', models.DO_NOTHING, db_column='cod_persona', primary_key=True, related_name='cod_personal_per')
    cod_turno = models.CharField(max_length=6, choices=turnos_choices, default='T1')
    observacion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rh_personal_turnos'
        unique_together = (('empresa', 'cod_tipo_persona', 'cod_persona', 'cod_turno'),)
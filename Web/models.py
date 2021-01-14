# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class RhPersonal(models.Model):
    empresa = models.OneToOneField('RhCargos', models.DO_NOTHING, db_column='empresa', primary_key=True)
    cod_personal = models.CharField(max_length=14)
    cod_tipo_persona = models.CharField(max_length=3)
    nombre = models.CharField(max_length=50)
    cod_departamento = models.IntegerField(blank=True, null=True)
    codigo_cargo = models.ForeignKey('RhCargos', models.DO_NOTHING, db_column='codigo_cargo', blank=True, null=True)
    cod_agencia = models.IntegerField(blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    telefono1 = models.CharField(max_length=10, blank=True, null=True)
    e_mail = models.CharField(max_length=30, blank=True, null=True)
    nacimiento = models.DateField(blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    fecha_egreso = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    estado_civil = models.CharField(max_length=1, blank=True, null=True)
    cuenta_corriente = models.CharField(max_length=20, blank=True, null=True)
    cuenta_ahorros = models.CharField(max_length=20, blank=True, null=True)
    activo = models.CharField(max_length=1, blank=True, null=True)
    cod_cliente = models.CharField(max_length=14, blank=True, null=True)
    cod_tipo_cliente = models.CharField(max_length=3, blank=True, null=True)
    codigo_contable = models.CharField(max_length=14, blank=True, null=True)
    useridc = models.CharField(max_length=3, blank=True, null=True)
    aud_fecha = models.DateField(blank=True, null=True)
    aud_usuario = models.CharField(max_length=30, blank=True, null=True)
    aud_terminal = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    cod_tipo_identificacion = models.IntegerField(blank=True, null=True)
    banco = models.CharField(max_length=3, blank=True, null=True)
    legado = models.CharField(max_length=14, blank=True, null=True)
    usuario_oracle = models.CharField(max_length=20, blank=True, null=True)
    fecha_reingreso = models.DateField(blank=True, null=True)
    empleo_juvenil = models.CharField(max_length=1, blank=True, null=True)
    tiempo_parcial = models.CharField(max_length=1, blank=True, null=True)
    motivo_salida = models.CharField(max_length=20, blank=True, null=True)
    region = models.CharField(max_length=20, blank=True, null=True)
    porcentaje_discap = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    discapacidad = models.CharField(max_length=2)
    ingreso_por = models.CharField(max_length=40, blank=True, null=True)
    condicion_discapacidad = models.CharField(max_length=3)
    ced_sutituye = models.CharField(max_length=14, blank=True, null=True)
    nacionalidad = models.CharField(max_length=30)
    e_mail_institucional = models.CharField(max_length=50, blank=True, null=True)
    telefono_enc = models.CharField(max_length=15, blank=True, null=True)
    horas_tiempo_parcial = models.FloatField(blank=True, null=True)
    tipo_contrato = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rh_personal'
        unique_together = (('empresa', 'cod_tipo_persona', 'cod_personal'),)

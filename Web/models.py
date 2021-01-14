# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class VtReporteAuditoriaGeneral(models.Model):
    empresa = models.FloatField()
    tipo_comprobante = models.CharField(max_length=3)
    cod_comprobante = models.CharField(max_length=9)
    cod_agencia = models.FloatField()
    cod_producto = models.CharField(max_length=50)
    producto = models.CharField(max_length=200)
    serie = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    chasis = models.CharField(max_length=20, blank=True, null=True)
    sobrante = models.CharField(max_length=1)
    faltante = models.CharField(max_length=1, blank=True, null=True)
    ingreso_manual_serie = models.CharField(max_length=1)
    categoria = models.CharField(max_length=10, blank=True, null=True)
    categoria2 = models.CharField(max_length=46, blank=True, null=True)
    cantidad = models.FloatField()
    estado_m = models.CharField(max_length=500, blank=True, null=True)
    kit_m = models.CharField(max_length=500, blank=True, null=True)
    observacion1 = models.CharField(max_length=500, blank=True, null=True)
    observacion2 = models.CharField(max_length=500, blank=True, null=True)
    rayon_r = models.CharField(max_length=500, blank=True, null=True)
    transferencia_r = models.CharField(max_length=500, blank=True, null=True)
    desperfecto_a = models.CharField(max_length=500, blank=True, null=True)
    promocional_a = models.CharField(max_length=500, blank=True, null=True)
    garantia_a = models.CharField(max_length=500, blank=True, null=True)
    porrecibir_a = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vt_reporte_auditoria_general'

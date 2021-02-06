# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class StProdPackingList(models.Model):
    cod_chasis = models.CharField(primary_key=True, max_length=20)
    cod_motor = models.CharField(max_length=30)
    cod_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='cod_producto')
    empresa = models.ForeignKey('Producto', models.DO_NOTHING, db_column='empresa')
    fecha = models.DateField()
    es_disponible = models.BooleanField(blank=True, null=True)
    es_anulado = models.BooleanField(blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    eliminado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_elimiacion = models.DateField(blank=True, null=True)
    camvcpn = models.CharField(max_length=20, blank=True, null=True)
    anio = models.IntegerField()
    color = models.CharField(max_length=30)
    marca = models.CharField(max_length=30, blank=True, null=True)
    cilindraje = models.IntegerField()
    pasajeros = models.IntegerField()
    origen = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    tonelaje = models.CharField(max_length=5)
    ejes = models.CharField(max_length=3)
    ruedas = models.CharField(max_length=3)
    tipo = models.CharField(max_length=40, blank=True, null=True)
    combustible = models.CharField(max_length=10, blank=True, null=True)
    color2 = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ST_PROD_PACKING_LIST'
        unique_together = (('cod_chasis', 'cod_producto', 'empresa'), ('cod_motor', 'empresa'), ('cod_chasis', 'empresa'),)

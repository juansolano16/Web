# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.forms.models import model_to_dict

############# VISTAS ##########################
class VtProdSerie(models.Model):
    empresa = models.IntegerField()
    cod_producto = models.CharField(max_length=40)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    serie = models.CharField(max_length=30, primary_key=True)
    chasis = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vt_prod_serie'



class VtReporteInventarioFinal(models.Model):
    tipo = models.CharField(max_length=4, blank=True, null=True)
    codigo = models.CharField(max_length=40, primary_key=True)
    producto = models.CharField(max_length=200)
    cod_categoria = models.CharField(max_length=200)
    tiene_devolucion = models.FloatField(blank=True, null=True)
    motor = models.CharField(max_length=30)
    chasis = models.CharField(max_length=20, blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    total = models.CharField(max_length=1, blank=True, null=True)
    agencia = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    dias = models.CharField(max_length=7, blank=True, null=True)
    empresa = models.IntegerField()
    cod_agencia = models.IntegerField(blank=True, null=True)
    #origen = models.CharField(max_length=500)
    invgrabado = models.IntegerField()
    factura = models.CharField(max_length=50)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vt_reporte_inventario'
        ordering = ['producto']

class VtResultadoAudMoto(models.Model):
    cod_agencia = models.IntegerField(blank=True, null=True, primary_key=True)
    agencia = models.CharField(max_length=50, blank=True, null=True)
    total_prod = models.FloatField(blank=True, null=True)
    registrados = models.FloatField(blank=True, null=True)
    porcentaje = models.FloatField(blank=True, null=True)
    sobrante = models.FloatField(blank=True, null=True)
    faltante = models.FloatField(blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vt_resultado_aud_moto'



class VtReporteRepuestos(models.Model):
    tipo = models.CharField(max_length=4, blank=True, null=True)
    codigo = models.CharField(max_length=40, primary_key=True)
    producto = models.CharField(max_length=200)
    cod_categoria = models.CharField(max_length=200)
    tiene_devolucion = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    grupo = models.CharField(max_length=50)
    dias = models.CharField(max_length=1, blank=True, null=True)
    empresa = models.IntegerField()
    cod_agencia = models.IntegerField(blank=True, null=True)
    origen = models.CharField(max_length=100, blank=True, null=True)
    invgrabado = models.IntegerField()
    cantidad_reg = models.IntegerField()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vt_reporte_repuestos'
        ordering = ['producto']

class VtResultadoAudRep(models.Model):
    cod_agencia = models.IntegerField(blank=True, null=True, primary_key=True)
    agencia = models.CharField(max_length=50)
    total_prod = models.FloatField(blank=True, null=True)
    registrados = models.FloatField(blank=True, null=True)
    porcentaje = models.FloatField(blank=True, null=True)
    sobrante = models.FloatField(blank=True, null=True)
    faltante = models.FloatField(blank=True, null=True)


    def toJSON(self):
        item = model_to_dict(self)
        return item


    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vt_resultado_aud_rep'



class VtReporteInvAuvi(models.Model):
    tipo = models.CharField(max_length=4, blank=True, null=True)
    codigo = models.CharField(max_length=40, primary_key=True)
    producto = models.CharField(max_length=200)
    cod_categoria = models.IntegerField()
    tiene_devolucion = models.IntegerField(blank=True, null=True)
    motor = models.CharField(max_length=30)
    chasis = models.CharField(max_length=20, blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    total = models.CharField(max_length=1, blank=True, null=True)
    agencia = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    dias = models.CharField(max_length=7, blank=True, null=True)
    empresa = models.IntegerField()
    cod_agencia = models.IntegerField(blank=True, null=True)
    invgrabado = models.IntegerField(blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vt_reporte_inv_auvi'
        ordering = ['producto']

class VtResultadoAudAuvi(models.Model):
    cod_agencia = models.IntegerField(blank=True, null=True, primary_key=True)
    agencia = models.CharField(max_length=50)
    total_prod = models.FloatField(blank=True, null=True)
    registrados = models.FloatField(blank=True, null=True)
    porcentaje = models.FloatField(blank=True, null=True)
    sobrante = models.FloatField(blank=True, null=True)
    faltante = models.FloatField(blank=True, null=True)


    def toJSON(self):
        item = model_to_dict(self)
        return item


    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vt_resultado_aud_auvi'


#***  REPORTE GENERAL ***
class VtReporteAuditoriaGeneral(models.Model):
    empresa = models.FloatField()
    tipo_comprobante = models.CharField(max_length=3)
    cod_comprobante = models.CharField(max_length=9, primary_key=True)
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
    cantidad_reg_r = models.CharField(max_length=500, blank=True, null=True)
    desperfecto_a = models.CharField(max_length=500, blank=True, null=True)
    promocional_a = models.CharField(max_length=500, blank=True, null=True)
    garantia_a = models.CharField(max_length=500, blank=True, null=True)
    porrecibir_a = models.CharField(max_length=500, blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vt_reporte_auditoria_general'
        ordering = ['-sobrante']



############# TABLAS #########
class StInventarioObservacion(models.Model):
    empresa = models.FloatField()
    secuencia = models.FloatField()
    observacion = models.CharField(max_length=100, blank=True, null=True, primary_key=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.observacion

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'st_inventario_observacion'
        unique_together = (('empresa', 'secuencia', 'observacion'),)


class StInventarioResultado(models.Model):
    empresa = models.FloatField()
    tipo_comprobante = models.CharField(max_length=3)
    cod_comprobante = models.CharField(max_length=9, primary_key=True)
    fecha = models.DateTimeField()
    cod_agencia = models.FloatField()
    cod_usuario = models.CharField(max_length=50, blank=True, null=True)
    cerrado = models.CharField(max_length=1, blank=True, null=True)
    fecha_aud = models.DateField(blank=True, null=True)
    usuario_aud = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.cod_comprobante)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'st_inventario_resultado'
        unique_together = (('empresa', 'tipo_comprobante', 'cod_comprobante'),)


class StInventarioResultadoD(models.Model):
    empresa = models.FloatField()
    tipo_comprobante = models.OneToOneField(StInventarioResultado, models.DO_NOTHING, db_column='tipo_comprobante', related_name='tipo_inv_res')
    cod_comprobante = models.OneToOneField(StInventarioResultado, models.DO_NOTHING, db_column='cod_comprobante', primary_key=True, related_name='comp_inv_res')
    secuencia = models.FloatField()
    cod_producto = models.CharField(max_length=50)
    serie = models.CharField(max_length=100, blank=True, null=True)
    sobrante = models.CharField(max_length=1)
    ingreso_manual_serie = models.CharField(max_length=1)
    categoria = models.CharField(max_length=10, blank=True, null=True)
    #observacion1 = models.CharField(max_length=100)
    #observacion2 = models.CharField(max_length=1000, blank=True, null=True)
    detalle = models.CharField(max_length=50, blank=True, null=True)
    valor_detalle = models.CharField(max_length=500, blank=True, null=True)
    cantidad = models.CharField(max_length=50, blank=True, null=True)
    cod_usuario = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return str(self.cod_comprobante)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'st_inventario_resultado_d'
        unique_together = (('empresa', 'tipo_comprobante', 'cod_comprobante', 'secuencia', 'cod_producto'),)
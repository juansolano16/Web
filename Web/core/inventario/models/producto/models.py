from django.db import models


########## PRODUCTOS MASTERMOTO ##############
from django.forms import model_to_dict

class Marca(models.Model):
    cod_marca = models.IntegerField(primary_key=True)
    empresa = models.IntegerField()
    nombre = models.CharField(max_length=50, verbose_name='nombre_cat')
    descuento_promocion = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return ('%s') % (self.nombre)


    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'marca'
        unique_together = (('empresa', 'cod_marca'),)


class Producto(models.Model):
    empresa = models.IntegerField()
    cod_producto = models.CharField(max_length=40, primary_key=True)
    tipo_inventario = models.CharField(max_length=1)
    cod_marca = models.CharField(max_length=50)
    cod_unidad = models.CharField(max_length=50)
    cod_alterno = models.CharField(max_length=14, blank=True, null=True)
    nombre = models.CharField(max_length=200)
    cod_barra = models.CharField(max_length=13, blank=True, null=True)
    useridc = models.CharField(max_length=3)
    niv_cod_nivel = models.CharField(max_length=8)
    niv_secuencia = models.CharField(max_length=6)
    niv_cat_emp_empresa = models.CharField(max_length=2)
    niv_cat_cod_categoria = models.CharField(max_length=10)
    promedio = models.DecimalField(max_digits=12, decimal_places=2)
    presentacion = models.CharField(max_length=8, blank=True, null=True)
    volumen = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    grado = models.IntegerField(blank=True, null=True)
    iva = models.CharField(max_length=1)
    referencia = models.CharField(max_length=200, blank=True, null=True)
    partida = models.CharField(max_length=10, blank=True, null=True)
    minimo = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    maximo = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    costo = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    dolar = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    activo = models.CharField(max_length=1)
    alcohol = models.CharField(max_length=1, blank=True, null=True)
    cod_unidad_r = models.CharField(max_length=50, blank=True, null=True)
    cod_modelo = models.CharField(max_length=8)
    cod_item = models.CharField(max_length=3)
    es_fabricado = models.CharField(max_length=1)
    cod_modelo_cat = models.CharField(max_length=8, blank=True, null=True)
    cod_item_cat = models.CharField(max_length=3, blank=True, null=True)
    cod_unidad_f = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cantidad_i = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    serie = models.CharField(max_length=1, blank=True, null=True)
    es_express = models.BooleanField(blank=True, null=True)
    precio = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cod_modelo_cat1 = models.CharField(max_length=8, blank=True, null=True)
    cod_item_cat1 = models.CharField(max_length=3, blank=True, null=True)
    bodega = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return ('%s %s') % (self.cod_producto, self.nombre)


    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'producto'
        unique_together = (('empresa', 'cod_producto'),)



########## PRODUCTOS MASTERMOTO WEB ##############
class vt_producto_web(models.Model):
    linea = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    subcategoria = models.CharField(max_length=50)
    cod_producto = models.CharField(max_length=50, primary_key=True)
    producto = models.CharField(max_length=200)
    grupo = models.CharField(max_length=200)
    bodegav = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'vt_producto_web'
        unique_together = (('cod_producto'),)

    def __str__(self):
        return ('%s: %s') % (self.cod_producto, self.producto)


class vt_producto_web2(models.Model):
    linea = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    subcategoria = models.CharField(max_length=50)
    cod_producto = models.CharField(max_length=50, primary_key=True)
    producto = models.CharField(max_length=200)
    grupo = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'vt_producto_web'
        unique_together = (('cod_producto'),)

    def __str__(self):
        return ('%s: %s') % (self.cod_producto, self.producto)


class StProductoDetalle(models.Model):
    empresa = models.IntegerField(primary_key=True)
    cod_producto = models.ForeignKey(vt_producto_web, models.DO_NOTHING, db_column='cod_producto',
                                     related_name='detalles')
    secuencia = models.FloatField()
    caracteristicas = models.CharField(max_length=50)
    detalle = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_producto_detalle'
        unique_together = (('empresa', 'cod_producto', 'secuencia'),)

    def __str__(self):
        return ('%s: %s') % (self.caracteristicas, self.detalle)

    def toJSON(self):
        item = model_to_dict(self)
        return item


class VtProductoDetalle(models.Model):
    empresa = models.IntegerField(primary_key=True)
    cod_producto = models.ForeignKey(vt_producto_web, models.DO_NOTHING, db_column='cod_producto')
    secuencia = models.FloatField()
    caracteristicas = models.CharField(max_length=50)
    detalle = models.CharField(max_length=4000, blank=True, null=True)
    nombre = models.CharField(max_length=2000, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'vt_st_producto_detalle'
        unique_together = (('empresa', 'cod_producto', 'secuencia'),)

    def __str__(self):
        return ('%s: %s') % (self.caracteristicas, self.detalle)

    def toJSON(self):
        item = model_to_dict(self)
        return item


class VtCaracteristicasProd(models.Model):
    caracteristicas = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return ('%s') % (self.caracteristicas)

    class Meta:
        managed = False
        db_table = 'vt_dist_prod_detalle'


class StProductoSerie(models.Model):
    # empresa = models.OneToOneField(Producto, models.DO_NOTHING, db_column='empresa', primary_key=True)
    empresa = models.IntegerField(primary_key=True)
    cod_producto = models.ForeignKey(vt_producto_web, models.DO_NOTHING, db_column='cod_producto',
                                     related_name='series')
    cod_interno = models.CharField(max_length=100, )
    color = models.CharField(max_length=40, blank=True, null=True)
    bodegav = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'vt_producto_serie_web'
        unique_together = (('empresa', 'cod_producto', 'cod_interno'),)

    def __str__(self):
        return ('%s: %s') % (self.cod_interno, self.color)

    def toJSON(self):
        item = model_to_dict(self)
        return item


class VtListaPrecio(models.Model):
    empresa = models.IntegerField(primary_key=True)
    cod_producto = models.ForeignKey(vt_producto_web, models.DO_NOTHING, db_column='cod_producto', related_name='precio')
    valor = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'vt_lista_precio'
        unique_together = (('empresa', 'cod_producto'),)

    def __str__(self):
        return ('%s: %s') % (self.cod_producto_id, self.valor)



########## PRODUCTOS AUVI ##############
class vt_producto_web_auvi(models.Model):
    linea = models.CharField(max_length=50)
    sublinea = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    segmento = models.CharField(max_length=50)
    subsegmento = models.CharField(max_length=50)
    cod_producto = models.CharField(max_length=50, primary_key=True)
    producto = models.CharField(max_length=200)
    grupo = models.CharField(max_length=200)
    bodegav = models.CharField(max_length=10)
    cod_prod_bod = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'vt_producto_web_auvi'
        unique_together = (('cod_producto'),)

    def __str__(self):
        return ('%s: %s') % (self.cod_producto, self.producto)


class StProductoDetalleAuvi(models.Model):
    empresa = models.IntegerField(primary_key=True)
    cod_producto = models.ForeignKey(vt_producto_web_auvi, models.DO_NOTHING, db_column='cod_producto',
                                     related_name='detalles')
    secuencia = models.FloatField()
    caracteristicas = models.CharField(max_length=50)
    detalle = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_producto_detalle'
        unique_together = (('empresa', 'cod_producto', 'secuencia'),)

    def __str__(self):
        return ('%s: %s') % (self.caracteristicas, self.detalle)

    def toJSON(self):
        item = model_to_dict(self)
        return item


class StProductoSerieAuvi(models.Model):
    empresa = models.IntegerField(primary_key=True)
    cod_producto = models.ForeignKey(vt_producto_web_auvi, models.DO_NOTHING, db_column='cod_producto',
                                     related_name='series')
    cod_interno = models.CharField(max_length=100, )
    color = models.CharField(max_length=40, blank=True, null=True)
    bodegav = models.CharField(max_length=10)
    cod_prod_bod = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'vt_producto_serie_web'
        unique_together = (('empresa', 'cod_producto', 'cod_interno'),)

    def __str__(self):
        return ('%s: %s') % (self.cod_interno, self.color)


class VtListaPrecioAuvi(models.Model):
    empresa = models.IntegerField(primary_key=True)
    cod_producto = models.ForeignKey(vt_producto_web_auvi, models.DO_NOTHING, db_column='cod_producto', related_name='precio')
    valor = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'vt_lista_precio'
        unique_together = (('empresa', 'cod_producto'),)

    def __str__(self):
        return ('%s: %s') % (self.cod_producto_id, self.valor)
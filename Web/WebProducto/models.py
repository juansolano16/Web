from django.db import models

# Create your models here.
# class CLiente(models.Model):
# 	nombre=models.CharField(max_length = 30)
# 	descricion=models.CharField(max_length = 30)

class Marca(models.Model):
    cod_marca = models.IntegerField()
    empresa = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descuento_promocion = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marca'
        unique_together = (('empresa', 'cod_marca'),)

    def __str__(self):
    	return ('%s, %s, %s, %s')  % (self.cod_marca, self.empresa, self.nombre, self.descuento_promocion)



class Unidad(models.Model):
    empresa = models.IntegerField(primary_key=True)
    cod_unidad = models.CharField(max_length=8)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'unidad'
        unique_together = (('empresa', 'cod_unidad'),)    

    def __str__(self):
    	return ('%s, %s, %s')  % (self.empresa, self.cod_unidad, self.nombre)	


class Producto(models.Model):
    empresa = models.OneToOneField('Unidad', models.DO_NOTHING, db_column='empresa', primary_key=True)
    cod_producto = models.CharField(max_length=40)
    tipo_inventario = models.CharField(max_length=1)
    cod_marca = models.ForeignKey(Marca, models.DO_NOTHING, db_column='cod_marca')
    #cod_unidad = models.ForeignKey('Unidad', models.DO_NOTHING, db_column='cod_unidad')
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
    #cod_unidad_r = models.ForeignKey('Unidad', models.DO_NOTHING, db_column='cod_unidad_r', blank=True, null=True)
    cod_modelo = models.CharField(max_length=8)
    cod_item = models.CharField(max_length=3)
    es_fabricado = models.CharField(max_length=1)
    cod_modelo_cat = models.CharField(max_length=8, blank=True, null=True)
    cod_item_cat = models.CharField(max_length=3, blank=True, null=True)
    #cod_unidad_f = models.ForeignKey('Unidad', models.DO_NOTHING, db_column='cod_unidad_f', blank=True, null=True)
    cantidad = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cantidad_i = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    serie = models.CharField(max_length=1, blank=True, null=True)
    es_express = models.BooleanField(blank=True, null=True)
    precio = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cod_modelo_cat1 = models.CharField(max_length=8, blank=True, null=True)
    cod_item_cat1 = models.CharField(max_length=3, blank=True, null=True)
    bodega = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'
        unique_together = (('empresa', 'cod_producto'),)    

    def __str__(self):
    	#return ('%s, %s, %s')  % (self.empresa, self.cod_producto, self.nombre)
    	return ('%s')  % (self.nombre)		



class vt_producto_web(models.Model):
    linea = models.CharField(max_length=50)
    sublinea = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    segmento = models.CharField(max_length=50)
    subsegmento = models.CharField(max_length=50)
    cod_producto = models.CharField(max_length=50, primary_key=True)
    producto = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'vt_producto_web' 
        unique_together = (('cod_producto'),)  



class StProductoDetalle(models.Model):
    #empresa = models.OneToOneField(Producto, models.DO_NOTHING, db_column='empresa', primary_key=True)
    empresa = models.IntegerField(primary_key=True)
    cod_producto = models.ForeignKey(vt_producto_web, models.DO_NOTHING, db_column='cod_producto', related_name='detalles')
    secuencia = models.FloatField()
    caracteristicas = models.CharField(max_length=50)
    detalle = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_producto_detalle'
        unique_together = (('empresa', 'cod_producto', 'secuencia'),)

    def __str__(self):
    	return ('%s: %s') % (self.caracteristicas, self.detalle)

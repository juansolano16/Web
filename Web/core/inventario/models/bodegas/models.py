from django.db import models
from django.forms import model_to_dict

from core.personal.models.personal.models import TgAgencia


class BodegaMassline(models.Model):
    cod_prov = models.CharField(primary_key=True, max_length=20)
    modelo = models.CharField(max_length=70)
    motor = models.CharField(max_length=30)
    chasis = models.CharField(max_length=30)
    anio = models.CharField(max_length=16)
    color = models.CharField(max_length=30, blank=True, null=True)
    camvcpn = models.CharField(max_length=20)
    marca = models.CharField(max_length=20, blank=True, null=True)
    origen = models.CharField(max_length=20, blank=True, null=True)
    locacion = models.CharField(max_length=12)
    cilindraje = models.CharField(max_length=10, blank=True, null=True)
    tonelaje = models.CharField(max_length=10, blank=True, null=True)
    ruc = models.CharField(max_length=13)
    descripcion = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'bodega_massline'
        unique_together = (('cod_prov', 'motor', 'chasis', 'anio', 'locacion', 'ruc', 'camvcpn'),)


class BodegaBajaj(models.Model):
    cod_prov = models.CharField(primary_key=True, max_length=20)
    modelo = models.CharField(max_length=70)
    motor = models.CharField(max_length=30)
    chasis = models.CharField(max_length=30)
    anio = models.CharField(max_length=16)
    color = models.CharField(max_length=30, blank=True, null=True)
    camvcpn = models.CharField(max_length=20)
    marca = models.CharField(max_length=20, blank=True, null=True)
    origen = models.CharField(max_length=20, blank=True, null=True)
    locacion = models.CharField(max_length=12)
    cilindraje = models.CharField(max_length=10, blank=True, null=True)
    tonelaje = models.CharField(max_length=10, blank=True, null=True)
    ruc = models.CharField(max_length=13)
    descripcion = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'bodega_bajaj'
        unique_together = (('cod_prov', 'motor', 'chasis', 'anio', 'locacion', 'ruc', 'camvcpn'),)


class BodegaDaytona(models.Model):
    cod_prov = models.CharField(primary_key=True, max_length=20)
    modelo = models.CharField(max_length=70)
    motor = models.CharField(max_length=30)
    chasis = models.CharField(max_length=30)
    anio = models.CharField(max_length=16)
    color = models.CharField(max_length=30, blank=True, null=True)
    camvcpn = models.CharField(max_length=20)
    marca = models.CharField(max_length=20, blank=True, null=True)
    origen = models.CharField(max_length=20, blank=True, null=True)
    locacion = models.CharField(max_length=12, blank=True, null=True)
    cilindraje = models.CharField(max_length=10, blank=True, null=True)
    tonelaje = models.CharField(max_length=10, blank=True, null=True)
    ruc = models.CharField(max_length=13)
    descripcion = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bodega_daytona'
        unique_together = (('cod_prov', 'motor', 'chasis', 'anio', 'ruc', 'camvcpn'),)


class StReservaProducto(models.Model):
    empresa = models.IntegerField(primary_key=True)
    tipo_comprobante = models.CharField(max_length=2)
    cod_comprobante = models.CharField(max_length=9)
    fecha_registro = models.DateField()
    usuario = models.CharField(max_length=15)
    cod_producto = models.CharField(max_length=40)
    numero_serie = models.CharField(max_length=30)
    chasis = models.CharField(max_length=40)
    camvcpn = models.CharField(max_length=40)
    origen = models.CharField(max_length=40)
    anio = models.FloatField()
    modelo = models.CharField(max_length=40, blank=True, null=True)
    color = models.CharField(max_length=20)
    marca = models.CharField(max_length=50)
    proveedor = models.CharField(max_length=15)
    aprobador_por = models.CharField(max_length=25, blank=True, null=True)
    fecha_aprobacion = models.DateField(blank=True, null=True)
    es_anulado = models.CharField(max_length=1)
    fechaentrega = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=30)
    cod_agencia = models.IntegerField()

    def toJSON(self):
        item = model_to_dict(self)
        item['agencia'] = TgAgencia.objects.get(empresa=self.empresa, cod_agencia = self.cod_agencia).nombre
        return item

    class Meta:
        managed = False
        db_table = 'st_reserva_producto'
        unique_together = (('empresa', 'tipo_comprobante', 'cod_comprobante', 'cod_producto', 'numero_serie'),)


class VtReservaBv(models.Model):
    ruc = models.CharField(max_length=15)
    cod_comprobante = models.CharField(max_length=9, primary_key=True)
    cod_agencia = models.IntegerField()
    agencia = models.CharField(max_length=50)
    cod_producto = models.CharField(max_length=40)
    cod_prov = models.CharField(max_length=80)
    numero_serie = models.CharField(max_length=30)
    chasis = models.CharField(max_length=40)
    camvcpn = models.CharField(max_length=40)
    anio = models.FloatField()
    origen = models.CharField(max_length=40)
    marca = models.CharField(max_length=50)
    proveedor = models.CharField(max_length=15)
    aprobador_por = models.CharField(max_length=25, blank=True, null=True)
    fecha_aprobacion = models.DateField(blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=4000, blank=True, null=True)
    cod_persona = models.CharField(max_length=50)
    nombre_persona = models.CharField(max_length=100)
    telefono1h = models.CharField(max_length=50)
    e_mailh = models.CharField(max_length=100)
    tipo_venta = models.CharField(max_length=50)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vt_reserva_bodega'


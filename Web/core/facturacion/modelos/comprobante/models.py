########## COMPROBANTES ELECTRONICOS ##############
import os

from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models import Q
from django.forms import model_to_dict

from config.settings import folder_img, static_url_img

ORDER_COLUMN_CHOICES_RE = [
    {"data": "agencia"},
    {"data": "tipo_comprobante"},
    {"data": "cod_comprobante"},
    #{"data": "comprobante_sri"},
    {"data": "cod_persona"},
    {"data": "nombre_persona"},
    {"data": "fecha"},
    {"data": "valor"},
]

class VtComprobanteWeb(models.Model):
    empresa = models.IntegerField()
    agencia = models.CharField(max_length=50)
    tipo_comprobante = models.CharField(max_length=50)
    cod_comprobante = models.CharField(max_length=9, primary_key=True)
    comprobante_sri = models.CharField(max_length=20, blank=True, null=True)
    cod_persona = models.CharField(max_length=14)
    nombre_persona = models.CharField(max_length=80, blank=True, null=True)
    fecha = models.DateTimeField()
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    forma_pago = models.CharField(max_length=3, blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self, exclude='fecha')
        item['fecha'] = self.fecha.strftime('%Y-%m-%d %H:%M:%S')
        return item

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vt_comprobante_web'


def query_vtComprobante_by_args(**kwargs):
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

    queryset = VtComprobanteWeb.objects.all()
    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(agencia__icontains=search_value) |
                                   Q(cod_comprobante__icontains=search_value) |
                                   #Q(comprobante_sri__icontains=search_value) |
                                   Q(cod_persona__icontains=search_value) |
                                   Q(nombre_persona__icontains=search_value) |
                                   Q(fecha__icontains=search_value) |
                                   Q(valor__icontains=search_value))
    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }


class VtComprobante(models.Model):
    empresa = models.IntegerField()
    tipo_comprobante = models.CharField(max_length=2)
    cod_comprobante = models.CharField(max_length=9, primary_key=True)
    cod_agencia = models.IntegerField()
    nom_agencia = models.CharField(max_length=50, blank=True, null=True, verbose_name='agencia')
    fecha = models.DateField()
    forma_pago = models.CharField(max_length=3, blank=True, null=True)
    cod_agente = models.CharField(max_length=14, blank=True, null=True)
    nom_agente = models.CharField(max_length=255, blank=True, null=True)
    cod_persona = models.CharField(max_length=14)
    nom_cliente = models.CharField(max_length=255, blank=True, null=True)
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    anulado = models.CharField(max_length=1, blank=True, null=True)
    cod_liquidacion = models.CharField(max_length=9)
    numero_pagos = models.IntegerField()
    observaciones = models.CharField(max_length=500, blank=True, null=True)
    useridc = models.CharField(max_length=3, blank=True, null=True)
    cod_politica = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=62, blank=True, null=True)
    verificador = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vt_comprobante'

    def toJSON(self):
        item = model_to_dict(self, exclude=['nom_agencia', 'nom_cliente'])
        item['agencia'] = self.nom_agencia
        item['nombre_persona'] = self.nom_cliente
        return item



################### IMAGEN COMPROBANTE ###########################
fs = FileSystemStorage(location=folder_img, base_url=static_url_img)

def get_upload_path(instance, filename):
    return os.path.join("%s" % instance.cod_comprobante, filename)

class StImagenesPagare(models.Model):
    empresa = models.FloatField()
    tipo_comprobante = models.CharField(max_length=2)
    cod_comprobante = models.CharField(max_length=15)
    cod_tipo_documento = models.FloatField()
    path_img = models.ImageField(storage=fs, upload_to=get_upload_path, blank=True, null=True)
    fecha_adicion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ST_IMAGENES_PAGARE'
        unique_together = (('empresa', 'tipo_comprobante', 'cod_comprobante', 'cod_tipo_documento'),)

    def toJSON(self):
        item = model_to_dict(self, exclude='path_img')
        item['path_img'] = self.path_img.url
        return item




################### COMPROBANTE VENTAS DIARIAS ###########################
class VtVentaMotor1(models.Model):
    ruc = models.CharField(max_length=13)
    cod_comprobante = models.CharField(max_length=9, primary_key=True)
    cod_agencia = models.IntegerField()
    agencia = models.CharField(max_length=50)
    cod_prov = models.CharField(blank=True, null=True, max_length=50)
    cod_producto = models.CharField(max_length=40)
    numero_serie = models.CharField(max_length=30)
    chasis = models.CharField(max_length=20)
    camvcpn = models.CharField(max_length=20, blank=True, null=True)
    anio = models.IntegerField()
    origen = models.CharField(max_length=50)
    marca = models.CharField(max_length=30, blank=True, null=True)
    proveedor = models.CharField(max_length=13, blank=True, null=True)
    fecha_venta = models.DateField()
    fecha_entrega = models.DateField()
    email = models.CharField(max_length=4000, blank=True, null=True)
    cod_persona = models.CharField(max_length=14)
    nombre_persona = models.CharField(max_length=80, blank=True, null=True)
    telefono1h = models.CharField(max_length=15, blank=True, null=True)
    e_mailh = models.CharField(max_length=60, blank=True, null=True)
    venta = models.CharField(max_length=19, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vt_venta_motor1'



################### COMPROBANTES ELECTRONICOS ###########################
class StComprobanteElectronico(models.Model):
    empresa = models.IntegerField()
    tipo_comprobante = models.CharField(max_length=50)
    cod_comprobante = models.CharField(max_length=50, primary_key=True)
    nro_autorizacion = models.CharField(max_length=49, blank=True, null=True)
    nro_serie = models.CharField(max_length=10, blank=True, null=True)
    fecha_validez = models.DateField(blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    autoimpresion = models.CharField(max_length=1, blank=True, null=True)
    tipo_comprobante_alt = models.CharField(max_length=2, blank=True, null=True)
    cod_comprobante_alt = models.CharField(max_length=9, blank=True, null=True)
    secuencia = models.IntegerField(blank=True, null=True)
    identificacion = models.CharField(max_length=14, blank=True, null=True)
    comprobante_sri = models.CharField(max_length=20, blank=True, null=True)
    archivo_xml = models.CharField(max_length=4000, blank=True, null=True)
    razon_social = models.CharField(max_length=200, blank=True, null=True)
    iva = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    direccion_matriz = models.CharField(max_length=200, blank=True, null=True)
    ruc = models.CharField(max_length=20, blank=True, null=True)
    resolucion = models.CharField(max_length=250, blank=True, null=True)
    archivo_xml_anulado = models.CharField(max_length=4000, blank=True, null=True)
    cod_tipo_contribuyente = models.IntegerField(blank=True, null=True)
    fecha_tipo_cont = models.DateField(blank=True, null=True)
    direccion_cliente = models.CharField(max_length=300, blank=True, null=True)
    leyenda_tipo_cont = models.CharField(max_length=50, blank=True, null=True)
    xml_electronico = models.TextField(blank=True, null=True)
    xml_pruebas = models.TextField(blank=True, null=True)
    clave_acceso = models.CharField(max_length=64, blank=True, null=True)
    clave_pruebas = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.cod_comprobante

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'ST_COMPROBANTE_ELECTRONICO'
        unique_together = (('cod_comprobante', 'tipo_comprobante', 'empresa'), ('tipo_comprobante', 'cod_comprobante'),)
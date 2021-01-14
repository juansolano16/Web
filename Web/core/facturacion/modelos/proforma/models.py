import os

from django.core.files.storage import FileSystemStorage
from django.db import models
from django.forms import model_to_dict
from datetime import datetime

from django_resized import ResizedImageField

from config.settings import folder_img, static_url_img

fs = FileSystemStorage(location=folder_img, base_url=static_url_img)


########## FACTURACION ELECTRONICA ##############

class StProformaCabeceraTmp(models.Model):
    cod_comprobante = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    empresa = models.IntegerField()
    cod_agencia = models.IntegerField()
    fecha = models.DateTimeField(blank=True, null=True)
    cod_forma_pago = models.CharField(max_length=3, blank=True, null=True)
    cod_tipo_identificacion = models.IntegerField(blank=True, null=True)
    cod_persona = models.CharField(max_length=14, blank=True, null=True)
    nombre_persona = models.CharField(max_length=50, blank=True, null=True)
    cod_tipo_identificacion_gar = models.IntegerField(blank=True, null=True)
    cod_persona_gar = models.CharField(max_length=14, blank=True, null=True)
    nombre_persona_gar = models.CharField(max_length=50, blank=True, null=True)
    num_cuotas = models.IntegerField(blank=True, null=True)
    base_imponible = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    base_exenta = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    iva = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    financiamiento = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    valor = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cod_bodega_egreso = models.IntegerField(blank=True, null=True)
    cod_politica = models.IntegerField(blank=True, null=True)
    fecha_vencimiento1 = models.DateField(blank=True, null=True)
    por_interes = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    apellido_persona = models.CharField(max_length=50, blank=True, null=True)
    apellido_persona_gar = models.CharField(max_length=50, blank=True, null=True)
    entrada = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    #cod_producto = models.CharField(max_length=100, blank=True, null=True)
    id_transaccion_tcr = models.CharField(max_length=100, blank=True, null=True)
    banco = models.CharField(max_length=50, blank=True, null=True)
    nom_tarjeta = models.CharField(max_length=50, blank=True, null=True)
    cuotas_tcr = models.FloatField(blank=True, null=True)
    autorizacion_tcr = models.CharField(max_length=100, blank=True, null=True)
    propietario_tcr = models.CharField(max_length=100, blank=True, null=True)
    fp_tcr = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_proforma_cabecera_tmp'
        unique_together = (('cod_comprobante', 'tipo_comprobante', 'empresa', 'cod_agencia'),)

    def __str__(self):
        return ('%s') % (self.cod_comprobante)


class StProformaDetalleTmp(models.Model):
    cod_comprobante = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    empresa = models.IntegerField()
    secuencia = models.IntegerField()
    cod_producto = models.CharField(max_length=40, blank=True, null=True)
    nombre_producto = models.CharField(max_length=200, blank=True, null=True)
    es_serie = models.BooleanField(blank=True, null=True)
    cod_estado_producto = models.CharField(max_length=2, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    iva = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_proforma_detalle_tmp'
        unique_together = (('cod_comprobante', 'tipo_comprobante', 'empresa', 'secuencia'),)


########## IMAGENES PROFORMA ##############
def get_upload_path(instance, filename):
    name = '%s_%s' % (instance.codigo_tipo_imagen_documento, datetime.now().strftime('%d-%m-%y_%H-%M-%S'))
    name = name + '.' + filename.split('.')[-1]
    return os.path.join("%s" % instance.cod_cliente, name)

class StClientesImagenesDocumento(models.Model):
    fecha_transaccion = models.DateField(primary_key=True)
    cod_cliente = models.CharField(max_length=30, blank=True, null=True)
    empresa = models.IntegerField()
    codigo_tipo_imagen_documento = models.IntegerField()
    documento = models.BinaryField(blank=True, null=True)
    adicionado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_adicion = models.DateField(blank=True, null=True)
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    anulado = models.CharField(max_length=1)
    procesado = models.CharField(max_length=2, blank=True, null=True)
    # path_dir = models.ImageField(storage=fs, upload_to=get_upload_path, max_length=200, blank=True, null=True)
    path_dir = ResizedImageField(quality=100, storage=fs, upload_to=get_upload_path, max_length=200, blank=True, null=True)
    documento1 = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_clientes_imagenes_documento'
        unique_together = (('fecha_transaccion', 'cod_cliente', 'empresa'),)


class VtImagenProforma(models.Model):
    empresa = models.FloatField(blank=True, null=True)
    tipo_comprobante = models.CharField(max_length=2, blank=True, null=True)
    cod_comprobante = models.CharField(max_length=9, primary_key=True)
    cod_agencia = models.IntegerField()
    agencia = models.CharField(max_length=50)
    fecha = models.DateField()
    cod_persona = models.CharField(max_length=14)
    persona = models.CharField(max_length=50)
    doc_sol = models.FloatField(blank=True, null=True)
    nombre = models.CharField(max_length=100)
    tiene_doc = models.CharField(max_length=1, blank=True, null=True)
    doc_img = models.IntegerField(blank=True, null=True)
    path_dir = models.CharField(max_length=200, blank=True, null=True)
    fecha_transaccion = models.DateField(blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self, exclude='path_dir')
        item['path_dir'] = '{}{}'.format(static_url_img, self.path_dir) if self.path_dir else ''
        return item

    class Meta:
        managed = False
        db_table = 'VT_IMAGEN_PROFORMA'


class VtProforma(models.Model):
    empresa = models.IntegerField()
    tipo_comprobante = models.CharField(max_length=2)
    cod_comprobante = models.CharField(max_length=9, primary_key=True)
    comprobante_manual = models.CharField(max_length=9)
    cod_agencia = models.IntegerField()
    nom_agencia = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateField()
    cod_forma_pago = models.CharField(max_length=3)
    cod_persona_age = models.CharField(max_length=14)
    nom_agente = models.CharField(max_length=255, blank=True, null=True)
    cod_persona = models.CharField(max_length=14)
    nom_cliente = models.CharField(max_length=255, blank=True, null=True)
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    es_invalido = models.BooleanField()
    es_anulado = models.BooleanField()
    es_aprobado = models.BooleanField()
    es_facturado = models.BooleanField()
    cantidad_mov = models.IntegerField()
    cantidad_mov_completo = models.IntegerField()
    fecha_sol_ver_telefonica = models.DateField(blank=True, null=True)
    fecha_ver_telefonica = models.DateField(blank=True, null=True)
    fecha_sol_ver_campo = models.DateField(blank=True, null=True)
    fecha_ver_campo = models.DateField(blank=True, null=True)
    fecha_negacion = models.DateField(blank=True, null=True)
    es_verificado = models.BooleanField(blank=True, null=True)
    es_detenido = models.BooleanField(blank=True, null=True)
    tipo_sol_amiga = models.BooleanField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    cod_parametro = models.IntegerField(blank=True, null=True)
    es_preaprobado = models.IntegerField(blank=True, null=True)
    puntaje_acierta = models.IntegerField(blank=True, null=True)
    es_envio_supervisor = models.BooleanField(blank=True, null=True)
    cat_credireport = models.CharField(max_length=4000, blank=True, null=True)
    cod_cat_cliente = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vt_PROFORMA'

    def toJSON(self):
        item = model_to_dict(self, exclude=['nom_agencia', 'nom_cliente'])
        item['agencia'] = self.nom_agencia
        item['persona'] = self.nom_cliente
        return item




# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class A(models.Model):
    codigo = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=10, blank=True, null=True)
    fecha_adicion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'a'


class AdAgencias(models.Model):
    codigo_agencia = models.IntegerField(primary_key=True)
    codigo_empresa = models.ForeignKey('AdEmpresas', models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono1 = models.CharField(max_length=15, blank=True, null=True)
    telefono2 = models.CharField(max_length=15, blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    codigo_parroquia = models.ForeignKey('AdParroquias', models.DO_NOTHING, db_column='codigo_parroquia')
    codigo_canton = models.ForeignKey('AdParroquias', models.DO_NOTHING, db_column='codigo_canton')
    codigo_provincia = models.ForeignKey('AdParroquias', models.DO_NOTHING, db_column='codigo_provincia')
    codigo_nacion = models.ForeignKey('AdParroquias', models.DO_NOTHING, db_column='codigo_nacion')
    codigo_region = models.ForeignKey('AdRegiones', models.DO_NOTHING, db_column='codigo_region')
    cod_categoria_zona = models.CharField(max_length=2, blank=True, null=True)
    empresa_zona = models.IntegerField(blank=True, null=True)
    secuencia_zona = models.IntegerField(blank=True, null=True)
    cod_nivel_zona = models.CharField(max_length=8, blank=True, null=True)
    codigo_zona = models.CharField(max_length=14, blank=True, null=True)
    ruc = models.CharField(max_length=20, blank=True, null=True)
    activo = models.CharField(max_length=1)
    cod_grupo_agencia = models.CharField(max_length=3, blank=True, null=True)
    cod_sitio = models.CharField(max_length=3)
    es_autorizado_sri = models.BooleanField()
    tipo_relacion_polcre = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_agencias'
        unique_together = (('codigo_agencia', 'codigo_empresa'), ('descripcion', 'codigo_empresa'),)


class AdAgenciasXCantones(models.Model):
    codigo_agencia = models.IntegerField(primary_key=True)
    codigo_canton = models.ForeignKey('AdCantonesXProvincias', models.DO_NOTHING, db_column='codigo_canton')
    codigo_provincia = models.ForeignKey('AdCantonesXProvincias', models.DO_NOTHING, db_column='codigo_provincia')
    codigo_region = models.ForeignKey('AdCantonesXProvincias', models.DO_NOTHING, db_column='codigo_region')
    codigo_nacion = models.ForeignKey('AdCantonesXProvincias', models.DO_NOTHING, db_column='codigo_nacion')
    codigo_empresa = models.ForeignKey('AdCantonesXProvincias', models.DO_NOTHING, db_column='codigo_empresa')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_agencias_x_cantones'
        unique_together = (('codigo_agencia', 'codigo_canton', 'codigo_provincia', 'codigo_region', 'codigo_nacion', 'codigo_empresa'),)


class AdAplicaciones(models.Model):
    codigo_aplicacion = models.CharField(primary_key=True, max_length=2)
    descripcion = models.CharField(unique=True, max_length=100)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_aplicaciones'


class AdAprobaciones(models.Model):
    codigo_tipo_aprobacion = models.OneToOneField('AdTiposAprobaciones', models.DO_NOTHING, db_column='codigo_tipo_aprobacion', primary_key=True)
    codigo_usuario = models.CharField(max_length=30)
    clave_aprobacion = models.CharField(max_length=30)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_aprobaciones'
        unique_together = (('codigo_tipo_aprobacion', 'codigo_usuario'),)


class AdBuros(models.Model):
    codigo_buro = models.IntegerField(primary_key=True)
    codigo_empresa = models.ForeignKey('AdEmpresas', models.DO_NOTHING, db_column='codigo_empresa')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_buros'
        unique_together = (('codigo_buro', 'codigo_empresa'),)


class AdCantones(models.Model):
    codigo_canton = models.CharField(primary_key=True, max_length=4)
    codigo_provincia = models.ForeignKey('AdProvincias', models.DO_NOTHING, db_column='codigo_provincia')
    codigo_nacion = models.ForeignKey('AdProvincias', models.DO_NOTHING, db_column='codigo_nacion')
    descripcion = models.CharField(max_length=50)
    sigla = models.CharField(max_length=3, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_cantones'
        unique_together = (('codigo_canton', 'codigo_provincia', 'codigo_nacion'),)


class AdCantonesXProvincias(models.Model):
    codigo_canton = models.OneToOneField(AdCantones, models.DO_NOTHING, db_column='codigo_canton', primary_key=True)
    codigo_provincia = models.ForeignKey('AdProvinciasXRegiones', models.DO_NOTHING, db_column='codigo_provincia')
    codigo_region = models.ForeignKey('AdProvinciasXRegiones', models.DO_NOTHING, db_column='codigo_region')
    codigo_nacion = models.ForeignKey('AdProvinciasXRegiones', models.DO_NOTHING, db_column='codigo_nacion')
    codigo_empresa = models.ForeignKey('AdProvinciasXRegiones', models.DO_NOTHING, db_column='codigo_empresa')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_cantones_x_provincias'
        unique_together = (('codigo_canton', 'codigo_provincia', 'codigo_region', 'codigo_nacion', 'codigo_empresa'),)


class AdCantonesXProvinciasEtp(models.Model):
    codigo_canton = models.CharField(primary_key=True, max_length=14)
    niv_cod_nivel_canton = models.CharField(max_length=8)
    niv_secuencia_canton = models.IntegerField()
    codigo_provincia = models.ForeignKey('AdProvinciasXRegionesEtp', models.DO_NOTHING, db_column='codigo_provincia')
    niv_cod_nivel_provincia = models.ForeignKey('AdProvinciasXRegionesEtp', models.DO_NOTHING, db_column='niv_cod_nivel_provincia')
    niv_secuencia_provincia = models.ForeignKey('AdProvinciasXRegionesEtp', models.DO_NOTHING, db_column='niv_secuencia_provincia')
    codigo_region = models.ForeignKey('AdProvinciasXRegionesEtp', models.DO_NOTHING, db_column='codigo_region')
    niv_cat_emp_empresa_canton = models.ForeignKey('AdProvinciasXRegionesEtp', models.DO_NOTHING, db_column='niv_cat_emp_empresa_canton')
    niv_cat_cod_categoria_canton = models.ForeignKey('AdProvinciasXRegionesEtp', models.DO_NOTHING, db_column='niv_cat_cod_categoria_canton')
    codigo_nacion = models.ForeignKey('AdProvinciasXRegionesEtp', models.DO_NOTHING, db_column='codigo_nacion')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_cantones_x_provincias_etp'
        unique_together = (('codigo_canton', 'niv_cod_nivel_canton', 'niv_secuencia_canton', 'codigo_provincia', 'niv_cod_nivel_provincia', 'niv_secuencia_provincia', 'codigo_region', 'niv_cat_emp_empresa_canton', 'niv_cat_cod_categoria_canton', 'codigo_nacion'),)


class AdEmpleadosGruposMails(models.Model):
    identificacion = models.OneToOneField('RhEmpleados', models.DO_NOTHING, db_column='identificacion', primary_key=True)
    codigo_grupo_mail = models.ForeignKey('AdGruposMails', models.DO_NOTHING, db_column='codigo_grupo_mail')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_empleados_grupos_mails'
        unique_together = (('identificacion', 'codigo_grupo_mail'),)


class AdEmpresas(models.Model):
    codigo_empresa = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    codigo_parroquia = models.ForeignKey('AdParroquias', models.DO_NOTHING, db_column='codigo_parroquia')
    codigo_canton = models.ForeignKey('AdParroquias', models.DO_NOTHING, db_column='codigo_canton')
    codigo_provincia = models.ForeignKey('AdParroquias', models.DO_NOTHING, db_column='codigo_provincia')
    codigo_nacion = models.ForeignKey('AdParroquias', models.DO_NOTHING, db_column='codigo_nacion')
    direccion = models.CharField(max_length=100)
    telefono1 = models.CharField(max_length=15, blank=True, null=True)
    telefono2 = models.CharField(max_length=15, blank=True, null=True)
    fax = models.CharField(max_length=15, blank=True, null=True)
    contabilidad_consulta_inicial = models.DateField()
    contabilidad_consulta_final = models.DateField()
    contabilidad_modifica_inicial = models.DateField()
    contabilidad_modifica_final = models.DateField()
    inventario_consulta_inicial = models.DateField()
    inventario_consulta_final = models.DateField()
    inventario_modifica_inicial = models.DateField()
    inventario_modifica_final = models.DateField()
    ruc = models.CharField(max_length=20)
    casilla = models.CharField(max_length=10, blank=True, null=True)
    contador_identificacion = models.CharField(max_length=20, blank=True, null=True)
    mensaje = models.CharField(max_length=100, blank=True, null=True)
    numero_patronal = models.CharField(max_length=10, blank=True, null=True)
    gerente_identificacion = models.CharField(max_length=20, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    anulado = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ad_empresas'


class AdGruposMails(models.Model):
    codigo_grupo_mail = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=10, blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_grupos_mails'


class AdImagenesFlujoProcesos(models.Model):
    codigo_simbolo = models.OneToOneField('AdSimbolosFlujoProcesos', models.DO_NOTHING, db_column='codigo_simbolo', primary_key=True)
    codigo_empresa = models.ForeignKey('AdSimbolosFlujoProcesos', models.DO_NOTHING, db_column='codigo_empresa')
    imagen = models.BinaryField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_imagenes_flujo_procesos'
        unique_together = (('codigo_simbolo', 'codigo_empresa'),)


class AdImpresorasXUsuarios(models.Model):
    codigo_usuario = models.CharField(primary_key=True, max_length=30)
    tipo_documento = models.ForeignKey('AdTiposDocumentosAImprimir', models.DO_NOTHING, db_column='tipo_documento')
    descripcion = models.CharField(max_length=200)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_impresoras_x_usuarios'
        unique_together = (('codigo_usuario', 'tipo_documento'),)


class AdLogosEmpresas(models.Model):
    codigo_empresa = models.OneToOneField(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa', primary_key=True)
    logo = models.BinaryField(blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_logos_empresas'


class AdMonedas(models.Model):
    codigo_moneda = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=10)
    codigo_nacion = models.IntegerField()
    signo = models.CharField(max_length=10)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_monedas'


class AdNaciones(models.Model):
    codigo_nacion = models.IntegerField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=100)
    capital = models.CharField(max_length=100)
    codigo_area = models.IntegerField()
    nacionalidad = models.CharField(max_length=50)
    continente = models.BooleanField()
    sigla = models.CharField(unique=True, max_length=2)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_naciones'


class AdNivelesPostgrado(models.Model):
    codigo_nivel_postgrado = models.IntegerField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=100)
    activo = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_niveles_postgrado'


class AdOpcionesSistema(models.Model):
    codigo_opcion = models.CharField(primary_key=True, max_length=15)
    codigo_aplicacion = models.ForeignKey(AdAplicaciones, models.DO_NOTHING, db_column='codigo_aplicacion')
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=100)
    codigo_opcion_principal = models.CharField(max_length=15, blank=True, null=True)
    codigo_aplicacion_principal = models.CharField(max_length=2, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_opciones_sistema'
        unique_together = (('codigo_opcion', 'codigo_aplicacion', 'codigo_empresa'),)


class AdParametrosGenerales(models.Model):
    codigo_empresa = models.OneToOneField('RhCargos', models.DO_NOTHING, db_column='codigo_empresa', primary_key=True)
    codigo_moneda = models.ForeignKey(AdMonedas, models.DO_NOTHING, db_column='codigo_moneda')
    porcentaje_iva = models.DecimalField(max_digits=7, decimal_places=4)
    tasa_interes_deudor = models.DecimalField(max_digits=7, decimal_places=4)
    tasa_interes_acreedor = models.DecimalField(max_digits=7, decimal_places=4)
    porcentaje_descuento = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    porcentaje_entrada = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    porcentaje_iess_patronal = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    porcentaje_iess_cesantia = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    porcentaje_iess_secap = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    porcentaje_iess_iece = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    porcentaje_refinanciacion = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    valor_acciones = models.BigIntegerField(blank=True, null=True)
    factor_venta = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    numero_decimales = models.IntegerField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    path_reportes_servidor = models.CharField(max_length=300, blank=True, null=True)
    path_reportes_cliente = models.CharField(max_length=300, blank=True, null=True)
    path_logos_empresas = models.CharField(max_length=300, blank=True, null=True)
    cierre_cartera_dias = models.IntegerField()
    compromiso_pago = models.CharField(max_length=10)
    nombre_archivo_cobro_celular = models.CharField(max_length=30, blank=True, null=True)
    path_leer_archivos_usb = models.CharField(max_length=200, blank=True, null=True)
    path_grabar_archivo_usb = models.CharField(max_length=200, blank=True, null=True)
    path_archivos_locales_cliente = models.CharField(max_length=200, blank=True, null=True)
    id_servidor = models.CharField(max_length=3)
    casa = models.CharField(max_length=10, blank=True, null=True)
    trabajo = models.CharField(max_length=10, blank=True, null=True)
    dir_no_valida = models.CharField(max_length=10, blank=True, null=True)
    dias_plazo_c_p = models.IntegerField(blank=True, null=True)
    intentos_comp_pago = models.IntegerField(blank=True, null=True)
    max_fecha_comp_pago = models.IntegerField(blank=True, null=True)
    codigo_segmento_cartera = models.IntegerField(blank=True, null=True)
    saldo_minimo_enviar_recaudador = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    codigo_cargo_cobrador = models.ForeignKey('RhCargos', models.DO_NOTHING, db_column='codigo_cargo_cobrador', blank=True, null=True)
    codigo_cargo_operador_telef = models.ForeignKey('RhCargos', models.DO_NOTHING, db_column='codigo_cargo_operador_telef', blank=True, null=True)
    codigo_cargo_verificador = models.ForeignKey('RhCargos', models.DO_NOTHING, db_column='codigo_cargo_verificador', blank=True, null=True)
    codigo_gestion_cli_no_ubicado = models.CharField(max_length=10, blank=True, null=True)
    trunk_domicilio = models.CharField(max_length=500, blank=True, null=True)
    trunk_celular = models.CharField(max_length=500, blank=True, null=True)
    compromiso_pago_call_center = models.CharField(max_length=10)
    dias_mora_env_recaud_exter = models.IntegerField()
    saldo_x_cuota_env_recaud_exter = models.DecimalField(max_digits=18, decimal_places=2)
    codigo_enviar_a_urd = models.CharField(max_length=10, blank=True, null=True)
    numero_campania_urd = models.IntegerField(blank=True, null=True)
    codigo_nacion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_parametros_generales'


class AdParametrosReport(models.Model):
    cod_servidor = models.IntegerField(primary_key=True)
    servidor = models.CharField(max_length=100)
    puerto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ad_parametros_report'


class AdParroquias(models.Model):
    codigo_parroquia = models.CharField(primary_key=True, max_length=4)
    codigo_canton = models.ForeignKey(AdCantones, models.DO_NOTHING, db_column='codigo_canton')
    codigo_provincia = models.ForeignKey(AdCantones, models.DO_NOTHING, db_column='codigo_provincia')
    codigo_nacion = models.ForeignKey(AdCantones, models.DO_NOTHING, db_column='codigo_nacion')
    descripcion = models.CharField(max_length=100)
    sigla = models.CharField(max_length=3)
    tipo = models.BooleanField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_parroquias'
        unique_together = (('codigo_parroquia', 'codigo_canton', 'codigo_provincia', 'codigo_nacion'),)


class AdPermisosAlSistemaXRol(models.Model):
    codigo_opcion = models.OneToOneField(AdOpcionesSistema, models.DO_NOTHING, db_column='codigo_opcion', primary_key=True)
    codigo_rol = models.ForeignKey('AdRoles', models.DO_NOTHING, db_column='codigo_rol')
    codigo_aplicacion = models.ForeignKey(AdOpcionesSistema, models.DO_NOTHING, db_column='codigo_aplicacion')
    codigo_empresa = models.ForeignKey(AdOpcionesSistema, models.DO_NOTHING, db_column='codigo_empresa')
    tiene_acceso = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_permisos_al_sistema_x_rol'
        unique_together = (('codigo_opcion', 'codigo_rol', 'codigo_aplicacion', 'codigo_empresa'),)


class AdPorcObjXSemana(models.Model):
    numero_semana = models.OneToOneField('AdSemanaFiscalXMes', models.DO_NOTHING, db_column='numero_semana', primary_key=True)
    periodo = models.ForeignKey('AdSemanaFiscalXMes', models.DO_NOTHING, db_column='periodo')
    codigo_empresa = models.ForeignKey('AdSemanaFiscalXMes', models.DO_NOTHING, db_column='codigo_empresa')
    fecha_inicial_semana = models.DateField()
    fecha_final_semana = models.DateField()
    porcentaje_objetivo_semana = models.DecimalField(max_digits=5, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_porc_obj_x_semana'
        unique_together = (('numero_semana', 'periodo', 'codigo_empresa'),)


class AdPorcObjXSemanaCobrador(models.Model):
    numero_semana = models.OneToOneField('AdSemanaFiscalXMes', models.DO_NOTHING, db_column='numero_semana', primary_key=True)
    identificacion_cobrador = models.ForeignKey('RhEmpleados', models.DO_NOTHING, db_column='identificacion_cobrador')
    periodo = models.ForeignKey('AdSemanaFiscalXMes', models.DO_NOTHING, db_column='periodo')
    codigo_empresa = models.ForeignKey('AdSemanaFiscalXMes', models.DO_NOTHING, db_column='codigo_empresa')
    fecha_inicial_semana = models.DateField()
    fecha_final_semana = models.DateField()
    porcentaje_objetivo_semana = models.DecimalField(max_digits=5, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_porc_obj_x_semana_cobrador'
        unique_together = (('numero_semana', 'identificacion_cobrador', 'periodo', 'codigo_empresa'),)


class AdPorcentajeObjXCobrador(models.Model):
    identificacion_cobrador = models.OneToOneField('RhEmpleados', models.DO_NOTHING, db_column='identificacion_cobrador', primary_key=True)
    codigo_segmento_cartera = models.ForeignKey('CcSegmentosDeCarteras', models.DO_NOTHING, db_column='codigo_segmento_cartera')
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    porcentaje_objetivo = models.DecimalField(max_digits=5, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_porcentaje_obj_x_cobrador'
        unique_together = (('identificacion_cobrador', 'codigo_segmento_cartera', 'codigo_empresa'),)


class AdProvincias(models.Model):
    codigo_provincia = models.CharField(primary_key=True, max_length=6)
    codigo_nacion = models.ForeignKey(AdNaciones, models.DO_NOTHING, db_column='codigo_nacion')
    descripcion = models.CharField(max_length=100)
    codigo_region = models.ForeignKey('AdRegiones', models.DO_NOTHING, db_column='codigo_region')
    sigla = models.CharField(max_length=3, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_provincias'
        unique_together = (('codigo_provincia', 'codigo_nacion'),)


class AdProvinciasXRegiones(models.Model):
    codigo_provincia = models.OneToOneField(AdProvincias, models.DO_NOTHING, db_column='codigo_provincia', primary_key=True)
    codigo_region = models.ForeignKey('AdRegionesXEmpresas', models.DO_NOTHING, db_column='codigo_region')
    codigo_nacion = models.ForeignKey('AdRegionesXEmpresas', models.DO_NOTHING, db_column='codigo_nacion')
    codigo_empresa = models.ForeignKey('AdRegionesXEmpresas', models.DO_NOTHING, db_column='codigo_empresa')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_provincias_x_regiones'
        unique_together = (('codigo_provincia', 'codigo_region', 'codigo_nacion', 'codigo_empresa'),)


class AdProvinciasXRegionesEtp(models.Model):
    codigo_provincia = models.CharField(primary_key=True, max_length=14)
    niv_cod_nivel_provincia = models.CharField(max_length=8)
    niv_secuencia_provincia = models.IntegerField()
    codigo_region = models.ForeignKey('AdRegionesXEmpresas', models.DO_NOTHING, db_column='codigo_region')
    niv_cat_emp_empresa_provincia = models.ForeignKey('AdRegionesXEmpresas', models.DO_NOTHING, db_column='niv_cat_emp_empresa_provincia')
    niv_cat_cod_categoria_provin = models.CharField(max_length=2)
    codigo_nacion = models.ForeignKey('AdRegionesXEmpresas', models.DO_NOTHING, db_column='codigo_nacion')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_provincias_x_regiones_etp'
        unique_together = (('codigo_provincia', 'niv_cod_nivel_provincia', 'niv_secuencia_provincia', 'codigo_region', 'niv_cat_emp_empresa_provincia', 'niv_cat_cod_categoria_provin', 'codigo_nacion'),)


class AdRegiones(models.Model):
    codigo_region = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_regiones'


class AdRegionesXEmpresas(models.Model):
    codigo_region = models.IntegerField(primary_key=True)
    codigo_nacion = models.ForeignKey(AdNaciones, models.DO_NOTHING, db_column='codigo_nacion')
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=300)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_regiones_x_empresas'
        unique_together = (('codigo_region', 'codigo_nacion', 'codigo_empresa'),)


class AdRoles(models.Model):
    codigo_rol = models.CharField(primary_key=True, max_length=30)
    descripcion = models.CharField(unique=True, max_length=100)
    abreviatura = models.CharField(max_length=10)
    acceso_total = models.CharField(max_length=1)
    activo = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_roles'


class AdSeguimientoCallCenter(models.Model):
    usuario = models.CharField(max_length=30)
    numero_campania = models.IntegerField(blank=True, null=True)
    id_servidor = models.CharField(max_length=3, blank=True, null=True)
    codigo_persona_encr = models.CharField(max_length=30, blank=True, null=True)
    codigo_usuario_externo = models.CharField(max_length=10, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    tracknum = models.CharField(max_length=100, blank=True, null=True)
    observaciones = models.CharField(max_length=4000, blank=True, null=True)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_forma = models.CharField(max_length=30, blank=True, null=True)
    calling_list = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_seguimiento_call_center'


class AdSemanaFiscalXMes(models.Model):
    numero_semana = models.BooleanField(primary_key=True)
    periodo = models.IntegerField()
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    fecha_inicial_semana = models.DateField()
    fecha_final_semana = models.DateField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_semana_fiscal_x_mes'
        unique_together = (('numero_semana', 'periodo', 'codigo_empresa'),)


class AdSimbolosFlujoProcesos(models.Model):
    codigo_simbolo = models.IntegerField(primary_key=True)
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=100)
    es_proceso_si_no = models.CharField(max_length=1)
    tiene_responsable_si_no = models.CharField(max_length=1)
    inicio_de_proceso_si_no = models.CharField(max_length=1)
    fin_de_proceso_si_no = models.CharField(max_length=1)
    es_desicion_si_no = models.CharField(max_length=1)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_simbolos_flujo_procesos'
        unique_together = (('codigo_simbolo', 'codigo_empresa'),)


class AdTiposAprobaciones(models.Model):
    codigo_tipo_aprobacion = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_tipos_aprobaciones'


class AdTiposDocumentosAImprimir(models.Model):
    tipo_documento = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_tipos_documentos_a_imprimir'


class AdTiposEventos(models.Model):
    codigo_tipo_evento = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_tipos_eventos'


class AdTitulos(models.Model):
    codigo_titulo = models.IntegerField(primary_key=True)
    codigo_nivel_postgrado = models.ForeignKey(AdNivelesPostgrado, models.DO_NOTHING, db_column='codigo_nivel_postgrado')
    descripcion = models.CharField(unique=True, max_length=150)
    sigla = models.CharField(max_length=15)
    nivel = models.BooleanField()
    activo = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_titulos'


class AdUsuarios(models.Model):
    codigo_usuario = models.CharField(primary_key=True, max_length=30)
    identificacion = models.CharField(max_length=20)
    clave_de_acceso = models.CharField(max_length=30)
    fecha_ultimo_ingreso = models.DateField(blank=True, null=True)
    empresa_actual = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='empresa_actual', blank=True, null=True)
    agencia_actual = models.IntegerField(blank=True, null=True)
    toda_bodega = models.CharField(max_length=1)
    toda_empresa = models.CharField(max_length=1)
    tipo_usuario = models.CharField(max_length=1)
    es_empleado = models.CharField(max_length=1)
    activo = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    useridc_anterior = models.CharField(max_length=3, blank=True, null=True)
    codigo_agencia_caja = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_agencia_caja', blank=True, null=True)
    codigo_usuario_externo = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_usuarios'


class AdUsuariosEmpresas(models.Model):
    codigo_usuario = models.OneToOneField(AdUsuarios, models.DO_NOTHING, db_column='codigo_usuario', primary_key=True)
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    caja = models.IntegerField(blank=True, null=True)
    comprobante = models.CharField(max_length=9, blank=True, null=True)
    fecha_comprobante = models.DateField(blank=True, null=True)
    super = models.CharField(max_length=1, blank=True, null=True)
    tsc = models.CharField(max_length=1)
    tipo_comprobante = models.CharField(max_length=2, blank=True, null=True)
    toda_agencia = models.CharField(max_length=1, blank=True, null=True)
    descuento_maximo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_usuarios_empresas'
        unique_together = (('codigo_usuario', 'codigo_empresa'),)


class AdUsuariosRoles(models.Model):
    codigo_rol = models.OneToOneField(AdRoles, models.DO_NOTHING, db_column='codigo_rol', primary_key=True)
    codigo_usuario = models.ForeignKey(AdUsuarios, models.DO_NOTHING, db_column='codigo_usuario')
    activo = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_usuarios_roles'
        unique_together = (('codigo_rol', 'codigo_usuario'),)


class AdUsuariosXAgencias(models.Model):
    codigo_usuario = models.OneToOneField(AdUsuariosEmpresas, models.DO_NOTHING, db_column='codigo_usuario', primary_key=True)
    codigo_agencia = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_agencia')
    codigo_empresa = models.ForeignKey(AdUsuariosEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_call_center = models.ForeignKey('CcCallCenter', models.DO_NOTHING, db_column='codigo_call_center', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_usuarios_x_agencias'
        unique_together = (('codigo_usuario', 'codigo_agencia', 'codigo_empresa'),)


class AdVerificaciones(models.Model):
    codigo_verificacion = models.IntegerField(primary_key=True)
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=100)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_verificaciones'
        unique_together = (('codigo_verificacion', 'codigo_empresa'),)


class AdZonas(models.Model):
    codigo_zona = models.IntegerField(primary_key=True)
    codigo_parroquia = models.ForeignKey(AdParroquias, models.DO_NOTHING, db_column='codigo_parroquia')
    codigo_canton = models.ForeignKey(AdParroquias, models.DO_NOTHING, db_column='codigo_canton')
    codigo_provincia = models.ForeignKey(AdParroquias, models.DO_NOTHING, db_column='codigo_provincia')
    codigo_nacion = models.ForeignKey(AdParroquias, models.DO_NOTHING, db_column='codigo_nacion')
    descripcion = models.CharField(max_length=100)
    sigla = models.CharField(max_length=3)
    activo = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_zonas'
        unique_together = (('codigo_zona', 'codigo_parroquia', 'codigo_canton', 'codigo_provincia', 'codigo_nacion'),)


class AfActivos(models.Model):
    cod_tipo = models.ForeignKey('AfTiposActivos', models.DO_NOTHING, db_column='cod_tipo')
    cod_activo = models.CharField(primary_key=True, max_length=14)
    empresa = models.ForeignKey('AfTiposActivos', models.DO_NOTHING, db_column='empresa')
    fecha_compra = models.DateField(blank=True, null=True)
    cod_activo_padre = models.ForeignKey('self', models.DO_NOTHING, db_column='cod_activo_padre', blank=True, null=True)
    valor_compra = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    valor_residual = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    cod_tipo_padre = models.ForeignKey('self', models.DO_NOTHING, db_column='cod_tipo_padre', blank=True, null=True)
    empresa_padre = models.ForeignKey('self', models.DO_NOTHING, db_column='empresa_padre', blank=True, null=True)
    estado = models.BooleanField()
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    usuario_actual = models.ForeignKey('RhEmpleados', models.DO_NOTHING, db_column='usuario_actual', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'af_activos'
        unique_together = (('cod_activo', 'cod_tipo', 'empresa'),)


class AfActivosSolicitudes(models.Model):
    cod_activo_solicitud = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'af_activos_solicitudes'


class AfComputadoras(models.Model):
    cod_activo = models.OneToOneField(AfActivos, models.DO_NOTHING, db_column='cod_activo', primary_key=True)
    empresa = models.ForeignKey(AfActivos, models.DO_NOTHING, db_column='empresa')
    nombre = models.CharField(max_length=50, blank=True, null=True)
    cod_marca = models.IntegerField()
    sistema_operativo = models.CharField(max_length=50)
    licencia = models.CharField(max_length=30, blank=True, null=True)
    mac_address = models.CharField(max_length=50)
    procesador = models.CharField(max_length=50, blank=True, null=True)
    memoria = models.CharField(max_length=50, blank=True, null=True)
    disco_duro = models.CharField(max_length=50, blank=True, null=True)
    mainboard = models.CharField(max_length=50, blank=True, null=True)
    numero_serie = models.CharField(max_length=30)
    modem = models.CharField(max_length=50, blank=True, null=True)
    tarjeta_red = models.CharField(max_length=50, blank=True, null=True)
    mouse = models.CharField(max_length=50, blank=True, null=True)
    teclado = models.CharField(max_length=50, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    cod_tipo = models.ForeignKey(AfActivos, models.DO_NOTHING, db_column='cod_tipo')

    class Meta:
        managed = False
        db_table = 'af_computadoras'
        unique_together = (('cod_activo', 'cod_tipo', 'empresa'),)


class AfMarcas(models.Model):
    cod_marca = models.IntegerField(primary_key=True)
    empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='empresa')
    nombre = models.CharField(max_length=50, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    cod_tipo = models.ForeignKey('AfTiposActivos', models.DO_NOTHING, db_column='cod_tipo')

    class Meta:
        managed = False
        db_table = 'af_marcas'
        unique_together = (('cod_marca', 'empresa'),)


class AfMovimientosActivos(models.Model):
    empresa_comp = models.IntegerField(blank=True, null=True)
    cod_comprobante = models.CharField(primary_key=True, max_length=9)
    cod_tipo_persona = models.CharField(max_length=3, blank=True, null=True)
    cod_comprobante_comp = models.CharField(max_length=9, blank=True, null=True)
    cod_persona = models.CharField(max_length=14, blank=True, null=True)
    tipo_comprobante_comp = models.CharField(max_length=2, blank=True, null=True)
    fecha_tranferencia = models.DateField(blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)
    cod_agencia_emp = models.IntegerField(blank=True, null=True)
    factura_manual = models.CharField(max_length=14, blank=True, null=True)
    valor = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    iva = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    ice = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    empresa_sol = models.IntegerField(blank=True, null=True)
    empresa = models.IntegerField()
    tipo = models.CharField(max_length=2)
    identificacion_emp = models.CharField(max_length=14, blank=True, null=True)
    empresa_emp = models.IntegerField(blank=True, null=True)
    tipo_comprobante_sol = models.CharField(max_length=2, blank=True, null=True)
    cod_comprobante_sol = models.CharField(max_length=9, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    empresa_trans = models.IntegerField(blank=True, null=True)
    cod_agencia_trans = models.IntegerField(blank=True, null=True)
    identificacion_trans = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'af_movimientos_activos'
        unique_together = (('cod_comprobante', 'tipo', 'empresa'),)


class AfMovimientosDetalles(models.Model):
    cod_comprobante = models.ForeignKey(AfMovimientosActivos, models.DO_NOTHING, db_column='cod_comprobante')
    secuencia = models.IntegerField(primary_key=True)
    cod_activo = models.ForeignKey(AfActivos, models.DO_NOTHING, db_column='cod_activo')
    cod_tipo = models.ForeignKey(AfActivos, models.DO_NOTHING, db_column='cod_tipo')
    cantidad = models.IntegerField(blank=True, null=True)
    debito_credito = models.BooleanField()
    valor = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    iva = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    ice = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    empresa = models.ForeignKey(AfMovimientosActivos, models.DO_NOTHING, db_column='empresa')
    tipo = models.ForeignKey(AfMovimientosActivos, models.DO_NOTHING, db_column='tipo')
    empresa_activo = models.ForeignKey(AfActivos, models.DO_NOTHING, db_column='empresa_activo')
    secuencia_sol = models.ForeignKey('AfSolicitudesDetalles', models.DO_NOTHING, db_column='secuencia_sol', blank=True, null=True)
    cod_comprobante_sol = models.ForeignKey('AfSolicitudesDetalles', models.DO_NOTHING, db_column='cod_comprobante_sol', blank=True, null=True)
    tipo_comprobante_sol = models.ForeignKey('AfSolicitudesDetalles', models.DO_NOTHING, db_column='tipo_comprobante_sol', blank=True, null=True)
    empresa_sol = models.ForeignKey('AfSolicitudesDetalles', models.DO_NOTHING, db_column='empresa_sol', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'af_movimientos_detalles'
        unique_together = (('secuencia', 'cod_comprobante', 'tipo', 'empresa'),)


class AfOrdenes(models.Model):
    cod_tipo = models.OneToOneField('AfTiposActivos', models.DO_NOTHING, db_column='cod_tipo', primary_key=True)
    cod_agencia = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='cod_agencia')
    empresa = models.ForeignKey('AfTiposActivos', models.DO_NOTHING, db_column='empresa')
    sigla = models.CharField(max_length=4, blank=True, null=True)
    secuencia = models.IntegerField(blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'af_ordenes'
        unique_together = (('cod_tipo', 'cod_agencia', 'empresa'),)


class AfPerifericos(models.Model):
    cod_activo = models.OneToOneField(AfActivos, models.DO_NOTHING, db_column='cod_activo', primary_key=True)
    empresa = models.ForeignKey(AfActivos, models.DO_NOTHING, db_column='empresa')
    cod_marca = models.IntegerField()
    nombre = models.CharField(max_length=50)
    numero_serie = models.CharField(max_length=30)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    cod_tipo = models.ForeignKey(AfActivos, models.DO_NOTHING, db_column='cod_tipo')
    cod_activo_padre = models.CharField(max_length=14, blank=True, null=True)
    cod_tipo_padre = models.IntegerField(blank=True, null=True)
    empresa_padre = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'af_perifericos'
        unique_together = (('cod_activo', 'cod_tipo', 'empresa'),)


class AfSolicitudes(models.Model):
    cod_comprobante = models.CharField(primary_key=True, max_length=9)
    empresa = models.IntegerField()
    tipo_comprobante = models.CharField(max_length=2)
    concepto = models.CharField(max_length=500)
    fecha = models.DateField()
    usuario_aprueba = models.ForeignKey(AdUsuarios, models.DO_NOTHING, db_column='usuario_aprueba', blank=True, null=True)
    estado = models.CharField(max_length=1)
    fecha_aprobacion = models.DateField(blank=True, null=True)
    usuario_aprueba_adm = models.ForeignKey(AdUsuarios, models.DO_NOTHING, db_column='usuario_aprueba_adm', blank=True, null=True)
    fecha_aprobacion_adm = models.DateField(blank=True, null=True)
    es_entregado = models.BooleanField(blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    empresa_emp = models.IntegerField(blank=True, null=True)
    cod_agencia_emp = models.IntegerField()
    identificacion_emp = models.CharField(max_length=14)
    estado_adm = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'af_solicitudes'
        unique_together = (('cod_comprobante', 'tipo_comprobante', 'empresa'),)


class AfSolicitudesDetalles(models.Model):
    cod_comprobante = models.CharField(max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    empresa = models.IntegerField()
    secuencia = models.IntegerField(primary_key=True)
    cantidad_solicitada = models.IntegerField(blank=True, null=True)
    cantidad_entregada = models.IntegerField(blank=True, null=True)
    cod_activo_solicitud = models.ForeignKey(AfActivosSolicitudes, models.DO_NOTHING, db_column='cod_activo_solicitud')
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'af_solicitudes_detalles'
        unique_together = (('secuencia', 'cod_comprobante', 'tipo_comprobante', 'empresa'),)


class AfTiposActivos(models.Model):
    cod_tipo = models.IntegerField(primary_key=True)
    empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='empresa')
    codigo_depreciacion = models.ForeignKey('AfTiposDepreciaciones', models.DO_NOTHING, db_column='codigo_depreciacion', blank=True, null=True)
    nombre = models.CharField(max_length=50)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'af_tipos_activos'
        unique_together = (('cod_tipo', 'empresa'),)


class AfTiposDepreciaciones(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    porcentaje = models.DecimalField(max_digits=6, decimal_places=2)
    vida_util = models.IntegerField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'af_tipos_depreciaciones'


class AfVehiculos(models.Model):
    cod_activo = models.OneToOneField(AfActivos, models.DO_NOTHING, db_column='cod_activo', primary_key=True)
    empresa = models.ForeignKey(AfActivos, models.DO_NOTHING, db_column='empresa')
    cod_marca = models.IntegerField()
    placa = models.CharField(max_length=10, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    anio = models.IntegerField()
    motor = models.CharField(max_length=50, blank=True, null=True)
    chasis = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    cod_tipo = models.ForeignKey(AfActivos, models.DO_NOTHING, db_column='cod_tipo')

    class Meta:
        managed = False
        db_table = 'af_vehiculos'
        unique_together = (('cod_activo', 'cod_tipo', 'empresa'),)


class ArAutorizacionesOrdenes(models.Model):
    codigo_orden = models.OneToOneField('ArOrdenesGarantia', models.DO_NOTHING, db_column='codigo_orden', primary_key=True)
    secuencia = models.IntegerField()
    codigo_empresa = models.ForeignKey('ArOrdenesGarantia', models.DO_NOTHING, db_column='codigo_empresa')
    codigo_cliente = models.CharField(max_length=14, blank=True, null=True)
    cod_comprobante_fac = models.CharField(max_length=9, blank=True, null=True)
    tipo_comprobante_fac = models.CharField(max_length=2, blank=True, null=True)
    cod_bodega_egresa = models.IntegerField(blank=True, null=True)
    cod_bodega_ingresa = models.IntegerField(blank=True, null=True)
    numero_serie_egresa = models.CharField(max_length=30, blank=True, null=True)
    numero_serie_ingresa = models.CharField(max_length=30, blank=True, null=True)
    cod_producto_egresa = models.CharField(max_length=14, blank=True, null=True)
    cod_producto_ingresa = models.CharField(max_length=14, blank=True, null=True)
    codigo_tecnico = models.CharField(max_length=30, blank=True, null=True)
    observaciones = models.CharField(max_length=500, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    autoriza = models.CharField(max_length=1, blank=True, null=True)
    usuario_autoriza = models.CharField(max_length=30, blank=True, null=True)
    usuario_niega = models.CharField(max_length=30, blank=True, null=True)
    observaciones_aut_nie = models.CharField(max_length=500, blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    cod_comprobante_gar = models.CharField(max_length=9, blank=True, null=True)
    tipo_comprobante_gar = models.CharField(max_length=2, blank=True, null=True)
    cod_comprobante_ip = models.CharField(max_length=9, blank=True, null=True)
    tipo_comprobante_ip = models.CharField(max_length=2, blank=True, null=True)
    secuencia_ip = models.IntegerField(blank=True, null=True)
    fecha_autoriza_niega = models.DateField(blank=True, null=True)
    estado_producto_egr = models.CharField(max_length=1, blank=True, null=True)
    estado_producto_ing = models.CharField(max_length=1, blank=True, null=True)
    remplazo_directo = models.CharField(max_length=1)
    remp_con_producto_ingresado = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ar_autorizaciones_ordenes'
        unique_together = (('codigo_orden', 'secuencia', 'codigo_empresa'),)


class ArBodegasGarantias(models.Model):
    cod_tipo_empresa = models.CharField(primary_key=True, max_length=4)
    codigo_empresa = models.IntegerField()
    cod_bodega_egresa = models.IntegerField()
    cod_bodega_ingresa = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ar_bodegas_garantias'
        unique_together = (('cod_tipo_empresa', 'codigo_empresa'),)


class ArCiudades(models.Model):
    codigo_ciudad = models.IntegerField(primary_key=True)
    codigo_provincia = models.ForeignKey('ArProvincias', models.DO_NOTHING, db_column='codigo_provincia')
    descripcion = models.CharField(max_length=50)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ar_ciudades'
        unique_together = (('codigo_ciudad', 'codigo_provincia'),)


class ArDistribuidores(models.Model):
    codigo_distribuidor = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ar_distribuidores'


class ArDuracionReparacion(models.Model):
    codigo_duracion = models.IntegerField(primary_key=True)
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=200)
    duracion = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    tipo_duracion = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ar_duracion_reparacion'
        unique_together = (('codigo_duracion', 'codigo_empresa'),)


class ArEstadosOrden(models.Model):
    codigo_estado_orden = models.IntegerField(primary_key=True)
    codigo_empresa = models.ForeignKey('self', models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=200)
    codigo_estado_orden_siguiente = models.ForeignKey('self', models.DO_NOTHING, db_column='codigo_estado_orden_siguiente', blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ar_estados_orden'
        unique_together = (('codigo_estado_orden', 'codigo_empresa'),)


class ArGarantiasTiempo(models.Model):
    codigo_garantia_tiempo = models.IntegerField(primary_key=True)
    cantidad_garantia = models.IntegerField()
    tipo_tiempo = models.CharField(max_length=1)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ar_garantias_tiempo'


class ArHistorialOrdenGarantia(models.Model):
    codigo_orden = models.OneToOneField('ArOrdenesGarantia', models.DO_NOTHING, db_column='codigo_orden', primary_key=True)
    secuencia = models.IntegerField()
    codigo_empresa = models.ForeignKey('ArOrdenesGarantia', models.DO_NOTHING, db_column='codigo_empresa')
    observaciones = models.CharField(max_length=500, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    codigo_estado_orden = models.ForeignKey(ArEstadosOrden, models.DO_NOTHING, db_column='codigo_estado_orden')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    fecha_ofrece_reponer = models.DateField(blank=True, null=True)
    fecha_repuso = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ar_historial_orden_garantia'
        unique_together = (('codigo_orden', 'secuencia', 'codigo_empresa'),)


class ArOrdenesGarantia(models.Model):
    codigo_orden = models.BigIntegerField(primary_key=True)
    codigo_empresa = models.IntegerField()
    codigo_tipo_orden = models.IntegerField()
    codigo_tecnico = models.CharField(max_length=30)
    codigo_duracion = models.IntegerField()
    codigo_estado_orden = models.IntegerField()
    codigo_distribuidor = models.IntegerField()
    numero_orden_manual = models.CharField(max_length=15)
    fecha = models.DateField()
    codigo_ciudad = models.IntegerField(blank=True, null=True)
    codigo_provincia = models.IntegerField(blank=True, null=True)
    codigo_agencia = models.IntegerField(blank=True, null=True)
    cod_comprobante_fac = models.CharField(max_length=9, blank=True, null=True)
    tipo_comprobante_fac = models.CharField(max_length=2, blank=True, null=True)
    problema = models.CharField(max_length=500)
    observaciones = models.CharField(max_length=500, blank=True, null=True)
    recibido_retorno = models.CharField(max_length=1, blank=True, null=True)
    transporte_retorno = models.CharField(max_length=30, blank=True, null=True)
    guia_retorno = models.CharField(max_length=20, blank=True, null=True)
    fecha_retorno = models.DateField(blank=True, null=True)
    observaciones_retorno = models.CharField(max_length=300, blank=True, null=True)
    recibido_reposicion = models.CharField(max_length=1, blank=True, null=True)
    transporte_reposicion = models.CharField(max_length=30, blank=True, null=True)
    guia_reposicion = models.CharField(max_length=20, blank=True, null=True)
    fecha_reposicion = models.DateField(blank=True, null=True)
    observaciones_reposicion = models.CharField(max_length=300, blank=True, null=True)
    encargado_bodega = models.CharField(max_length=30, blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_cliente = models.CharField(max_length=14, blank=True, null=True)
    fecha_cierre_orden = models.DateField(blank=True, null=True)
    informe_tecnico = models.CharField(max_length=500, blank=True, null=True)
    cerrado_por_tecnico = models.CharField(max_length=1)
    fecha_cierre_orden_tecnico = models.DateField(blank=True, null=True)
    fecha_inicio_revision = models.DateField(blank=True, null=True)
    cod_comprobante_st = models.CharField(max_length=9, blank=True, null=True)
    tipo_comprobante_st = models.CharField(max_length=2, blank=True, null=True)
    factura_servicio_tecnico = models.CharField(max_length=1, blank=True, null=True)
    autoriza_sin_factura_st = models.CharField(max_length=30, blank=True, null=True)
    cod_producto = models.CharField(max_length=14, blank=True, null=True)
    numero_serie = models.CharField(max_length=30, blank=True, null=True)
    cod_tipo_persona = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ar_ordenes_garantia'
        unique_together = (('codigo_orden', 'codigo_empresa'),)


class ArOrdenesGarantiaDetalle(models.Model):
    codigo_orden = models.OneToOneField(ArOrdenesGarantia, models.DO_NOTHING, db_column='codigo_orden', primary_key=True)
    secuencia = models.IntegerField()
    codigo_empresa = models.ForeignKey(ArOrdenesGarantia, models.DO_NOTHING, db_column='codigo_empresa')
    cod_comprobante_gar = models.CharField(max_length=9, blank=True, null=True)
    tipo_comprobante_gar = models.CharField(max_length=2, blank=True, null=True)
    observaciones = models.CharField(max_length=500, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    autoriza = models.CharField(max_length=1, blank=True, null=True)
    usuario_autoriza = models.CharField(max_length=30, blank=True, null=True)
    usuario_niega = models.CharField(max_length=30, blank=True, null=True)
    observaciones_aut_nie = models.CharField(max_length=500, blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    fecha_autoriza_niega = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ar_ordenes_garantia_detalle'
        unique_together = (('codigo_orden', 'secuencia', 'codigo_empresa'),)


class ArProductosRemplazoDirecto(models.Model):
    codigo_producto = models.CharField(primary_key=True, max_length=14)
    numero_serie = models.CharField(max_length=30)
    codigo_empresa = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ar_productos_remplazo_directo'
        unique_together = (('codigo_producto', 'numero_serie', 'codigo_empresa'),)


class ArProductosServTecn(models.Model):
    codigo_orden = models.OneToOneField(ArOrdenesGarantia, models.DO_NOTHING, db_column='codigo_orden', primary_key=True)
    secuencia = models.IntegerField()
    codigo_empresa = models.ForeignKey(ArOrdenesGarantia, models.DO_NOTHING, db_column='codigo_empresa')
    numero_serie = models.CharField(max_length=30, blank=True, null=True)
    cod_producto = models.CharField(max_length=14, blank=True, null=True)
    observaciones = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ar_productos_serv_tecn'
        unique_together = (('codigo_orden', 'secuencia', 'codigo_empresa'),)


class ArProvincias(models.Model):
    codigo_provincia = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ar_provincias'


class ArRemplazosPorGarantias(models.Model):
    cod_comprobante_gar = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante_gar = models.CharField(max_length=2)
    secuencia_gar = models.IntegerField()
    codigo_empresa = models.ForeignKey(ArOrdenesGarantia, models.DO_NOTHING, db_column='codigo_empresa')
    cod_comprobante_ing = models.CharField(max_length=9, blank=True, null=True)
    tipo_comprobante_ing = models.CharField(max_length=2, blank=True, null=True)
    secuencia_ing = models.IntegerField(blank=True, null=True)
    codigo_empresa_ing = models.IntegerField(blank=True, null=True)
    numero_serie_defecto = models.CharField(max_length=30, blank=True, null=True)
    numero_serie_remplazo = models.CharField(max_length=30, blank=True, null=True)
    cod_producto_defecto = models.CharField(max_length=14, blank=True, null=True)
    cod_producto_remplazo = models.CharField(max_length=14, blank=True, null=True)
    codigo_tecnico = models.CharField(max_length=30)
    observaciones = models.CharField(max_length=500, blank=True, null=True)
    fecha = models.DateField()
    ya_fue_remplazado = models.CharField(max_length=1)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    fecha_remplazo = models.DateField(blank=True, null=True)
    tipo_proveedor = models.CharField(max_length=3, blank=True, null=True)
    codigo_proveedor = models.CharField(max_length=14, blank=True, null=True)
    usuario_remplazo = models.CharField(max_length=30, blank=True, null=True)
    bodega_remplazo = models.IntegerField(blank=True, null=True)
    bodega_defecto = models.IntegerField(blank=True, null=True)
    cod_comprobante_rem = models.CharField(max_length=9, blank=True, null=True)
    tipo_comprobante_rem = models.CharField(max_length=2, blank=True, null=True)
    estado_producto_defecto = models.CharField(max_length=1, blank=True, null=True)
    estado_producto_remplazo = models.CharField(max_length=1, blank=True, null=True)
    codigo_orden = models.ForeignKey(ArOrdenesGarantia, models.DO_NOTHING, db_column='codigo_orden', blank=True, null=True)
    nota_credito = models.CharField(max_length=12, blank=True, null=True)
    observaciones_nota_credito = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ar_remplazos_por_garantias'
        unique_together = (('cod_comprobante_gar', 'tipo_comprobante_gar', 'secuencia_gar', 'codigo_empresa'),)


class ArServicioGarantias(models.Model):
    codigo_orden = models.BigIntegerField(primary_key=True)
    codigo_empresa = models.IntegerField()
    codigo_tipo_orden = models.IntegerField()
    codigo_tecnico = models.CharField(max_length=30)
    codigo_duracion = models.IntegerField()
    codigo_estado_orden = models.IntegerField()
    numero_orden_manual = models.IntegerField()
    fecha = models.DateField()
    codigo_ciudad = models.IntegerField(blank=True, null=True)
    codigo_provincia = models.IntegerField(blank=True, null=True)
    codigo_agencia = models.IntegerField(blank=True, null=True)
    cod_comprobante_fac = models.CharField(max_length=9, blank=True, null=True)
    tipo_comprobante_fac = models.CharField(max_length=2, blank=True, null=True)
    problema = models.CharField(max_length=500)
    observaciones = models.CharField(max_length=500, blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_cliente = models.CharField(max_length=14, blank=True, null=True)
    fecha_cierre = models.DateField(blank=True, null=True)
    fecha_inicio_revision = models.DateField(blank=True, null=True)
    numero_serie_ingresa = models.CharField(max_length=30, blank=True, null=True)
    cod_producto_ingresa = models.CharField(max_length=14, blank=True, null=True)
    estado_producto_ing = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ar_servicio_garantias'
        unique_together = (('codigo_orden', 'codigo_empresa'),)


class ArTallerServicioTecnico(models.Model):
    codigo = models.CharField(primary_key=True, max_length=30)
    codigo_empresa = models.ForeignKey('ArTiposTecnico', models.DO_NOTHING, db_column='codigo_empresa')
    codigo_tipo_taller = models.ForeignKey('ArTiposTecnico', models.DO_NOTHING, db_column='codigo_tipo_taller')
    descripcion = models.CharField(max_length=200)
    codigo_provincia = models.ForeignKey(ArCiudades, models.DO_NOTHING, db_column='codigo_provincia')
    codigo_ciudad = models.ForeignKey(ArCiudades, models.DO_NOTHING, db_column='codigo_ciudad')
    codigo_marca = models.IntegerField()
    nombre_contacto = models.CharField(max_length=200, blank=True, null=True)
    telefono1 = models.CharField(max_length=12, blank=True, null=True)
    extencion1 = models.CharField(max_length=5, blank=True, null=True)
    telefono2 = models.CharField(max_length=12, blank=True, null=True)
    extencion2 = models.CharField(max_length=5, blank=True, null=True)
    telefono3 = models.CharField(max_length=12, blank=True, null=True)
    extencion3 = models.CharField(max_length=5, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    email2 = models.CharField(max_length=60, blank=True, null=True)
    email3 = models.CharField(max_length=60, blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    ruc = models.CharField(max_length=14)
    tipo_identificacion = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ar_taller_servicio_tecnico'
        unique_together = (('codigo', 'codigo_empresa'),)


class ArTecnicos(models.Model):
    codigo_tecnico = models.OneToOneField(AdUsuarios, models.DO_NOTHING, db_column='codigo_tecnico', primary_key=True)
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_tipo_tecnico = models.ForeignKey('ArTiposTecnico', models.DO_NOTHING, db_column='codigo_tipo_tecnico')

    class Meta:
        managed = False
        db_table = 'ar_tecnicos'
        unique_together = (('codigo_tecnico', 'codigo_empresa'),)


class ArTempOrdenesGarantia(models.Model):
    codigo_orden = models.BigIntegerField(primary_key=True)
    codigo_empresa = models.IntegerField()
    codigo_tipo_orden = models.IntegerField(blank=True, null=True)
    codigo_tecnico = models.CharField(max_length=30, blank=True, null=True)
    codigo_duracion = models.IntegerField(blank=True, null=True)
    codigo_estado_orden = models.IntegerField(blank=True, null=True)
    codigo_distribuidor = models.IntegerField(blank=True, null=True)
    numero_orden_manual = models.CharField(max_length=15, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    codigo_ciudad = models.IntegerField(blank=True, null=True)
    codigo_provincia = models.IntegerField(blank=True, null=True)
    codigo_agencia = models.IntegerField(blank=True, null=True)
    cod_comprobante_fac = models.CharField(max_length=9, blank=True, null=True)
    tipo_comprobante_fac = models.CharField(max_length=2, blank=True, null=True)
    problema = models.CharField(max_length=500, blank=True, null=True)
    observaciones = models.CharField(max_length=500, blank=True, null=True)
    recibido_retorno = models.CharField(max_length=1, blank=True, null=True)
    transporte_retorno = models.CharField(max_length=30, blank=True, null=True)
    guia_retorno = models.CharField(max_length=20, blank=True, null=True)
    fecha_retorno = models.DateField(blank=True, null=True)
    observaciones_retorno = models.CharField(max_length=300, blank=True, null=True)
    recibido_reposicion = models.CharField(max_length=1, blank=True, null=True)
    transporte_reposicion = models.CharField(max_length=30, blank=True, null=True)
    guia_reposicion = models.CharField(max_length=20, blank=True, null=True)
    fecha_reposicion = models.DateField(blank=True, null=True)
    observaciones_reposicion = models.CharField(max_length=300, blank=True, null=True)
    encargado_bodega = models.CharField(max_length=30, blank=True, null=True)
    codigo_cliente = models.CharField(max_length=14, blank=True, null=True)
    fecha_cierre_orden = models.DateField(blank=True, null=True)
    informe_tecnico = models.CharField(max_length=500, blank=True, null=True)
    cerrado_por_tecnico = models.CharField(max_length=1, blank=True, null=True)
    fecha_cierre_orden_tecnico = models.DateField(blank=True, null=True)
    fecha_inicio_revision = models.DateField(blank=True, null=True)
    cod_comprobante_st = models.CharField(max_length=9, blank=True, null=True)
    tipo_comprobante_st = models.CharField(max_length=2, blank=True, null=True)
    factura_servicio_tecnico = models.CharField(max_length=1, blank=True, null=True)
    autoriza_sin_factura_st = models.CharField(max_length=30, blank=True, null=True)
    numero_color = models.IntegerField(blank=True, null=True)
    cod_producto = models.CharField(max_length=14, blank=True, null=True)
    numero_serie = models.CharField(max_length=30, blank=True, null=True)
    cod_tipo_persona = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ar_temp_ordenes_garantia'
        unique_together = (('codigo_orden', 'codigo_empresa'),)


class ArTempSeriesProductos(models.Model):
    cod_producto = models.CharField(primary_key=True, max_length=14)
    numero_serie = models.CharField(max_length=30)
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ar_temp_series_productos'
        unique_together = (('cod_producto', 'numero_serie', 'empresa'),)


class ArTiposOrden(models.Model):
    codigo_tipo_orden = models.IntegerField(primary_key=True)
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=200)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ar_tipos_orden'
        unique_together = (('codigo_tipo_orden', 'codigo_empresa'),)


class ArTiposTecnico(models.Model):
    codigo_tipo_tecnico = models.CharField(primary_key=True, max_length=1)
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=50)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ar_tipos_tecnico'
        unique_together = (('codigo_tipo_tecnico', 'codigo_empresa'),)


class B(models.Model):
    codigo = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=10, blank=True, null=True)
    fecha_adicion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'b'


class CcAdjetivos(models.Model):
    codigo_adjetivo = models.IntegerField(primary_key=True)
    codigo_buro = models.ForeignKey(AdBuros, models.DO_NOTHING, db_column='codigo_buro')
    codigo_empresa = models.ForeignKey(AdBuros, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=100)
    codigo_tipo_gestion = models.ForeignKey('CcTiposGestiones', models.DO_NOTHING, db_column='codigo_tipo_gestion', blank=True, null=True)
    codigo_area = models.ForeignKey('CcTiposGestiones', models.DO_NOTHING, db_column='codigo_area', blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_adjetivos'
        unique_together = (('codigo_adjetivo', 'codigo_buro', 'codigo_empresa'),)


class CcAgenciasCallCenter(models.Model):
    codigo_agencia = models.OneToOneField(AdAgencias, models.DO_NOTHING, db_column='codigo_agencia', primary_key=True)
    codigo_call_center = models.ForeignKey('CcCallCenter', models.DO_NOTHING, db_column='codigo_call_center')
    codigo_empresa = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_empresa')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_agencias_call_center'
        unique_together = (('codigo_agencia', 'codigo_call_center', 'codigo_empresa'),)


class CcAgenciasCallCenterVentas(models.Model):
    codigo_agencia = models.OneToOneField(AdAgencias, models.DO_NOTHING, db_column='codigo_agencia', primary_key=True)
    codigo_call_center = models.ForeignKey('CcCallCenterVentas', models.DO_NOTHING, db_column='codigo_call_center')
    codigo_empresa = models.ForeignKey('CcCallCenterVentas', models.DO_NOTHING, db_column='codigo_empresa')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_agencias_call_center_ventas'
        unique_together = (('codigo_agencia', 'codigo_call_center', 'codigo_empresa'),)


class CcAgendaCobrador(models.Model):
    cod_comprobante = models.OneToOneField('CcCabeceraClientesCobrador', models.DO_NOTHING, db_column='cod_comprobante', primary_key=True)
    tipo_comprobante = models.ForeignKey('CcCabeceraClientesCobrador', models.DO_NOTHING, db_column='tipo_comprobante')
    periodo = models.ForeignKey('CcCabeceraClientesCobrador', models.DO_NOTHING, db_column='periodo')
    codigo_call_center = models.ForeignKey('CcCabeceraClientesCobrador', models.DO_NOTHING, db_column='codigo_call_center')
    codigo_empresa = models.ForeignKey('CcCabeceraClientesCobrador', models.DO_NOTHING, db_column='codigo_empresa')
    dia_visita = models.IntegerField()
    hora_visita = models.IntegerField()
    minutos_visita = models.IntegerField()
    identificacion_cobrador_act = models.ForeignKey('RhEmpleados', models.DO_NOTHING, db_column='identificacion_cobrador_act')
    codigo_segmento_cartera_act = models.ForeignKey('CcSegmentosDeCarteras', models.DO_NOTHING, db_column='codigo_segmento_cartera_act')
    cod_persona = models.CharField(max_length=14)
    cod_tipo_persona = models.CharField(max_length=3)
    total_asignado = models.DecimalField(max_digits=18, decimal_places=2)
    credito_gestionado_si_no = models.CharField(max_length=1)
    credito_cobrado_si_no = models.CharField(max_length=1)
    cobro_en_efectivo = models.DecimalField(max_digits=18, decimal_places=2)
    interes_mora_cobrado = models.DecimalField(max_digits=18, decimal_places=2)
    gasto_cobranza_cobrado = models.DecimalField(max_digits=18, decimal_places=2)
    interes_mora_generado = models.DecimalField(max_digits=18, decimal_places=2)
    gasto_cobranza_generado = models.DecimalField(max_digits=18, decimal_places=2)
    total_a_cobrar = models.DecimalField(max_digits=18, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    dia_visita_agendar = models.IntegerField()
    codigo_cargo = models.ForeignKey('CcCabeceraClientesCobrador', models.DO_NOTHING, db_column='codigo_cargo')

    class Meta:
        managed = False
        db_table = 'cc_agenda_cobrador'
        unique_together = (('cod_comprobante', 'tipo_comprobante', 'periodo', 'codigo_call_center', 'codigo_empresa'),)


class CcAnticiposXAplicar(models.Model):
    numero_cancelacion_manual = models.CharField(primary_key=True, max_length=9)
    codigo_empresa = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_empresa')
    identificacion_cobrador = models.ForeignKey('RhEmpleados', models.DO_NOTHING, db_column='identificacion_cobrador')
    fecha_cobro = models.DateField()
    cod_persona = models.CharField(max_length=14)
    cod_tipo_persona = models.CharField(max_length=3)
    codigo_agencia_caja = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_agencia_caja')
    numero_anticipo_st_ant = models.CharField(max_length=9, blank=True, null=True)
    tipo_anticipo_st_ant = models.CharField(max_length=2, blank=True, null=True)
    valor_cobrado = models.DecimalField(max_digits=18, decimal_places=2)
    documento_impreso = models.CharField(max_length=1, blank=True, null=True)
    documento_impreso_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_impresion_documento = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=1)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_anticipos_x_aplicar'
        unique_together = (('numero_cancelacion_manual', 'codigo_empresa'),)


class CcAplicaEncuesta(models.Model):
    codigo_cliente = models.OneToOneField('CcPersonasCampaniasTelefon', models.DO_NOTHING, db_column='codigo_cliente', primary_key=True)
    codigo_campania = models.ForeignKey('CcPersonasCampaniasTelefon', models.DO_NOTHING, db_column='codigo_campania')
    codigo_area = models.ForeignKey('CcPersonasCampaniasTelefon', models.DO_NOTHING, db_column='codigo_area')
    codigo_empresa = models.ForeignKey('CcPersonasCampaniasTelefon', models.DO_NOTHING, db_column='codigo_empresa')
    cita = models.CharField(max_length=1, blank=True, null=True)
    fecha_cita = models.DateField(blank=True, null=True)
    numero_cita = models.IntegerField(blank=True, null=True)
    fecha_cita_efectivizada = models.DateField(blank=True, null=True)
    tarjeta = models.CharField(max_length=1, blank=True, null=True)
    observacion = models.CharField(max_length=400, blank=True, null=True)
    cod_agencia_cita = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='cod_agencia_cita', blank=True, null=True)
    codigo_tipo_entrega = models.ForeignKey('CcTiposEntrega', models.DO_NOTHING, db_column='codigo_tipo_entrega', blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    cod_agencia_tarjeta = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='cod_agencia_tarjeta', blank=True, null=True)
    direccion_entrega = models.CharField(max_length=200, blank=True, null=True)
    telefono1 = models.CharField(max_length=10, blank=True, null=True)
    telefono2 = models.CharField(max_length=10, blank=True, null=True)
    cedula = models.CharField(max_length=14, blank=True, null=True)
    identificacion_telefonista = models.ForeignKey('CcTelefonistasCampanias', models.DO_NOTHING, db_column='identificacion_telefonista', blank=True, null=True)
    conforme_producto = models.CharField(max_length=1, blank=True, null=True)
    observaciones_conf_prod = models.CharField(max_length=300, blank=True, null=True)
    conforme_valor_cuotas = models.CharField(max_length=1, blank=True, null=True)
    observaciones_conf_val_cuo = models.CharField(max_length=300, blank=True, null=True)
    actualizo_datos = models.CharField(max_length=1, blank=True, null=True)
    codigo_ciudad = models.CharField(max_length=14, blank=True, null=True)
    direccion_entrega2 = models.CharField(max_length=200, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    codigo_tipo_ingreso = models.ForeignKey('CcTiposIngresos', models.DO_NOTHING, db_column='codigo_tipo_ingreso', blank=True, null=True)
    valor_ingresos = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    referencia1 = models.CharField(max_length=100, blank=True, null=True)
    telefono_ref1 = models.CharField(max_length=9, blank=True, null=True)
    referencia2 = models.CharField(max_length=100, blank=True, null=True)
    telefono_ref2 = models.CharField(max_length=9, blank=True, null=True)
    referencia3 = models.CharField(max_length=100, blank=True, null=True)
    telefono_ref3 = models.CharField(max_length=9, blank=True, null=True)
    codigo_cliente_anterior = models.CharField(max_length=14, blank=True, null=True)
    direccion_sistemas = models.CharField(max_length=200, blank=True, null=True)
    lugar_trabajo = models.CharField(max_length=100, blank=True, null=True)
    direccion_lugar_trabajo = models.CharField(max_length=200, blank=True, null=True)
    telefono_lugar_trabajo = models.CharField(max_length=9, blank=True, null=True)
    conforme_atencion = models.CharField(max_length=1, blank=True, null=True)
    observaciones_conf_aten = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_aplica_encuesta'
        unique_together = (('codigo_cliente', 'codigo_campania', 'codigo_area', 'codigo_empresa'),)


class CcAplicaEncuestaRota(models.Model):
    secuencia = models.OneToOneField('CcPersonasCampaniasTeleRot', models.DO_NOTHING, db_column='secuencia', primary_key=True)
    codigo_cliente = models.ForeignKey('CcPersonasCampaniasTeleRot', models.DO_NOTHING, db_column='codigo_cliente')
    codigo_campania = models.ForeignKey('CcPersonasCampaniasTeleRot', models.DO_NOTHING, db_column='codigo_campania')
    codigo_area = models.ForeignKey('CcPersonasCampaniasTeleRot', models.DO_NOTHING, db_column='codigo_area')
    codigo_empresa = models.ForeignKey('CcPersonasCampaniasTeleRot', models.DO_NOTHING, db_column='codigo_empresa')
    cita = models.CharField(max_length=1, blank=True, null=True)
    fecha_cita = models.DateField(blank=True, null=True)
    numero_cita = models.IntegerField(blank=True, null=True)
    fecha_cita_efectivizada = models.DateField(blank=True, null=True)
    tarjeta = models.CharField(max_length=1, blank=True, null=True)
    observacion = models.CharField(max_length=400, blank=True, null=True)
    cod_agencia_cita = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='cod_agencia_cita', blank=True, null=True)
    codigo_tipo_entrega = models.ForeignKey('CcTiposEntrega', models.DO_NOTHING, db_column='codigo_tipo_entrega', blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    cod_agencia_tarjeta = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='cod_agencia_tarjeta', blank=True, null=True)
    direccion_entrega = models.CharField(max_length=200, blank=True, null=True)
    telefono1 = models.CharField(max_length=10, blank=True, null=True)
    telefono2 = models.CharField(max_length=10, blank=True, null=True)
    cedula = models.CharField(max_length=14, blank=True, null=True)
    identificacion_telefonista = models.ForeignKey('CcTelefonistasCampanias', models.DO_NOTHING, db_column='identificacion_telefonista', blank=True, null=True)
    conforme_producto = models.CharField(max_length=1, blank=True, null=True)
    observaciones_conf_prod = models.CharField(max_length=300, blank=True, null=True)
    conforme_valor_cuotas = models.CharField(max_length=1, blank=True, null=True)
    observaciones_conf_val_cuo = models.CharField(max_length=300, blank=True, null=True)
    actualizo_datos = models.CharField(max_length=1, blank=True, null=True)
    codigo_ciudad = models.CharField(max_length=14, blank=True, null=True)
    direccion_entrega2 = models.CharField(max_length=200, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    codigo_tipo_ingreso = models.ForeignKey('CcTiposIngresos', models.DO_NOTHING, db_column='codigo_tipo_ingreso', blank=True, null=True)
    valor_ingresos = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    referencia1 = models.CharField(max_length=100, blank=True, null=True)
    telefono_ref1 = models.CharField(max_length=9, blank=True, null=True)
    referencia2 = models.CharField(max_length=100, blank=True, null=True)
    telefono_ref2 = models.CharField(max_length=9, blank=True, null=True)
    referencia3 = models.CharField(max_length=100, blank=True, null=True)
    telefono_ref3 = models.CharField(max_length=9, blank=True, null=True)
    codigo_cliente_anterior = models.CharField(max_length=14, blank=True, null=True)
    direccion_sistemas = models.CharField(max_length=200, blank=True, null=True)
    lugar_trabajo = models.CharField(max_length=100, blank=True, null=True)
    direccion_lugar_trabajo = models.CharField(max_length=200, blank=True, null=True)
    telefono_lugar_trabajo = models.CharField(max_length=9, blank=True, null=True)
    tipo_comprobante = models.CharField(max_length=2, blank=True, null=True)
    cod_comprobante = models.CharField(max_length=9, blank=True, null=True)
    estado_reimprime_tarjeta = models.CharField(max_length=1, blank=True, null=True)
    conforme_atencion = models.CharField(max_length=1, blank=True, null=True)
    observaciones_conf_aten = models.CharField(max_length=300, blank=True, null=True)
    cod_agencia_atendio = models.IntegerField(blank=True, null=True)
    cod_agente_atendio = models.CharField(max_length=14, blank=True, null=True)
    informo_promociones = models.CharField(max_length=1, blank=True, null=True)
    cod_agencia_informo = models.IntegerField(blank=True, null=True)
    sugerencia_informo = models.CharField(max_length=200, blank=True, null=True)
    cod_agente_informo = models.CharField(max_length=14, blank=True, null=True)
    codigo_pregunta = models.IntegerField(blank=True, null=True)
    anio_mes_pregunta = models.IntegerField(blank=True, null=True)
    respuesta_pregunta_mes = models.CharField(max_length=300, blank=True, null=True)
    opcion_pregunta_mes = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_aplica_encuesta_rota'
        unique_together = (('secuencia', 'codigo_cliente', 'codigo_campania', 'codigo_area', 'codigo_empresa'),)


class CcAreaGestiones(models.Model):
    codigo_area = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=10)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_area_gestiones'


class CcAreaTiposGestiones(models.Model):
    codigo_area_tipo_gestion = models.IntegerField(primary_key=True)
    codigo_area = models.ForeignKey(CcAreaGestiones, models.DO_NOTHING, db_column='codigo_area')
    descripcion = models.CharField(max_length=100)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_call_center = models.ForeignKey('CcCallCenter', models.DO_NOTHING, db_column='codigo_call_center')

    class Meta:
        managed = False
        db_table = 'cc_area_tipos_gestiones'
        unique_together = (('codigo_area_tipo_gestion', 'codigo_area', 'codigo_call_center'),)


class CcAuditoriaCabCliCob(models.Model):
    old_codigo_comprobante = models.CharField(max_length=9)
    old_tipo_comprobante = models.CharField(max_length=2)
    old_periodo = models.IntegerField()
    old_codigo_call_center = models.IntegerField()
    old_codigo_empresa = models.IntegerField()
    old_identificacion_cobrador_ac = models.CharField(max_length=20)
    old_codigo_segmento_cartera_ac = models.IntegerField()
    old_codigo_call_center_act = models.IntegerField()
    old_identificacion_cobrador_or = models.CharField(max_length=20)
    old_codigo_segmento_cartera_or = models.IntegerField()
    old_codigo_tipo_persona = models.CharField(max_length=3)
    old_codigo_persona = models.CharField(max_length=14)
    old_total_cuotas = models.IntegerField()
    old_total_valor = models.DecimalField(max_digits=14, decimal_places=2)
    old_anulado = models.CharField(max_length=1)
    old_adicionado_por = models.CharField(max_length=30)
    old_fecha_adicion = models.DateField()
    old_modificado_por = models.CharField(max_length=30, blank=True, null=True)
    old_fecha_modificacion = models.DateField(blank=True, null=True)
    old_codigo_agencia = models.IntegerField()
    old_codigo_item_act = models.CharField(max_length=3)
    old_codigo_modelo_act = models.CharField(max_length=8)
    old_codigo_item = models.CharField(max_length=3)
    old_codigo_modelo = models.CharField(max_length=8)
    old_codigo_empresa_asig_car = models.IntegerField()
    old_carga_inicial = models.CharField(max_length=1)
    old_codigo_cargo = models.IntegerField()
    new_codigo_comprobante = models.CharField(max_length=9, blank=True, null=True)
    new_tipo_comprobante = models.CharField(max_length=2, blank=True, null=True)
    new_periodo = models.IntegerField(blank=True, null=True)
    new_codigo_call_center = models.IntegerField(blank=True, null=True)
    new_codigo_empresa = models.IntegerField(blank=True, null=True)
    new_identificacion_cobrador_ac = models.CharField(max_length=20, blank=True, null=True)
    new_codigo_segmento_cartera_ac = models.IntegerField(blank=True, null=True)
    new_codigo_call_center_act = models.IntegerField(blank=True, null=True)
    new_identificacion_cobrador_or = models.CharField(max_length=20, blank=True, null=True)
    new_codigo_segmento_cartera_or = models.IntegerField(blank=True, null=True)
    new_codigo_tipo_persona = models.CharField(max_length=3, blank=True, null=True)
    new_codigo_persona = models.CharField(max_length=14, blank=True, null=True)
    new_total_cuotas = models.IntegerField(blank=True, null=True)
    new_total_valor = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    new_anulado = models.CharField(max_length=1, blank=True, null=True)
    new_adicionado_por = models.CharField(max_length=30, blank=True, null=True)
    new_fecha_adicion = models.DateField(blank=True, null=True)
    new_modificado_por = models.CharField(max_length=30, blank=True, null=True)
    new_fecha_modificacion = models.DateField(blank=True, null=True)
    new_codigo_agencia = models.IntegerField(blank=True, null=True)
    new_codigo_item_act = models.CharField(max_length=3, blank=True, null=True)
    new_codigo_modelo_act = models.CharField(max_length=8, blank=True, null=True)
    new_codigo_item = models.CharField(max_length=3, blank=True, null=True)
    new_codigo_modelo = models.CharField(max_length=8, blank=True, null=True)
    new_codigo_empresa_asig_car = models.IntegerField(blank=True, null=True)
    new_carga_inicial = models.CharField(max_length=1, blank=True, null=True)
    new_codigo_cargo = models.IntegerField(blank=True, null=True)
    adicionado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_adicion = models.DateField(blank=True, null=True)
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    eliminado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_eliminacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_auditoria_cab_cli_cob'


class CcAuditoriaComRec(models.Model):
    old_codigo_comprobante = models.CharField(max_length=9)
    old_tipo_comprobante = models.CharField(max_length=2)
    old_codigo_empresa = models.IntegerField()
    old_periodo = models.IntegerField()
    old_identificacion_cobrador = models.CharField(max_length=20)
    old_codigo_item = models.CharField(max_length=3)
    old_codigo_segmento_cartera = models.IntegerField()
    old_codigo_empresa_asig_car = models.IntegerField()
    old_codigo_modelo = models.CharField(max_length=8)
    old_codigo_call_center = models.IntegerField()
    old_codigo_agencia = models.IntegerField()
    old_cuenta_cancelada = models.CharField(max_length=1)
    old_anulado = models.CharField(max_length=1)
    old_adicionado_por = models.CharField(max_length=30)
    old_fecha_adicion = models.DateField()
    old_modificado_por = models.CharField(max_length=30, blank=True, null=True)
    old_fecha_modificacion = models.DateField(blank=True, null=True)
    old_cod_tipo_identificacion = models.IntegerField()
    old_cod_cliente = models.CharField(max_length=14)
    old_codigo_cargo = models.IntegerField()
    new_codigo_comprobante = models.CharField(max_length=9, blank=True, null=True)
    new_tipo_comprobante = models.CharField(max_length=2, blank=True, null=True)
    new_codigo_empresa = models.IntegerField(blank=True, null=True)
    new_periodo = models.IntegerField(blank=True, null=True)
    new_identificacion_cobrador = models.CharField(max_length=20, blank=True, null=True)
    new_codigo_item = models.CharField(max_length=3, blank=True, null=True)
    new_codigo_segmento_cartera = models.IntegerField(blank=True, null=True)
    new_codigo_empresa_asig_car = models.IntegerField(blank=True, null=True)
    new_codigo_modelo = models.CharField(max_length=8, blank=True, null=True)
    new_codigo_call_center = models.IntegerField(blank=True, null=True)
    new_codigo_agencia = models.IntegerField(blank=True, null=True)
    new_cuenta_cancelada = models.CharField(max_length=1, blank=True, null=True)
    new_anulado = models.CharField(max_length=1, blank=True, null=True)
    new_adicionado_por = models.CharField(max_length=30, blank=True, null=True)
    new_fecha_adicion = models.DateField(blank=True, null=True)
    new_modificado_por = models.CharField(max_length=30, blank=True, null=True)
    new_fecha_modificacion = models.DateField(blank=True, null=True)
    new_cod_tipo_identificacion = models.IntegerField(blank=True, null=True)
    new_cod_cliente = models.CharField(max_length=14, blank=True, null=True)
    new_codigo_cargo = models.IntegerField(blank=True, null=True)
    adicionado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_adicion = models.DateField(blank=True, null=True)
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    eliminado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_eliminacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_auditoria_com_rec'


class CcAuditoriaDetCliCob(models.Model):
    old_numero_vencimiento = models.IntegerField()
    old_codigo_comprobante = models.CharField(max_length=9)
    old_tipo_comprobante = models.CharField(max_length=2)
    old_codigo_forma_pago = models.CharField(max_length=3)
    old_periodo = models.IntegerField()
    old_codigo_call_center = models.IntegerField()
    old_codigo_empresa = models.IntegerField()
    old_identificacion_cobrador_ac = models.CharField(max_length=20)
    old_codigo_segmento_cartera_ac = models.IntegerField()
    old_codigo_call_center_act = models.IntegerField()
    old_identificacion_cobrador_or = models.CharField(max_length=20)
    old_codigo_segmento_cartera_or = models.IntegerField()
    old_fecha_vencimiento = models.DateField()
    old_saldo_cuota = models.DecimalField(max_digits=14, decimal_places=2)
    old_anulado = models.CharField(max_length=1)
    old_adicionado_por = models.CharField(max_length=30)
    old_fecha_adicion = models.DateField()
    old_modificado_por = models.CharField(max_length=30, blank=True, null=True)
    old_fecha_modificacion = models.DateField(blank=True, null=True)
    old_codigo_item = models.CharField(max_length=3)
    old_codigo_modelo = models.CharField(max_length=8)
    old_codigo_item_act = models.CharField(max_length=3)
    old_codigo_modelo_act = models.CharField(max_length=8)
    old_codigo_agencia = models.IntegerField()
    old_codigo_empresa_asig_car = models.IntegerField()
    old_carga_inicial = models.CharField(max_length=1)
    old_codigo_cargo = models.IntegerField()
    new_numero_vencimiento = models.IntegerField(blank=True, null=True)
    new_codigo_comprobante = models.CharField(max_length=9, blank=True, null=True)
    new_tipo_comprobante = models.CharField(max_length=2, blank=True, null=True)
    new_codigo_forma_pago = models.CharField(max_length=3, blank=True, null=True)
    new_periodo = models.IntegerField(blank=True, null=True)
    new_codigo_call_center = models.IntegerField(blank=True, null=True)
    new_codigo_empresa = models.IntegerField(blank=True, null=True)
    new_identificacion_cobrador_ac = models.CharField(max_length=20, blank=True, null=True)
    new_codigo_segmento_cartera_ac = models.IntegerField(blank=True, null=True)
    new_codigo_call_center_act = models.IntegerField(blank=True, null=True)
    new_identificacion_cobrador_or = models.CharField(max_length=20, blank=True, null=True)
    new_codigo_segmento_cartera_or = models.IntegerField(blank=True, null=True)
    new_fecha_vencimiento = models.DateField(blank=True, null=True)
    new_saldo_cuota = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    new_anulado = models.CharField(max_length=1, blank=True, null=True)
    new_adicionado_por = models.CharField(max_length=30, blank=True, null=True)
    new_fecha_adicion = models.DateField(blank=True, null=True)
    new_modificado_por = models.CharField(max_length=30, blank=True, null=True)
    new_fecha_modificacion = models.DateField(blank=True, null=True)
    new_codigo_item = models.CharField(max_length=3, blank=True, null=True)
    new_codigo_modelo = models.CharField(max_length=8, blank=True, null=True)
    new_codigo_item_act = models.CharField(max_length=3, blank=True, null=True)
    new_codigo_modelo_act = models.CharField(max_length=8, blank=True, null=True)
    new_codigo_agencia = models.IntegerField(blank=True, null=True)
    new_codigo_empresa_asig_car = models.IntegerField(blank=True, null=True)
    new_carga_inicial = models.CharField(max_length=1, blank=True, null=True)
    new_codigo_cargo = models.IntegerField(blank=True, null=True)
    adicionado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_adicion = models.DateField(blank=True, null=True)
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    eliminado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_eliminacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_auditoria_det_cli_cob'


class CcBalancesMensuales(models.Model):
    cod_comprobante = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    periodo_cierre = models.IntegerField()
    cartera = models.CharField(max_length=3)
    codigo_agencia = models.IntegerField()
    codigo_empresa = models.IntegerField()
    codigo_politica = models.IntegerField()
    nombre_politica = models.CharField(max_length=100)
    codigo_estado_cuota = models.CharField(max_length=3, blank=True, null=True)
    codigo_persona = models.CharField(max_length=14)
    codigo_tipo_persona = models.CharField(max_length=3)
    zona_geograficah = models.CharField(max_length=15, blank=True, null=True)
    nombre_parroquia = models.CharField(max_length=50, blank=True, null=True)
    cod_modelo = models.CharField(max_length=8, blank=True, null=True)
    cod_item = models.CharField(max_length=3, blank=True, null=True)
    nombre_zona = models.CharField(max_length=50, blank=True, null=True)
    cuotas_gratis = models.DecimalField(max_digits=4, decimal_places=2)
    factura_manual = models.CharField(max_length=9)
    numero_pagos = models.IntegerField()
    cod_agente = models.CharField(max_length=14, blank=True, null=True)
    nombre_vendedor = models.CharField(max_length=255, blank=True, null=True)
    fecha_vencimiento = models.DateField()
    direccion_calleh = models.CharField(max_length=200, blank=True, null=True)
    numero_casa = models.CharField(max_length=20, blank=True, null=True)
    calle_transversal = models.CharField(max_length=100, blank=True, null=True)
    telefono1h = models.CharField(max_length=15, blank=True, null=True)
    telefono2h = models.CharField(max_length=15, blank=True, null=True)
    cod_cat_cliente = models.CharField(max_length=8, blank=True, null=True)
    cod_producto = models.CharField(max_length=14, blank=True, null=True)
    nombre_producto = models.CharField(max_length=200, blank=True, null=True)
    cod_modelo_cat = models.CharField(max_length=8, blank=True, null=True)
    cod_item_cat = models.CharField(max_length=3, blank=True, null=True)
    nombre_linea = models.CharField(max_length=50, blank=True, null=True)
    es_empleado = models.CharField(max_length=100)
    saldo_anticipo = models.DecimalField(max_digits=14, decimal_places=2)
    fecha_inicio_mes = models.DateField()
    fecha_fin_mes = models.DateField()
    valor_mes_actual_vencido = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_29_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_28_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_27_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_26_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_25_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_24_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_23_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_22_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_21_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_20_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_19_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_18_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_17_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_16_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_15_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_14_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_13_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_12_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_11_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_10_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_09_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_08_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_07_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_06_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_05_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_04_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_03_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_02_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_01_mes = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_01_mes = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_02_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_03_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_04_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_05_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_06_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_07_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_08_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_09_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_10_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_11_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_12_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_mas_12_meses = models.DecimalField(max_digits=14, decimal_places=2)
    interes_mora_generado = models.DecimalField(max_digits=14, decimal_places=2)
    interes_mora_abonado = models.DecimalField(max_digits=14, decimal_places=2)
    gasto_cobranza_generado = models.DecimalField(max_digits=14, decimal_places=2)
    gasto_cobranza_abonado = models.DecimalField(max_digits=14, decimal_places=2)
    dias_atraso_adelanto = models.IntegerField()
    codigo_segmento_cartera = models.IntegerField(blank=True, null=True)
    nombre_segmento_cartera = models.CharField(max_length=100, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    negociado_con = models.CharField(max_length=255, blank=True, null=True)
    numero_negociacion = models.IntegerField(blank=True, null=True)
    valor_cuota = models.DecimalField(max_digits=14, decimal_places=2)
    verificacion_campo_por = models.CharField(max_length=105, blank=True, null=True)
    verificacion_telefonica_por = models.CharField(max_length=105, blank=True, null=True)
    credito_aprobado_por = models.CharField(max_length=105, blank=True, null=True)
    codigo_call_center = models.IntegerField(blank=True, null=True)
    nombre_call_center = models.CharField(max_length=100, blank=True, null=True)
    anio_venta = models.IntegerField(blank=True, null=True)
    mes_venta = models.IntegerField(blank=True, null=True)
    dia_venta = models.IntegerField(blank=True, null=True)
    dia_vencimiento = models.IntegerField(blank=True, null=True)
    ultima_gestion = models.CharField(max_length=10, blank=True, null=True)
    fecha_ultima_gestion = models.DateField(blank=True, null=True)
    cupo_aprobado = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    credijaher = models.CharField(max_length=1, blank=True, null=True)
    valor_entrada = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    valor_adicional = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cod_garante = models.CharField(max_length=14, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    valor_ingresos = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrador_asignado = models.CharField(max_length=100, blank=True, null=True)
    fecha_aplicacion_fondo = models.DateField(blank=True, null=True)
    monto_credito = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    fecha_ultimo_pago = models.DateField(blank=True, null=True)
    numero_cuotas_canceladas = models.IntegerField(blank=True, null=True)
    numero_cuotas_mora = models.IntegerField(blank=True, null=True)
    operador_asignado = models.CharField(max_length=100, blank=True, null=True)
    presupuesto = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nro_credijaher = models.CharField(max_length=21, blank=True, null=True)
    total_vencido = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    total_x_vencer = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    saldo_del_credito = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    codigo_ocupacion_laboral = models.CharField(max_length=3, blank=True, null=True)
    ocupacion_laboral = models.CharField(max_length=100, blank=True, null=True)
    calificacion_central_riesgo = models.CharField(max_length=1, blank=True, null=True)
    codigo_tipo_vivienda = models.CharField(max_length=3, blank=True, null=True)
    tipo_vivienda = models.CharField(max_length=100, blank=True, null=True)
    total_creditos_vigentes = models.IntegerField()
    codigo_marca = models.IntegerField(blank=True, null=True)
    nombre_marca = models.CharField(max_length=50, blank=True, null=True)
    nombre_categoria_cliente = models.CharField(max_length=30, blank=True, null=True)
    nombre_cliente = models.CharField(max_length=255, blank=True, null=True)
    fecha_ult_cobro = models.DateField(blank=True, null=True)
    nombre_agencia = models.CharField(max_length=50, blank=True, null=True)
    nombre_ultima_gestion = models.CharField(max_length=100, blank=True, null=True)
    cod_segmen_cartera_bal_ant = models.IntegerField(blank=True, null=True)
    nombre_segmen_carte_bal_ant = models.CharField(max_length=100, blank=True, null=True)
    fecha_ult_actualiz_sal_act_hoy = models.DateField(blank=True, null=True)
    saldo_actual_hoy = models.DecimalField(max_digits=18, decimal_places=2)
    dias_minimo_cobro = models.DecimalField(max_digits=10, decimal_places=2)
    dias_maximo_cobro = models.DecimalField(max_digits=10, decimal_places=2)
    dias_promedio_cobro = models.DecimalField(max_digits=10, decimal_places=2)
    dias_minimo_entre_cobros = models.DecimalField(max_digits=10, decimal_places=2)
    dias_maximo_entre_cobros = models.DecimalField(max_digits=10, decimal_places=2)
    dias_promedio_entre_cobros = models.DecimalField(max_digits=10, decimal_places=2)
    total_gestiones_call_center = models.IntegerField()
    total_gestiones_positivas_call = models.IntegerField()
    total_gestiones_cobrad_verif = models.IntegerField()
    valor_cancelado_desde = models.DecimalField(max_digits=10, decimal_places=2)
    total_cuotas_cancelad_desde = models.IntegerField()
    intangible_garantia_extendida = models.DecimalField(max_digits=10, decimal_places=2)
    intangible_linea_blanca = models.DecimalField(max_digits=10, decimal_places=2)
    intangible_arroba = models.DecimalField(max_digits=10, decimal_places=2)
    tsc = models.CharField(max_length=1)
    sumatoria_dias_atraso = models.BigIntegerField()
    promocion_cuotas_gratis = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_balances_mensuales'
        unique_together = (('cod_comprobante', 'tipo_comprobante', 'periodo_cierre', 'cartera', 'codigo_agencia', 'codigo_empresa'),)


class CcBancoPreguntas(models.Model):
    codigo_banco_pregunta = models.IntegerField(primary_key=True)
    codigo_tipo_respuesta = models.ForeignKey('CcTiposRespuestas', models.DO_NOTHING, db_column='codigo_tipo_respuesta')
    codigo_tipo_encuesta = models.ForeignKey('CcTiposEncuestas', models.DO_NOTHING, db_column='codigo_tipo_encuesta')
    codigo_area_tipo_gestion = models.ForeignKey('CcTiposEncuestas', models.DO_NOTHING, db_column='codigo_area_tipo_gestion')
    codigo_area = models.ForeignKey('CcTiposEncuestas', models.DO_NOTHING, db_column='codigo_area')
    codigo_empresa = models.ForeignKey('CcTiposRespuestas', models.DO_NOTHING, db_column='codigo_empresa')
    pregunta = models.CharField(max_length=200)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_call_center = models.ForeignKey('CcTiposEncuestas', models.DO_NOTHING, db_column='codigo_call_center')

    class Meta:
        managed = False
        db_table = 'cc_banco_preguntas'
        unique_together = (('codigo_banco_pregunta', 'codigo_tipo_respuesta', 'codigo_tipo_encuesta', 'codigo_area_tipo_gestion', 'codigo_area', 'codigo_call_center', 'codigo_empresa'),)


class CcCabeceraCampaniasCobranza(models.Model):
    numero_campania = models.IntegerField(primary_key=True)
    id_servidor = models.CharField(max_length=3)
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=300)
    periodo = models.IntegerField()
    anulado = models.CharField(max_length=1)
    vigente_si_no = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_cabecera_campanias_cobranza'
        unique_together = (('numero_campania', 'id_servidor', 'codigo_empresa'),)


class CcCabeceraClientesAsignados(models.Model):
    codigo_comprobante = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    periodo = models.IntegerField()
    codigo_call_center = models.IntegerField()
    codigo_empresa = models.IntegerField()
    identificacion_telefonista_act = models.CharField(max_length=20)
    codigo_segmento_cartera_act = models.IntegerField()
    codigo_call_center_act = models.IntegerField()
    identificacion_telefonista = models.CharField(max_length=20)
    codigo_segmento_cartera = models.IntegerField()
    codigo_tipo_persona = models.CharField(max_length=3)
    codigo_persona = models.CharField(max_length=14)
    total_cuotas = models.IntegerField()
    total_valor = models.DecimalField(max_digits=14, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_agencia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cc_cabecera_clientes_asignados'
        unique_together = (('codigo_comprobante', 'tipo_comprobante', 'periodo', 'codigo_call_center', 'codigo_empresa'),)


class CcCabeceraClientesCobrador(models.Model):
    codigo_comprobante = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    periodo = models.IntegerField()
    codigo_call_center = models.IntegerField()
    codigo_empresa = models.IntegerField()
    identificacion_cobrador_act = models.CharField(max_length=20)
    codigo_segmento_cartera_act = models.IntegerField()
    codigo_call_center_act = models.IntegerField()
    identificacion_cobrador_ori = models.CharField(max_length=20)
    codigo_segmento_cartera_ori = models.IntegerField()
    codigo_tipo_persona = models.CharField(max_length=3)
    codigo_persona = models.CharField(max_length=14)
    total_cuotas = models.IntegerField()
    total_valor = models.DecimalField(max_digits=14, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_agencia = models.IntegerField()
    codigo_item_act = models.CharField(max_length=3)
    codigo_modelo_act = models.CharField(max_length=8)
    codigo_item_ori = models.CharField(max_length=3)
    codigo_modelo_ori = models.CharField(max_length=8)
    codigo_empresa_asignar_cartera = models.IntegerField()
    carga_inicial = models.CharField(max_length=1)
    codigo_cargo = models.IntegerField()
    cliente_ubicado_si_no = models.CharField(max_length=1, blank=True, null=True)
    cliente_ubicado_por = models.CharField(max_length=30, blank=True, null=True)
    cnu_cod_etapa = models.BooleanField(blank=True, null=True)
    cnu_empresa = models.IntegerField(blank=True, null=True)
    fecha_actualizacion_cod_etapa = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_cabecera_clientes_cobrador'
        unique_together = (('codigo_comprobante', 'tipo_comprobante', 'periodo', 'codigo_call_center', 'codigo_cargo', 'codigo_empresa'),)


class CcCabeceraVerificacionesPoc(models.Model):
    codigo_comprobante = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    tipo_persona = models.BooleanField()
    codigo_empresa = models.IntegerField()
    fecha_sol_ver_campo = models.DateField(blank=True, null=True)
    usuario_sol_ver_campo = models.ForeignKey(AdUsuarios, models.DO_NOTHING, db_column='usuario_sol_ver_campo', blank=True, null=True)
    fecha_ver_campo = models.DateField(blank=True, null=True)
    usuario_ver_campo = models.ForeignKey(AdUsuarios, models.DO_NOTHING, db_column='usuario_ver_campo', blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    puntos_extras = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    concepto = models.CharField(max_length=100, blank=True, null=True)
    es_puntos_extras = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_cabecera_verificaciones_poc'
        unique_together = (('codigo_comprobante', 'tipo_comprobante', 'tipo_persona', 'codigo_empresa'),)


class CcCalificaciones(models.Model):
    codigo_edad_mora = models.OneToOneField('CcEdadMora', models.DO_NOTHING, db_column='codigo_edad_mora', primary_key=True)
    codigo_calificacion = models.CharField(max_length=1)
    codigo_buro = models.ForeignKey('CcEdadMora', models.DO_NOTHING, db_column='codigo_buro')
    codigo_empresa = models.ForeignKey('CcEdadMora', models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=100)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_calificaciones'
        unique_together = (('codigo_edad_mora', 'codigo_calificacion', 'codigo_buro', 'codigo_empresa'),)


class CcCallCenter(models.Model):
    codigo_call_center = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_usuario_a_gestionar = models.ForeignKey(AdUsuarios, models.DO_NOTHING, db_column='codigo_usuario_a_gestionar', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_call_center'


class CcCallCenterVentas(models.Model):
    codigo_call_center = models.IntegerField(primary_key=True)
    codigo_empresa = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_call_center_ventas'
        unique_together = (('codigo_call_center', 'codigo_empresa'),)


class CcCambiarEstadoCuotasPlano(models.Model):
    cod_comprobante = models.CharField(max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    codigo_empresa = models.IntegerField()
    cod_estado_cuota = models.CharField(max_length=3)
    id_servidor = models.CharField(max_length=3)
    periodo = models.IntegerField()
    codigo_agencia = models.IntegerField(blank=True, null=True)
    observacion = models.CharField(max_length=2000, blank=True, null=True)
    estado = models.CharField(max_length=1)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_cambiar_estado_cuotas_plano'


class CcCampanias(models.Model):
    codigo_campania = models.IntegerField(primary_key=True)
    codigo_area = models.ForeignKey(CcAreaGestiones, models.DO_NOTHING, db_column='codigo_area')
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=100)
    anulado = models.CharField(max_length=1)
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    campania_cerrada_abierta = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_grupo_mail = models.ForeignKey(AdGruposMails, models.DO_NOTHING, db_column='codigo_grupo_mail', blank=True, null=True)
    es_rotativa = models.CharField(max_length=1, blank=True, null=True)
    celular_si_no = models.CharField(max_length=1, blank=True, null=True)
    total_clientes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_campanias'
        unique_together = (('codigo_campania', 'codigo_area', 'codigo_empresa'),)


class CcCampaniasCallcenterC(models.Model):
    numero_campania = models.IntegerField(primary_key=True)
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=300)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    tipo_campania = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cc_campanias_callcenter_c'
        unique_together = (('numero_campania', 'tipo_campania', 'codigo_empresa'),)


class CcCampaniasCallcenterD(models.Model):
    cod_comprobante = models.CharField(primary_key=True, max_length=9)
    numero_campania = models.IntegerField()
    periodo = models.IntegerField()
    codigo_call_center = models.IntegerField()
    tipo_comprobante = models.CharField(max_length=2)
    codigo_empresa = models.IntegerField()
    id_servidor = models.CharField(max_length=3)
    cod_tipo_persona = models.CharField(max_length=3)
    cod_persona = models.CharField(max_length=14)
    identificacion_cobrador_act = models.CharField(max_length=20)
    identificacion_cobrador_ori = models.CharField(max_length=20)
    codigo_segmento_cartera = models.IntegerField(blank=True, null=True)
    codigo_agencia = models.IntegerField()
    saldo_asignado = models.DecimalField(max_digits=18, decimal_places=2)
    tipo_campania = models.CharField(max_length=1)
    fecha_volver_a_llamar = models.DateField(blank=True, null=True)
    fecha_compromiso_pago = models.DateField(blank=True, null=True)
    dia_vencimiento = models.IntegerField(blank=True, null=True)
    carga_inicial = models.CharField(max_length=1)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    cliente_ubicado_si_no = models.CharField(max_length=1, blank=True, null=True)
    cliente_ubicado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_actualizacion_cod_etapa = models.DateField(blank=True, null=True)
    cnu_cod_etapa = models.BooleanField(blank=True, null=True)
    cnu_empresa = models.IntegerField(blank=True, null=True)
    cod_origen = models.CharField(max_length=50, blank=True, null=True)
    codigo_prioridad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_campanias_callcenter_d'
        unique_together = (('cod_comprobante', 'numero_campania', 'periodo', 'codigo_call_center', 'tipo_comprobante', 'tipo_campania', 'codigo_empresa'),)


class CcCampaniasCobranzas(models.Model):
    numero_campania = models.IntegerField(primary_key=True)
    telefono = models.CharField(max_length=20)
    cod_comprobante = models.CharField(max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    id_servidor = models.CharField(max_length=3)
    codigo_empresa = models.IntegerField()
    codigo_tipo_persona = models.CharField(max_length=3)
    codigo_persona = models.CharField(max_length=14)
    periodo = models.IntegerField()
    fecha_carga_informacion = models.DateField()
    codigo_persona_encr = models.CharField(max_length=30)
    enviado_a_mysql = models.CharField(max_length=1)
    monto_asignado = models.DecimalField(max_digits=18, decimal_places=2)
    saldo_actual = models.DecimalField(max_digits=18, decimal_places=2)
    call_result = models.CharField(max_length=30, blank=True, null=True)
    duracion_llamada_segundos = models.IntegerField(blank=True, null=True)
    fecha_llamada = models.DateField(blank=True, null=True)
    acc_codigo_agencia = models.IntegerField(blank=True, null=True)
    acc_codigo_call_center = models.IntegerField(blank=True, null=True)
    acc_codigo_empresa = models.IntegerField(blank=True, null=True)
    cliente_llamado_si_no = models.CharField(max_length=1)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    celular_si_no = models.CharField(max_length=1)
    numero_campania_eventual = models.IntegerField(blank=True, null=True)
    vigente_si_no = models.CharField(max_length=1)
    telefono_es_del_cli_gar_ref = models.CharField(max_length=1, blank=True, null=True)
    fecha_volver_a_llamar = models.DateField(blank=True, null=True)
    tipo_telefono = models.CharField(max_length=2)
    dias_atrasados = models.IntegerField()
    cancelar_parte_entera = models.BigIntegerField()
    cancelar_parte_decimal = models.IntegerField()
    dias_plazo_a_cancelar = models.IntegerField()
    nombres = models.CharField(max_length=300)
    fecha_vencimiento_mas_antiguo = models.DateField(blank=True, null=True)
    trunk = models.CharField(max_length=500, blank=True, null=True)
    nombres_ref_gar = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_campanias_cobranzas'
        unique_together = (('numero_campania', 'telefono', 'cod_comprobante', 'tipo_comprobante', 'id_servidor', 'codigo_empresa'),)


class CcCancelacionesXAplicar(models.Model):
    numero_cancelacion_manual = models.CharField(primary_key=True, max_length=9)
    tipo_cancelacion = models.CharField(max_length=2)
    codigo_empresa = models.IntegerField()
    cod_comprobante = models.CharField(max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    identificacion_cobrador = models.CharField(max_length=20)
    cod_persona = models.CharField(max_length=14)
    cod_tipo_persona = models.CharField(max_length=3)
    codigo_agencia_comprobante = models.IntegerField()
    codigo_agencia_caja = models.IntegerField()
    fecha_cobro = models.DateField()
    capital_cobrado = models.DecimalField(max_digits=18, decimal_places=2)
    interes_mora_cobrado = models.DecimalField(max_digits=18, decimal_places=2)
    gasto_cobranza_cobrado = models.DecimalField(max_digits=18, decimal_places=2)
    banco = models.CharField(max_length=50, blank=True, null=True)
    numero_cheque = models.CharField(max_length=20, blank=True, null=True)
    numero_cuenta_corriente = models.CharField(max_length=20, blank=True, null=True)
    numero_cancelacion_st_can = models.CharField(max_length=9, blank=True, null=True)
    tipo_cancelacion_st_can = models.CharField(max_length=2, blank=True, null=True)
    numero_anticipo_st_ant = models.CharField(max_length=9, blank=True, null=True)
    tipo_anticipo_st_ant = models.CharField(max_length=2, blank=True, null=True)
    documento_impreso = models.CharField(max_length=1)
    documento_impreso_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_impresion_documento = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=1)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_cancelaciones_x_aplicar'
        unique_together = (('numero_cancelacion_manual', 'tipo_cancelacion', 'codigo_empresa'),)


class CcCartasClientes(models.Model):
    codigo_carta = models.CharField(primary_key=True, max_length=10)
    encabezado = models.CharField(max_length=500)
    cuerpo = models.CharField(max_length=3000)
    pie = models.CharField(max_length=500)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    codigo_tipo_gestion = models.CharField(max_length=10, blank=True, null=True)
    codigo_area = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_cartas_clientes'


class CcCarteraResumen(models.Model):
    periodo = models.IntegerField(primary_key=True)
    cod_politica = models.IntegerField()
    cod_parroquia = models.CharField(max_length=12)
    cod_zona = models.CharField(max_length=3)
    cod_agencia = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='cod_agencia')
    cod_empresa = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='cod_empresa')
    aniomes_vencimiento = models.IntegerField()
    valor_vencimiento = models.DecimalField(max_digits=14, decimal_places=2)
    saldo_vencimiento = models.DecimalField(max_digits=14, decimal_places=2)
    saldo_vencido = models.DecimalField(max_digits=14, decimal_places=2)
    saldo_x_vencer = models.DecimalField(max_digits=14, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    cod_modelo = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'cc_cartera_resumen'
        unique_together = (('periodo', 'aniomes_vencimiento', 'cod_politica', 'cod_zona', 'cod_parroquia', 'cod_modelo', 'cod_agencia', 'cod_empresa'),)


class CcClientesALlamar(models.Model):
    periodo = models.IntegerField()
    telefono = models.CharField(max_length=20)
    codigo_persona = models.CharField(max_length=14)
    codigo_tipo_persona = models.CharField(max_length=3)
    codigo_agencia = models.IntegerField()
    codigo_empresa = models.IntegerField()
    codigo_persona_encr = models.CharField(max_length=30)
    record_status = models.CharField(max_length=30)
    enviado_a_mysql = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    anulado = models.CharField(max_length=1)
    numero_carga = models.IntegerField(primary_key=True)
    cod_comprobante = models.CharField(max_length=9, blank=True, null=True)
    tipo_comprobante = models.CharField(max_length=2, blank=True, null=True)
    codigo_empresa_comprobante = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_clientes_a_llamar'
        unique_together = (('numero_carga', 'fecha_adicion', 'periodo', 'telefono', 'codigo_persona', 'codigo_tipo_persona', 'codigo_agencia', 'codigo_empresa'),)


class CcClientesALlamarCopy(models.Model):
    periodo = models.IntegerField()
    telefono = models.CharField(max_length=20)
    codigo_persona = models.CharField(max_length=14)
    codigo_tipo_persona = models.CharField(max_length=3)
    codigo_agencia = models.IntegerField()
    codigo_empresa = models.IntegerField()
    codigo_persona_encr = models.CharField(max_length=30)
    record_status = models.CharField(max_length=30)
    enviado_a_mysql = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    anulado = models.CharField(max_length=1)
    numero_carga = models.IntegerField()
    cod_comprobante = models.CharField(max_length=9, blank=True, null=True)
    tipo_comprobante = models.CharField(max_length=2, blank=True, null=True)
    codigo_empresa_comprobante = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_clientes_a_llamar_copy'


class CcClientesGestionarTelefon(models.Model):
    cod_comprobante = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    codigo_periodo_gestion = models.IntegerField()
    codigo_area_tipo_gestion = models.IntegerField()
    codigo_area = models.IntegerField()
    codigo_empresa = models.IntegerField()
    identificacion_telefonista_ori = models.CharField(max_length=20)
    codigo_area_tipo_gestion_ori = models.IntegerField()
    codigo_area_ori = models.IntegerField()
    identificacion_telefonista_act = models.CharField(max_length=20)
    codigo_area_tipo_gestion_act = models.IntegerField()
    codigo_area_act = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_persona = models.CharField(max_length=14)
    codigo_tipo_persona = models.CharField(max_length=3)
    fecha_comprobante = models.DateField()
    codigo_agencia = models.IntegerField()
    codigo_call_center = models.IntegerField()
    codigo_call_center_ori = models.IntegerField()
    codigo_call_center_act = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cc_clientes_gestionar_telefon'
        unique_together = (('cod_comprobante', 'tipo_comprobante', 'codigo_periodo_gestion', 'codigo_area_tipo_gestion', 'codigo_area', 'codigo_call_center', 'codigo_empresa'),)


class CcClientesNoAsignados(models.Model):
    codigo_comprobante = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    codigo_empresa = models.IntegerField()
    periodo = models.IntegerField()
    codigo_persona = models.CharField(max_length=14)
    codigo_agencia = models.IntegerField(blank=True, null=True)
    error = models.CharField(max_length=2000, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_clientes_no_asignados'
        unique_together = (('codigo_comprobante', 'tipo_comprobante', 'codigo_empresa', 'periodo'),)


class CcCobradoresXInstituciones(models.Model):
    identificacion_cobrador = models.OneToOneField('RhEmpleados', models.DO_NOTHING, db_column='identificacion_cobrador', primary_key=True)
    cod_institucion = models.CharField(max_length=14)
    codigo_empresa = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_cobradores_x_instituciones'
        unique_together = (('identificacion_cobrador', 'cod_institucion', 'codigo_empresa'),)


class CcCobrosNoAplicadosCel(models.Model):
    codigo_call_center = models.ForeignKey(CcCallCenter, models.DO_NOTHING, db_column='codigo_call_center')
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    registro = models.CharField(max_length=4000, blank=True, null=True)
    tipo_archivo = models.CharField(max_length=15)
    error = models.CharField(max_length=4000)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_cobros_no_aplicados_cel'


class CcComprACargarEnCampanias(models.Model):
    numero_comprobante_campania = models.IntegerField(primary_key=True)
    cod_comprobante = models.CharField(max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    id_servidor = models.CharField(max_length=3)
    codigo_empresa = models.IntegerField()
    periodo = models.IntegerField()
    codigo_agencia = models.IntegerField()
    codigo_call_center = models.IntegerField()
    numero_campania = models.IntegerField(blank=True, null=True)
    observacion = models.CharField(max_length=500, blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    nombre_campania = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_compr_a_cargar_en_campanias'
        unique_together = (('numero_comprobante_campania', 'cod_comprobante', 'tipo_comprobante', 'id_servidor', 'codigo_empresa'),)


class CcComprobantesCampania(models.Model):
    codigo_comprobante = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    codigo_empresa = models.IntegerField()
    codigo_campania = models.IntegerField()
    codigo_area = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    valor = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    agencia = models.IntegerField(blank=True, null=True)
    cod_tipo_persona = models.CharField(max_length=3, blank=True, null=True)
    cod_persona = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_comprobantes_campania'
        unique_together = (('codigo_comprobante', 'tipo_comprobante', 'codigo_empresa'),)


class CcComprobantesProcSieXPla(models.Model):
    cod_comprobante = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    codigo_agencia = models.IntegerField()
    codigo_canton = models.CharField(max_length=4)
    codigo_provincia = models.CharField(max_length=6)
    codigo_region = models.IntegerField()
    codigo_politica = models.IntegerField()
    codigo_nacion = models.IntegerField()
    codigo_empresa = models.IntegerField()
    periodo_cierre = models.IntegerField()
    plazo = models.IntegerField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_comprobantes_proc_sie_x_pla'
        unique_together = (('cod_comprobante', 'tipo_comprobante', 'codigo_agencia', 'codigo_canton', 'codigo_provincia', 'codigo_region', 'codigo_politica', 'codigo_nacion', 'codigo_empresa'),)


class CcComprobantesProcesadosSie(models.Model):
    cod_comprobante = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    codigo_agencia = models.IntegerField()
    codigo_canton = models.CharField(max_length=4)
    codigo_provincia = models.CharField(max_length=6)
    codigo_region = models.IntegerField()
    codigo_politica = models.IntegerField()
    codigo_nacion = models.IntegerField()
    codigo_empresa = models.IntegerField()
    periodo_cierre = models.IntegerField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_comprobantes_procesados_sie'
        unique_together = (('cod_comprobante', 'tipo_comprobante', 'codigo_agencia', 'codigo_canton', 'codigo_provincia', 'codigo_region', 'codigo_politica', 'codigo_nacion', 'codigo_empresa'),)


class CcComprobantesRecaudadoras(models.Model):
    codigo_comprobante = models.OneToOneField(CcCabeceraClientesCobrador, models.DO_NOTHING, db_column='codigo_comprobante', primary_key=True)
    tipo_comprobante = models.ForeignKey(CcCabeceraClientesCobrador, models.DO_NOTHING, db_column='tipo_comprobante')
    codigo_empresa = models.ForeignKey(CcCabeceraClientesCobrador, models.DO_NOTHING, db_column='codigo_empresa')
    periodo = models.ForeignKey(CcCabeceraClientesCobrador, models.DO_NOTHING, db_column='periodo')
    identificacion_cobrador = models.CharField(max_length=20)
    codigo_item = models.CharField(max_length=3)
    codigo_segmento_cartera = models.IntegerField()
    codigo_empresa_asignar_cartera = models.IntegerField()
    codigo_modelo = models.CharField(max_length=8)
    codigo_call_center = models.ForeignKey(CcCabeceraClientesCobrador, models.DO_NOTHING, db_column='codigo_call_center')
    codigo_agencia = models.IntegerField()
    cuenta_cancelada = models.CharField(max_length=1)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    cod_tipo_identificacion = models.IntegerField()
    cod_cliente = models.CharField(max_length=14)
    codigo_cargo = models.ForeignKey(CcCabeceraClientesCobrador, models.DO_NOTHING, db_column='codigo_cargo')

    class Meta:
        managed = False
        db_table = 'cc_comprobantes_recaudadoras'
        unique_together = (('codigo_comprobante', 'tipo_comprobante', 'codigo_empresa'),)


class CcCreditosAnalizar(models.Model):
    codigo_comprobante = models.OneToOneField(CcCabeceraClientesCobrador, models.DO_NOTHING, db_column='codigo_comprobante', primary_key=True)
    tipo_comprobante = models.ForeignKey(CcCabeceraClientesCobrador, models.DO_NOTHING, db_column='tipo_comprobante')
    periodo = models.ForeignKey(CcCabeceraClientesCobrador, models.DO_NOTHING, db_column='periodo')
    codigo_call_center = models.ForeignKey(CcCabeceraClientesCobrador, models.DO_NOTHING, db_column='codigo_call_center')
    codigo_empresa = models.ForeignKey(CcCabeceraClientesCobrador, models.DO_NOTHING, db_column='codigo_empresa')
    codigo_usuario_a_gestionar = models.ForeignKey(AdUsuarios, models.DO_NOTHING, db_column='codigo_usuario_a_gestionar')
    scc_identificacion_cobrador = models.ForeignKey('CcSegmentosCarterasCobrad', models.DO_NOTHING, db_column='scc_identificacion_cobrador', blank=True, null=True)
    scc_codigo_item = models.ForeignKey('CcSegmentosCarterasCobrad', models.DO_NOTHING, db_column='scc_codigo_item', blank=True, null=True)
    scc_codigo_segmento_cartera = models.ForeignKey('CcSegmentosCarterasCobrad', models.DO_NOTHING, db_column='scc_codigo_segmento_cartera', blank=True, null=True)
    scc_codigo_modelo = models.ForeignKey('CcSegmentosCarterasCobrad', models.DO_NOTHING, db_column='scc_codigo_modelo', blank=True, null=True)
    scc_codigo_call_center = models.ForeignKey('CcSegmentosCarterasCobrad', models.DO_NOTHING, db_column='scc_codigo_call_center', blank=True, null=True)
    scc_codigo_empresa = models.ForeignKey('CcSegmentosCarterasCobrad', models.DO_NOTHING, db_column='scc_codigo_empresa', blank=True, null=True)
    observacion = models.CharField(max_length=300, blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_empresa_asignar_cartera = models.ForeignKey('CcSegmentosCarterasCobrad', models.DO_NOTHING, db_column='codigo_empresa_asignar_cartera')
    codigo_cargo = models.ForeignKey(CcCabeceraClientesCobrador, models.DO_NOTHING, db_column='codigo_cargo')

    class Meta:
        managed = False
        db_table = 'cc_creditos_analizar'
        unique_together = (('codigo_comprobante', 'tipo_comprobante', 'periodo', 'codigo_call_center', 'codigo_cargo', 'codigo_empresa'),)


class CcCupoOpcionalCampanias(models.Model):
    cod_cliente = models.CharField(max_length=14, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    cupo = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_cupo_opcional_campanias'


class CcDatcredExcepClientes(models.Model):
    codigo_empresa = models.OneToOneField(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa', primary_key=True)
    identificacion = models.CharField(max_length=14)
    nombre = models.CharField(max_length=200)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_datcred_excep_clientes'
        unique_together = (('codigo_empresa', 'identificacion'),)


class CcDatcredExcepEstCuota(models.Model):
    codigo_empresa = models.OneToOneField(AdBuros, models.DO_NOTHING, db_column='codigo_empresa', primary_key=True)
    cod_estado_cuota = models.CharField(max_length=3)
    codigo_buro = models.ForeignKey(AdBuros, models.DO_NOTHING, db_column='codigo_buro')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_datcred_excep_est_cuota'
        unique_together = (('codigo_empresa', 'cod_estado_cuota', 'codigo_buro'),)


class CcDatcredExcepPolit(models.Model):
    codigo_empresa = models.OneToOneField(AdBuros, models.DO_NOTHING, db_column='codigo_empresa', primary_key=True)
    codigo_politica = models.IntegerField()
    codigo_buro = models.ForeignKey(AdBuros, models.DO_NOTHING, db_column='codigo_buro')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_datcred_excep_polit'
        unique_together = (('codigo_empresa', 'codigo_politica', 'codigo_buro'),)


class CcDetalleClientesAsignados(models.Model):
    numero_vencimiento = models.IntegerField(primary_key=True)
    codigo_comprobante = models.ForeignKey(CcCabeceraClientesAsignados, models.DO_NOTHING, db_column='codigo_comprobante')
    tipo_comprobante = models.ForeignKey(CcCabeceraClientesAsignados, models.DO_NOTHING, db_column='tipo_comprobante')
    codigo_forma_pago = models.CharField(max_length=3)
    periodo = models.ForeignKey(CcCabeceraClientesAsignados, models.DO_NOTHING, db_column='periodo')
    codigo_call_center = models.ForeignKey('CcSegmentosCarterasTelefon', models.DO_NOTHING, db_column='codigo_call_center')
    codigo_empresa = models.ForeignKey(CcCabeceraClientesAsignados, models.DO_NOTHING, db_column='codigo_empresa')
    identificacion_telefonista_act = models.ForeignKey('CcSegmentosCarterasTelefon', models.DO_NOTHING, db_column='identificacion_telefonista_act')
    codigo_segmento_cartera_act = models.ForeignKey('CcSegmentosCarterasTelefon', models.DO_NOTHING, db_column='codigo_segmento_cartera_act')
    codigo_call_center_act = models.ForeignKey('CcSegmentosCarterasTelefon', models.DO_NOTHING, db_column='codigo_call_center_act')
    identificacion_telefonista = models.ForeignKey('CcSegmentosCarterasTelefon', models.DO_NOTHING, db_column='identificacion_telefonista')
    codigo_segmento_cartera = models.ForeignKey('CcSegmentosCarterasTelefon', models.DO_NOTHING, db_column='codigo_segmento_cartera')
    fecha_vencimiento = models.DateField()
    saldo_cuota = models.DecimalField(max_digits=14, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_detalle_clientes_asignados'
        unique_together = (('numero_vencimiento', 'codigo_comprobante', 'tipo_comprobante', 'codigo_forma_pago', 'periodo', 'codigo_call_center', 'codigo_empresa'),)


class CcDetalleClientesCobrador(models.Model):
    numero_vencimiento = models.IntegerField(primary_key=True)
    codigo_comprobante = models.ForeignKey(CcCabeceraClientesCobrador, models.DO_NOTHING, db_column='codigo_comprobante')
    tipo_comprobante = models.ForeignKey(CcCabeceraClientesCobrador, models.DO_NOTHING, db_column='tipo_comprobante')
    codigo_forma_pago = models.CharField(max_length=3)
    periodo = models.ForeignKey(CcCabeceraClientesCobrador, models.DO_NOTHING, db_column='periodo')
    codigo_call_center = models.ForeignKey(CcCabeceraClientesCobrador, models.DO_NOTHING, db_column='codigo_call_center')
    codigo_empresa = models.ForeignKey(CcCabeceraClientesCobrador, models.DO_NOTHING, db_column='codigo_empresa')
    identificacion_cobrador_act = models.ForeignKey('CcSegmentosCarterasCobrad', models.DO_NOTHING, db_column='identificacion_cobrador_act')
    codigo_segmento_cartera_act = models.ForeignKey('CcSegmentosCarterasCobrad', models.DO_NOTHING, db_column='codigo_segmento_cartera_act')
    codigo_call_center_act = models.ForeignKey('CcSegmentosCarterasCobrad', models.DO_NOTHING, db_column='codigo_call_center_act')
    identificacion_cobrador_ori = models.ForeignKey('CcSegmentosCarterasCobrad', models.DO_NOTHING, db_column='identificacion_cobrador_ori')
    codigo_segmento_cartera_ori = models.ForeignKey('CcSegmentosCarterasCobrad', models.DO_NOTHING, db_column='codigo_segmento_cartera_ori')
    fecha_vencimiento = models.DateField()
    saldo_cuota = models.DecimalField(max_digits=14, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_item_ori = models.ForeignKey('CcSegmentosCarterasCobrad', models.DO_NOTHING, db_column='codigo_item_ori')
    codigo_modelo_ori = models.ForeignKey('CcSegmentosCarterasCobrad', models.DO_NOTHING, db_column='codigo_modelo_ori')
    codigo_item_act = models.ForeignKey('CcSegmentosCarterasCobrad', models.DO_NOTHING, db_column='codigo_item_act')
    codigo_modelo_act = models.ForeignKey('CcSegmentosCarterasCobrad', models.DO_NOTHING, db_column='codigo_modelo_act')
    codigo_agencia = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_agencia')
    codigo_empresa_asignar_cartera = models.ForeignKey('CcSegmentosCarterasCobrad', models.DO_NOTHING, db_column='codigo_empresa_asignar_cartera')
    carga_inicial = models.CharField(max_length=1)
    codigo_cargo = models.ForeignKey(CcCabeceraClientesCobrador, models.DO_NOTHING, db_column='codigo_cargo')
    cliente_ubicado_si_no = models.CharField(max_length=1, blank=True, null=True)
    cliente_ubicado_por = models.CharField(max_length=30, blank=True, null=True)
    cnu_cod_etapa = models.BooleanField(blank=True, null=True)
    cnu_empresa = models.IntegerField(blank=True, null=True)
    fecha_actualizacion_cod_etapa = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_detalle_clientes_cobrador'
        unique_together = (('numero_vencimiento', 'codigo_comprobante', 'tipo_comprobante', 'codigo_forma_pago', 'periodo', 'codigo_call_center', 'codigo_cargo', 'codigo_empresa'),)


class CcDetallePreguntasCampanias(models.Model):
    codigo_respuesta = models.IntegerField(primary_key=True)
    codigo_tipo_respuesta = models.ForeignKey('CcPreguntasCampanias', models.DO_NOTHING, db_column='codigo_tipo_respuesta')
    codigo_pregunta_campania = models.ForeignKey('CcPreguntasCampanias', models.DO_NOTHING, db_column='codigo_pregunta_campania')
    codigo_campania = models.ForeignKey('CcPreguntasCampanias', models.DO_NOTHING, db_column='codigo_campania')
    codigo_area = models.ForeignKey('CcPreguntasCampanias', models.DO_NOTHING, db_column='codigo_area')
    codigo_empresa = models.ForeignKey('CcPreguntasCampanias', models.DO_NOTHING, db_column='codigo_empresa')
    codigo_pregunta_campania_sig = models.ForeignKey('CcPreguntasCampanias', models.DO_NOTHING, db_column='codigo_pregunta_campania_sig', blank=True, null=True)
    codigo_tipo_respuesta_sig = models.ForeignKey('CcPreguntasCampanias', models.DO_NOTHING, db_column='codigo_tipo_respuesta_sig', blank=True, null=True)
    codigo_campania_sig = models.ForeignKey('CcPreguntasCampanias', models.DO_NOTHING, db_column='codigo_campania_sig', blank=True, null=True)
    codigo_area_sig = models.ForeignKey('CcPreguntasCampanias', models.DO_NOTHING, db_column='codigo_area_sig', blank=True, null=True)
    codigo_empresa_sig = models.ForeignKey('CcPreguntasCampanias', models.DO_NOTHING, db_column='codigo_empresa_sig', blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_pregunta_campania_ant = models.ForeignKey('CcPreguntasCampanias', models.DO_NOTHING, db_column='codigo_pregunta_campania_ant', blank=True, null=True)
    codigo_tipo_respuesta_ant = models.ForeignKey('CcPreguntasCampanias', models.DO_NOTHING, db_column='codigo_tipo_respuesta_ant', blank=True, null=True)
    codigo_campania_ant = models.ForeignKey('CcPreguntasCampanias', models.DO_NOTHING, db_column='codigo_campania_ant', blank=True, null=True)
    codigo_area_ant = models.ForeignKey('CcPreguntasCampanias', models.DO_NOTHING, db_column='codigo_area_ant', blank=True, null=True)
    codigo_empresa_ant = models.ForeignKey('CcPreguntasCampanias', models.DO_NOTHING, db_column='codigo_empresa_ant', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_detalle_preguntas_campanias'
        unique_together = (('codigo_respuesta', 'codigo_tipo_respuesta', 'codigo_pregunta_campania', 'codigo_campania', 'codigo_area', 'codigo_empresa'),)


class CcDetalleVerificacionesPoc(models.Model):
    codigo_comprobante = models.OneToOneField(CcCabeceraVerificacionesPoc, models.DO_NOTHING, db_column='codigo_comprobante', primary_key=True)
    tipo_comprobante = models.ForeignKey(CcCabeceraVerificacionesPoc, models.DO_NOTHING, db_column='tipo_comprobante')
    codigo_tipo_verificacion_peso = models.ForeignKey('CcTiposVerificacionesPesos', models.DO_NOTHING, db_column='codigo_tipo_verificacion_peso')
    codigo_tipo_verificacion = models.ForeignKey('CcTiposVerificacionesPesos', models.DO_NOTHING, db_column='codigo_tipo_verificacion')
    tipo_persona = models.ForeignKey(CcCabeceraVerificacionesPoc, models.DO_NOTHING, db_column='tipo_persona')
    codigo_empresa = models.ForeignKey('CcTiposVerificacionesPesos', models.DO_NOTHING, db_column='codigo_empresa')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    concepto = models.CharField(max_length=100, blank=True, null=True)
    secuencia = models.ForeignKey('CcTiposVerificacionesPesos', models.DO_NOTHING, db_column='secuencia')
    codigo_verificacion = models.ForeignKey('CcTiposVerificacionesPesos', models.DO_NOTHING, db_column='codigo_verificacion')

    class Meta:
        managed = False
        db_table = 'cc_detalle_verificaciones_poc'
        unique_together = (('codigo_comprobante', 'tipo_comprobante', 'codigo_tipo_verificacion_peso', 'codigo_tipo_verificacion', 'tipo_persona', 'codigo_verificacion', 'secuencia', 'codigo_empresa'),)


class CcDocumentosHojaRutaXCobr(models.Model):
    numero_documento = models.BigIntegerField(primary_key=True)
    identificacion_cobrador = models.ForeignKey('RhEmpleados', models.DO_NOTHING, db_column='identificacion_cobrador')
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    nombre_archivo_enviado = models.CharField(max_length=1000)
    estado = models.CharField(max_length=1)
    enviado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_envio = models.DateField(blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_documentos_hoja_ruta_x_cobr'
        unique_together = (('numero_documento', 'identificacion_cobrador', 'codigo_empresa'),)


class CcEdadMora(models.Model):
    codigo_edad_mora = models.IntegerField(primary_key=True)
    codigo_buro = models.ForeignKey(AdBuros, models.DO_NOTHING, db_column='codigo_buro')
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=30)
    dias_mora_inicial = models.IntegerField(blank=True, null=True)
    dias_mora_final = models.IntegerField(blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_edad_mora'
        unique_together = (('codigo_edad_mora', 'codigo_buro', 'codigo_empresa'),)


class CcEmpresasAsignarCarteras(models.Model):
    codigo_empresa_asignar_cartera = models.IntegerField(primary_key=True)
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=200)
    rec_identificacion = models.ForeignKey('CcRecaudadoras', models.DO_NOTHING, db_column='rec_identificacion', blank=True, null=True)
    rec_codigo_empresa = models.ForeignKey('CcRecaudadoras', models.DO_NOTHING, db_column='rec_codigo_empresa', blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    cartera_propia_si_no = models.CharField(max_length=1)
    codigo_jaher = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_empresas_asignar_carteras'
        unique_together = (('codigo_empresa_asignar_cartera', 'codigo_empresa'),)


class CcEnviarCancelacionesInst(models.Model):
    numero_envio = models.BigIntegerField(primary_key=True)
    cod_institucion = models.CharField(max_length=14)
    codigo_empresa = models.IntegerField()
    cod_persona = models.CharField(max_length=14)
    cod_tipo_persona = models.CharField(max_length=3)
    cod_comprobante = models.CharField(max_length=9, blank=True, null=True)
    tipo_comprobante = models.CharField(max_length=2, blank=True, null=True)
    cuotas_gratis = models.DecimalField(max_digits=4, decimal_places=2)
    valor_archivo = models.DecimalField(max_digits=18, decimal_places=2)
    valor_aplicar = models.DecimalField(max_digits=18, decimal_places=2)
    porcentaje_comision = models.DecimalField(max_digits=6, decimal_places=3)
    valor_comision = models.DecimalField(max_digits=18, decimal_places=2)
    codigo_agencia = models.IntegerField(blank=True, null=True)
    fecha_envio = models.DateField(blank=True, null=True)
    enviado_por = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=1)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_enviar_cancelaciones_inst'
        unique_together = (('numero_envio', 'cod_institucion', 'codigo_empresa'),)


class CcEnviarDatacredito(models.Model):
    periodo = models.IntegerField(primary_key=True)
    codigo_buro = models.ForeignKey(AdBuros, models.DO_NOTHING, db_column='codigo_buro')
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    codigo_credito = models.CharField(max_length=18)
    identificacion = models.CharField(max_length=13)
    nombre_completo = models.CharField(max_length=60)
    fecha_nacimiento = models.IntegerField()
    fecha_apertura = models.IntegerField()
    fecha_vencimiento = models.IntegerField()
    valor_cuota = models.IntegerField()
    novedad = models.IntegerField()
    adjetivo = models.IntegerField()
    tipo_identificacion = models.BooleanField()
    valor_inicial = models.IntegerField()
    valor_saldo_deuda = models.IntegerField()
    valor_saldo_mora = models.IntegerField()
    tipo_de_moneda = models.BooleanField()
    tipo_de_obligacion = models.BooleanField()
    tipo_de_garantia = models.BooleanField()
    calificacion = models.CharField(max_length=1, blank=True, null=True)
    ciudad_residencia = models.CharField(max_length=20)
    direccion_residencia = models.CharField(max_length=300)
    telefono_residencia = models.CharField(max_length=15)
    ciudad_laboral = models.CharField(max_length=20)
    telefono_laboral = models.CharField(max_length=15, blank=True, null=True)
    ciudad_correspondencia = models.CharField(max_length=20, blank=True, null=True)
    direccion_correspondencia = models.CharField(max_length=300, blank=True, null=True)
    ciiu = models.IntegerField(blank=True, null=True)
    total_cuotas = models.IntegerField()
    cuotas_canceladas = models.IntegerField()
    cuotas_en_mora = models.IntegerField()
    fecha_de_pago = models.IntegerField()
    oficina_radicacion = models.CharField(max_length=15)
    ciudad_de_radicacion = models.CharField(max_length=20)
    forma_de_pago = models.BooleanField()
    periodicidad_de_pago = models.BooleanField()
    edad_de_mora = models.IntegerField()
    fecha_de_actualizacion = models.IntegerField()
    marca_de_autorizacion = models.BooleanField()
    garante = models.IntegerField()
    anulado = models.CharField(max_length=1)
    enviado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_enviar_datacredito'
        unique_together = (('periodo', 'codigo_buro', 'codigo_empresa', 'codigo_credito', 'identificacion'),)


class CcErrorTelefonosClientes(models.Model):
    telefono = models.CharField(primary_key=True, max_length=15)
    cod_persona = models.CharField(max_length=14)
    periodo = models.ForeignKey('CcPeriodosCobradores', models.DO_NOTHING, db_column='periodo')
    codigo_call_center = models.ForeignKey('CcPeriodosCobradores', models.DO_NOTHING, db_column='codigo_call_center')
    cod_tipo_persona = models.CharField(max_length=3)
    codigo_empresa = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_empresa')
    codigo_agencia = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_agencia')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    identificacion_jefe_inmediato = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_error_telefonos_clientes'
        unique_together = (('telefono', 'cod_persona', 'periodo', 'codigo_call_center', 'cod_tipo_persona', 'codigo_empresa'),)


class CcEstadisticasCancelaciones(models.Model):
    cod_comprobante = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    periodo_cierre = models.IntegerField()
    cartera = models.CharField(max_length=3)
    codigo_agencia = models.IntegerField()
    codigo_empresa = models.IntegerField()
    nombre_agencia = models.CharField(max_length=100)
    codigo_persona = models.CharField(max_length=14)
    codigo_tipo_persona = models.CharField(max_length=3)
    apellidos_nombres_cliente = models.CharField(max_length=300)
    codigo_call_center = models.IntegerField()
    nombre_call_center = models.CharField(max_length=100)
    dias_minimo_cobro = models.DecimalField(max_digits=10, decimal_places=2)
    dias_maximo_cobro = models.DecimalField(max_digits=10, decimal_places=2)
    dias_promedio_cobro = models.DecimalField(max_digits=10, decimal_places=2)
    dias_minimo_entre_cobros = models.DecimalField(max_digits=10, decimal_places=2)
    dias_maximo_entre_cobros = models.DecimalField(max_digits=10, decimal_places=2)
    dias_promedio_entre_cobros = models.DecimalField(max_digits=10, decimal_places=2)
    total_gestiones_call_center = models.IntegerField()
    total_gestiones_positivas_call = models.IntegerField()
    total_gestiones_cobrad_verif = models.IntegerField()
    valor_cancelado_desde = models.DecimalField(max_digits=10, decimal_places=2)
    total_cuotas_cancelad_desde = models.IntegerField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    id_servidor = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'cc_estadisticas_cancelaciones'
        unique_together = (('cod_comprobante', 'tipo_comprobante', 'periodo_cierre', 'cartera', 'codigo_agencia', 'codigo_empresa'),)


class CcEventosRealizados(models.Model):
    secuencia = models.IntegerField(primary_key=True)
    identificacion_telefonista = models.ForeignKey('RhEmpleados', models.DO_NOTHING, db_column='identificacion_telefonista')
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    fecha_hora_inicial = models.DateField()
    fecha_hora_final = models.DateField(blank=True, null=True)
    codigo_tipo_evento = models.ForeignKey(AdTiposEventos, models.DO_NOTHING, db_column='codigo_tipo_evento')
    pct_codigo_cliente = models.ForeignKey('CcPersonasCampaniasTelefon', models.DO_NOTHING, db_column='pct_codigo_cliente', blank=True, null=True)
    pct_codigo_campania = models.ForeignKey('CcPersonasCampaniasTelefon', models.DO_NOTHING, db_column='pct_codigo_campania', blank=True, null=True)
    pct_codigo_area = models.ForeignKey('CcPersonasCampaniasTelefon', models.DO_NOTHING, db_column='pct_codigo_area', blank=True, null=True)
    pct_codigo_empresa = models.ForeignKey('CcPersonasCampaniasTelefon', models.DO_NOTHING, db_column='pct_codigo_empresa', blank=True, null=True)
    cca_codigo_comprobante = models.ForeignKey(CcCabeceraClientesAsignados, models.DO_NOTHING, db_column='cca_codigo_comprobante', blank=True, null=True)
    cca_tipo_comprobante = models.ForeignKey(CcCabeceraClientesAsignados, models.DO_NOTHING, db_column='cca_tipo_comprobante', blank=True, null=True)
    cca_periodo = models.ForeignKey(CcCabeceraClientesAsignados, models.DO_NOTHING, db_column='cca_periodo', blank=True, null=True)
    cca_codigo_call_center = models.ForeignKey(CcCabeceraClientesAsignados, models.DO_NOTHING, db_column='cca_codigo_call_center', blank=True, null=True)
    cca_codigo_empresa = models.ForeignKey(CcCabeceraClientesAsignados, models.DO_NOTHING, db_column='cca_codigo_empresa', blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_eventos_realizados'
        unique_together = (('secuencia', 'identificacion_telefonista', 'codigo_empresa'),)


class CcEventosRealizadosRota(models.Model):
    secuencia = models.IntegerField(primary_key=True)
    identificacion_telefonista = models.ForeignKey('RhEmpleados', models.DO_NOTHING, db_column='identificacion_telefonista')
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    fecha_hora_inicial = models.DateField()
    fecha_hora_final = models.DateField(blank=True, null=True)
    codigo_tipo_evento = models.ForeignKey(AdTiposEventos, models.DO_NOTHING, db_column='codigo_tipo_evento')
    pct_secuencia = models.ForeignKey('CcPersonasCampaniasTeleRot', models.DO_NOTHING, db_column='pct_secuencia', blank=True, null=True)
    pct_codigo_cliente = models.ForeignKey('CcPersonasCampaniasTeleRot', models.DO_NOTHING, db_column='pct_codigo_cliente', blank=True, null=True)
    pct_codigo_campania = models.ForeignKey('CcPersonasCampaniasTeleRot', models.DO_NOTHING, db_column='pct_codigo_campania', blank=True, null=True)
    pct_codigo_area = models.ForeignKey('CcPersonasCampaniasTeleRot', models.DO_NOTHING, db_column='pct_codigo_area', blank=True, null=True)
    pct_codigo_empresa = models.ForeignKey('CcPersonasCampaniasTeleRot', models.DO_NOTHING, db_column='pct_codigo_empresa', blank=True, null=True)
    cca_codigo_comprobante = models.ForeignKey(CcCabeceraClientesAsignados, models.DO_NOTHING, db_column='cca_codigo_comprobante', blank=True, null=True)
    cca_tipo_comprobante = models.ForeignKey(CcCabeceraClientesAsignados, models.DO_NOTHING, db_column='cca_tipo_comprobante', blank=True, null=True)
    cca_periodo = models.ForeignKey(CcCabeceraClientesAsignados, models.DO_NOTHING, db_column='cca_periodo', blank=True, null=True)
    cca_codigo_call_center = models.ForeignKey(CcCabeceraClientesAsignados, models.DO_NOTHING, db_column='cca_codigo_call_center', blank=True, null=True)
    cca_codigo_empresa = models.ForeignKey(CcCabeceraClientesAsignados, models.DO_NOTHING, db_column='cca_codigo_empresa', blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_eventos_realizados_rota'
        unique_together = (('secuencia', 'identificacion_telefonista', 'codigo_empresa'),)


class CcFlujoCorriente(models.Model):
    periodo = models.IntegerField(primary_key=True)
    fecha_vencimiento = models.DateField()
    codigo_agencia = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_agencia')
    codigo_canton = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_canton')
    codigo_provincia = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_provincia')
    codigo_region = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_region')
    codigo_politica = models.IntegerField()
    cod_modelo_cat_linea = models.CharField(max_length=8)
    cod_item_cat_linea = models.CharField(max_length=3)
    cod_marca = models.IntegerField()
    cod_cat_cliente = models.CharField(max_length=8)
    es_empleado = models.CharField(max_length=100)
    codigo_nacion = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_nacion')
    codigo_empresa = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_empresa')
    nombre_agencia = models.CharField(max_length=50)
    nombre_canton = models.CharField(max_length=50)
    nombre_provincia = models.CharField(max_length=100)
    nombre_region = models.CharField(max_length=300)
    nombre_linea = models.CharField(max_length=50)
    nombre_marca = models.CharField(max_length=50)
    nombre_politica = models.CharField(max_length=100)
    nombre_categoria_cliente = models.CharField(max_length=30)
    valor_vencimiento = models.DecimalField(max_digits=30, decimal_places=2)
    saldo_vencimiento = models.DecimalField(max_digits=30, decimal_places=2)
    cobro_vencimiento = models.DecimalField(max_digits=30, decimal_places=2)
    cobro_efectivo_vencimiento = models.DecimalField(max_digits=30, decimal_places=2)
    porcentaje_vencimiento = models.DecimalField(max_digits=20, decimal_places=5)
    mes_cerrado = models.CharField(max_length=1)
    fecha_ult_ejecucion = models.DateField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_flujo_corriente'
        unique_together = (('periodo', 'fecha_vencimiento', 'codigo_agencia', 'codigo_canton', 'codigo_provincia', 'codigo_region', 'codigo_politica', 'cod_modelo_cat_linea', 'cod_item_cat_linea', 'cod_marca', 'cod_cat_cliente', 'es_empleado', 'codigo_nacion', 'codigo_empresa'),)


class CcFormaDePago(models.Model):
    codigo_forma_pago = models.IntegerField(primary_key=True)
    codigo_buro = models.ForeignKey(AdBuros, models.DO_NOTHING, db_column='codigo_buro')
    codigo_empresa = models.ForeignKey(AdBuros, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=100)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_forma_de_pago'
        unique_together = (('codigo_forma_pago', 'codigo_buro', 'codigo_empresa'),)


class CcHistoricoVentasVencimien(models.Model):
    secuencia = models.BigIntegerField(blank=True, null=True)
    aniomes_vencimiento = models.IntegerField()
    aniomes_venta = models.IntegerField()
    periodo = models.IntegerField()
    saldo_vencimiento = models.DecimalField(max_digits=18, decimal_places=2)
    valor_vencimiento = models.DecimalField(max_digits=18, decimal_places=2)
    saldo_vencido = models.DecimalField(max_digits=18, decimal_places=2)
    saldo_x_vencer = models.DecimalField(max_digits=18, decimal_places=2)
    valor_venta = models.DecimalField(max_digits=18, decimal_places=2)
    valor_venta_consolidado = models.DecimalField(max_digits=18, decimal_places=2)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_agencia = models.IntegerField()
    codigo_parroquia = models.CharField(max_length=14, blank=True, null=True)
    codigo_politica = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_historico_ventas_vencimien'


class CcIndiceDeMorosidad(models.Model):
    periodo = models.IntegerField(primary_key=True)
    anio_mes_venta = models.IntegerField()
    codigo_agencia = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_agencia')
    codigo_canton = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_canton')
    codigo_provincia = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_provincia')
    codigo_region = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_region')
    codigo_politica = models.IntegerField()
    cod_modelo_cat_linea = models.CharField(max_length=8)
    cod_item_cat_linea = models.CharField(max_length=3)
    cod_marca = models.IntegerField()
    codigo_nacion = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_nacion')
    codigo_empresa = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_empresa')
    nombre_agencia = models.CharField(max_length=50)
    nombre_canton = models.CharField(max_length=50)
    nombre_provincia = models.CharField(max_length=100)
    nombre_region = models.CharField(max_length=300)
    nombre_linea = models.CharField(max_length=50)
    nombre_marca = models.CharField(max_length=50)
    nombre_politica = models.CharField(max_length=100)
    valor_ventas = models.DecimalField(max_digits=30, decimal_places=2)
    saldo_cartera = models.DecimalField(max_digits=30, decimal_places=2)
    total_cartera_al_cierre = models.DecimalField(max_digits=30, decimal_places=2)
    valor_cobrado = models.DecimalField(max_digits=30, decimal_places=2)
    cartera_vencida = models.DecimalField(max_digits=30, decimal_places=2)
    porcentaje_productividad = models.DecimalField(max_digits=20, decimal_places=5)
    porcentaje_indice_morosidad = models.DecimalField(max_digits=20, decimal_places=5)
    pagos_anticipados = models.DecimalField(max_digits=30, decimal_places=2)
    mes_cerrado = models.CharField(max_length=1)
    fecha_ult_ejecucion = models.DateField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_indice_de_morosidad'
        unique_together = (('periodo', 'anio_mes_venta', 'codigo_agencia', 'codigo_canton', 'codigo_provincia', 'codigo_region', 'codigo_politica', 'cod_modelo_cat_linea', 'cod_item_cat_linea', 'cod_marca', 'codigo_nacion', 'codigo_empresa'),)


class CcIndiceDeMorosidadXPlazo(models.Model):
    periodo = models.IntegerField(primary_key=True)
    anio_mes_venta = models.IntegerField()
    plazo = models.IntegerField()
    codigo_agencia = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_agencia')
    codigo_canton = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_canton')
    codigo_provincia = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_provincia')
    codigo_region = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_region')
    codigo_politica = models.IntegerField()
    cod_modelo_cat_linea = models.CharField(max_length=8)
    cod_item_cat_linea = models.CharField(max_length=3)
    cod_marca = models.IntegerField()
    codigo_nacion = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_nacion')
    codigo_empresa = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_empresa')
    nombre_agencia = models.CharField(max_length=50)
    nombre_canton = models.CharField(max_length=50)
    nombre_provincia = models.CharField(max_length=100)
    nombre_region = models.CharField(max_length=300)
    nombre_linea = models.CharField(max_length=50)
    nombre_marca = models.CharField(max_length=50)
    nombre_politica = models.CharField(max_length=100)
    valor_ventas = models.DecimalField(max_digits=30, decimal_places=2)
    saldo_cartera = models.DecimalField(max_digits=30, decimal_places=2)
    total_cartera_al_cierre = models.DecimalField(max_digits=30, decimal_places=2)
    valor_cobrado = models.DecimalField(max_digits=30, decimal_places=2)
    cartera_vencida = models.DecimalField(max_digits=30, decimal_places=2)
    porcentaje_productividad = models.DecimalField(max_digits=20, decimal_places=5)
    porcentaje_indice_morosidad = models.DecimalField(max_digits=20, decimal_places=5)
    pagos_anticipados = models.DecimalField(max_digits=30, decimal_places=2)
    mes_cerrado = models.CharField(max_length=1)
    fecha_ult_ejecucion = models.DateField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_indice_de_morosidad_x_plazo'
        unique_together = (('periodo', 'anio_mes_venta', 'plazo', 'codigo_agencia', 'codigo_canton', 'codigo_provincia', 'codigo_region', 'codigo_politica', 'cod_modelo_cat_linea', 'cod_item_cat_linea', 'cod_marca', 'codigo_nacion', 'codigo_empresa'),)


class CcIndiceRecupXTipoGestor(models.Model):
    periodo = models.IntegerField(primary_key=True)
    codigo_call_center = models.ForeignKey(CcCallCenter, models.DO_NOTHING, db_column='codigo_call_center')
    codigo_segmento_cartera = models.IntegerField()
    codigo_canton = models.CharField(max_length=4)
    codigo_provincia = models.CharField(max_length=6)
    codigo_region = models.IntegerField()
    codigo_nacion = models.IntegerField()
    codigo_empresa = models.IntegerField()
    nombre_call_center = models.CharField(max_length=100)
    nombre_canton = models.CharField(max_length=50)
    nombre_provincia = models.CharField(max_length=100)
    nombre_region = models.CharField(max_length=300)
    nombre_segmento_cartera = models.CharField(max_length=100, blank=True, null=True)
    creditos_sin_gestion = models.IntegerField()
    cobro_efectivo_sin_gestion = models.DecimalField(max_digits=30, decimal_places=2)
    creditos_gestion_call_center = models.IntegerField()
    cobro_efectivo_gestion_cal_cen = models.DecimalField(max_digits=30, decimal_places=2)
    creditos_gestion_cobrador = models.IntegerField()
    cobro_efectivo_gestion_cobrad = models.DecimalField(max_digits=30, decimal_places=2)
    creditos_gestion_cal_cob = models.IntegerField()
    cobro_efectivo_gestion_cal_cob = models.DecimalField(max_digits=30, decimal_places=2)
    creditos_total = models.IntegerField()
    cobro_efectivo_total = models.DecimalField(max_digits=30, decimal_places=2)
    mes_cerrado = models.CharField(max_length=1)
    fecha_ult_ejecucion = models.DateField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_indice_recup_x_tipo_gestor'
        unique_together = (('periodo', 'codigo_call_center', 'codigo_segmento_cartera', 'codigo_canton', 'codigo_provincia', 'codigo_region', 'codigo_nacion', 'codigo_empresa'),)


class CcJefesCobrador(models.Model):
    identificacion = models.OneToOneField('RhEmpleados', models.DO_NOTHING, db_column='identificacion', primary_key=True)
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    identificacion_jefe_inmediato = models.ForeignKey('self', models.DO_NOTHING, db_column='identificacion_jefe_inmediato', blank=True, null=True)
    codigo_empresa_jefe_inmediato = models.ForeignKey('self', models.DO_NOTHING, db_column='codigo_empresa_jefe_inmediato', blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_jefes_cobrador'
        unique_together = (('identificacion', 'codigo_empresa'),)


class CcLineasIntangibles(models.Model):
    nombre_columna_balance = models.CharField(primary_key=True, max_length=30)
    empresa = models.IntegerField()
    cod_modelo = models.CharField(max_length=8)
    cod_item = models.CharField(max_length=3)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_lineas_intangibles'
        unique_together = (('nombre_columna_balance', 'empresa'),)


class CcMenXPolXZonOriginal(models.Model):
    periodo_cierre = models.IntegerField(primary_key=True)
    codigo_agencia = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_agencia')
    codigo_politica = models.IntegerField()
    cartera = models.CharField(max_length=3)
    codigo_empresa = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_empresa')
    fecha_inicio_mes = models.DateField()
    fecha_fin_mes = models.DateField()
    valor_mes_actual_vencido = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_29_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_28_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_27_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_26_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_25_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_24_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_23_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_22_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_21_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_20_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_19_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_18_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_17_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_16_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_15_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_14_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_13_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_12_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_11_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_10_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_09_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_08_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_07_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_06_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_05_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_04_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_03_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_02_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_01_mes = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_01_mes = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_02_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_03_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_04_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_05_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_06_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_07_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_08_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_09_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_10_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_11_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_12_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_mas_12_meses = models.DecimalField(max_digits=14, decimal_places=2)
    interes_mora_generado = models.DecimalField(max_digits=14, decimal_places=2)
    interes_mora_abonado = models.DecimalField(max_digits=14, decimal_places=2)
    gasto_cobranza_generado = models.DecimalField(max_digits=14, decimal_places=2)
    gasto_cobranza_abonado = models.DecimalField(max_digits=14, decimal_places=2)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    historial_credit_mes_cierre = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    historial_credit_30_dias_atr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    historial_credit_60_dias_atr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    historial_credit_90_dias_atr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    historial_credit_180_dias_atr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    historial_credit_360_dias_atr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_men_x_pol_x_zon_original'
        unique_together = (('periodo_cierre', 'codigo_agencia', 'codigo_politica', 'cartera', 'codigo_empresa'),)


class CcMensajesCobrarIntMorGto(models.Model):
    fecha_envio = models.DateField(primary_key=True)
    cod_comprobante = models.CharField(max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    codigo_empresa = models.IntegerField()
    cod_persona = models.CharField(max_length=14)
    cod_tipo_persona = models.CharField(max_length=3)
    fecha_recepcion = models.DateField()
    celular_cobrador = models.CharField(max_length=10)
    identificacion_cobrador = models.CharField(max_length=14)
    interes_mora_a_cobrar = models.DecimalField(max_digits=18, decimal_places=2)
    gasto_cobranza_a_cobrar = models.DecimalField(max_digits=18, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_mensajes_cobrar_int_mor_gto'
        unique_together = (('fecha_envio', 'cod_comprobante', 'tipo_comprobante', 'codigo_empresa'),)


class CcMensuales(models.Model):
    periodo_cierre = models.IntegerField(primary_key=True)
    codigo_agencia = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_agencia')
    cartera = models.CharField(max_length=3)
    codigo_empresa = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_empresa')
    fecha_inicio_mes = models.DateField()
    fecha_fin_mes = models.DateField()
    valor_mes_actual_vencido = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_29_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_28_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_27_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_26_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_25_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_24_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_23_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_22_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_21_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_20_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_19_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_18_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_17_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_16_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_15_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_14_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_13_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_12_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_11_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_10_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_09_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_08_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_07_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_06_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_05_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_04_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_03_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_02_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_01_mes = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_01_mes = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_02_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_03_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_04_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_05_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_06_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_07_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_08_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_09_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_10_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_11_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_12_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_mas_12_meses = models.DecimalField(max_digits=14, decimal_places=2)
    interes_mora_generado = models.DecimalField(max_digits=14, decimal_places=2)
    interes_mora_abonado = models.DecimalField(max_digits=14, decimal_places=2)
    gasto_cobranza_generado = models.DecimalField(max_digits=14, decimal_places=2)
    gasto_cobranza_abonado = models.DecimalField(max_digits=14, decimal_places=2)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_mensuales'
        unique_together = (('periodo_cierre', 'codigo_agencia', 'cartera', 'codigo_empresa'),)


class CcMensualesXPoliticaXZona(models.Model):
    periodo_cierre = models.IntegerField(primary_key=True)
    codigo_agencia = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_agencia')
    codigo_politica = models.IntegerField()
    cartera = models.CharField(max_length=3)
    codigo_empresa = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_empresa')
    fecha_inicio_mes = models.DateField()
    fecha_fin_mes = models.DateField()
    valor_mes_actual_vencido = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_29_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_28_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_27_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_26_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_25_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_24_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_23_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_22_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_21_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_20_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_19_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_18_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_17_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_16_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_15_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_14_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_13_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_12_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_11_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_10_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_09_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_08_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_07_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_06_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_05_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_04_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_03_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_02_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_01_mes = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_01_mes = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_02_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_03_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_04_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_05_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_06_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_07_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_08_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_09_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_10_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_11_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_12_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_mas_12_meses = models.DecimalField(max_digits=14, decimal_places=2)
    interes_mora_generado = models.DecimalField(max_digits=14, decimal_places=2)
    interes_mora_abonado = models.DecimalField(max_digits=14, decimal_places=2)
    gasto_cobranza_generado = models.DecimalField(max_digits=14, decimal_places=2)
    gasto_cobranza_abonado = models.DecimalField(max_digits=14, decimal_places=2)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    historial_credit_mes_cierre = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    historial_credit_30_dias_atr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    historial_credit_60_dias_atr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    historial_credit_90_dias_atr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    historial_credit_180_dias_atr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    historial_credit_360_dias_atr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    historial_credit_120_dias_atr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    historial_credit_150_dias_atr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    historial_credit_210_dias_atr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    historial_credit_240_dias_atr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    historial_credit_270_dias_atr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    historial_credit_300_dias_atr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    historial_credit_330_dias_atr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    historial_credit_mas_360_dias = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_mensuales_x_politica_x_zona'
        unique_together = (('periodo_cierre', 'codigo_agencia', 'codigo_politica', 'cartera', 'codigo_empresa'),)


class CcMovGestOtros(models.Model):
    secuencia = models.IntegerField(primary_key=True)
    codigo_comprobante = models.CharField(max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    codigo_empresa = models.IntegerField()
    codigo_tipo_gestion = models.CharField(max_length=10)
    codigo_area = models.IntegerField()
    codigo_tipo_persona = models.CharField(max_length=3)
    codigo_persona = models.CharField(max_length=14)
    tipo_mayor_detalle = models.CharField(max_length=1)
    fecha_compromiso_pago = models.DateField(blank=True, null=True)
    observaciones = models.CharField(max_length=4000, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_usuario_gestion = models.CharField(max_length=30)
    cod_tipo_persona_age_anterior = models.CharField(max_length=3, blank=True, null=True)
    cod_persona_age_anterior = models.CharField(max_length=14, blank=True, null=True)
    fecha_transaccion = models.DateField()
    calificacion = models.IntegerField(blank=True, null=True)
    solicitud = models.CharField(max_length=9, blank=True, null=True)
    codigo_empresa_age_anterior = models.IntegerField(blank=True, null=True)
    fecha_volver_a_llamar = models.DateField(blank=True, null=True)
    telefono_a_llamar = models.CharField(max_length=15, blank=True, null=True)
    telefono_es_del_cli_gar_ref = models.CharField(max_length=1, blank=True, null=True)
    es_efectivo = models.BooleanField(blank=True, null=True)
    es_cliente_ubicado = models.BooleanField(blank=True, null=True)
    telefono_localizado = models.CharField(max_length=15, blank=True, null=True)
    codigo_tipo_contacto = models.CharField(max_length=3, blank=True, null=True)
    telefono_contacto = models.CharField(max_length=15, blank=True, null=True)
    tct_codigo_tipo_contacto = models.IntegerField(blank=True, null=True)
    tct_codigo_empresa = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_mov_gest_otros'
        unique_together = (('secuencia', 'codigo_comprobante', 'tipo_comprobante', 'codigo_empresa'),)


class CcMovimientosGestiones(models.Model):
    secuencia = models.IntegerField(primary_key=True)
    codigo_comprobante = models.CharField(max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    codigo_empresa = models.IntegerField()
    codigo_tipo_gestion = models.CharField(max_length=10)
    codigo_area = models.IntegerField()
    codigo_tipo_persona = models.CharField(max_length=3)
    codigo_persona = models.CharField(max_length=14)
    tipo_mayor_detalle = models.CharField(max_length=1)
    fecha_compromiso_pago = models.DateField(blank=True, null=True)
    observaciones = models.CharField(max_length=4000, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_usuario_gestion = models.CharField(max_length=30)
    cod_tipo_persona_age_anterior = models.CharField(max_length=3, blank=True, null=True)
    cod_persona_age_anterior = models.CharField(max_length=14, blank=True, null=True)
    fecha_transaccion = models.DateField()
    calificacion = models.IntegerField(blank=True, null=True)
    solicitud = models.CharField(max_length=9, blank=True, null=True)
    codigo_empresa_age_anterior = models.IntegerField(blank=True, null=True)
    fecha_volver_a_llamar = models.DateField(blank=True, null=True)
    telefono_a_llamar = models.CharField(max_length=15, blank=True, null=True)
    telefono_es_del_cli_gar_ref = models.CharField(max_length=1, blank=True, null=True)
    es_efectivo = models.BooleanField(blank=True, null=True)
    es_cliente_ubicado = models.BooleanField(blank=True, null=True)
    telefono_localizado = models.CharField(max_length=15, blank=True, null=True)
    codigo_tipo_contacto = models.CharField(max_length=3, blank=True, null=True)
    telefono_contacto = models.CharField(max_length=15, blank=True, null=True)
    tct_codigo_tipo_contacto = models.IntegerField(blank=True, null=True)
    tct_codigo_empresa = models.IntegerField(blank=True, null=True)
    tiempo_gestion = models.IntegerField(blank=True, null=True)
    valor_cobrado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    num_comprobante = models.CharField(max_length=20, blank=True, null=True)
    latitud_ges = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitud_ges = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    contacto_ges = models.CharField(max_length=50, blank=True, null=True)
    porc_bateria_ges = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_movimientos_gestiones'
        unique_together = (('secuencia', 'codigo_comprobante', 'tipo_comprobante', 'codigo_empresa'),)


class CcNivelesGestiones(models.Model):
    codigo_nivel = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    numero_caracteres = models.IntegerField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_niveles_gestiones'


class CcNovedadesObligaciones(models.Model):
    codigo_edad_mora = models.OneToOneField(CcEdadMora, models.DO_NOTHING, db_column='codigo_edad_mora', primary_key=True)
    codigo_novedad_obligacion = models.IntegerField()
    codigo_buro = models.ForeignKey(CcEdadMora, models.DO_NOTHING, db_column='codigo_buro')
    codigo_empresa = models.ForeignKey(CcEdadMora, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=100)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_novedades_obligaciones'
        unique_together = (('codigo_edad_mora', 'codigo_novedad_obligacion', 'codigo_buro', 'codigo_empresa'),)


class CcParametrosGenerales(models.Model):
    codigo_agencia = models.OneToOneField(AdAgencias, models.DO_NOTHING, db_column='codigo_agencia', primary_key=True)
    codigo_empresa = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_empresa')
    ultimo_cierre_balance = models.IntegerField()
    activo = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_parametros_generales'
        unique_together = (('codigo_agencia', 'codigo_empresa'),)


class CcPeriodosCallCenter(models.Model):
    periodo = models.IntegerField(primary_key=True)
    codigo_call_center = models.ForeignKey(CcCallCenter, models.DO_NOTHING, db_column='codigo_call_center')
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_periodos_call_center'
        unique_together = (('periodo', 'codigo_call_center'),)


class CcPeriodosCerrados(models.Model):
    periodo_cierre = models.IntegerField(primary_key=True)
    codigo_agencia = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_agencia')
    codigo_empresa = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_empresa')
    cartera = models.CharField(max_length=3)
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_periodos_cerrados'
        unique_together = (('periodo_cierre', 'codigo_agencia', 'codigo_empresa', 'cartera'),)


class CcPeriodosCobradores(models.Model):
    periodo = models.IntegerField(primary_key=True)
    codigo_call_center = models.ForeignKey(CcCallCenter, models.DO_NOTHING, db_column='codigo_call_center')
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_periodos_cobradores'
        unique_together = (('periodo', 'codigo_call_center'),)


class CcPeriodosEjecutarCierres(models.Model):
    periodo_cierre = models.IntegerField(primary_key=True)
    codigo_empresa = models.ForeignKey('CcTiposCarteras', models.DO_NOTHING, db_column='codigo_empresa')
    cartera = models.ForeignKey('CcTiposCarteras', models.DO_NOTHING, db_column='cartera')
    codigo_proceso = models.ForeignKey('CcProcesos', models.DO_NOTHING, db_column='codigo_proceso')
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    estado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_periodos_ejecutar_cierres'
        unique_together = (('periodo_cierre', 'codigo_empresa', 'cartera', 'codigo_proceso'),)


class CcPeriodosGestiones(models.Model):
    codigo_periodo_gestion = models.IntegerField(primary_key=True)
    codigo_area_tipo_gestion = models.ForeignKey(CcAreaTiposGestiones, models.DO_NOTHING, db_column='codigo_area_tipo_gestion')
    codigo_area = models.ForeignKey(CcAreaTiposGestiones, models.DO_NOTHING, db_column='codigo_area')
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_call_center = models.ForeignKey(CcAreaTiposGestiones, models.DO_NOTHING, db_column='codigo_call_center')

    class Meta:
        managed = False
        db_table = 'cc_periodos_gestiones'
        unique_together = (('codigo_periodo_gestion', 'codigo_area_tipo_gestion', 'codigo_area', 'codigo_call_center', 'codigo_empresa'),)


class CcPersonasCampaniasTeleRot(models.Model):
    secuencia = models.IntegerField(primary_key=True)
    codigo_cliente = models.CharField(max_length=14)
    codigo_campania = models.ForeignKey('CcTelefonistasCampanias', models.DO_NOTHING, db_column='codigo_campania')
    codigo_area = models.ForeignKey('CcTelefonistasCampanias', models.DO_NOTHING, db_column='codigo_area')
    codigo_empresa = models.ForeignKey('CcTelefonistasCampanias', models.DO_NOTHING, db_column='codigo_empresa')
    identificacion_telefonista_act = models.ForeignKey('CcTelefonistasCampanias', models.DO_NOTHING, db_column='identificacion_telefonista_act')
    identificacion_telefonista_ori = models.ForeignKey('CcTelefonistasCampanias', models.DO_NOTHING, db_column='identificacion_telefonista_ori')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    cod_origen_cliente = models.CharField(max_length=2, blank=True, null=True)
    row_id = models.CharField(max_length=50, blank=True, null=True)
    verificacion_campo = models.CharField(max_length=50, blank=True, null=True)
    cod_agencia_cliente = models.IntegerField(blank=True, null=True)
    call_result = models.CharField(max_length=30, blank=True, null=True)
    duracion_llamada = models.IntegerField(blank=True, null=True)
    fecha_llamada = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_personas_campanias_tele_rot'
        unique_together = (('secuencia', 'codigo_cliente', 'codigo_campania', 'codigo_area', 'codigo_empresa'),)


class CcPersonasCampaniasTelefon(models.Model):
    codigo_cliente = models.CharField(primary_key=True, max_length=14)
    codigo_campania = models.ForeignKey('CcTelefonistasCampanias', models.DO_NOTHING, db_column='codigo_campania')
    codigo_area = models.ForeignKey('CcTelefonistasCampanias', models.DO_NOTHING, db_column='codigo_area')
    codigo_empresa = models.ForeignKey('CcTelefonistasCampanias', models.DO_NOTHING, db_column='codigo_empresa')
    identificacion_telefonista_act = models.ForeignKey('CcTelefonistasCampanias', models.DO_NOTHING, db_column='identificacion_telefonista_act')
    identificacion_telefonista_ori = models.ForeignKey('CcTelefonistasCampanias', models.DO_NOTHING, db_column='identificacion_telefonista_ori')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    cod_origen_cliente = models.CharField(max_length=2, blank=True, null=True)
    row_id = models.CharField(max_length=50, blank=True, null=True)
    verificacion_campo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_personas_campanias_telefon'
        unique_together = (('codigo_cliente', 'codigo_campania', 'codigo_area', 'codigo_empresa'),)


class CcPoliticasCredCallCenter(models.Model):
    codigo_politica = models.IntegerField(primary_key=True)
    codigo_empresa = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_politicas_cred_call_center'
        unique_together = (('codigo_politica', 'codigo_empresa'),)


class CcPoliticasCredCobradInsti(models.Model):
    codigo_politica = models.IntegerField(primary_key=True)
    codigo_empresa = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_politicas_cred_cobrad_insti'
        unique_together = (('codigo_politica', 'codigo_empresa'),)


class CcPoliticasCredCobradores(models.Model):
    codigo_politica = models.IntegerField(primary_key=True)
    codigo_empresa = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_politicas_cred_cobradores'
        unique_together = (('codigo_politica', 'codigo_empresa'),)


class CcPorcBaseCalculoXCobrad(models.Model):
    identificacion_cobrador = models.OneToOneField('RhEmpleados', models.DO_NOTHING, db_column='identificacion_cobrador', primary_key=True)
    codigo_segmento_cartera = models.ForeignKey('CcPorcBaseCalculoXSegmen', models.DO_NOTHING, db_column='codigo_segmento_cartera')
    codigo_call_center = models.ForeignKey('CcPorcBaseCalculoXSegmen', models.DO_NOTHING, db_column='codigo_call_center')
    codigo_empresa = models.ForeignKey('CcPorcBaseCalculoXSegmen', models.DO_NOTHING, db_column='codigo_empresa')
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_porc_base_calculo_x_cobrad'
        unique_together = (('identificacion_cobrador', 'codigo_segmento_cartera', 'codigo_call_center', 'codigo_empresa'),)


class CcPorcBaseCalculoXSegmen(models.Model):
    codigo_segmento_cartera = models.OneToOneField('CcSegmentosDeCarteras', models.DO_NOTHING, db_column='codigo_segmento_cartera', primary_key=True)
    codigo_call_center = models.ForeignKey(CcCallCenter, models.DO_NOTHING, db_column='codigo_call_center')
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_porc_base_calculo_x_segmen'
        unique_together = (('codigo_segmento_cartera', 'codigo_call_center', 'codigo_empresa'),)


class CcPreguntasCampanias(models.Model):
    codigo_pregunta_campania = models.IntegerField(primary_key=True)
    codigo_tipo_respuesta = models.ForeignKey('CcTiposRespuestas', models.DO_NOTHING, db_column='codigo_tipo_respuesta')
    codigo_campania = models.IntegerField()
    codigo_area = models.IntegerField()
    codigo_empresa = models.ForeignKey('CcTiposRespuestas', models.DO_NOTHING, db_column='codigo_empresa')
    pregunta = models.CharField(max_length=4000)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    pregunta_raiz_si_no = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_preguntas_campanias'
        unique_together = (('codigo_pregunta_campania', 'codigo_tipo_respuesta', 'codigo_campania', 'codigo_area', 'codigo_empresa'),)


class CcPrimerasCuotas(models.Model):
    periodo = models.IntegerField(primary_key=True)
    fecha_vencimiento_pri_cuo = models.DateField()
    codigo_agencia = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_agencia')
    codigo_canton = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_canton')
    codigo_provincia = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_provincia')
    codigo_region = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_region')
    codigo_politica = models.IntegerField()
    cod_modelo_cat_linea = models.CharField(max_length=8)
    cod_item_cat_linea = models.CharField(max_length=3)
    cod_marca = models.IntegerField()
    cod_cat_cliente = models.CharField(max_length=8)
    es_empleado = models.CharField(max_length=100)
    codigo_nacion = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_nacion')
    codigo_empresa = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_empresa')
    nombre_agencia = models.CharField(max_length=50)
    nombre_canton = models.CharField(max_length=50)
    nombre_provincia = models.CharField(max_length=100)
    nombre_region = models.CharField(max_length=300)
    nombre_linea = models.CharField(max_length=50)
    nombre_marca = models.CharField(max_length=50)
    nombre_categoria_cliente = models.CharField(max_length=30)
    nombre_politica = models.CharField(max_length=100)
    valor_primeras_cuotas = models.DecimalField(max_digits=30, decimal_places=2)
    saldo_primeras_cuotas = models.DecimalField(max_digits=30, decimal_places=2)
    cobro_primeras_cuotas = models.DecimalField(max_digits=30, decimal_places=2)
    cobro_efectivo_pri_cuo = models.DecimalField(max_digits=30, decimal_places=2)
    porcentaje_primeras_cuotas = models.DecimalField(max_digits=20, decimal_places=5)
    mes_cerrado = models.CharField(max_length=1)
    fecha_ult_ejecucion = models.DateField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_primeras_cuotas'
        unique_together = (('periodo', 'fecha_vencimiento_pri_cuo', 'codigo_agencia', 'codigo_canton', 'codigo_provincia', 'codigo_region', 'codigo_politica', 'cod_modelo_cat_linea', 'cod_item_cat_linea', 'cod_marca', 'cod_cat_cliente', 'es_empleado', 'codigo_nacion', 'codigo_empresa'),)


class CcPrioridadesCallCenter(models.Model):
    codigo_prioridad = models.IntegerField(primary_key=True)
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=200)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_prioridades_call_center'
        unique_together = (('codigo_prioridad', 'codigo_empresa'),)


class CcProcesos(models.Model):
    codigo_proceso = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=250)
    estado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_procesos'


class CcProducMesPresentePuntual(models.Model):
    periodo = models.IntegerField(primary_key=True)
    fecha_vencimiento = models.DateField()
    codigo_agencia = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_agencia')
    codigo_canton = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_canton')
    codigo_provincia = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_provincia')
    codigo_region = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_region')
    codigo_politica = models.IntegerField()
    cod_modelo_cat_linea = models.CharField(max_length=8)
    cod_item_cat_linea = models.CharField(max_length=3)
    cod_marca = models.IntegerField()
    cod_cat_cliente = models.CharField(max_length=8)
    es_empleado = models.CharField(max_length=100)
    codigo_nacion = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_nacion')
    codigo_empresa = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_empresa')
    nombre_agencia = models.CharField(max_length=50)
    nombre_canton = models.CharField(max_length=50)
    nombre_provincia = models.CharField(max_length=100)
    nombre_region = models.CharField(max_length=300)
    nombre_linea = models.CharField(max_length=50)
    nombre_marca = models.CharField(max_length=50)
    nombre_categoria_cliente = models.CharField(max_length=30)
    nombre_politica = models.CharField(max_length=100)
    valor_vencimiento = models.DecimalField(max_digits=30, decimal_places=2)
    saldo_vencimiento = models.DecimalField(max_digits=30, decimal_places=2)
    cobro_vencimiento = models.DecimalField(max_digits=30, decimal_places=2)
    cobro_efectivo_vencimiento = models.DecimalField(max_digits=30, decimal_places=2)
    porcentaje_vencimiento = models.DecimalField(max_digits=20, decimal_places=5)
    mes_cerrado = models.CharField(max_length=1)
    fecha_ult_ejecucion = models.DateField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_produc_mes_presente_puntual'
        unique_together = (('periodo', 'fecha_vencimiento', 'codigo_agencia', 'codigo_canton', 'codigo_provincia', 'codigo_region', 'codigo_politica', 'cod_modelo_cat_linea', 'cod_item_cat_linea', 'cod_marca', 'cod_cat_cliente', 'es_empleado', 'codigo_nacion', 'codigo_empresa'),)


class CcProducMesPresenteTotal(models.Model):
    periodo = models.IntegerField(primary_key=True)
    fecha_vencimiento = models.DateField()
    codigo_agencia = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_agencia')
    codigo_canton = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_canton')
    codigo_provincia = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_provincia')
    codigo_region = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_region')
    codigo_politica = models.IntegerField()
    cod_modelo_cat_linea = models.CharField(max_length=8)
    cod_item_cat_linea = models.CharField(max_length=3)
    cod_marca = models.IntegerField()
    cod_cat_cliente = models.CharField(max_length=8)
    es_empleado = models.CharField(max_length=100)
    codigo_nacion = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_nacion')
    codigo_empresa = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_empresa')
    nombre_agencia = models.CharField(max_length=50)
    nombre_canton = models.CharField(max_length=50)
    nombre_provincia = models.CharField(max_length=100)
    nombre_region = models.CharField(max_length=300)
    nombre_linea = models.CharField(max_length=50)
    nombre_marca = models.CharField(max_length=50)
    nombre_categoria_cliente = models.CharField(max_length=30)
    nombre_politica = models.CharField(max_length=100)
    valor_vencimiento = models.DecimalField(max_digits=30, decimal_places=2)
    saldo_vencimiento = models.DecimalField(max_digits=30, decimal_places=2)
    cobro_vencimiento = models.DecimalField(max_digits=30, decimal_places=2)
    cobro_efectivo_vencimiento = models.DecimalField(max_digits=30, decimal_places=2)
    porcentaje_vencimiento = models.DecimalField(max_digits=20, decimal_places=5)
    mes_cerrado = models.CharField(max_length=1)
    fecha_ult_ejecucion = models.DateField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_produc_mes_presente_total'
        unique_together = (('periodo', 'fecha_vencimiento', 'codigo_agencia', 'codigo_canton', 'codigo_provincia', 'codigo_region', 'codigo_politica', 'cod_modelo_cat_linea', 'cod_item_cat_linea', 'cod_marca', 'cod_cat_cliente', 'es_empleado', 'codigo_nacion', 'codigo_empresa'),)


class CcRangoDiasMoraBuro(models.Model):
    codigo_rango_dias_mora_buro = models.IntegerField(primary_key=True)
    codigo_buro = models.ForeignKey(AdBuros, models.DO_NOTHING, db_column='codigo_buro')
    codigo_empresa = models.ForeignKey(AdBuros, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=100)
    dias_mora_inicial = models.IntegerField()
    dias_mora_final = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_rango_dias_mora_buro'
        unique_together = (('codigo_rango_dias_mora_buro', 'codigo_buro', 'codigo_empresa'),)


class CcRangosVencXSegmentos(models.Model):
    codigo_segmento_cartera = models.OneToOneField('CcSegmentosDeCarteras', models.DO_NOTHING, db_column='codigo_segmento_cartera', primary_key=True)
    dias_inicial = models.IntegerField()
    dias_final = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    porcentaje_presupuesto = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_rangos_venc_x_segmentos'
        unique_together = (('codigo_segmento_cartera', 'dias_inicial', 'dias_final'),)


class CcRecaudadoras(models.Model):
    identificacion = models.CharField(primary_key=True, max_length=20)
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    tipo_identificacion = models.BooleanField()
    descripcion = models.CharField(max_length=20)
    directorio_recibir_archivos = models.CharField(max_length=600)
    directorio_enviar_archivos = models.CharField(max_length=600)
    persona_contacto = models.CharField(max_length=200)
    email_persona_contacto = models.CharField(max_length=100)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_recaudadoras'
        unique_together = (('identificacion', 'codigo_empresa'),)


class CcRespuestas(models.Model):
    codigo_respuesta = models.IntegerField(primary_key=True)
    codigo_tipo_respuesta = models.ForeignKey('CcTiposRespuestas', models.DO_NOTHING, db_column='codigo_tipo_respuesta')
    codigo_empresa = models.ForeignKey('CcTiposRespuestas', models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=100)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_respuestas'
        unique_together = (('codigo_respuesta', 'codigo_tipo_respuesta', 'codigo_empresa'),)


class CcRespuestasCampanias(models.Model):
    codigo_cliente = models.OneToOneField(CcPersonasCampaniasTelefon, models.DO_NOTHING, db_column='codigo_cliente', primary_key=True)
    codigo_pregunta_campania = models.ForeignKey(CcDetallePreguntasCampanias, models.DO_NOTHING, db_column='codigo_pregunta_campania')
    codigo_campania = models.ForeignKey(CcDetallePreguntasCampanias, models.DO_NOTHING, db_column='codigo_campania')
    codigo_tipo_respuesta = models.ForeignKey(CcDetallePreguntasCampanias, models.DO_NOTHING, db_column='codigo_tipo_respuesta')
    codigo_area = models.ForeignKey(CcDetallePreguntasCampanias, models.DO_NOTHING, db_column='codigo_area')
    codigo_empresa = models.ForeignKey(CcDetallePreguntasCampanias, models.DO_NOTHING, db_column='codigo_empresa')
    codigo_respuesta = models.ForeignKey(CcDetallePreguntasCampanias, models.DO_NOTHING, db_column='codigo_respuesta')
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    observacion = models.CharField(max_length=400, blank=True, null=True)
    identificacion_telefonista = models.ForeignKey('CcTelefonistasCampanias', models.DO_NOTHING, db_column='identificacion_telefonista')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    fecha_cita = models.DateField(blank=True, null=True)
    numero_cita = models.IntegerField(blank=True, null=True)
    mail = models.CharField(max_length=100, blank=True, null=True)
    fecha_cita_efectivizada = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_respuestas_campanias'
        unique_together = (('codigo_cliente', 'codigo_pregunta_campania', 'codigo_campania', 'codigo_tipo_respuesta', 'codigo_area', 'codigo_empresa'),)


class CcRespuestasCampaniasRota(models.Model):
    secuencia = models.OneToOneField(CcPersonasCampaniasTeleRot, models.DO_NOTHING, db_column='secuencia', primary_key=True)
    codigo_cliente = models.ForeignKey(CcPersonasCampaniasTeleRot, models.DO_NOTHING, db_column='codigo_cliente')
    codigo_pregunta_campania = models.ForeignKey(CcPreguntasCampanias, models.DO_NOTHING, db_column='codigo_pregunta_campania')
    codigo_campania = models.ForeignKey('CcTelefonistasCampanias', models.DO_NOTHING, db_column='codigo_campania')
    codigo_tipo_respuesta = models.ForeignKey(CcPreguntasCampanias, models.DO_NOTHING, db_column='codigo_tipo_respuesta')
    codigo_area = models.ForeignKey('CcTelefonistasCampanias', models.DO_NOTHING, db_column='codigo_area')
    codigo_empresa = models.ForeignKey('CcTelefonistasCampanias', models.DO_NOTHING, db_column='codigo_empresa')
    codigo_respuesta = models.ForeignKey(CcDetallePreguntasCampanias, models.DO_NOTHING, db_column='codigo_respuesta')
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    observacion = models.CharField(max_length=400, blank=True, null=True)
    identificacion_telefonista = models.ForeignKey('CcTelefonistasCampanias', models.DO_NOTHING, db_column='identificacion_telefonista')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    fecha_cita = models.DateField(blank=True, null=True)
    numero_cita = models.IntegerField(blank=True, null=True)
    mail = models.CharField(max_length=100, blank=True, null=True)
    fecha_cita_efectivizada = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_respuestas_campanias_rota'
        unique_together = (('secuencia', 'codigo_cliente', 'codigo_pregunta_campania', 'codigo_campania', 'codigo_tipo_respuesta', 'codigo_area', 'codigo_empresa'),)


class CcRespuestasEncuestas(models.Model):
    cod_comprobante = models.OneToOneField(CcClientesGestionarTelefon, models.DO_NOTHING, db_column='cod_comprobante', primary_key=True)
    tipo_comprobante = models.ForeignKey(CcClientesGestionarTelefon, models.DO_NOTHING, db_column='tipo_comprobante')
    codigo_periodo_gestion = models.ForeignKey(CcClientesGestionarTelefon, models.DO_NOTHING, db_column='codigo_periodo_gestion')
    codigo_banco_pregunta = models.ForeignKey(CcBancoPreguntas, models.DO_NOTHING, db_column='codigo_banco_pregunta')
    codigo_tipo_respuesta = models.ForeignKey(CcBancoPreguntas, models.DO_NOTHING, db_column='codigo_tipo_respuesta')
    codigo_tipo_encuesta = models.ForeignKey(CcBancoPreguntas, models.DO_NOTHING, db_column='codigo_tipo_encuesta')
    codigo_area_tipo_gestion = models.ForeignKey(CcBancoPreguntas, models.DO_NOTHING, db_column='codigo_area_tipo_gestion')
    codigo_area = models.ForeignKey(CcBancoPreguntas, models.DO_NOTHING, db_column='codigo_area')
    codigo_empresa = models.ForeignKey(CcBancoPreguntas, models.DO_NOTHING, db_column='codigo_empresa')
    codigo_respuesta = models.ForeignKey(CcRespuestas, models.DO_NOTHING, db_column='codigo_respuesta')
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    observacion = models.CharField(max_length=400, blank=True, null=True)
    identificacion_telefonista = models.ForeignKey('CcTelefonistasAreaTiposGes', models.DO_NOTHING, db_column='identificacion_telefonista')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_call_center = models.ForeignKey(CcBancoPreguntas, models.DO_NOTHING, db_column='codigo_call_center')

    class Meta:
        managed = False
        db_table = 'cc_respuestas_encuestas'
        unique_together = (('cod_comprobante', 'tipo_comprobante', 'codigo_periodo_gestion', 'codigo_banco_pregunta', 'codigo_tipo_respuesta', 'codigo_tipo_encuesta', 'codigo_area_tipo_gestion', 'codigo_area', 'codigo_call_center', 'codigo_empresa'),)


class CcResumenAgendaCobradores(models.Model):
    dia_visita = models.IntegerField(primary_key=True)
    periodo = models.ForeignKey(CcPeriodosCobradores, models.DO_NOTHING, db_column='periodo')
    codigo_segmento_cartera = models.ForeignKey('CcSegmentosDeCarteras', models.DO_NOTHING, db_column='codigo_segmento_cartera')
    identificacion_cobrador = models.ForeignKey('RhEmpleados', models.DO_NOTHING, db_column='identificacion_cobrador')
    codigo_call_center = models.ForeignKey(CcPeriodosCobradores, models.DO_NOTHING, db_column='codigo_call_center')
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    total_creditos = models.IntegerField()
    total_visitados = models.IntegerField()
    total_no_visitados = models.IntegerField()
    total_creditos_cobrados = models.IntegerField()
    porcentaje_participacion = models.DecimalField(max_digits=5, decimal_places=2)
    capital_asignado = models.DecimalField(max_digits=18, decimal_places=2)
    interes_mora_generado = models.DecimalField(max_digits=18, decimal_places=2)
    gasto_cobranza_generado = models.DecimalField(max_digits=18, decimal_places=2)
    cobros_en_efectivo = models.DecimalField(max_digits=18, decimal_places=2)
    interes_mora_cobrado = models.DecimalField(max_digits=18, decimal_places=2)
    gasto_cobranza_cobrado = models.DecimalField(max_digits=18, decimal_places=2)
    porcentaje_cumplimiento = models.DecimalField(max_digits=5, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_resumen_agenda_cobradores'
        unique_together = (('dia_visita', 'periodo', 'codigo_segmento_cartera', 'identificacion_cobrador', 'codigo_call_center', 'codigo_empresa'),)


class CcResumenCuotasGratis(models.Model):
    plazo = models.IntegerField(primary_key=True)
    periodo = models.IntegerField()
    negociado_con = models.CharField(max_length=255)
    codigo_agencia = models.IntegerField()
    codigo_empresa = models.IntegerField()
    nombre_ciudad = models.CharField(max_length=200)
    numero_creditos = models.IntegerField()
    total_vencido = models.DecimalField(max_digits=18, decimal_places=2)
    total_x_vencer = models.DecimalField(max_digits=18, decimal_places=2)
    total_cartera = models.DecimalField(max_digits=18, decimal_places=2)
    total_credito = models.DecimalField(max_digits=18, decimal_places=2)
    total_cuotas_gratis_generado = models.DecimalField(max_digits=18, decimal_places=2)
    total_ganaron_cuotas_gratis = models.DecimalField(max_digits=18, decimal_places=2)
    total_perdieron_cuotas_gratis = models.DecimalField(max_digits=18, decimal_places=2)
    total_cuotas_gratis_cobradas = models.DecimalField(max_digits=18, decimal_places=2)
    total_cuotas_gratis_vencidas = models.DecimalField(max_digits=18, decimal_places=2)
    total_cuotas_gratis_x_vencer = models.DecimalField(max_digits=18, decimal_places=2)
    total_cuo_gra_generado_periodo = models.DecimalField(max_digits=18, decimal_places=2)
    total_cuo_gra_cobradas_periodo = models.DecimalField(max_digits=18, decimal_places=2)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_resumen_cuotas_gratis'
        unique_together = (('plazo', 'periodo', 'negociado_con', 'codigo_agencia', 'codigo_empresa'),)


class CcResumenGestionesCallCent(models.Model):
    identificacion_gestor_telefon = models.CharField(primary_key=True, max_length=20)
    periodo = models.IntegerField()
    codigo_call_center = models.ForeignKey(CcCallCenter, models.DO_NOTHING, db_column='codigo_call_center')
    codigo_segmento_cartera = models.IntegerField()
    codigo_canton = models.CharField(max_length=4)
    codigo_provincia = models.CharField(max_length=6)
    codigo_region = models.IntegerField()
    codigo_nacion = models.IntegerField()
    tipo_campania = models.CharField(max_length=1)
    carga_inicial = models.CharField(max_length=1)
    codigo_empresa = models.IntegerField()
    nombre_gestor_telefonico = models.CharField(max_length=200)
    nombre_call_center = models.CharField(max_length=100)
    nombre_canton = models.CharField(max_length=50)
    nombre_provincia = models.CharField(max_length=100)
    nombre_region = models.CharField(max_length=300)
    nombre_tipo_campania = models.CharField(max_length=300)
    nombre_segmento_cartera = models.CharField(max_length=100, blank=True, null=True)
    numero_creditos_asignados = models.IntegerField()
    numero_creditos_gestionados = models.IntegerField()
    porcentaje_cumplimiento = models.DecimalField(max_digits=10, decimal_places=5)
    cobro_efectivo_por_caja = models.DecimalField(max_digits=30, decimal_places=2)
    cobro_efectivo_por_cobrador = models.DecimalField(max_digits=30, decimal_places=2)
    presupuesto = models.DecimalField(max_digits=30, decimal_places=2)
    numero_gestiones_positivas = models.IntegerField()
    presupuesto_gestiones_positiva = models.DecimalField(max_digits=30, decimal_places=2)
    numero_cancelaciones_positivas = models.IntegerField()
    monto_recup_efec_gestiones_pos = models.DecimalField(max_digits=30, decimal_places=2)
    porcentaje_productivid_num_cre = models.DecimalField(max_digits=10, decimal_places=5)
    porcentaje_productivid_en_mon = models.DecimalField(max_digits=10, decimal_places=5)
    mes_cerrado = models.CharField(max_length=1)
    fecha_ult_ejecucion = models.DateField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_resumen_gestiones_call_cent'
        unique_together = (('identificacion_gestor_telefon', 'periodo', 'codigo_call_center', 'codigo_segmento_cartera', 'codigo_canton', 'codigo_provincia', 'codigo_region', 'codigo_nacion', 'tipo_campania', 'carga_inicial', 'codigo_empresa'),)


class CcSaldosCuotasMensuales(models.Model):
    cod_comprobante = models.CharField(primary_key=True, max_length=9)
    numero_vencimiento = models.IntegerField()
    periodo_cierre = models.IntegerField()
    tipo_comprobante = models.CharField(max_length=2)
    cod_forma_pago = models.CharField(max_length=3)
    codigo_empresa = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_empresa')
    codigo_agencia = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_agencia')
    codigo_tipo_persona = models.CharField(max_length=3)
    codigo_persona = models.CharField(max_length=14)
    fecha_vencimiento = models.DateField()
    valor_vencimiento = models.DecimalField(max_digits=14, decimal_places=2)
    saldo_vencimiento = models.DecimalField(max_digits=14, decimal_places=2)
    dias_atraso_adelanto = models.IntegerField()
    interes_mora_generado = models.DecimalField(max_digits=14, decimal_places=2)
    interes_mora_abonado = models.DecimalField(max_digits=14, decimal_places=2)
    gasto_cobranza_generado = models.DecimalField(max_digits=14, decimal_places=2)
    gasto_cobranza_abonado = models.DecimalField(max_digits=14, decimal_places=2)
    cartera = models.CharField(max_length=3)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_estado_cuota = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_saldos_cuotas_mensuales'
        unique_together = (('cod_comprobante', 'numero_vencimiento', 'periodo_cierre', 'tipo_comprobante', 'cod_forma_pago', 'codigo_agencia', 'codigo_empresa'),)


class CcSegmentosCarterasCobrad(models.Model):
    identificacion_cobrador = models.OneToOneField('RhEmpleados', models.DO_NOTHING, db_column='identificacion_cobrador', primary_key=True)
    codigo_segmento_cartera = models.ForeignKey('CcSegmentosDeCarteras', models.DO_NOTHING, db_column='codigo_segmento_cartera')
    codigo_call_center = models.ForeignKey(CcCallCenter, models.DO_NOTHING, db_column='codigo_call_center')
    activo = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_item = models.CharField(max_length=3)
    codigo_modelo = models.CharField(max_length=8)
    codigo_empresa = models.ForeignKey('RhCargos', models.DO_NOTHING, db_column='codigo_empresa')
    es_institucion_si_no = models.CharField(max_length=1)
    asignar_resto_cartera_si_no = models.CharField(max_length=1)
    codigo_empresa_asignar_cartera = models.ForeignKey(CcEmpresasAsignarCarteras, models.DO_NOTHING, db_column='codigo_empresa_asignar_cartera')
    cartera_propia_si_no = models.CharField(max_length=1)
    codigo_cargo = models.ForeignKey('RhCargos', models.DO_NOTHING, db_column='codigo_cargo')
    asignar_cartera_fin_mes = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cc_segmentos_carteras_cobrad'
        unique_together = (('identificacion_cobrador', 'codigo_item', 'codigo_segmento_cartera', 'codigo_empresa_asignar_cartera', 'codigo_modelo', 'codigo_call_center', 'codigo_cargo', 'codigo_empresa'),)


class CcSegmentosCarterasTelefon(models.Model):
    identificacion_telefonista = models.OneToOneField('RhEmpleados', models.DO_NOTHING, db_column='identificacion_telefonista', primary_key=True)
    codigo_segmento_cartera = models.ForeignKey('CcSegmentosDeCarteras', models.DO_NOTHING, db_column='codigo_segmento_cartera')
    codigo_call_center = models.ForeignKey(CcCallCenter, models.DO_NOTHING, db_column='codigo_call_center')
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    activo = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cc_segmentos_carteras_telefon'
        unique_together = (('identificacion_telefonista', 'codigo_segmento_cartera', 'codigo_call_center'),)


class CcSegmentosDeCarteras(models.Model):
    codigo_segmento_cartera = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    rango_inicial = models.IntegerField()
    rango_final = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    porcentaje_recuperacion = models.DecimalField(max_digits=5, decimal_places=2)
    codigo_segmento_anterior = models.ForeignKey('self', models.DO_NOTHING, db_column='codigo_segmento_anterior', blank=True, null=True)
    codigo_segmento_siguiente = models.ForeignKey('self', models.DO_NOTHING, db_column='codigo_segmento_siguiente', blank=True, null=True)
    imprime_carta = models.CharField(max_length=1, blank=True, null=True)
    carta = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_segmentos_de_carteras'


class CcSegmentosXPoliticas(models.Model):
    codigo_segmento_cartera = models.OneToOneField(CcSegmentosDeCarteras, models.DO_NOTHING, db_column='codigo_segmento_cartera', primary_key=True)
    codigo_politica = models.IntegerField()
    codigo_empresa = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_segmentos_x_politicas'
        unique_together = (('codigo_segmento_cartera', 'codigo_politica', 'codigo_empresa'),)


class CcSiembraMensual(models.Model):
    codigo_empresa = models.IntegerField()
    codigo_call_center = models.IntegerField(blank=True, null=True)
    call_center = models.CharField(max_length=100)
    anio_mes_venta = models.IntegerField(primary_key=True)
    total_creditos = models.IntegerField(blank=True, null=True)
    monto_ventas = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nro_cred_2005 = models.IntegerField(blank=True, null=True)
    saldo_2005 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nro_cred_2006 = models.IntegerField(blank=True, null=True)
    saldo_2006 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nro_cred_2007 = models.IntegerField(blank=True, null=True)
    saldo_2007 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nro_cred_2008 = models.IntegerField(blank=True, null=True)
    saldo_2008 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nro_cred_2009 = models.IntegerField(blank=True, null=True)
    saldo_2009 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nro_cred_2010 = models.IntegerField(blank=True, null=True)
    saldo_2010 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nro_cred_2011 = models.IntegerField(blank=True, null=True)
    saldo_2011 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nro_cred_ene = models.IntegerField(blank=True, null=True)
    saldo_ene = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nro_cred_feb = models.IntegerField(blank=True, null=True)
    saldo_feb = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nro_cred_mar = models.IntegerField(blank=True, null=True)
    saldo_mar = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nro_cred_abr = models.IntegerField(blank=True, null=True)
    saldo_abr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nro_cred_may = models.IntegerField(blank=True, null=True)
    saldo_may = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nro_cred_jun = models.IntegerField(blank=True, null=True)
    saldo_jun = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nro_cred_jul = models.IntegerField(blank=True, null=True)
    saldo_jul = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nro_cred_ago = models.IntegerField(blank=True, null=True)
    saldo_ago = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nro_cred_sep = models.IntegerField(blank=True, null=True)
    saldo_sep = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nro_cred_oct = models.IntegerField(blank=True, null=True)
    saldo_oct = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nro_cred_nov = models.IntegerField(blank=True, null=True)
    saldo_nov = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nro_cred_dic = models.IntegerField(blank=True, null=True)
    saldo_dic = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_adicion = models.DateField(blank=True, null=True)
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    cred_cob_2005 = models.IntegerField(blank=True, null=True)
    total_cob_2005 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_2005 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    porc_pend_2005 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    cred_cob_2006 = models.IntegerField(blank=True, null=True)
    total_cob_2006 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_2006 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    porc_pend_2006 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    cred_cob_2007 = models.IntegerField(blank=True, null=True)
    total_cob_2007 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_2007 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    porc_pend_2007 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    cred_cob_2008 = models.IntegerField(blank=True, null=True)
    total_cob_2008 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_2008 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    porc_pend_2008 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    cred_cob_2009 = models.IntegerField(blank=True, null=True)
    total_cob_2009 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_2009 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    porc_pend_2009 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    cred_cob_2010 = models.IntegerField(blank=True, null=True)
    total_cob_2010 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_2010 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    porc_pend_2010 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    cred_cob_2011 = models.IntegerField(blank=True, null=True)
    total_cob_2011 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_2011 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    porc_pend_2011 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    cred_cob_ene = models.IntegerField(blank=True, null=True)
    total_cob_ene = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_ene = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    porc_pend_ene = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    cred_cob_feb = models.IntegerField(blank=True, null=True)
    total_cob_feb = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_feb = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    porc_pend_feb = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    cred_cob_mar = models.IntegerField(blank=True, null=True)
    total_cob_mar = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_mar = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    porc_pend_mar = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    cred_cob_abr = models.IntegerField(blank=True, null=True)
    total_cob_abr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_abr = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    porc_pend_abr = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    cred_cob_may = models.IntegerField(blank=True, null=True)
    total_cob_may = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_may = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    porc_pend_may = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    cred_cob_jun = models.IntegerField(blank=True, null=True)
    total_cob_jun = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_jun = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    porc_pend_jun = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    cred_cob_jul = models.IntegerField(blank=True, null=True)
    total_cob_jul = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_jul = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    porc_pend_jul = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    cred_cob_ago = models.IntegerField(blank=True, null=True)
    total_cob_ago = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_ago = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    porc_pend_ago = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    cred_cob_sep = models.IntegerField(blank=True, null=True)
    total_cob_sep = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_sep = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    porc_pend_sep = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    cred_cob_oct = models.IntegerField(blank=True, null=True)
    total_cob_oct = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_oct = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    porc_pend_oct = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    cred_cob_nov = models.IntegerField(blank=True, null=True)
    total_cob_nov = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_nov = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    porc_pend_nov = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    cred_cob_dic = models.IntegerField(blank=True, null=True)
    total_cob_dic = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_dic = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    porc_pend_dic = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    nro_cred_2012 = models.IntegerField(blank=True, null=True)
    saldo_2012 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cred_cob_2012 = models.IntegerField(blank=True, null=True)
    total_cob_2012 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_2012 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    porc_pend_2012 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    nro_cred_2013 = models.IntegerField(blank=True, null=True)
    saldo_2013 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cred_cob_2013 = models.IntegerField(blank=True, null=True)
    total_cob_2013 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_2013 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    porc_pend_2013 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    nro_cred_2014 = models.IntegerField(blank=True, null=True)
    saldo_2014 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cred_cob_2014 = models.IntegerField(blank=True, null=True)
    total_cob_2014 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porc_cob_2014 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    porc_pend_2014 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    nro_cred_2015 = models.IntegerField(blank=True, null=True)
    saldo_2015 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cred_cob_2015 = models.IntegerField(blank=True, null=True)
    total_cob_2015 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    porc_cob_2015 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    porc_pend_2015 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    nro_cred_2016 = models.IntegerField(blank=True, null=True)
    saldo_2016 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    cred_cob_2016 = models.IntegerField(blank=True, null=True)
    total_cob_2016 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    porc_cob_2016 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    porc_pend_2016 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    nro_cred_2017 = models.IntegerField(blank=True, null=True)
    saldo_2017 = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    cred_cob_2017 = models.IntegerField(blank=True, null=True)
    total_cob_2017 = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    porc_cob_2017 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    porc_pend_2017 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    nro_cred_2018 = models.IntegerField(blank=True, null=True)
    saldo_2018 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cred_cob_2018 = models.IntegerField(blank=True, null=True)
    total_cob_2018 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    porc_cob_2018 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    porc_pend_2018 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    nro_cred_2019 = models.IntegerField(blank=True, null=True)
    saldo_2019 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    cred_cob_2019 = models.IntegerField(blank=True, null=True)
    total_cob_2019 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    porc_cob_2019 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    porc_pend_2019 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    nro_cred_2020 = models.IntegerField(blank=True, null=True)
    saldo_2020 = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    cred_cob_2020 = models.IntegerField(blank=True, null=True)
    total_cob_2020 = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    porc_cob_2020 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    porc_pend_2020 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_siembra_mensual'
        unique_together = (('anio_mes_venta', 'call_center', 'codigo_empresa'),)


class CcSiembraXVencimiento(models.Model):
    anio_mes_vencimiento = models.IntegerField(primary_key=True)
    anio_mes_venta = models.IntegerField()
    codigo_agencia = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_agencia')
    codigo_canton = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_canton')
    codigo_provincia = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_provincia')
    codigo_region = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_region')
    codigo_politica = models.IntegerField()
    cod_modelo_cat_linea = models.CharField(max_length=8)
    cod_item_cat_linea = models.CharField(max_length=3)
    cod_marca = models.IntegerField()
    codigo_nacion = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_nacion')
    codigo_empresa = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_empresa')
    nombre_agencia = models.CharField(max_length=50)
    nombre_canton = models.CharField(max_length=50)
    nombre_provincia = models.CharField(max_length=100)
    nombre_region = models.CharField(max_length=300)
    nombre_linea = models.CharField(max_length=50)
    nombre_marca = models.CharField(max_length=50)
    nombre_politica = models.CharField(max_length=100)
    valor_vencimiento = models.DecimalField(max_digits=30, decimal_places=2)
    fecha_ult_ejecucion = models.DateField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_siembra_x_vencimiento'
        unique_together = (('anio_mes_vencimiento', 'anio_mes_venta', 'codigo_agencia', 'codigo_canton', 'codigo_provincia', 'codigo_region', 'codigo_politica', 'cod_modelo_cat_linea', 'cod_item_cat_linea', 'cod_marca', 'codigo_nacion', 'codigo_empresa'),)


class CcSiembraXVencimientoXPla(models.Model):
    anio_mes_vencimiento = models.IntegerField(primary_key=True)
    anio_mes_venta = models.IntegerField()
    plazo = models.IntegerField()
    codigo_agencia = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_agencia')
    codigo_canton = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_canton')
    codigo_provincia = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_provincia')
    codigo_region = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_region')
    codigo_politica = models.IntegerField()
    cod_modelo_cat_linea = models.CharField(max_length=8)
    cod_item_cat_linea = models.CharField(max_length=3)
    cod_marca = models.IntegerField()
    codigo_nacion = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_nacion')
    codigo_empresa = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_empresa')
    nombre_agencia = models.CharField(max_length=50)
    nombre_canton = models.CharField(max_length=50)
    nombre_provincia = models.CharField(max_length=100)
    nombre_region = models.CharField(max_length=300)
    nombre_linea = models.CharField(max_length=50)
    nombre_marca = models.CharField(max_length=50)
    nombre_politica = models.CharField(max_length=100)
    valor_vencimiento = models.DecimalField(max_digits=30, decimal_places=2)
    fecha_ult_ejecucion = models.DateField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_siembra_x_vencimiento_x_pla'
        unique_together = (('anio_mes_vencimiento', 'anio_mes_venta', 'plazo', 'codigo_agencia', 'codigo_canton', 'codigo_provincia', 'codigo_region', 'codigo_politica', 'cod_modelo_cat_linea', 'cod_item_cat_linea', 'cod_marca', 'codigo_nacion', 'codigo_empresa'),)


class CcTelefonistasAreaTiposGes(models.Model):
    identificacion_telefonista = models.OneToOneField('RhEmpleados', models.DO_NOTHING, db_column='identificacion_telefonista', primary_key=True)
    codigo_area_tipo_gestion = models.ForeignKey(CcAreaTiposGestiones, models.DO_NOTHING, db_column='codigo_area_tipo_gestion')
    codigo_area = models.ForeignKey(CcAreaTiposGestiones, models.DO_NOTHING, db_column='codigo_area')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_call_center = models.ForeignKey(CcAreaTiposGestiones, models.DO_NOTHING, db_column='codigo_call_center')

    class Meta:
        managed = False
        db_table = 'cc_telefonistas_area_tipos_ges'
        unique_together = (('identificacion_telefonista', 'codigo_area_tipo_gestion', 'codigo_area', 'codigo_call_center'),)


class CcTelefonistasCampanias(models.Model):
    identificacion_telefonista = models.ForeignKey('RhEmpleados', models.DO_NOTHING, db_column='identificacion_telefonista')
    codigo_area = models.ForeignKey(CcCampanias, models.DO_NOTHING, db_column='codigo_area')
    codigo_empresa = models.ForeignKey(CcCampanias, models.DO_NOTHING, db_column='codigo_empresa')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_campania = models.OneToOneField(CcCampanias, models.DO_NOTHING, db_column='codigo_campania', primary_key=True)

    class Meta:
        managed = False
        db_table = 'cc_telefonistas_campanias'
        unique_together = (('codigo_campania', 'identificacion_telefonista', 'codigo_area', 'codigo_empresa'),)


class CcTelefonistasXCallCenter(models.Model):
    identificacion_telefonista = models.OneToOneField('RhEmpleados', models.DO_NOTHING, db_column='identificacion_telefonista', primary_key=True)
    codigo_call_center = models.IntegerField()
    codigo_empresa = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_telefonistas_x_call_center'
        unique_together = (('identificacion_telefonista', 'codigo_call_center', 'codigo_empresa'),)


class CcTelefonistasXCampanias(models.Model):
    identificacion_telefonista = models.OneToOneField('RhEmpleados', models.DO_NOTHING, db_column='identificacion_telefonista', primary_key=True)
    numero_campania = models.ForeignKey(CcCampaniasCallcenterC, models.DO_NOTHING, db_column='numero_campania')
    codigo_call_center = models.ForeignKey(CcCallCenter, models.DO_NOTHING, db_column='codigo_call_center')
    tipo_campania = models.ForeignKey(CcCampaniasCallcenterC, models.DO_NOTHING, db_column='tipo_campania')
    codigo_empresa = models.ForeignKey(CcCampaniasCallcenterC, models.DO_NOTHING, db_column='codigo_empresa')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_telefonistas_x_campanias'
        unique_together = (('identificacion_telefonista', 'numero_campania', 'codigo_call_center', 'tipo_campania', 'codigo_empresa'),)


class CcTelefonosCoinciden(models.Model):
    codigo_cliente_externo = models.CharField(primary_key=True, max_length=14)
    codigo_cliente_interno = models.CharField(max_length=14)
    codigo_campania = models.ForeignKey(CcCampanias, models.DO_NOTHING, db_column='codigo_campania')
    codigo_area = models.ForeignKey(CcCampanias, models.DO_NOTHING, db_column='codigo_area')
    codigo_empresa = models.ForeignKey(CcCampanias, models.DO_NOTHING, db_column='codigo_empresa')
    telefono1_externo = models.CharField(max_length=20, blank=True, null=True)
    telefono2_externo = models.CharField(max_length=20, blank=True, null=True)
    telefono1_interno = models.CharField(max_length=20, blank=True, null=True)
    telefono2_interno = models.CharField(max_length=20, blank=True, null=True)
    si_es_tel_cli_interno = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_telefonos_coinciden'
        unique_together = (('codigo_cliente_externo', 'codigo_cliente_interno', 'codigo_campania', 'codigo_area', 'codigo_empresa'),)


class CcTempAgencias(models.Model):
    cod_agencia = models.IntegerField()
    nombre = models.CharField(max_length=50)
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cc_temp_agencias'


class CcTempAnios2(models.Model):
    anio = models.IntegerField()
    empresa = models.IntegerField()
    seleccionado = models.CharField(max_length=1)
    usuario = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cc_temp_anios2'


class CcTempCallCenter(models.Model):
    codigo_usuario = models.CharField(max_length=30)
    nombre_forma = models.CharField(max_length=30)
    codigo_empresa = models.IntegerField()
    codigo_call_center = models.OneToOneField(CcCallCenter, models.DO_NOTHING, db_column='codigo_call_center', primary_key=True)
    nombre_call_center = models.CharField(max_length=100)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_call_center'
        unique_together = (('codigo_call_center', 'codigo_usuario', 'nombre_forma', 'codigo_empresa'),)


class CcTempCargaEventual(models.Model):
    cod_comprobante = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    codigo_empresa = models.IntegerField()
    saldo_asignado = models.DecimalField(max_digits=18, decimal_places=2)
    tipo_campania = models.CharField(max_length=1)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_carga_eventual'
        unique_together = (('cod_comprobante', 'tipo_comprobante', 'tipo_campania', 'codigo_empresa'),)


class CcTempCiudades(models.Model):
    codigo = models.CharField(max_length=14)
    nombre = models.CharField(max_length=50)
    niv_cat_cod_categoria = models.CharField(max_length=2)
    niv_cat_emp_empresa = models.IntegerField()
    niv_secuencia = models.IntegerField()
    niv_cod_nivel = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'cc_temp_ciudades'


class CcTempCiudades2(models.Model):
    codigo = models.CharField(max_length=14)
    nombre = models.CharField(max_length=50)
    niv_cat_cod_categoria = models.CharField(max_length=2)
    niv_cat_emp_empresa = models.IntegerField()
    niv_secuencia = models.IntegerField()
    niv_cod_nivel = models.CharField(max_length=8)
    seleccionado = models.CharField(max_length=1)
    usuario = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cc_temp_ciudades2'


class CcTempClientes2(models.Model):
    empresa = models.IntegerField()
    cod_cliente = models.CharField(max_length=14)
    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    seleccionado = models.CharField(max_length=1)
    usuario = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cc_temp_clientes2'


class CcTempCobDiaRecaudExter(models.Model):
    numero_vencimiento = models.IntegerField()
    cod_comprobante_fp = models.CharField(max_length=9)
    tipo_comprobante_fp = models.CharField(max_length=2)
    cod_forma_pago_fp = models.CharField(max_length=3)
    tipo_cancelacion = models.CharField(max_length=2)
    numero_cancelacion = models.CharField(max_length=9)
    fecha_cancelacion = models.DateField()
    cod_agencia = models.IntegerField()
    valor_cuota_gratis = models.DecimalField(max_digits=18, decimal_places=2)
    valor_efectivo = models.DecimalField(max_digits=18, decimal_places=2)
    valor_devoluciones = models.DecimalField(max_digits=18, decimal_places=2)
    valor_descuentos = models.DecimalField(max_digits=18, decimal_places=2)
    valor_interes_mora = models.DecimalField(max_digits=18, decimal_places=2)
    valor_gasto_cobranza = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cc_temp_cob_dia_recaud_exter'


class CcTempCobradores(models.Model):
    codigo_empresa = models.IntegerField()
    codigo_usuario = models.CharField(max_length=30)
    nombre_forma = models.CharField(max_length=30)
    codigo_call_center = models.IntegerField()
    codigo_segmento_cartera = models.IntegerField()
    identificacion_cobrador = models.CharField(max_length=20)
    nombre_cobrador = models.CharField(max_length=105)

    class Meta:
        managed = False
        db_table = 'cc_temp_cobradores'


class CcTempCobradoresAge(models.Model):
    codigo_usuario = models.CharField(max_length=30)
    identificacion = models.CharField(max_length=20)
    codigo_agente = models.CharField(max_length=14)

    class Meta:
        managed = False
        db_table = 'cc_temp_cobradores_age'


class CcTempCobrosContactCenter(models.Model):
    ciudad = models.CharField(max_length=100)
    segmento_de_cartera = models.CharField(max_length=100)
    responsable = models.CharField(primary_key=True, max_length=100)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    total_asignacion = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_1 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_1 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_2 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_2 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_3 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_3 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_4 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_4 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_5 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_5 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_6 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_6 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_7 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_7 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_8 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_8 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_9 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_9 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_10 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_10 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_11 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_11 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_12 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_12 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_13 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_13 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_14 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_14 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_15 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_15 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_16 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_16 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_17 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_17 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_18 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_18 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_19 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_19 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_20 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_20 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_21 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_21 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_22 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_22 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_23 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_23 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_24 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_24 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_25 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_25 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_26 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_26 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_27 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_27 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_28 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_28 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_29 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_29 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_30 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_30 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    carga_dia_31 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrado_dia_31 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    total_cobrado = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    primera_quincena = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    segunda_quincena = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_cobros_contact_center'
        unique_together = (('responsable', 'ciudad', 'segmento_de_cartera'),)


class CcTempCobrosDiarios(models.Model):
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    agencia_cobro = models.CharField(max_length=100)
    fecha_cancelacion = models.DateField()
    cod_cliente = models.CharField(max_length=14, blank=True, null=True)
    nombres_clientes = models.CharField(max_length=255, blank=True, null=True)
    cuotas = models.CharField(max_length=20)
    tramo = models.CharField(max_length=100, blank=True, null=True)
    comprobante = models.CharField(max_length=12)
    cobrador = models.CharField(max_length=255, blank=True, null=True)
    numero_cancelacion = models.CharField(max_length=10)
    cancelacion_manual = models.CharField(max_length=10, blank=True, null=True)
    valor_cobro_asignado = models.DecimalField(max_digits=14, decimal_places=2)
    cuota_gratis = models.DecimalField(max_digits=14, decimal_places=2)
    descuentos = models.DecimalField(max_digits=14, decimal_places=2)
    interes_mora = models.DecimalField(max_digits=14, decimal_places=2)
    gastos_cobranza = models.DecimalField(max_digits=14, decimal_places=2)
    dias_mora_cobro = models.IntegerField()
    total = models.DecimalField(max_digits=14, decimal_places=2)
    devoluciones = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cod_age_cobro = models.IntegerField(blank=True, null=True)
    cod_age_factura = models.IntegerField()
    agencia_factura = models.CharField(max_length=100, blank=True, null=True)
    fecha_factura = models.DateField()
    fecha_cuota_mas_atrasada = models.DateField()
    fecha_balance = models.DateField()
    dias_mora_al_cierre_balance = models.IntegerField()
    cobro_anticipado = models.DecimalField(max_digits=18, decimal_places=2)
    total_cobro = models.DecimalField(max_digits=18, decimal_places=2)
    codigo_segmento_cartera_cierre = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_cobros_diarios'


class CcTempCobrosXAsignacion(models.Model):
    ciudad = models.CharField(max_length=100)
    segmento_de_cartera = models.CharField(max_length=100)
    asignado_a = models.CharField(primary_key=True, max_length=100)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    total_asignacion = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia1_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia1_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia2_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia2_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia3_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia3_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia4_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia4_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia5_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia5_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia6_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia6_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia7_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia7_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia8_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia8_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia9_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia9_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia10_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia10_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia11_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia11_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia12_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia12_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia13_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia13_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia14_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia14_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia15_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia15_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia16_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia16_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia17_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia17_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia18_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia18_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia19_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia19_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia20_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia20_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia21_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia21_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia22_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia22_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia23_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia23_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia24_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia24_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia25_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia25_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia26_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia26_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia27_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia27_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia28_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia28_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia29_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia29_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia30_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia30_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia31_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dia31_caj = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    total_cobrado = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    primera_quincena = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    segunda_quincena = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    num_cred_asig = models.IntegerField(blank=True, null=True)
    compromisos_pago = models.IntegerField(blank=True, null=True)
    comp_pago_cumplidos = models.IntegerField(blank=True, null=True)
    total_asig_adelantada = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    total_cobrado_adel = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_cobros_x_asignacion'
        unique_together = (('asignado_a', 'ciudad', 'segmento_de_cartera'),)


class CcTempCobrosXDiasMora(models.Model):
    ciudad = models.CharField(primary_key=True, max_length=100)
    anio_venta = models.IntegerField()
    codigo_empresa = models.IntegerField()
    cartera_menos_1 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobros_menos_1 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cartera_1_5 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobros_1_5 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cartera_6_15 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobros_6_15 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cartera_16_30 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobros_16_30 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cartera_31_60 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobros_31_60 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cartera_61_90 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobros_61_90 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cartera_91_120 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobros_91_120 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cartera_121_150 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobros_121_150 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cartera_151_180 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobros_151_180 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cartera_181_210 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobros_181_210 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cartera_211_240 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobros_211_240 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cartera_241_270 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobros_241_270 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cartera_271_300 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobros_271_300 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cartera_301_330 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobros_301_330 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cartera_331_360 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobros_331_360 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cartera_361_720 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobros_361_720 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cartera_mas_720 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobros_mas_720 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    total_cartera = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    total_cobrado = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    agente = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'cc_temp_cobros_x_dias_mora'
        unique_together = (('ciudad', 'anio_venta', 'agente', 'codigo_empresa'),)


class CcTempCompPagoContactCen(models.Model):
    call_center = models.IntegerField(primary_key=True)
    dia_gestion = models.IntegerField()
    cod_operador = models.CharField(max_length=30)
    num_cred_gestionados = models.IntegerField(blank=True, null=True)
    num_comp_pago = models.IntegerField(blank=True, null=True)
    saldo_comp_pago = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    valor_cobrado = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_comp_pago_contact_cen'
        unique_together = (('call_center', 'dia_gestion', 'cod_operador'),)


class CcTempCompromisosPagos(models.Model):
    codigo_comprobante = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    codigo_empresa = models.IntegerField()
    numero_cuotas = models.CharField(max_length=10)
    codigo_forma_pago = models.CharField(max_length=3)
    codigo_tipo_persona = models.CharField(max_length=3)
    codigo_persona = models.CharField(max_length=14)
    identificacion_cobrador_act = models.CharField(max_length=20)
    nombres_telefonistas = models.CharField(max_length=105)
    dia_compromiso_pago = models.CharField(max_length=2)
    nombre_cliente = models.CharField(max_length=255)
    zona_geograficah = models.CharField(max_length=15, blank=True, null=True)
    nombre_parroquia = models.CharField(max_length=50, blank=True, null=True)
    direccion_calleh = models.CharField(max_length=200, blank=True, null=True)
    calle_transversal = models.CharField(max_length=100, blank=True, null=True)
    telefono1h = models.CharField(max_length=15, blank=True, null=True)
    telefono2h = models.CharField(max_length=15, blank=True, null=True)
    valor_cuota = models.DecimalField(max_digits=14, decimal_places=2)
    saldos_cuotas = models.DecimalField(max_digits=14, decimal_places=2)
    gasto_cobranza = models.DecimalField(max_digits=14, decimal_places=2)
    interes_mora = models.DecimalField(max_digits=14, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cc_temp_compromisos_pagos'
        unique_together = (('codigo_comprobante', 'tipo_comprobante', 'dia_compromiso_pago', 'codigo_empresa'),)


class CcTempCreditosAprobados(models.Model):
    ciudad = models.CharField(max_length=100)
    agencia = models.CharField(max_length=150)
    cod_comprobante = models.CharField(max_length=9)
    tipo_comprobante = models.CharField(max_length=2, blank=True, null=True)
    num_solicitud = models.CharField(max_length=14, blank=True, null=True)
    identificacion_cliente = models.CharField(max_length=14, blank=True, null=True)
    nombre_cliente = models.CharField(max_length=200, blank=True, null=True)
    codigo_politica = models.IntegerField(blank=True, null=True)
    nombre_politica = models.CharField(max_length=50, blank=True, null=True)
    fecha_venta = models.DateField(blank=True, null=True)
    fecha_primera_cuota = models.DateField(blank=True, null=True)
    plazo = models.IntegerField(blank=True, null=True)
    calificacion = models.CharField(max_length=8, blank=True, null=True)
    vendedor = models.CharField(max_length=200, blank=True, null=True)
    zona = models.CharField(max_length=50, blank=True, null=True)
    parroquia = models.CharField(max_length=100, blank=True, null=True)
    linea = models.CharField(max_length=50, blank=True, null=True)
    garante = models.CharField(max_length=2, blank=True, null=True)
    edad_cliente = models.IntegerField(blank=True, null=True)
    ingreso_cliente = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    ingreso_conyuge = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    tipo_vivienda = models.CharField(max_length=50, blank=True, null=True)
    bono_solidario = models.CharField(max_length=2, blank=True, null=True)
    monto_compra = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cuotas_gratis = models.IntegerField(blank=True, null=True)
    valor_cuota = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    verif_telefonica = models.CharField(max_length=200, blank=True, null=True)
    verif_campo = models.CharField(max_length=200, blank=True, null=True)
    aprobado_por = models.CharField(max_length=200, blank=True, null=True)
    cargo_aprobador = models.CharField(max_length=100, blank=True, null=True)
    ocupacion_laboral = models.CharField(max_length=50, blank=True, null=True)
    credijaher = models.CharField(max_length=2, blank=True, null=True)
    negociado_con = models.CharField(max_length=50, blank=True, null=True)
    devolucion = models.CharField(max_length=2, blank=True, null=True)
    calificacion_central = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_creditos_aprobados'


class CcTempCreditosClientes(models.Model):
    cod_persona = models.CharField(max_length=14)
    tipo_persona = models.CharField(max_length=3)
    empresa = models.IntegerField()
    tipo_comprobante = models.CharField(max_length=2)
    cod_comprobante = models.CharField(primary_key=True, max_length=9)
    saldo_credito = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    capital_vencido = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_creditos_clientes'
        unique_together = (('cod_comprobante', 'tipo_comprobante', 'cod_persona', 'tipo_persona'),)


class CcTempCumObjSegCar(models.Model):
    periodo = models.IntegerField()
    identificacion_telefonista = models.CharField(primary_key=True, max_length=20)
    codigo_segmento_cartera = models.IntegerField()
    codigo_call_center = models.IntegerField()
    dia = models.IntegerField()
    total_clientes = models.DecimalField(max_digits=18, decimal_places=2)
    monto_asignado = models.DecimalField(max_digits=18, decimal_places=2)
    recuperado_efectivo = models.DecimalField(max_digits=18, decimal_places=2)
    monto_recuperado = models.DecimalField(max_digits=18, decimal_places=2)
    saldo_cartera = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    recuperado_efectivo_anticipado = models.DecimalField(max_digits=18, decimal_places=2)
    porcentaje_presupuesto = models.DecimalField(max_digits=5, decimal_places=2)
    total_devoluciones = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_cum_obj_seg_car'
        unique_together = (('identificacion_telefonista', 'dia', 'codigo_segmento_cartera', 'periodo', 'codigo_call_center'),)


class CcTempCumObjSegCarXZon(models.Model):
    empresa = models.FloatField()
    cod_modelo = models.CharField(max_length=8)
    cod_item = models.CharField(max_length=3)
    periodo = models.IntegerField()
    identificacion_cobrador = models.CharField(max_length=20)
    codigo_segmento_cartera = models.IntegerField()
    codigo_call_center = models.IntegerField()
    dia = models.IntegerField(primary_key=True)
    total_clientes = models.DecimalField(max_digits=18, decimal_places=2)
    monto_asignado = models.DecimalField(max_digits=18, decimal_places=2)
    recuperado_efectivo = models.DecimalField(max_digits=18, decimal_places=2)
    monto_recuperado = models.DecimalField(max_digits=18, decimal_places=2)
    saldo_cartera = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    recuperado_efectivo_anticipado = models.DecimalField(max_digits=18, decimal_places=2)
    porcentaje_presupuesto = models.DecimalField(max_digits=5, decimal_places=2)
    total_devoluciones = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_cum_obj_seg_car_x_zon'
        unique_together = (('dia', 'cod_item', 'cod_modelo', 'identificacion_cobrador', 'codigo_segmento_cartera', 'periodo', 'codigo_call_center', 'empresa'),)


class CcTempCumObjXCiudad(models.Model):
    periodo = models.IntegerField()
    identificacion_telefonista = models.CharField(primary_key=True, max_length=20)
    codigo_segmento_cartera = models.IntegerField()
    codigo_call_center = models.IntegerField()
    total_clientes = models.DecimalField(max_digits=18, decimal_places=2)
    monto_asignado = models.DecimalField(max_digits=18, decimal_places=2)
    recuperado_efectivo = models.DecimalField(max_digits=18, decimal_places=2)
    monto_recuperado = models.DecimalField(max_digits=18, decimal_places=2)
    saldo_cartera = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    recuperado_efectivo_anticipado = models.DecimalField(max_digits=18, decimal_places=2)
    porcentaje_presupuesto = models.DecimalField(max_digits=5, decimal_places=2)
    total_devoluciones = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descuentos = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_cum_obj_x_ciudad'
        unique_together = (('identificacion_telefonista', 'codigo_segmento_cartera', 'periodo', 'codigo_call_center'),)


class CcTempCumpObjAnios(models.Model):
    identificacion_cobrador = models.CharField(max_length=20, blank=True, null=True)
    anio_venta = models.CharField(max_length=20, blank=True, null=True)
    total_clientes = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_asignado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    recuperado_efectivo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_recuperado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    saldo_cartera = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    recuperado_efectivo_anticipado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    devoluciones = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descuentos = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_cump_obj_anios'


class CcTempCumpObjAniosGer(models.Model):
    identificacion_cobrador = models.CharField(max_length=20, blank=True, null=True)
    codigo_segmento_cartera = models.IntegerField(blank=True, null=True)
    codigo_call_center = models.IntegerField(blank=True, null=True)
    anio_venta = models.CharField(max_length=20, blank=True, null=True)
    total_clientes = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_asignado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    recuperado_efectivo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_recuperado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    saldo_cartera = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    recuperado_efectivo_anticipado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    devoluciones = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descuentos = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_cump_obj_anios_ger'


class CcTempCumpObjRangos(models.Model):
    identificacion_cobrador = models.CharField(max_length=20, blank=True, null=True)
    dia_inicial = models.CharField(max_length=10, blank=True, null=True)
    dia_final = models.CharField(max_length=10, blank=True, null=True)
    total_clientes = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_asignado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    recuperado_efectivo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_recuperado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    saldo_cartera = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    recuperado_efectivo_anticipado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    devoluciones = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descuentos = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_cump_obj_rangos'


class CcTempCumpObjRangosGer(models.Model):
    identificacion_cobrador = models.CharField(max_length=20, blank=True, null=True)
    codigo_segmento_cartera = models.IntegerField(blank=True, null=True)
    codigo_call_center = models.IntegerField(blank=True, null=True)
    dia_inicial = models.CharField(max_length=10, blank=True, null=True)
    dia_final = models.CharField(max_length=10, blank=True, null=True)
    total_clientes = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_asignado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    recuperado_efectivo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_recuperado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    saldo_cartera = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    recuperado_efectivo_anticipado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    devoluciones = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descuentos = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_cump_obj_rangos_ger'


class CcTempCumplimientoObjetivos(models.Model):
    periodo = models.IntegerField()
    identificacion_telefonista = models.CharField(max_length=20)
    dia = models.IntegerField()
    total_clientes = models.DecimalField(max_digits=18, decimal_places=2)
    monto_asignado = models.DecimalField(max_digits=18, decimal_places=2)
    recuperado_efectivo = models.DecimalField(max_digits=18, decimal_places=2)
    monto_recuperado = models.DecimalField(max_digits=18, decimal_places=2)
    saldo_cartera = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    recuperado_efectivo_anticipado = models.DecimalField(max_digits=18, decimal_places=2)
    devoluciones = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_cumplimiento_objetivos'


class CcTempGestionesClientes(models.Model):
    periodo = models.IntegerField()
    identificacion_telefonista = models.CharField(max_length=20)
    codigo_tipo_gestion = models.CharField(max_length=10, blank=True, null=True)
    dia_vencimiento = models.IntegerField()
    codigo_comprobante = models.CharField(max_length=9)
    tipo_comprobante = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'cc_temp_gestiones_clientes'


class CcTempHistoricoCarterXAge(models.Model):
    codigo_agencia = models.IntegerField(primary_key=True)
    segmento_cartera = models.CharField(max_length=10)
    cartera = models.CharField(max_length=3)
    codigo_empresa = models.IntegerField()
    enero = models.DecimalField(max_digits=14, decimal_places=2)
    febrero = models.DecimalField(max_digits=14, decimal_places=2)
    marzo = models.DecimalField(max_digits=14, decimal_places=2)
    abril = models.DecimalField(max_digits=14, decimal_places=2)
    mayo = models.DecimalField(max_digits=14, decimal_places=2)
    junio = models.DecimalField(max_digits=14, decimal_places=2)
    julio = models.DecimalField(max_digits=14, decimal_places=2)
    agosto = models.DecimalField(max_digits=14, decimal_places=2)
    septiembre = models.DecimalField(max_digits=14, decimal_places=2)
    octubre = models.DecimalField(max_digits=14, decimal_places=2)
    noviembre = models.DecimalField(max_digits=14, decimal_places=2)
    diciembre = models.DecimalField(max_digits=14, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cc_temp_historico_carter_x_age'
        unique_together = (('codigo_agencia', 'segmento_cartera', 'cartera', 'codigo_empresa'),)


class CcTempHistoricoCarterXEmp(models.Model):
    segmento_cartera = models.CharField(primary_key=True, max_length=10)
    cartera = models.CharField(max_length=3)
    codigo_empresa = models.IntegerField()
    enero = models.DecimalField(max_digits=14, decimal_places=2)
    febrero = models.DecimalField(max_digits=14, decimal_places=2)
    marzo = models.DecimalField(max_digits=14, decimal_places=2)
    abril = models.DecimalField(max_digits=14, decimal_places=2)
    mayo = models.DecimalField(max_digits=14, decimal_places=2)
    junio = models.DecimalField(max_digits=14, decimal_places=2)
    julio = models.DecimalField(max_digits=14, decimal_places=2)
    agosto = models.DecimalField(max_digits=14, decimal_places=2)
    septiembre = models.DecimalField(max_digits=14, decimal_places=2)
    octubre = models.DecimalField(max_digits=14, decimal_places=2)
    noviembre = models.DecimalField(max_digits=14, decimal_places=2)
    diciembre = models.DecimalField(max_digits=14, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cc_temp_historico_carter_x_emp'
        unique_together = (('segmento_cartera', 'cartera', 'codigo_empresa'),)


class CcTempHojaRuta(models.Model):
    codigo_cobrador = models.CharField(max_length=20)
    codigo_zona = models.CharField(max_length=14)
    codigo_call_center = models.IntegerField()
    cod_comprobante = models.CharField(max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    numero_vencimiento = models.IntegerField()
    cod_cliente = models.CharField(max_length=14)
    plazo = models.IntegerField(blank=True, null=True)
    cuotas_canceladas = models.IntegerField(blank=True, null=True)
    valor_cuota = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    vencido_meses_atras = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    vencido_mese_3 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    vencido_mese_2 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    vencido_mese_1 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    vencido_mes_actual = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    interes = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    gastos_cobranza = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    saldo_actual = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_hoja_ruta'


class CcTempHojaRutaCobradores(models.Model):
    codigo_comprobante = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante = models.CharField(max_length=3)
    codigo_empresa = models.IntegerField()
    identificacion_cliente = models.CharField(max_length=14)
    identificacion_garante = models.CharField(max_length=14, blank=True, null=True)
    identificacion_cobrador = models.CharField(max_length=20)
    codigo_producto = models.CharField(max_length=14, blank=True, null=True)
    nombre_producto = models.CharField(max_length=50, blank=True, null=True)
    numero_cuotas = models.CharField(max_length=10)
    fecha_cuota_antigua = models.DateField()
    valor_cuota = models.DecimalField(max_digits=14, decimal_places=2)
    saldo_cuotas = models.DecimalField(max_digits=14, decimal_places=2)
    gasto_cobranza = models.DecimalField(max_digits=14, decimal_places=2)
    interes_mora = models.DecimalField(max_digits=14, decimal_places=2)
    dia_vencimiento = models.IntegerField()
    zona_geografica = models.CharField(max_length=14)
    nombre_parroquia = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cc_temp_hoja_ruta_cobradores'
        unique_together = (('codigo_comprobante', 'tipo_comprobante', 'codigo_empresa'),)


class CcTempHuaquillas(models.Model):
    cod_comprobante = models.CharField(max_length=9)
    tipo_comprobante = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'cc_temp_huaquillas'


class CcTempIndurama(models.Model):
    identificacion = models.CharField(max_length=20, blank=True, null=True)
    comprobante = models.CharField(max_length=20, blank=True, null=True)
    saldocredito = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    plazo = models.IntegerField(blank=True, null=True)
    identificacion2 = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_indurama'


class CcTempInstituciones(models.Model):
    codigo_empresa = models.IntegerField()
    codigo_usuario = models.CharField(max_length=30)
    nombre_forma = models.CharField(max_length=30)
    codigo_call_center = models.IntegerField()
    codigo_segmento_cartera = models.IntegerField()
    codigo_institucion = models.CharField(max_length=14)
    nombre_institucion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cc_temp_instituciones'


class CcTempJefesCobrador(models.Model):
    identificacion = models.CharField(primary_key=True, max_length=20)
    codigo_empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cc_temp_jefes_cobrador'
        unique_together = (('identificacion', 'codigo_empresa'),)


class CcTempMensuales(models.Model):
    cod_comprobante = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    periodo_cierre = models.IntegerField()
    cartera = models.CharField(max_length=3)
    codigo_agencia = models.IntegerField()
    codigo_empresa = models.IntegerField()
    codigo_politica = models.IntegerField()
    nombre_politica = models.CharField(max_length=100)
    codigo_estado_cuota = models.CharField(max_length=3, blank=True, null=True)
    codigo_persona = models.CharField(max_length=14)
    codigo_tipo_persona = models.CharField(max_length=3)
    zona_geograficah = models.CharField(max_length=15, blank=True, null=True)
    nombre_parroquia = models.CharField(max_length=50, blank=True, null=True)
    cod_modelo = models.CharField(max_length=8, blank=True, null=True)
    cod_item = models.CharField(max_length=3, blank=True, null=True)
    nombre_zona = models.CharField(max_length=50, blank=True, null=True)
    cuotas_gratis = models.DecimalField(max_digits=4, decimal_places=2)
    factura_manual = models.CharField(max_length=9)
    numero_pagos = models.IntegerField()
    cod_agente = models.CharField(max_length=14, blank=True, null=True)
    nombre_vendedor = models.CharField(max_length=255, blank=True, null=True)
    fecha_vencimiento = models.DateField()
    direccion_calleh = models.CharField(max_length=200, blank=True, null=True)
    numero_casa = models.CharField(max_length=20, blank=True, null=True)
    calle_transversal = models.CharField(max_length=100, blank=True, null=True)
    telefono1h = models.CharField(max_length=15, blank=True, null=True)
    telefono2h = models.CharField(max_length=15, blank=True, null=True)
    cod_cat_cliente = models.CharField(max_length=8, blank=True, null=True)
    cod_producto = models.CharField(max_length=14, blank=True, null=True)
    nombre_producto = models.CharField(max_length=50, blank=True, null=True)
    cod_modelo_cat = models.CharField(max_length=8, blank=True, null=True)
    cod_item_cat = models.CharField(max_length=3, blank=True, null=True)
    nombre_linea = models.CharField(max_length=50, blank=True, null=True)
    es_empleado = models.CharField(max_length=100)
    saldo_anticipo = models.DecimalField(max_digits=14, decimal_places=2)
    fecha_inicio_mes = models.DateField()
    fecha_fin_mes = models.DateField()
    valor_mes_actual_vencido = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_29_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_28_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_27_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_26_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_25_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_24_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_23_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_22_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_21_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_20_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_19_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_18_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_17_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_16_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_15_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_14_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_13_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_12_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_11_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_10_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_09_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_08_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_07_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_06_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_05_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_04_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_03_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_02_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_x_vencer_01_mes = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_01_mes = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_02_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_03_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_04_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_05_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_06_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_07_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_08_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_09_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_10_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_11_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_12_meses = models.DecimalField(max_digits=14, decimal_places=2)
    valor_vencido_mas_12_meses = models.DecimalField(max_digits=14, decimal_places=2)
    interes_mora_generado = models.DecimalField(max_digits=14, decimal_places=2)
    interes_mora_abonado = models.DecimalField(max_digits=14, decimal_places=2)
    gasto_cobranza_generado = models.DecimalField(max_digits=14, decimal_places=2)
    gasto_cobranza_abonado = models.DecimalField(max_digits=14, decimal_places=2)
    dias_atraso_adelanto = models.IntegerField()
    codigo_segmento_cartera = models.IntegerField(blank=True, null=True)
    nombre_segmento_cartera = models.CharField(max_length=100, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    negociado_con = models.CharField(max_length=255, blank=True, null=True)
    numero_negociacion = models.IntegerField(blank=True, null=True)
    valor_cuota = models.DecimalField(max_digits=14, decimal_places=2)
    verificacion_campo_por = models.CharField(max_length=105, blank=True, null=True)
    verificacion_telefonica_por = models.CharField(max_length=105, blank=True, null=True)
    credito_aprobado_por = models.CharField(max_length=105, blank=True, null=True)
    codigo_call_center = models.IntegerField(blank=True, null=True)
    nombre_call_center = models.CharField(max_length=100, blank=True, null=True)
    anio_venta = models.IntegerField(blank=True, null=True)
    mes_venta = models.IntegerField(blank=True, null=True)
    dia_venta = models.IntegerField(blank=True, null=True)
    dia_vencimiento = models.IntegerField(blank=True, null=True)
    ultima_gestion = models.CharField(max_length=10, blank=True, null=True)
    fecha_ultima_gestion = models.DateField(blank=True, null=True)
    cupo_aprobado = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    credijaher = models.CharField(max_length=1, blank=True, null=True)
    valor_entrada = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    valor_adicional = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cod_garante = models.CharField(max_length=14, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    valor_ingresos = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cobrador_asignado = models.CharField(max_length=100, blank=True, null=True)
    fecha_aplicacion_fondo = models.DateField(blank=True, null=True)
    monto_credito = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    fecha_ultimo_pago = models.DateField(blank=True, null=True)
    numero_cuotas_canceladas = models.IntegerField(blank=True, null=True)
    numero_cuotas_mora = models.IntegerField(blank=True, null=True)
    operador_asignado = models.CharField(max_length=100, blank=True, null=True)
    presupuesto = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nro_credijaher = models.CharField(max_length=21, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_mensuales'
        unique_together = (('cod_comprobante', 'tipo_comprobante', 'periodo_cierre', 'cartera', 'codigo_agencia', 'codigo_empresa'),)


class CcTempMovimiento(models.Model):
    empresa = models.IntegerField()
    tipo_comprobante = models.CharField(max_length=2)
    cod_comprobante = models.CharField(max_length=9)
    secuencia = models.IntegerField()
    cod_producto = models.CharField(max_length=14)
    cantidad = models.DecimalField(max_digits=14, decimal_places=2)
    precio = models.DecimalField(max_digits=14, decimal_places=2)
    total = models.DecimalField(max_digits=14, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cc_temp_movimiento'


class CcTempParroquias(models.Model):
    codigo_usuario = models.CharField(max_length=30)
    nombre_forma = models.CharField(max_length=30)
    codigo_parroquia = models.CharField(max_length=14)
    codigo_zona = models.CharField(max_length=14)
    codigo_modelo = models.CharField(max_length=8)
    codigo_empresa = models.IntegerField()
    nombre_parroquia = models.CharField(max_length=50)
    cantidad_clientes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_parroquias'


class CcTempPoliticaCredito(models.Model):
    cod_politica = models.IntegerField(blank=True, null=True)
    empresa = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_politica_credito'


class CcTempPrimerasCuotas(models.Model):
    ciudad = models.CharField(primary_key=True, max_length=150)
    creditos_ciudad = models.IntegerField(blank=True, null=True)
    monto_ciudad = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    mes_vencimiento = models.IntegerField()
    mes_evaluado = models.IntegerField()
    num_creditos_venc = models.IntegerField(blank=True, null=True)
    total_venc = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    monto_venc = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    valor_mes = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    creditos_mes = models.IntegerField(blank=True, null=True)
    total_mes = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_primeras_cuotas'
        unique_together = (('ciudad', 'mes_vencimiento', 'mes_evaluado'),)


class CcTempPrimerasCuotasVenc(models.Model):
    ciudad = models.CharField(max_length=100)
    cod_comprobante = models.CharField(max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    cod_cliente = models.CharField(max_length=14)
    nombre_cliente = models.CharField(max_length=50)
    fecha_venta = models.DateField()
    saldo_vencido = models.DecimalField(max_digits=14, decimal_places=2)
    negociado_con = models.CharField(max_length=50, blank=True, null=True)
    num_negociacion = models.IntegerField(blank=True, null=True)
    dias_mora = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_primeras_cuotas_venc'


class CcTempSectores(models.Model):
    codigo = models.CharField(max_length=14)
    nombre = models.CharField(max_length=50)
    niv_cat_cod_categoria = models.CharField(max_length=2, blank=True, null=True)
    niv_cat_emp_empresa = models.IntegerField(blank=True, null=True)
    niv_secuencia = models.IntegerField(blank=True, null=True)
    niv_cod_nivel = models.CharField(max_length=8, blank=True, null=True)
    cla_codigo = models.CharField(max_length=14)
    cla_niv_cat_cod_categoria = models.CharField(max_length=2)
    cla_niv_cat_emp_empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cc_temp_sectores'


class CcTempSegmentosCarteras(models.Model):
    codigo_usuario = models.CharField(max_length=30)
    nombre_forma = models.CharField(max_length=30)
    codigo_empresa = models.IntegerField()
    codigo_segmento_cartera = models.OneToOneField(CcSegmentosDeCarteras, models.DO_NOTHING, db_column='codigo_segmento_cartera', primary_key=True)
    nombre_segmento_cartera = models.CharField(max_length=100)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_segmentos_carteras'
        unique_together = (('codigo_segmento_cartera', 'codigo_usuario', 'nombre_forma', 'codigo_empresa'),)


class CcTempStPolCre(models.Model):
    codigo_politica = models.IntegerField(primary_key=True)
    codigo_usuario = models.CharField(max_length=30)
    nombre_forma = models.CharField(max_length=30)
    codigo_empresa = models.IntegerField()
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cc_temp_st_pol_cre'
        unique_together = (('codigo_politica', 'codigo_usuario', 'nombre_forma', 'codigo_empresa'),)


class CcTempSubirProductos(models.Model):
    empresa = models.IntegerField()
    cod_producto = models.CharField(max_length=14)
    precio = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    seleccionado = models.CharField(max_length=1)
    usuario = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cc_temp_subir_productos'


class CcTempTelefonosPersonasCam(models.Model):
    telefono = models.CharField(primary_key=True, max_length=20)
    codigo_persona = models.CharField(max_length=14)
    numero_campania = models.IntegerField()
    codigo_empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cc_temp_telefonos_personas_cam'
        unique_together = (('telefono', 'codigo_persona', 'numero_campania', 'codigo_empresa'),)


class CcTempTgSitio(models.Model):
    cod_sitio = models.CharField(max_length=3)
    nombre = models.CharField(max_length=50)
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cc_temp_tg_sitio'


class CcTempVencimientosMes(models.Model):
    ciudad = models.CharField(primary_key=True, max_length=200)
    aaaamm_cobro = models.IntegerField()
    aaaamm_cuota_analizar = models.IntegerField()
    codigo_empresa = models.IntegerField()
    total_creditos_analizar = models.DecimalField(max_digits=18, decimal_places=2)
    valor_creditos_analizar = models.DecimalField(max_digits=18, decimal_places=2)
    total_creditos_saldo = models.DecimalField(max_digits=18, decimal_places=2)
    saldo = models.DecimalField(max_digits=18, decimal_places=2)
    total_creditos_cobrados_atrasa = models.DecimalField(max_digits=18, decimal_places=2)
    total_cobros_atrasados = models.DecimalField(max_digits=18, decimal_places=2)
    total_creditos_adelantados = models.DecimalField(max_digits=18, decimal_places=2)
    total_cobros_adelantados = models.DecimalField(max_digits=18, decimal_places=2)
    porcentaje_cobrado = models.DecimalField(max_digits=5, decimal_places=2)
    porcentaje_pendiente = models.DecimalField(max_digits=5, decimal_places=2)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_vencimientos_mes'
        unique_together = (('ciudad', 'aaaamm_cobro', 'aaaamm_cuota_analizar', 'codigo_empresa'),)


class CcTempVendedores2(models.Model):
    empresa = models.IntegerField()
    cod_tipo_persona = models.CharField(max_length=3)
    cod_vendedor = models.CharField(max_length=14)
    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=40)
    seleccionado = models.CharField(max_length=1)
    usuario = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cc_temp_vendedores2'


class CcTempVentasVencimientos(models.Model):
    secuencia = models.BigIntegerField(primary_key=True)
    aniomes_vencimiento = models.IntegerField()
    aniomes_venta = models.IntegerField()
    periodo = models.IntegerField()
    saldo_vencimiento = models.DecimalField(max_digits=18, decimal_places=2)
    valor_vencimiento = models.DecimalField(max_digits=18, decimal_places=2)
    saldo_vencido = models.DecimalField(max_digits=18, decimal_places=2)
    saldo_x_vencer = models.DecimalField(max_digits=18, decimal_places=2)
    valor_venta = models.DecimalField(max_digits=18, decimal_places=2)
    valor_venta_consolidado = models.DecimalField(max_digits=18, decimal_places=2)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_agencia = models.IntegerField()
    codigo_parroquia = models.CharField(max_length=14, blank=True, null=True)
    codigo_politica = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_ventas_vencimientos'
        unique_together = (('secuencia', 'aniomes_vencimiento', 'aniomes_venta', 'codigo_agencia', 'periodo'),)


class CcTempZonas(models.Model):
    empresa = models.IntegerField()
    cod_modelo = models.CharField(max_length=8)
    cod_item = models.CharField(max_length=3)
    nombre = models.CharField(max_length=50)
    cod_categoria_deffecto = models.CharField(max_length=2, blank=True, null=True)
    emp_empresa_defecto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_temp_zonas'


class CcTempZonas2(models.Model):
    empresa = models.IntegerField()
    e_mail = models.CharField(max_length=30)
    seleccionado = models.CharField(max_length=1)
    usuario = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cc_temp_zonas2'


class CcTipoCancelacion(models.Model):
    empresa = models.IntegerField(primary_key=True)
    cod_tipo_cancelacion = models.CharField(max_length=2)
    debito_credito = models.BooleanField()
    capital_interes = models.CharField(max_length=1)
    tipo_cancelacion = models.CharField(max_length=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_tipo_cancelacion'
        unique_together = (('empresa', 'cod_tipo_cancelacion'),)


class CcTiposCarteras(models.Model):
    codigo_empresa = models.OneToOneField(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa', primary_key=True)
    cartera = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_tipos_carteras'
        unique_together = (('codigo_empresa', 'cartera'),)


class CcTiposContactoTelefonico(models.Model):
    codigo_tipo_contacto = models.IntegerField(primary_key=True)
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(unique=True, max_length=20)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    resultado_tipo_contacto = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cc_tipos_contacto_telefonico'
        unique_together = (('codigo_tipo_contacto', 'codigo_empresa'),)


class CcTiposDeIdentificacion(models.Model):
    codigo_tipo_identificacion = models.BooleanField(primary_key=True)
    codigo_buro = models.ForeignKey(AdBuros, models.DO_NOTHING, db_column='codigo_buro')
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=40)
    equivalente_empresa = models.BooleanField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_tipos_de_identificacion'
        unique_together = (('codigo_tipo_identificacion', 'codigo_buro', 'codigo_empresa'),)


class CcTiposEncuestas(models.Model):
    codigo_tipo_encuesta = models.IntegerField(primary_key=True)
    codigo_area_tipo_gestion = models.ForeignKey(CcAreaTiposGestiones, models.DO_NOTHING, db_column='codigo_area_tipo_gestion')
    codigo_area = models.ForeignKey(CcAreaTiposGestiones, models.DO_NOTHING, db_column='codigo_area')
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=100)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_call_center = models.ForeignKey(CcAreaTiposGestiones, models.DO_NOTHING, db_column='codigo_call_center')

    class Meta:
        managed = False
        db_table = 'cc_tipos_encuestas'
        unique_together = (('codigo_tipo_encuesta', 'codigo_area_tipo_gestion', 'codigo_area', 'codigo_call_center', 'codigo_empresa'),)


class CcTiposEntrega(models.Model):
    codigo_tipo_entrega = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20, blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_tipos_entrega'


class CcTiposGesCarCallCenter(models.Model):
    codigo_estado_cuota = models.CharField(primary_key=True, max_length=3)
    codigo_empresa = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_tipos_ges_car_call_center'
        unique_together = (('codigo_estado_cuota', 'codigo_empresa'),)


class CcTiposGesCarCobrador(models.Model):
    codigo_estado_cuota = models.CharField(primary_key=True, max_length=3)
    codigo_empresa = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_tipos_ges_car_cobrador'
        unique_together = (('codigo_estado_cuota', 'codigo_empresa'),)


class CcTiposGesCarCobradorInst(models.Model):
    codigo_estado_cuota = models.CharField(primary_key=True, max_length=3)
    codigo_empresa = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_tipos_ges_car_cobrador_inst'
        unique_together = (('codigo_estado_cuota', 'codigo_empresa'),)


class CcTiposGestiones(models.Model):
    codigo_tipo_gestion = models.CharField(primary_key=True, max_length=10)
    codigo_area = models.ForeignKey(CcAreaGestiones, models.DO_NOTHING, db_column='codigo_area')
    descripcion = models.CharField(max_length=100)
    tipo_mayor_detalle = models.CharField(max_length=1)
    codigo_tipo_gestion_padre = models.ForeignKey('self', models.DO_NOTHING, db_column='codigo_tipo_gestion_padre', blank=True, null=True)
    codigo_area_padre = models.ForeignKey('self', models.DO_NOTHING, db_column='codigo_area_padre', blank=True, null=True)
    codigo_nivel = models.ForeignKey(CcNivelesGestiones, models.DO_NOTHING, db_column='codigo_nivel')
    abreviatura = models.CharField(max_length=15)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    visualiza_call_center = models.CharField(max_length=1)
    mover_segmento_cartera = models.CharField(max_length=1, blank=True, null=True)
    codigo_segmento_cartera = models.ForeignKey(CcSegmentosDeCarteras, models.DO_NOTHING, db_column='codigo_segmento_cartera', blank=True, null=True)
    visualizar_cobradores = models.CharField(max_length=1)
    es_efectivo = models.BooleanField(blank=True, null=True)
    visualizar_urd = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cc_tipos_gestiones'
        unique_together = (('codigo_tipo_gestion', 'codigo_area'),)


class CcTiposIngresos(models.Model):
    codigo_tipo_ingreso = models.CharField(primary_key=True, max_length=3)
    descripcion = models.CharField(max_length=100)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_tipos_ingresos'


class CcTiposProcesosCartera(models.Model):
    codigo_tipo_proceso = models.IntegerField(primary_key=True)
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=300)
    observaciones = models.CharField(max_length=500, blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_tipos_procesos_cartera'
        unique_together = (('codigo_tipo_proceso', 'codigo_empresa'),)


class CcTiposRecaudadores(models.Model):
    codigo_tipo_recaudador = models.IntegerField(primary_key=True)
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=200)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_tipos_recaudadores'
        unique_together = (('codigo_tipo_recaudador', 'codigo_empresa'),)


class CcTiposRespuestas(models.Model):
    codigo_tipo_respuesta = models.IntegerField(primary_key=True)
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=100)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_tipos_respuestas'
        unique_together = (('codigo_tipo_respuesta', 'codigo_empresa'),)


class CcTiposVerificaciones(models.Model):
    codigo_tipo_verificacion = models.IntegerField(primary_key=True)
    codigo_empresa = models.ForeignKey(AdVerificaciones, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(unique=True, max_length=100)
    peso_maximo = models.DecimalField(max_digits=6, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_verificacion = models.ForeignKey(AdVerificaciones, models.DO_NOTHING, db_column='codigo_verificacion')
    es_referencia = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_tipos_verificaciones'
        unique_together = (('codigo_tipo_verificacion', 'codigo_verificacion', 'codigo_empresa'),)


class CcTiposVerificacionesPesos(models.Model):
    codigo_tipo_verificacion_peso = models.IntegerField(primary_key=True)
    codigo_tipo_verificacion = models.ForeignKey(CcTiposVerificaciones, models.DO_NOTHING, db_column='codigo_tipo_verificacion')
    codigo_empresa = models.ForeignKey(CcTiposVerificaciones, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_verificacion = models.ForeignKey(CcTiposVerificaciones, models.DO_NOTHING, db_column='codigo_verificacion')
    tiene_concepto = models.CharField(max_length=1)
    secuencia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cc_tipos_verificaciones_pesos'
        unique_together = (('codigo_tipo_verificacion_peso', 'codigo_tipo_verificacion', 'codigo_verificacion', 'codigo_empresa', 'secuencia'),)


class CcVentasResumen(models.Model):
    aniomes_venta = models.IntegerField(primary_key=True)
    cod_politica = models.IntegerField()
    cod_parroquia = models.CharField(max_length=8)
    cod_zona = models.CharField(max_length=3)
    cod_modelo = models.CharField(max_length=8)
    cod_agencia = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='cod_agencia')
    cod_empresa = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='cod_empresa')
    valor_venta = models.DecimalField(max_digits=14, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_ventas_resumen'
        unique_together = (('aniomes_venta', 'cod_politica', 'cod_parroquia', 'cod_zona', 'cod_agencia', 'cod_empresa'),)


class CcVitacoraEjecucionProcesos(models.Model):
    fecha_ejecucion = models.DateField()
    codigo_proceso = models.IntegerField()
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    cartera = models.CharField(max_length=3)
    estado = models.CharField(max_length=2)
    resultado = models.CharField(max_length=1000)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_vitacora_ejecucion_procesos'


class CoComproProcesadosSiembEtp(models.Model):
    cod_comprobante = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    codigo_canton = models.CharField(max_length=14)
    niv_cod_nivel_canton = models.CharField(max_length=8)
    niv_secuencia_canton = models.IntegerField()
    codigo_provincia = models.CharField(max_length=14)
    niv_cod_nivel_provincia = models.CharField(max_length=8)
    niv_secuencia_provincia = models.IntegerField()
    codigo_region = models.IntegerField()
    niv_cat_emp_empresa_canton = models.IntegerField()
    niv_cat_cod_categoria_canton = models.CharField(max_length=2)
    codigo_politica = models.IntegerField()
    codigo_nacion = models.IntegerField()
    codigo_agencia = models.IntegerField()
    periodo_cierre = models.IntegerField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'co_compro_procesados_siemb_etp'
        unique_together = (('cod_comprobante', 'tipo_comprobante', 'niv_cat_emp_empresa_canton'),)


class CoIndiceDeMorosidad(models.Model):
    periodo = models.IntegerField(primary_key=True)
    anio_mes_venta = models.IntegerField()
    codigo_cliente = models.CharField(max_length=14)
    codigo_canton = models.CharField(max_length=14)
    codigo_provincia = models.CharField(max_length=14)
    codigo_region = models.IntegerField()
    codigo_politica = models.IntegerField()
    cod_modelo_cat_linea = models.CharField(max_length=8)
    cod_item_cat_linea = models.CharField(max_length=3)
    cod_marca = models.IntegerField()
    codigo_nacion = models.IntegerField()
    codigo_empresa = models.IntegerField()
    nombre_canton = models.CharField(max_length=50)
    nombre_provincia = models.CharField(max_length=100)
    nombre_region = models.CharField(max_length=300)
    nombre_linea = models.CharField(max_length=50)
    nombre_marca = models.CharField(max_length=50)
    nombre_politica = models.CharField(max_length=100)
    nombre_cliente = models.CharField(max_length=255)
    valor_ventas = models.DecimalField(max_digits=30, decimal_places=2)
    saldo_cartera = models.DecimalField(max_digits=30, decimal_places=2)
    total_cartera_al_cierre = models.DecimalField(max_digits=30, decimal_places=2)
    valor_cobrado = models.DecimalField(max_digits=30, decimal_places=2)
    cartera_vencida = models.DecimalField(max_digits=30, decimal_places=2)
    porcentaje_productividad = models.DecimalField(max_digits=20, decimal_places=5)
    porcentaje_indice_morosidad = models.DecimalField(max_digits=20, decimal_places=5)
    pagos_anticipados = models.DecimalField(max_digits=30, decimal_places=2)
    mes_cerrado = models.CharField(max_length=1)
    fecha_ult_ejecucion = models.DateField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'co_indice_de_morosidad'
        unique_together = (('periodo', 'anio_mes_venta', 'codigo_cliente', 'codigo_canton', 'codigo_provincia', 'codigo_region', 'codigo_politica', 'cod_modelo_cat_linea', 'cod_item_cat_linea', 'cod_marca', 'codigo_nacion', 'codigo_empresa'),)


class CoParametrosPedidos(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    fecha_1 = models.DateField(blank=True, null=True)
    fecha_2 = models.DateField(blank=True, null=True)
    fecha_3 = models.DateField(blank=True, null=True)
    valor_1 = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    valor_2 = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    valor_3 = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'co_parametros_pedidos'


class CoPresupXVenLinMarDet(models.Model):
    periodo = models.IntegerField(primary_key=True)
    cod_persona = models.CharField(max_length=14)
    cod_item_linea = models.CharField(max_length=3)
    cod_marca = models.IntegerField()
    cod_modelo_linea = models.CharField(max_length=8)
    cod_tipo_persona = models.CharField(max_length=3)
    empresa = models.IntegerField()
    presupuesto_mensual = models.DecimalField(max_digits=30, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'co_presup_x_ven_lin_mar_det'
        unique_together = (('periodo', 'cod_persona', 'cod_item_linea', 'cod_marca', 'cod_modelo_linea', 'cod_tipo_persona', 'empresa'),)


class CoSiembraXVencimiento(models.Model):
    anio_mes_vencimiento = models.IntegerField(primary_key=True)
    anio_mes_venta = models.IntegerField()
    codigo_cliente = models.CharField(max_length=14)
    codigo_canton = models.CharField(max_length=14)
    codigo_provincia = models.CharField(max_length=14)
    codigo_region = models.IntegerField()
    codigo_politica = models.IntegerField()
    cod_modelo_cat_linea = models.CharField(max_length=8)
    cod_item_cat_linea = models.CharField(max_length=3)
    cod_marca = models.IntegerField()
    codigo_nacion = models.IntegerField()
    codigo_empresa = models.IntegerField()
    nombre_canton = models.CharField(max_length=50)
    nombre_provincia = models.CharField(max_length=100)
    nombre_region = models.CharField(max_length=300)
    nombre_linea = models.CharField(max_length=50)
    nombre_marca = models.CharField(max_length=50)
    nombre_politica = models.CharField(max_length=100)
    valor_vencimiento = models.DecimalField(max_digits=30, decimal_places=2)
    fecha_ult_ejecucion = models.DateField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    nombre_cliente = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'co_siembra_x_vencimiento'
        unique_together = (('anio_mes_vencimiento', 'anio_mes_venta', 'codigo_cliente', 'codigo_canton', 'codigo_provincia', 'codigo_region', 'codigo_politica', 'cod_modelo_cat_linea', 'cod_item_cat_linea', 'cod_marca', 'codigo_nacion', 'codigo_empresa'),)


class CoTempCodigosBuffer(models.Model):
    cod_producto = models.CharField(primary_key=True, max_length=14)
    empresa = models.IntegerField()
    nombre = models.CharField(max_length=50)
    buffer = models.DecimalField(max_digits=14, decimal_places=6, blank=True, null=True)
    porcentaje_negro = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    porcentaje_rojo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    porcentaje_amarillo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    porcentaje_verde = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    buffer_sugerido = models.DecimalField(max_digits=14, decimal_places=6, blank=True, null=True)
    fecha_ultimo_cambio = models.DateField(blank=True, null=True)
    proximo_cambio = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'co_temp_codigos_buffer'
        unique_together = (('cod_producto', 'empresa'),)


class CoTempDatosClientesMora(models.Model):
    cod_cliente = models.CharField(primary_key=True, max_length=14)
    empresa = models.IntegerField()
    codigo_parametro = models.CharField(max_length=3, blank=True, null=True)
    valor_1 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    valor_2 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    valor_3 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'co_temp_datos_clientes_mora'
        unique_together = (('cod_cliente', 'empresa'),)


class CoTempEdadesCartera(models.Model):
    anio_mes = models.IntegerField(primary_key=True)
    tipo_documento = models.CharField(max_length=2)
    empresa = models.IntegerField()
    valor = models.DecimalField(max_digits=13, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'co_temp_edades_cartera'
        unique_together = (('anio_mes', 'tipo_documento', 'empresa'),)


class CoTempFacturasPendientes(models.Model):
    cod_comprobante = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    cuota = models.IntegerField()
    secuencia = models.IntegerField()
    empresa = models.IntegerField()
    valor_cuota = models.DecimalField(max_digits=14, decimal_places=2)
    saldo_cuota = models.DecimalField(max_digits=14, decimal_places=2)
    fecha_cuota = models.DateField()
    cheque = models.CharField(max_length=20, blank=True, null=True)
    valor_cheque = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    fecha_deposito_cheque = models.DateField(blank=True, null=True)
    descripcion_cuota = models.CharField(max_length=10)
    descripcion_cheque = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'co_temp_facturas_pendientes'
        unique_together = (('cod_comprobante', 'tipo_comprobante', 'cuota', 'secuencia', 'empresa'),)


class CoTempKardexClientes(models.Model):
    cod_comprobante = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    cuota = models.IntegerField()
    secuencia = models.IntegerField()
    empresa = models.IntegerField()
    valor_cuota = models.DecimalField(max_digits=14, decimal_places=2)
    saldo_cuota = models.DecimalField(max_digits=14, decimal_places=2)
    fecha_cuota = models.DateField()
    tipo_pago = models.CharField(max_length=3, blank=True, null=True)
    cod_comprobante_pago = models.CharField(max_length=9, blank=True, null=True)
    tipo_comprobante_pago = models.CharField(max_length=2, blank=True, null=True)
    cod_banco = models.CharField(max_length=3, blank=True, null=True)
    che_let = models.CharField(max_length=20, blank=True, null=True)
    valor_pago = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    fecha_pago = models.DateField(blank=True, null=True)
    descripcion_cuota = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'co_temp_kardex_clientes'
        unique_together = (('cod_comprobante', 'tipo_comprobante', 'cuota', 'secuencia', 'empresa'),)


class CoTempMercaderiaDisponible(models.Model):
    cod_producto = models.CharField(primary_key=True, max_length=14)
    descripcion = models.CharField(max_length=100)
    empresa = models.IntegerField()
    valor = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'co_temp_mercaderia_disponible'
        unique_together = (('cod_producto', 'descripcion', 'empresa'),)


class CoTempVentasXMarcas(models.Model):
    anio_mes = models.IntegerField(primary_key=True)
    cod_marca = models.IntegerField()
    empresa = models.IntegerField()
    valor = models.DecimalField(max_digits=13, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'co_temp_ventas_x_marcas'
        unique_together = (('anio_mes', 'cod_marca', 'empresa'),)


class CoTiposNegociaciones(models.Model):
    cod_tipo_negociacion = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    activo = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'co_tipos_negociaciones'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class FpDefinicionDeProcesos(models.Model):
    codigo_proceso = models.IntegerField(primary_key=True)
    codigo_area = models.ForeignKey(CcAreaGestiones, models.DO_NOTHING, db_column='codigo_area')
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=500)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fp_definicion_de_procesos'
        unique_together = (('codigo_proceso', 'codigo_area', 'codigo_empresa'),)


class FpDiagramaFlujoDeProcesos(models.Model):
    secuencia_dfp = models.IntegerField(primary_key=True)
    codigo_proceso = models.ForeignKey('self', models.DO_NOTHING, db_column='codigo_proceso')
    codigo_area = models.ForeignKey('self', models.DO_NOTHING, db_column='codigo_area')
    codigo_empresa = models.ForeignKey('self', models.DO_NOTHING, db_column='codigo_empresa')
    codigo_simbolo = models.ForeignKey(AdSimbolosFlujoProcesos, models.DO_NOTHING, db_column='codigo_simbolo')
    descripcion_proceso = models.CharField(max_length=500)
    siguiente_proceso_verdadero = models.ForeignKey('self', models.DO_NOTHING, db_column='siguiente_proceso_verdadero')
    siguiente_proceso_falso = models.ForeignKey('self', models.DO_NOTHING, db_column='siguiente_proceso_falso', blank=True, null=True)
    duracion_proceso_horas = models.IntegerField()
    duracion_proceso_minutos = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fp_diagrama_flujo_de_procesos'
        unique_together = (('secuencia_dfp', 'codigo_proceso', 'codigo_area', 'codigo_empresa'),)


class FpListasDeControl(models.Model):
    codigo_lista_control = models.IntegerField(primary_key=True)
    codigo_empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='codigo_empresa')
    descripcion = models.CharField(max_length=100)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fp_listas_de_control'
        unique_together = (('codigo_lista_control', 'codigo_empresa'),)


class FpListasDeControlDeSalida(models.Model):
    secuencia_dfp = models.OneToOneField(FpDiagramaFlujoDeProcesos, models.DO_NOTHING, db_column='secuencia_dfp', primary_key=True)
    codigo_proceso = models.ForeignKey(FpDiagramaFlujoDeProcesos, models.DO_NOTHING, db_column='codigo_proceso')
    codigo_lista_control = models.ForeignKey(FpListasDeControl, models.DO_NOTHING, db_column='codigo_lista_control')
    codigo_area = models.ForeignKey(FpDiagramaFlujoDeProcesos, models.DO_NOTHING, db_column='codigo_area')
    codigo_empresa = models.ForeignKey(FpDiagramaFlujoDeProcesos, models.DO_NOTHING, db_column='codigo_empresa')
    obligatorio_si_no = models.CharField(max_length=1)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fp_listas_de_control_de_salida'
        unique_together = (('secuencia_dfp', 'codigo_proceso', 'codigo_lista_control', 'codigo_area', 'codigo_empresa'),)


class FpResponsablesDelDfp(models.Model):
    secuencia_dfp = models.OneToOneField(FpDiagramaFlujoDeProcesos, models.DO_NOTHING, db_column='secuencia_dfp', primary_key=True)
    codigo_proceso = models.ForeignKey(FpDiagramaFlujoDeProcesos, models.DO_NOTHING, db_column='codigo_proceso')
    identificacion_empleado = models.ForeignKey('RhEmpleados', models.DO_NOTHING, db_column='identificacion_empleado')
    codigo_area = models.ForeignKey(FpDiagramaFlujoDeProcesos, models.DO_NOTHING, db_column='codigo_area')
    codigo_agencia = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_agencia')
    codigo_empresa = models.ForeignKey(FpDiagramaFlujoDeProcesos, models.DO_NOTHING, db_column='codigo_empresa')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fp_responsables_del_dfp'
        unique_together = (('secuencia_dfp', 'codigo_proceso', 'identificacion_empleado', 'codigo_area', 'codigo_agencia', 'codigo_empresa'),)


class Nov2010StCentroCostoD(models.Model):
    cod_centro_costo = models.CharField(max_length=10)
    cod_centro_costo_detalle = models.CharField(primary_key=True, max_length=10)
    aa = models.IntegerField()
    empresa = models.IntegerField()
    porcentaje = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nov2010_st_centro_costo_d'
        unique_together = (('cod_centro_costo_detalle', 'cod_centro_costo', 'aa', 'empresa'),)


class ParametrosIrDiscapacidad(models.Model):
    desde = models.DecimalField(primary_key=True, max_digits=9, decimal_places=2)
    hasta = models.DecimalField(max_digits=9, decimal_places=2)
    porcentaje_beneficio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'parametros_ir_discapacidad'
        unique_together = (('desde', 'hasta', 'porcentaje_beneficio'),)


class PruebasCheques(models.Model):
    empresa = models.IntegerField(blank=True, null=True)
    cod_tipo_persona = models.CharField(max_length=3, blank=True, null=True)
    cod_persona = models.CharField(max_length=14, blank=True, null=True)
    cod_banco = models.CharField(max_length=3, blank=True, null=True)
    cheque = models.CharField(max_length=20, blank=True, null=True)
    numero_negociacion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pruebas_cheques'


class PruebasCheques2(models.Model):
    empresa = models.IntegerField(blank=True, null=True)
    cod_tipo_persona = models.CharField(max_length=3, blank=True, null=True)
    cod_persona = models.CharField(max_length=14, blank=True, null=True)
    cod_banco = models.CharField(max_length=3, blank=True, null=True)
    cheque = models.CharField(max_length=20, blank=True, null=True)
    numero_negociacion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pruebas_cheques2'


class PruebasCheques3(models.Model):
    empresa = models.IntegerField(blank=True, null=True)
    cod_tipo_persona = models.CharField(max_length=3, blank=True, null=True)
    cod_persona = models.CharField(max_length=14, blank=True, null=True)
    cod_banco = models.CharField(max_length=3, blank=True, null=True)
    cheque = models.CharField(max_length=20, blank=True, null=True)
    numero_negociacion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pruebas_cheques3'


class PruebasCheques4(models.Model):
    empresa = models.IntegerField(blank=True, null=True)
    cod_tipo_persona = models.CharField(max_length=3, blank=True, null=True)
    cod_persona = models.CharField(max_length=14, blank=True, null=True)
    cod_banco = models.CharField(max_length=3, blank=True, null=True)
    cheque = models.CharField(max_length=20, blank=True, null=True)
    numero_negociacion = models.IntegerField(blank=True, null=True)
    cod_persona_ban_ven = models.CharField(max_length=14, blank=True, null=True)
    cod_tipo_persona_ban_ven = models.CharField(max_length=3, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pruebas_cheques4'


class RhBase(models.Model):
    empresa = models.IntegerField(primary_key=True)
    ruc = models.CharField(max_length=13)
    periodo = models.CharField(max_length=4)
    tipo_id = models.CharField(max_length=1)
    identificacion = models.CharField(max_length=13)
    apellidos = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    establecimiento = models.CharField(max_length=3)
    residencia = models.CharField(max_length=2)
    pais_residencia = models.CharField(max_length=3)
    aplica_convenio = models.CharField(max_length=2)
    condicion = models.CharField(max_length=2)
    porcentaje_dis = models.IntegerField()
    tipo_id_dis = models.CharField(max_length=1)
    sueldos_salarios = models.DecimalField(max_digits=12, decimal_places=2)
    comisiones_bonos = models.DecimalField(max_digits=12, decimal_places=2)
    participa_utilidades = models.DecimalField(max_digits=12, decimal_places=2)
    ing_otros_emple = models.DecimalField(max_digits=12, decimal_places=2)
    imp_renta = models.DecimalField(max_digits=12, decimal_places=2)
    decimo_3ro = models.DecimalField(max_digits=12, decimal_places=2)
    decimo_4to = models.DecimalField(max_digits=12, decimal_places=2)
    fondos_reserva = models.DecimalField(max_digits=12, decimal_places=2)
    salario_digno = models.DecimalField(max_digits=12, decimal_places=2)
    otros_ing_sin_renta = models.DecimalField(max_digits=12, decimal_places=2)
    ingresos_gravados = models.DecimalField(max_digits=12, decimal_places=2)
    sistema_salario = models.BooleanField()
    aporte_personal = models.DecimalField(max_digits=12, decimal_places=2)
    aporte_personal_ot = models.DecimalField(max_digits=12, decimal_places=2)
    gp_vivienda = models.DecimalField(max_digits=12, decimal_places=2)
    gp_salud = models.DecimalField(max_digits=12, decimal_places=2)
    gp_educacion = models.DecimalField(max_digits=12, decimal_places=2)
    gp_alimentacion = models.DecimalField(max_digits=12, decimal_places=2)
    gp_vestimenta = models.DecimalField(max_digits=12, decimal_places=2)
    exoneracion_dis = models.DecimalField(max_digits=12, decimal_places=2)
    exoneracion_3raedad = models.DecimalField(max_digits=12, decimal_places=2)
    base_imponible = models.DecimalField(max_digits=12, decimal_places=2)
    imp_renta_causado = models.DecimalField(max_digits=12, decimal_places=2)
    imp_retenido_otr = models.DecimalField(max_digits=12, decimal_places=2)
    imp_asumido = models.DecimalField(max_digits=12, decimal_places=2)
    imp_retenido = models.DecimalField(max_digits=12, decimal_places=2)
    useridc = models.CharField(max_length=3)
    aud_fecha = models.DateField(blank=True, null=True)
    aud_usuario = models.CharField(max_length=30, blank=True, null=True)
    aud_terminal = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rh_base'
        unique_together = (('empresa', 'ruc', 'periodo'),)


class RhBeneficios(models.Model):
    empresa = models.IntegerField(primary_key=True)
    cod_beneficio = models.CharField(max_length=3)
    nombre = models.CharField(max_length=50)
    orden = models.IntegerField(blank=True, null=True)
    debito_credito = models.CharField(max_length=1, blank=True, null=True)
    proviciona = models.CharField(max_length=1, blank=True, null=True)
    impreso = models.CharField(max_length=1, blank=True, null=True)
    activo = models.CharField(max_length=1, blank=True, null=True)
    useridc = models.CharField(max_length=3, blank=True, null=True)
    aud_fecha = models.DateField(blank=True, null=True)
    aud_usuario = models.CharField(max_length=30, blank=True, null=True)
    aud_terminal = models.CharField(max_length=50, blank=True, null=True)
    acumulable = models.CharField(max_length=1, blank=True, null=True)
    codigo = models.CharField(max_length=14, blank=True, null=True)
    aa = models.IntegerField()
    ncorto = models.CharField(max_length=20, blank=True, null=True)
    clase = models.CharField(max_length=50, blank=True, null=True)
    grupo = models.CharField(max_length=100, blank=True, null=True)
    idgrupo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rh_beneficios'
        unique_together = (('empresa', 'cod_beneficio', 'aa'),)


class RhBeneficiosMm(models.Model):
    empresa = models.IntegerField(primary_key=True)
    cod_beneficio = models.CharField(max_length=3)
    nombre = models.CharField(max_length=50)
    orden = models.IntegerField(blank=True, null=True)
    debito_credito = models.CharField(max_length=1, blank=True, null=True)
    proviciona = models.CharField(max_length=1, blank=True, null=True)
    impreso = models.CharField(max_length=1, blank=True, null=True)
    activo = models.CharField(max_length=1, blank=True, null=True)
    useridc = models.CharField(max_length=3, blank=True, null=True)
    aud_fecha = models.DateField(blank=True, null=True)
    aud_usuario = models.CharField(max_length=30, blank=True, null=True)
    aud_terminal = models.CharField(max_length=50, blank=True, null=True)
    acumulable = models.CharField(max_length=1, blank=True, null=True)
    codigo = models.CharField(max_length=14, blank=True, null=True)
    aa = models.IntegerField()
    ncorto = models.CharField(max_length=20, blank=True, null=True)
    clase = models.CharField(max_length=50, blank=True, null=True)
    grupo = models.CharField(max_length=100, blank=True, null=True)
    idgrupo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rh_beneficios_mm'
        unique_together = (('empresa', 'cod_beneficio', 'aa'),)


class RhBeneficiosPersonal(models.Model):
    empresa = models.IntegerField(primary_key=True)
    cod_personal = models.CharField(max_length=14)
    cod_beneficio = models.CharField(max_length=3)
    cantidad = models.IntegerField(blank=True, null=True)
    valor = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    modificable = models.CharField(max_length=1, blank=True, null=True)
    activo = models.CharField(max_length=1, blank=True, null=True)
    useridc = models.CharField(max_length=3, blank=True, null=True)
    aud_fecha = models.DateField(blank=True, null=True)
    aud_usuario = models.CharField(max_length=30, blank=True, null=True)
    aud_terminal = models.CharField(max_length=50, blank=True, null=True)
    secuencia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rh_beneficios_personal'
        unique_together = (('empresa', 'cod_personal', 'cod_beneficio', 'secuencia'), ('empresa', 'cod_personal', 'cod_beneficio'),)


class RhCargoComision(models.Model):
    empresa = models.IntegerField(primary_key=True)
    cod_cargo = models.IntegerField()
    tramo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    activo = models.CharField(max_length=1)
    valor = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_adicion = models.DateField(blank=True, null=True)
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    cod_agencia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rh_cargo_comision'
        unique_together = (('empresa', 'cod_cargo', 'tramo', 'cod_agencia'),)


class RhCargos(models.Model):
    codigo_cargo = models.IntegerField(primary_key=True)
    codigo_empresa = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    activo = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_adicion = models.DateField(blank=True, null=True)
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    movilizacion = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rh_cargos'
        unique_together = (('codigo_cargo', 'codigo_empresa'), ('descripcion', 'codigo_empresa'),)


class RhComisiones(models.Model):
    empresa = models.IntegerField(primary_key=True)
    cod_comision = models.CharField(max_length=10)
    tramo = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    activo = models.CharField(max_length=1)
    rango_desde = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rango_hasta = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    valor = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_adicion = models.DateField(blank=True, null=True)
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rh_comisiones'
        unique_together = (('empresa', 'cod_comision'),)


class RhComprobante(models.Model):
    empresa = models.OneToOneField('RhPersonal', models.DO_NOTHING, db_column='empresa', primary_key=True)
    tipo_comprobante = models.CharField(max_length=2)
    cod_comprobante = models.CharField(max_length=9)
    cod_tipo_persona = models.ForeignKey('RhPersonal', models.DO_NOTHING, db_column='cod_tipo_persona')
    nombre_persona = models.CharField(max_length=40, blank=True, null=True)
    cod_persona = models.ForeignKey('RhPersonal', models.DO_NOTHING, db_column='cod_persona')
    fecha = models.DateField()
    cod_agente = models.CharField(max_length=14, blank=True, null=True)
    diastrabajados = models.DecimalField(max_digits=6, decimal_places=2)
    totalingresos = models.DecimalField(max_digits=14, decimal_places=2)
    totalegresos = models.DecimalField(max_digits=14, decimal_places=2)
    totalrol = models.DecimalField(max_digits=14, decimal_places=2)
    observaciones = models.CharField(max_length=2000, blank=True, null=True)
    anulado = models.CharField(max_length=1, blank=True, null=True)
    cod_liquidacion = models.CharField(max_length=9)
    useridc = models.CharField(max_length=3)
    aud_fecha = models.DateField(blank=True, null=True)
    aud_usuario = models.CharField(max_length=30, blank=True, null=True)
    aud_terminal = models.CharField(max_length=50, blank=True, null=True)
    estado_grabado = models.CharField(max_length=1, blank=True, null=True)
    estado_contabilizado = models.CharField(max_length=1, blank=True, null=True)
    cod_agencia = models.IntegerField()
    forma_pago = models.CharField(max_length=3, blank=True, null=True)
    cod_opago = models.CharField(max_length=9, blank=True, null=True)
    idsec = models.FloatField()
    diasvacaciones = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rh_comprobante'
        unique_together = (('fecha', 'cod_persona', 'idsec'), ('empresa', 'tipo_comprobante', 'cod_comprobante', 'cod_persona', 'idsec'),)


class RhCondicionDiscapacidad(models.Model):
    empresa = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'rh_condicion_discapacidad'
        unique_together = (('empresa', 'codigo'),)


class RhDepartamentos(models.Model):
    cod_departamento = models.IntegerField(primary_key=True)
    empresa = models.IntegerField()
    nombre = models.CharField(max_length=50)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rh_departamentos'
        unique_together = (('cod_departamento', 'empresa'),)


class RhEmpleados(models.Model):
    identificacion = models.CharField(primary_key=True, max_length=20)
    tipo_identificacion = models.BooleanField()
    apellido_paterno = models.CharField(max_length=25)
    apellido_materno = models.CharField(max_length=25)
    nombres = models.CharField(max_length=50)
    telefono1 = models.CharField(max_length=15, blank=True, null=True)
    telefono2 = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=100)
    numero_domicilio = models.CharField(max_length=10, blank=True, null=True)
    personeria = models.CharField(max_length=1)
    codigo_titulo = models.ForeignKey(AdTitulos, models.DO_NOTHING, db_column='codigo_titulo')
    activo = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rh_empleados'


class RhEmpleadosEmpresas(models.Model):
    identificacion = models.CharField(primary_key=True, max_length=14)
    codigo_agencia_emp = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_agencia_emp')
    codigo_empresa_emp = models.ForeignKey(AdAgencias, models.DO_NOTHING, db_column='codigo_empresa_emp')
    identificacion_jefe = models.ForeignKey(RhEmpleados, models.DO_NOTHING, db_column='identificacion_jefe', blank=True, null=True)
    codigo_departamento = models.IntegerField()
    codigo_cargo = models.ForeignKey(RhCargos, models.DO_NOTHING, db_column='codigo_cargo')
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField(blank=True, null=True)
    activo = models.CharField(max_length=1)
    email = models.CharField(max_length=100, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rh_empleados_empresas'
        unique_together = (('identificacion', 'codigo_empresa_emp', 'codigo_agencia_emp'),)


class RhFotosEmpleados(models.Model):
    identificacion = models.OneToOneField(RhEmpleados, models.DO_NOTHING, db_column='identificacion', primary_key=True)
    foto = models.BinaryField(blank=True, null=True)
    activo = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rh_fotos_empleados'


class RhHorarios(models.Model):
    empresa = models.IntegerField(primary_key=True)
    cod_tipo_persona = models.CharField(max_length=3)
    cod_persona = models.CharField(max_length=14)
    legado = models.CharField(max_length=4, blank=True, null=True)
    registro = models.IntegerField()
    dia = models.CharField(max_length=30)
    contratadas = models.DecimalField(max_digits=16, decimal_places=2)
    fechainicio = models.DateField(blank=True, null=True)
    fechafin = models.DateField(blank=True, null=True)
    activo = models.CharField(max_length=1)
    useridc = models.CharField(max_length=3, blank=True, null=True)
    aud_fecha = models.DateField(blank=True, null=True)
    aud_usuario = models.CharField(max_length=30, blank=True, null=True)
    aud_terminal = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rh_horarios'
        unique_together = (('empresa', 'cod_tipo_persona', 'cod_persona', 'registro', 'dia'),)


class RhMarcacion(models.Model):
    empresa = models.IntegerField(primary_key=True)
    cod_agencia = models.IntegerField()
    cod_persona = models.CharField(max_length=14)
    legado = models.CharField(max_length=14, blank=True, null=True)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    dia = models.CharField(max_length=15, blank=True, null=True)
    fecha = models.DateField()
    entrada1 = models.CharField(max_length=20, blank=True, null=True)
    salida1 = models.CharField(max_length=20, blank=True, null=True)
    horas1 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    entrada2 = models.CharField(max_length=20, blank=True, null=True)
    salida2 = models.CharField(max_length=20, blank=True, null=True)
    horas2 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    trabajadas = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    contratadas = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    extras = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    ordinarias = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    extraordinarias = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rh_marcacion'
        unique_together = (('empresa', 'cod_agencia', 'cod_persona', 'fecha'),)


class RhMarcacionJefeAgencia(models.Model):
    empresa = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=20)
    cod_agencias = models.IntegerField(blank=True, null=True)
    grupo_empresa = models.CharField(max_length=30, blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rh_marcacion_jefe_agencia'
        unique_together = (('empresa', 'usuario'),)


class RhMovimiento(models.Model):
    empresa = models.ForeignKey(RhComprobante, models.DO_NOTHING, db_column='empresa')
    tipo_comprobante = models.ForeignKey(RhComprobante, models.DO_NOTHING, db_column='tipo_comprobante')
    cod_comprobante = models.OneToOneField(RhComprobante, models.DO_NOTHING, db_column='cod_comprobante', primary_key=True)
    cod_tipo_persona = models.CharField(max_length=3)
    cod_beneficio = models.CharField(max_length=3)
    cod_persona = models.ForeignKey(RhComprobante, models.DO_NOTHING, db_column='cod_persona')
    secuencia = models.IntegerField()
    fecha = models.DateField()
    debito_credito = models.BooleanField()
    cantidad = models.DecimalField(max_digits=14, decimal_places=2)
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    idsec = models.ForeignKey(RhComprobante, models.DO_NOTHING, db_column='idsec')

    class Meta:
        managed = False
        db_table = 'rh_movimiento'
        unique_together = (('cod_comprobante', 'tipo_comprobante', 'empresa', 'cod_persona', 'cod_beneficio', 'idsec', 'debito_credito'),)


class RhPersonal(models.Model):
    empresa = models.OneToOneField(RhCargos, models.DO_NOTHING, db_column='empresa', primary_key=True)
    cod_personal = models.CharField(max_length=14)
    cod_tipo_persona = models.CharField(max_length=3)
    nombre = models.CharField(max_length=50)
    cod_departamento = models.IntegerField(blank=True, null=True)
    codigo_cargo = models.ForeignKey(RhCargos, models.DO_NOTHING, db_column='codigo_cargo', blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'rh_personal'
        unique_together = (('empresa', 'cod_tipo_persona', 'cod_personal'),)


class RhPersonalD(models.Model):
    empresa = models.OneToOneField(RhPersonal, models.DO_NOTHING, db_column='empresa', primary_key=True)
    cod_tipo_persona = models.ForeignKey(RhPersonal, models.DO_NOTHING, db_column='cod_tipo_persona')
    cod_personal = models.ForeignKey(RhPersonal, models.DO_NOTHING, db_column='cod_personal')
    cod_agencia = models.IntegerField()
    ingreso_por = models.CharField(max_length=40)
    reemplazode = models.CharField(max_length=14, blank=True, null=True)
    cod_cargo = models.IntegerField()
    descripcion_cargo = models.CharField(max_length=200)
    fcargo_desde = models.DateField()
    fcargo_hasta = models.DateField(blank=True, null=True)
    f_ingreso = models.DateField()
    f_egreso = models.DateField(blank=True, null=True)
    registro_actual = models.CharField(max_length=3)
    secuencia = models.IntegerField()
    usuario_modifica = models.CharField(max_length=30)
    motivo_salida = models.CharField(max_length=20, blank=True, null=True)
    fecha_aud = models.DateField()

    class Meta:
        managed = False
        db_table = 'rh_personal_d'
        unique_together = (('empresa', 'cod_personal', 'cod_tipo_persona', 'registro_actual', 'secuencia'),)


class RhPersonalEncuesta(models.Model):
    empresa = models.OneToOneField(RhPersonal, models.DO_NOTHING, db_column='empresa', primary_key=True)
    id_encuesta = models.CharField(max_length=20)
    cod_tipo_persona = models.ForeignKey(RhPersonal, models.DO_NOTHING, db_column='cod_tipo_persona')
    cod_persona = models.ForeignKey(RhPersonal, models.DO_NOTHING, db_column='cod_persona')
    ciudad_reg = models.CharField(max_length=40, blank=True, null=True)
    agencia_reg = models.CharField(max_length=50, blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    pregunta = models.CharField(max_length=500)
    respuesta = models.CharField(max_length=1000, blank=True, null=True)
    fecha_registro = models.DateField()
    fecha_aud = models.DateField(blank=True, null=True)
    fecha_ficha = models.DateField(blank=True, null=True)
    id_encuesta_fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rh_personal_encuesta'
        unique_together = (('empresa', 'id_encuesta', 'cod_tipo_persona', 'cod_persona', 'pregunta', 'fecha_registro'), ('id_encuesta', 'cod_persona', 'pregunta', 'fecha_ficha'),)


class RhPersonalInstruccion(models.Model):
    empresa = models.OneToOneField(RhPersonal, models.DO_NOTHING, db_column='empresa', primary_key=True)
    cod_personal = models.ForeignKey(RhPersonal, models.DO_NOTHING, db_column='cod_personal')
    cod_tipo_persona = models.ForeignKey(RhPersonal, models.DO_NOTHING, db_column='cod_tipo_persona')
    nivel_instruccion = models.CharField(max_length=20)
    institucion = models.CharField(max_length=40, blank=True, null=True)
    observacion = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rh_personal_instruccion'
        unique_together = (('empresa', 'cod_personal', 'cod_tipo_persona'),)


class RhPersonalJornada(models.Model):
    empresa = models.OneToOneField(RhPersonal, models.DO_NOTHING, db_column='empresa', primary_key=True)
    cod_tipo_persona = models.ForeignKey(RhPersonal, models.DO_NOTHING, db_column='cod_tipo_persona')
    cod_personal = models.ForeignKey(RhPersonal, models.DO_NOTHING, db_column='cod_personal')
    horas = models.FloatField()
    fdesde = models.DateField()
    fhasta = models.DateField()

    class Meta:
        managed = False
        db_table = 'rh_personal_jornada'
        unique_together = (('empresa', 'cod_personal', 'fdesde', 'fhasta'),)


class RhPersonalSs(models.Model):
    empresa = models.OneToOneField('RhSalarioSectorial', models.DO_NOTHING, db_column='empresa', primary_key=True)
    cod_personal = models.CharField(max_length=14)
    codigo_iess = models.ForeignKey('RhSalarioSectorial', models.DO_NOTHING, db_column='codigo_iess')
    aa = models.ForeignKey('RhSalarioSectorial', models.DO_NOTHING, db_column='aa')
    secuencia = models.IntegerField()
    fecha_reg = models.DateField(blank=True, null=True)
    valor = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    activo = models.CharField(max_length=1, blank=True, null=True)
    useridc = models.CharField(max_length=3, blank=True, null=True)
    aud_fecha = models.DateField(blank=True, null=True)
    aud_usuario = models.CharField(max_length=30, blank=True, null=True)
    aud_terminal = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rh_personal_ss'
        unique_together = (('empresa', 'cod_personal', 'codigo_iess', 'aa', 'secuencia'),)


class RhRegistroHoras(models.Model):
    empresa = models.IntegerField()
    registro = models.BigIntegerField()
    departamento = models.CharField(max_length=30)
    legado = models.CharField(max_length=14)
    nombre = models.CharField(max_length=50)
    fechahora = models.DateField()
    useridc = models.CharField(max_length=3, blank=True, null=True)
    aud_fecha = models.DateField(blank=True, null=True)
    aud_usuario = models.CharField(max_length=30, blank=True, null=True)
    aud_terminal = models.CharField(max_length=50, blank=True, null=True)
    latitud = models.CharField(max_length=50, blank=True, null=True)
    longitud = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rh_registro_horas'


class RhResidencia(models.Model):
    empresa = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'rh_residencia'
        unique_together = (('empresa', 'codigo'),)


class RhResidenciaTrabajador(models.Model):
    empresa = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'rh_residencia_trabajador'
        unique_together = (('empresa', 'codigo'),)


class RhResultadosEncuesta(models.Model):
    empresa = models.IntegerField(primary_key=True)
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
    id = models.FloatField(blank=True, null=True)
    condicion = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rh_resultados_encuesta'
        unique_together = (('empresa', 'id_encuesta', 'cod_persona', 'ficha'), ('empresa', 'id_encuesta', 'cod_tipo_persona', 'cod_persona'),)


class RhSalarioSectorial(models.Model):
    empresa = models.IntegerField(primary_key=True)
    anexo = models.CharField(max_length=10)
    concepto = models.CharField(max_length=200)
    aa = models.IntegerField()
    cargo = models.CharField(max_length=300)
    estructura = models.CharField(max_length=4)
    detalles = models.CharField(max_length=900, blank=True, null=True)
    codigo_iess = models.CharField(max_length=15)
    salariosectorial = models.DecimalField(max_digits=18, decimal_places=2)
    activo = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'rh_salario_sectorial'
        unique_together = (('empresa', 'aa', 'codigo_iess'), ('empresa', 'cargo', 'aa'),)


class RhTipoIdentificacion(models.Model):
    empresa = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=1)
    descripcion = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'rh_tipo_identificacion'
        unique_together = (('empresa', 'codigo'),)


class RhVacaciones(models.Model):
    empresa = models.OneToOneField(RhPersonal, models.DO_NOTHING, db_column='empresa', primary_key=True)
    cod_tipo_persona = models.ForeignKey(RhPersonal, models.DO_NOTHING, db_column='cod_tipo_persona')
    cod_persona = models.ForeignKey(RhPersonal, models.DO_NOTHING, db_column='cod_persona')
    periodo = models.CharField(max_length=9)
    dias_laborados = models.IntegerField(blank=True, null=True)
    dias_vacaciones = models.IntegerField(blank=True, null=True)
    aud_usuario = models.CharField(max_length=30)
    saldo_dias = models.IntegerField(blank=True, null=True)
    aud_fecha = models.DateField()
    fecha_ultimo_rol = models.DateField(blank=True, null=True)
    es_pagado = models.CharField(max_length=2, blank=True, null=True)
    dias_x_pagar = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rh_vacaciones'
        unique_together = (('empresa', 'cod_tipo_persona', 'cod_persona', 'periodo'),)


class RhVacacionesD(models.Model):
    empresa = models.OneToOneField(RhVacaciones, models.DO_NOTHING, db_column='empresa', primary_key=True)
    cod_tipo_persona = models.ForeignKey(RhVacaciones, models.DO_NOTHING, db_column='cod_tipo_persona')
    cod_personal = models.ForeignKey(RhVacaciones, models.DO_NOTHING, db_column='cod_personal')
    periodo = models.ForeignKey(RhVacaciones, models.DO_NOTHING, db_column='periodo')
    dias_vacaciones = models.IntegerField(blank=True, null=True)
    fdesde = models.DateField(blank=True, null=True)
    fhasta = models.DateField(blank=True, null=True)
    sec = models.FloatField()
    usuario_aud = models.CharField(max_length=30)
    aud_fecha = models.DateField()
    valor_x_pagar = models.FloatField()
    saldo = models.FloatField()

    class Meta:
        managed = False
        db_table = 'rh_vacaciones_d'
        unique_together = (('empresa', 'cod_tipo_persona', 'cod_personal', 'periodo', 'sec'),)


class RhVacacionesFp(models.Model):
    empresa = models.OneToOneField(RhComprobante, models.DO_NOTHING, db_column='empresa', primary_key=True)
    cod_tipo_persona = models.ForeignKey(RhVacacionesD, models.DO_NOTHING, db_column='cod_tipo_persona')
    cod_persona = models.ForeignKey(RhComprobante, models.DO_NOTHING, db_column='cod_persona')
    periodo = models.ForeignKey(RhVacacionesD, models.DO_NOTHING, db_column='periodo')
    empresa_rh = models.IntegerField()
    tipo_comprobante = models.ForeignKey(RhComprobante, models.DO_NOTHING, db_column='tipo_comprobante')
    cod_comprobante = models.ForeignKey(RhComprobante, models.DO_NOTHING, db_column='cod_comprobante')
    idsec_rh = models.ForeignKey(RhComprobante, models.DO_NOTHING, db_column='idsec_rh')
    sec = models.ForeignKey(RhVacacionesD, models.DO_NOTHING, db_column='sec')

    class Meta:
        managed = False
        db_table = 'rh_vacaciones_fp'
        unique_together = (('empresa', 'cod_tipo_persona', 'cod_persona', 'periodo', 'sec', 'cod_comprobante'),)


class SiCabeceraRequerimientos(models.Model):
    numero_requerimiento = models.BigIntegerField(primary_key=True)
    titulo_requerimiento = models.CharField(max_length=200)
    codigo_usuario_asignado = models.ForeignKey(AdUsuarios, models.DO_NOTHING, db_column='codigo_usuario_asignado')
    codigo_prioridad = models.ForeignKey('SiPrioridades', models.DO_NOTHING, db_column='codigo_prioridad')
    codigo_estado_requerimiento = models.ForeignKey('SiEstadosRequerimientos', models.DO_NOTHING, db_column='codigo_estado_requerimiento')
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    menu = models.ForeignKey('SiMenus', models.DO_NOTHING, db_column='menu', blank=True, null=True)
    forma = models.CharField(max_length=8, blank=True, null=True)
    codigo_agencia_solicitante = models.ForeignKey(AdUsuariosXAgencias, models.DO_NOTHING, db_column='codigo_agencia_solicitante')
    codigo_empresa_solicitante = models.ForeignKey(AdUsuariosXAgencias, models.DO_NOTHING, db_column='codigo_empresa_solicitante')
    codigo_usuario_solicitante = models.ForeignKey(AdUsuariosXAgencias, models.DO_NOTHING, db_column='codigo_usuario_solicitante')
    ultima_actualizacion_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_ultima_actualizacion = models.DateField(blank=True, null=True)
    codigo_tipo_asistencia = models.ForeignKey('SiTiposAsistencias', models.DO_NOTHING, db_column='codigo_tipo_asistencia', blank=True, null=True)
    codigo_error = models.CharField(max_length=30, blank=True, null=True)
    numero_requerimiento_anterior = models.ForeignKey('self', models.DO_NOTHING, db_column='numero_requerimiento_anterior', blank=True, null=True)
    numero_requerimiento_siguiente = models.ForeignKey('self', models.DO_NOTHING, db_column='numero_requerimiento_siguiente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'si_cabecera_requerimientos'


class SiDetalleRequerimientos(models.Model):
    numero_requerimiento = models.OneToOneField(SiCabeceraRequerimientos, models.DO_NOTHING, db_column='numero_requerimiento', primary_key=True)
    secuencia = models.IntegerField()
    accion = models.CharField(max_length=2000)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_tipo_solucion = models.ForeignKey('SiTiposSoluciones', models.DO_NOTHING, db_column='codigo_tipo_solucion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'si_detalle_requerimientos'
        unique_together = (('numero_requerimiento', 'secuencia'),)


class SiDuracionRequeriXPriorida(models.Model):
    numero_requerimiento = models.OneToOneField(SiCabeceraRequerimientos, models.DO_NOTHING, db_column='numero_requerimiento', primary_key=True)
    codigo_estado_requerimiento = models.ForeignKey('SiEstadosRequerimientos', models.DO_NOTHING, db_column='codigo_estado_requerimiento')
    codigo_prioridad = models.ForeignKey('SiPrioridades', models.DO_NOTHING, db_column='codigo_prioridad')
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'si_duracion_requeri_x_priorida'
        unique_together = (('numero_requerimiento', 'codigo_prioridad', 'codigo_estado_requerimiento'),)


class SiEstadosRequerimientos(models.Model):
    codigo_estado_requerimiento = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30)
    codigo_estado_requer_siguiente = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'si_estados_requerimientos'


class SiMenus(models.Model):
    menu = models.CharField(primary_key=True, max_length=40)
    descripcion = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'si_menus'


class SiPrioridades(models.Model):
    codigo_prioridad = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    duracion_dias_prioridad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'si_prioridades'


class SiSecuencias(models.Model):
    codigo_secuencia = models.IntegerField(primary_key=True)
    secuencia = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'si_secuencias'


class SiSolucionesAplicadas(models.Model):
    menu = models.OneToOneField(SiMenus, models.DO_NOTHING, db_column='menu', primary_key=True)
    forma = models.CharField(max_length=8)
    secuencia = models.IntegerField()
    titulo_requerimiento = models.CharField(max_length=200)
    solucion_aplicada = models.CharField(max_length=2000)
    codigo_usuario_asignado = models.ForeignKey(AdUsuarios, models.DO_NOTHING, db_column='codigo_usuario_asignado')
    codigo_usuario_solicitante = models.ForeignKey(AdUsuarios, models.DO_NOTHING, db_column='codigo_usuario_solicitante')
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'si_soluciones_aplicadas'
        unique_together = (('menu', 'forma', 'secuencia'),)


class SiTipoUsuarios(models.Model):
    codigo_tipo_usuario = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'si_tipo_usuarios'


class SiTiposAsistencias(models.Model):
    codigo_tipo_asistencia = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    es_activo = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'si_tipos_asistencias'


class SiTiposSoluciones(models.Model):
    codigo_tipo_solucion = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    es_activo = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'si_tipos_soluciones'


class SiUsuariosCall(models.Model):
    codigo_usuario = models.OneToOneField(AdUsuarios, models.DO_NOTHING, db_column='codigo_usuario', primary_key=True)
    codigo_tipo_usuario = models.ForeignKey(SiTipoUsuarios, models.DO_NOTHING, db_column='codigo_tipo_usuario')
    es_activo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'si_usuarios_call'


class StCategorias(models.Model):
    codigo_categoria = models.IntegerField(primary_key=True)
    codigo_empresa = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_categorias'
        unique_together = (('codigo_categoria', 'codigo_empresa'),)


class StCategoriasClientesLineas(models.Model):
    cod_item = models.CharField(primary_key=True, max_length=3)
    cod_modelo = models.CharField(max_length=8)
    cod_cat_cliente = models.CharField(max_length=8)
    empresa = models.IntegerField()
    num_cuotas = models.IntegerField()
    por_descuento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    es_anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_categorias_clientes_lineas'
        unique_together = (('cod_item', 'cod_modelo', 'cod_cat_cliente', 'empresa'),)


class StCategoriasProducto(models.Model):
    codigo_producto = models.CharField(primary_key=True, max_length=14)
    codigo_empresa = models.ForeignKey(StCategorias, models.DO_NOTHING, db_column='codigo_empresa')
    codigo_categoria = models.ForeignKey(StCategorias, models.DO_NOTHING, db_column='codigo_categoria')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_categorias_producto'
        unique_together = (('codigo_producto', 'codigo_empresa'),)


class StCategoriasPromocion(models.Model):
    cod_categoria_promocion = models.IntegerField(primary_key=True)
    empresa = models.IntegerField()
    descripcion_categoria = models.CharField(max_length=50)
    cantidad_minima = models.CharField(max_length=5)
    anulado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_categorias_promocion'
        unique_together = (('cod_categoria_promocion', 'empresa'),)


class StCategoriasTranspBodZona(models.Model):
    codigo_categoria = models.OneToOneField(StCategorias, models.DO_NOTHING, db_column='codigo_categoria', primary_key=True)
    codigo_transportista = models.ForeignKey('StTransportistas', models.DO_NOTHING, db_column='codigo_transportista')
    codigo_bodega_origen = models.IntegerField()
    zona_geografica = models.CharField(max_length=14)
    codigo_empresa = models.ForeignKey('StTransportistas', models.DO_NOTHING, db_column='codigo_empresa')
    valor_tarifa = models.DecimalField(max_digits=12, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_categorias_transp_bod_zona'
        unique_together = (('codigo_categoria', 'codigo_transportista', 'codigo_bodega_origen', 'zona_geografica', 'codigo_empresa'),)


class StClientesDescuento(models.Model):
    codigo_cliente = models.CharField(primary_key=True, max_length=14)
    codigo_empresa = models.IntegerField()
    porcentaje_descuento_linea = models.DecimalField(max_digits=5, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    codigo_modelo = models.CharField(max_length=8)
    codigo_item = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'st_clientes_descuento'
        unique_together = (('codigo_cliente', 'codigo_modelo', 'codigo_item', 'codigo_empresa'),)


class StClientesDescuentoProducto(models.Model):
    codigo_cliente = models.CharField(primary_key=True, max_length=14)
    codigo_producto = models.CharField(max_length=14)
    codigo_empresa = models.IntegerField()
    porcentaje_descuento_producto = models.DecimalField(max_digits=5, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_clientes_descuento_producto'
        unique_together = (('codigo_cliente', 'codigo_producto', 'codigo_empresa'),)


class StClientesMayoreo(models.Model):
    numero_encuesta = models.IntegerField(primary_key=True)
    codigo_cliente = models.CharField(max_length=14)
    empresa = models.IntegerField()
    telefono1 = models.CharField(max_length=9, blank=True, null=True)
    telefono2 = models.CharField(max_length=9, blank=True, null=True)
    telefono3 = models.CharField(max_length=9, blank=True, null=True)
    pregunta1 = models.CharField(max_length=300)
    cumplimiento_entrega = models.CharField(max_length=1, blank=True, null=True)
    precios_estables = models.CharField(max_length=1, blank=True, null=True)
    calidad = models.CharField(max_length=1, blank=True, null=True)
    promociones_comerciales = models.CharField(max_length=1, blank=True, null=True)
    variedad_modelos = models.CharField(max_length=1, blank=True, null=True)
    facilidades_pago = models.CharField(max_length=1, blank=True, null=True)
    garantia = models.CharField(max_length=1, blank=True, null=True)
    seguridad = models.CharField(max_length=1, blank=True, null=True)
    precio = models.CharField(max_length=1, blank=True, null=True)
    atencion_personalizada = models.CharField(max_length=1, blank=True, null=True)
    otra = models.CharField(max_length=200, blank=True, null=True)
    observacion = models.CharField(max_length=300, blank=True, null=True)
    pregunta2 = models.CharField(max_length=300, blank=True, null=True)
    calif_cumplimiento_entrega = models.BooleanField(blank=True, null=True)
    calif_facilidades_pago = models.BooleanField(blank=True, null=True)
    calif_precios_estables = models.BooleanField(blank=True, null=True)
    calif_garantia = models.BooleanField(blank=True, null=True)
    calif_calidad = models.BooleanField(blank=True, null=True)
    calif_seguridad = models.BooleanField(blank=True, null=True)
    calif_promociones_comerciales = models.BooleanField(blank=True, null=True)
    calif_precio = models.BooleanField(blank=True, null=True)
    fecha_volver_llamar = models.DateField(blank=True, null=True)
    encuestado = models.CharField(max_length=1)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    nombre_cliente = models.CharField(max_length=300, blank=True, null=True)
    ciudad = models.CharField(max_length=60, blank=True, null=True)
    zona_geografica = models.CharField(max_length=15, blank=True, null=True)
    provincia = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_clientes_mayoreo'
        unique_together = (('numero_encuesta', 'codigo_cliente', 'empresa'),)


class StClientesRetail(models.Model):
    numero_encuesta = models.IntegerField(primary_key=True)
    codigo_cliente = models.CharField(max_length=14)
    empresa = models.IntegerField()
    telefono1 = models.CharField(max_length=9, blank=True, null=True)
    telefono2 = models.CharField(max_length=9, blank=True, null=True)
    telefono3 = models.CharField(max_length=9, blank=True, null=True)
    pregunta1 = models.CharField(max_length=300)
    calidad = models.CharField(max_length=1, blank=True, null=True)
    servicio_cliente = models.CharField(max_length=1, blank=True, null=True)
    seguridad = models.CharField(max_length=1, blank=True, null=True)
    precio = models.CharField(max_length=1, blank=True, null=True)
    facilidades_pago = models.CharField(max_length=1, blank=True, null=True)
    garantia = models.CharField(max_length=1, blank=True, null=True)
    servicio_postventa = models.CharField(max_length=1, blank=True, null=True)
    variedad_modelos = models.CharField(max_length=1, blank=True, null=True)
    otra = models.CharField(max_length=200, blank=True, null=True)
    observacion = models.CharField(max_length=300, blank=True, null=True)
    pregunta2 = models.CharField(max_length=300)
    calif_calidad = models.BooleanField(blank=True, null=True)
    calif_servicio_cliente = models.BooleanField(blank=True, null=True)
    calif_seguridad = models.BooleanField(blank=True, null=True)
    calif_precio = models.BooleanField(blank=True, null=True)
    calif_facilidades_pago = models.BooleanField(blank=True, null=True)
    calif_garantia = models.BooleanField(blank=True, null=True)
    calif_servicio_post_venta = models.BooleanField(blank=True, null=True)
    fecha_volver_llamar = models.DateField(blank=True, null=True)
    encuestado = models.CharField(max_length=1)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    nombre_cliente = models.CharField(max_length=300, blank=True, null=True)
    ciudad = models.CharField(max_length=60, blank=True, null=True)
    zona_geografica = models.CharField(max_length=15, blank=True, null=True)
    provincia = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_clientes_retail'
        unique_together = (('numero_encuesta', 'codigo_cliente', 'empresa'),)


class StClientesUbicacionLocal(models.Model):
    numero_encuesta = models.IntegerField(primary_key=True)
    codigo_cliente = models.CharField(max_length=14)
    empresa = models.IntegerField()
    nombre_cliente = models.CharField(max_length=300, blank=True, null=True)
    provincia = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.CharField(max_length=60, blank=True, null=True)
    zona_geografica = models.CharField(max_length=15, blank=True, null=True)
    telefono1 = models.CharField(max_length=9, blank=True, null=True)
    telefono2 = models.CharField(max_length=9, blank=True, null=True)
    telefono3 = models.CharField(max_length=9, blank=True, null=True)
    pregunta1 = models.CharField(max_length=300)
    credito_rapido = models.CharField(max_length=1, blank=True, null=True)
    facilidades_de_pago = models.CharField(max_length=1, blank=True, null=True)
    buenos_precios = models.CharField(max_length=1, blank=True, null=True)
    garantia = models.CharField(max_length=1, blank=True, null=True)
    calidad = models.CharField(max_length=1, blank=True, null=True)
    seguridad = models.CharField(max_length=1, blank=True, null=True)
    promociones_comerciales = models.CharField(max_length=1, blank=True, null=True)
    cerca_de_su_hogar = models.CharField(max_length=1, blank=True, null=True)
    variedad_de_modelos = models.CharField(max_length=1, blank=True, null=True)
    atencion_personalizada = models.CharField(max_length=1, blank=True, null=True)
    otra = models.CharField(max_length=200, blank=True, null=True)
    pregunta2 = models.CharField(max_length=300)
    tipo_credito = models.CharField(max_length=1, blank=True, null=True)
    pregunta3 = models.CharField(max_length=300)
    calif_facilidades_pago = models.BooleanField(blank=True, null=True)
    calif_buenos_precios = models.BooleanField(blank=True, null=True)
    calif_garantia = models.BooleanField(blank=True, null=True)
    calif_calidad = models.BooleanField(blank=True, null=True)
    calif_seguridad = models.BooleanField(blank=True, null=True)
    calif_cerca_de_su_hogar = models.BooleanField(blank=True, null=True)
    calif_promociones_comerciales = models.BooleanField(blank=True, null=True)
    pregunta4 = models.CharField(max_length=300)
    calif_centro_de_la_ciudad = models.BooleanField(blank=True, null=True)
    calif_sector_coral_centro = models.BooleanField(blank=True, null=True)
    calif_sector_totoracocha = models.BooleanField(blank=True, null=True)
    calif_sector_mercado_9_octubre = models.BooleanField(blank=True, null=True)
    calif_sector_mercado_10_agosto = models.BooleanField(blank=True, null=True)
    pregunta5 = models.CharField(max_length=300)
    respuesta_pregunta5 = models.CharField(max_length=200, blank=True, null=True)
    pregunta6 = models.CharField(max_length=300)
    sony = models.CharField(max_length=1, blank=True, null=True)
    lg = models.CharField(max_length=1, blank=True, null=True)
    samsumg = models.CharField(max_length=1, blank=True, null=True)
    panasonic = models.CharField(max_length=1, blank=True, null=True)
    indurama = models.CharField(max_length=1, blank=True, null=True)
    mabe = models.CharField(max_length=1, blank=True, null=True)
    durex = models.CharField(max_length=1, blank=True, null=True)
    electrolux = models.CharField(max_length=1, blank=True, null=True)
    general_electric = models.CharField(max_length=1, blank=True, null=True)
    otra_marca = models.CharField(max_length=200, blank=True, null=True)
    pregunta7 = models.CharField(max_length=300)
    shineray = models.CharField(max_length=1, blank=True, null=True)
    daytona = models.CharField(max_length=1, blank=True, null=True)
    ranger = models.CharField(max_length=1, blank=True, null=True)
    motor_uno = models.CharField(max_length=1, blank=True, null=True)
    tunder = models.CharField(max_length=1, blank=True, null=True)
    tundra = models.CharField(max_length=1, blank=True, null=True)
    fecha_volver_llamar = models.DateField(blank=True, null=True)
    encuestado = models.CharField(max_length=1)
    anulado = models.CharField(max_length=1)
    observacion = models.CharField(max_length=400, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_clientes_ubicacion_local'
        unique_together = (('numero_encuesta', 'codigo_cliente', 'empresa'),)


class StClientesXZonas(models.Model):
    codigo_cliente = models.CharField(primary_key=True, max_length=14)
    zona_geografica = models.CharField(max_length=14)
    codigo_empresa = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_clientes_x_zonas'
        unique_together = (('codigo_cliente', 'zona_geografica', 'codigo_empresa'),)


class StClientesZonasP(models.Model):
    cod_cliente = models.CharField(max_length=14)
    empresa = models.ForeignKey('StVendedoresP', models.DO_NOTHING, db_column='empresa')
    nombre = models.CharField(max_length=255)
    cod_vendedor = models.ForeignKey('StVendedoresP', models.DO_NOTHING, db_column='cod_vendedor')
    cod_tipo_persona = models.ForeignKey('StVendedoresP', models.DO_NOTHING, db_column='cod_tipo_persona')
    direccion_calleh = models.CharField(max_length=200)
    codigo_ciudad = models.CharField(max_length=14)
    nombre_ciudad = models.CharField(max_length=50)
    telefono1h = models.CharField(max_length=15)
    cupo = models.DecimalField(max_digits=14, decimal_places=2)
    saldo = models.DecimalField(max_digits=14, decimal_places=2)
    saldo_sin_cuotas = models.DecimalField(max_digits=14, decimal_places=2)
    es_enviado = models.BooleanField()
    calle_transversal = models.CharField(max_length=50, blank=True, null=True)
    numero_casa = models.CharField(max_length=20, blank=True, null=True)
    empresa_trabajoh = models.CharField(max_length=50, blank=True, null=True)
    codigo_zona = models.ForeignKey('StZonasDespachos', models.DO_NOTHING, db_column='codigo_zona', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_clientes_zonas_p'


class StDescLineaPeriodoClie(models.Model):
    codigo_modelo = models.CharField(primary_key=True, max_length=8)
    codigo_item = models.CharField(max_length=3)
    periodo_inicial = models.DateField()
    periodo_final = models.DateField()
    codigo_cliente = models.CharField(max_length=14)
    cantidad_minima = models.DecimalField(max_digits=9, decimal_places=2)
    cantidad_maxima = models.DecimalField(max_digits=9, decimal_places=2)
    codigo_empresa = models.IntegerField()
    valor_descuento = models.DecimalField(max_digits=5, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    numero_meses = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'st_desc_linea_periodo_clie'
        unique_together = (('codigo_modelo', 'codigo_item', 'periodo_inicial', 'periodo_final', 'codigo_cliente', 'cantidad_minima', 'cantidad_maxima', 'numero_meses', 'codigo_empresa'),)


class StDescProductoPeriodoClie(models.Model):
    codigo_producto = models.CharField(primary_key=True, max_length=14)
    periodo_inicial = models.DateField()
    periodo_final = models.DateField()
    codigo_cliente = models.CharField(max_length=14)
    cantidad_minima = models.DecimalField(max_digits=9, decimal_places=2)
    cantidad_maxima = models.DecimalField(max_digits=9, decimal_places=2)
    codigo_empresa = models.IntegerField()
    valor_descuento = models.DecimalField(max_digits=5, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    numero_meses = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'st_desc_producto_periodo_clie'
        unique_together = (('codigo_producto', 'periodo_inicial', 'periodo_final', 'codigo_cliente', 'cantidad_minima', 'cantidad_maxima', 'numero_meses', 'codigo_empresa'),)


class StDescuentosPromocion(models.Model):
    codigo_descuento = models.IntegerField(primary_key=True)
    empresa = models.ForeignKey(StCategoriasPromocion, models.DO_NOTHING, db_column='empresa')
    cod_categoria_promocion = models.ForeignKey(StCategoriasPromocion, models.DO_NOTHING, db_column='cod_categoria_promocion')
    cantidad_inicial = models.IntegerField()
    cantidad_final = models.IntegerField()
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_descuentos_promocion'
        unique_together = (('codigo_descuento', 'empresa'),)


class StFacturasPedidos(models.Model):
    cod_comprobante = models.CharField(primary_key=True, max_length=9)
    cod_pedido = models.ForeignKey('StPedidosDetalles', models.DO_NOTHING, db_column='cod_pedido')
    secuencia_mov = models.IntegerField()
    secuencia_ped = models.ForeignKey('StPedidosDetalles', models.DO_NOTHING, db_column='secuencia_ped')
    tipo_comprobante = models.CharField(max_length=2)
    cod_tipo_pedido = models.ForeignKey('StPedidosDetalles', models.DO_NOTHING, db_column='cod_tipo_pedido')
    empresa = models.ForeignKey('StPedidosDetalles', models.DO_NOTHING, db_column='empresa')
    es_anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    es_venta_o_garantia = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_facturas_pedidos'
        unique_together = (('cod_comprobante', 'cod_pedido', 'secuencia_mov', 'secuencia_ped', 'tipo_comprobante', 'cod_tipo_pedido', 'empresa'),)


class StGuiaRemision(models.Model):
    cod_guia = models.CharField(primary_key=True, max_length=9)
    tipo_guia = models.CharField(max_length=2)
    cod_comprobante = models.CharField(max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    empresa = models.IntegerField()
    cod_transportista = models.IntegerField()
    placa = models.CharField(max_length=9)
    cod_chofer = models.CharField(max_length=14)
    fecha_guia = models.DateField()
    cod_agencia = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    zona_geografica = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_guia_remision'
        unique_together = (('cod_guia', 'tipo_guia', 'cod_comprobante', 'tipo_comprobante', 'empresa'),)


class StItemsPromocion(models.Model):
    empresa = models.OneToOneField(StCategoriasPromocion, models.DO_NOTHING, db_column='empresa', primary_key=True)
    cod_producto = models.CharField(max_length=14)
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    cod_categoria_promocion = models.ForeignKey(StCategoriasPromocion, models.DO_NOTHING, db_column='cod_categoria_promocion')
    requerido = models.CharField(max_length=1)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_items_promocion'
        unique_together = (('empresa', 'cod_producto'),)


class StObservacionesCltesCartera(models.Model):
    cod_persona = models.CharField(primary_key=True, max_length=14)
    cod_tipo_persona = models.CharField(max_length=3)
    secuencia = models.IntegerField()
    empresa = models.IntegerField()
    fecha = models.DateField(blank=True, null=True)
    observacion = models.CharField(max_length=1000, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_observaciones_cltes_cartera'
        unique_together = (('cod_persona', 'cod_tipo_persona', 'secuencia', 'empresa'),)


class StParametrosAsterisk(models.Model):
    codigo_asterisk = models.CharField(primary_key=True, max_length=14)
    ip_asterisk = models.CharField(max_length=15, blank=True, null=True)
    puerto_asterisk = models.CharField(max_length=5, blank=True, null=True)
    usuario_asterisk = models.CharField(max_length=50, blank=True, null=True)
    pass_asterisk = models.CharField(max_length=10, blank=True, null=True)
    contexto_interno = models.CharField(max_length=100, blank=True, null=True)
    contexto_externo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_parametros_asterisk'


class StPedidosArroba(models.Model):
    cod_pedido = models.OneToOneField('StPedidosCabeceras', models.DO_NOTHING, db_column='cod_pedido', primary_key=True)
    cod_tipo_pedido = models.ForeignKey('StPedidosCabeceras', models.DO_NOTHING, db_column='cod_tipo_pedido')
    empresa = models.ForeignKey('StPedidosCabeceras', models.DO_NOTHING, db_column='empresa')
    fecha = models.DateField(blank=True, null=True)
    transferencia = models.CharField(max_length=50, blank=True, null=True)
    transporte = models.CharField(max_length=30, blank=True, null=True)
    procesado = models.CharField(max_length=1)
    aprobado = models.CharField(max_length=1)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    observaciones = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_pedidos_arroba'
        unique_together = (('cod_pedido', 'cod_tipo_pedido', 'empresa'),)


class StPedidosCabeceras(models.Model):
    cod_pedido = models.CharField(primary_key=True, max_length=9)
    cod_tipo_pedido = models.CharField(max_length=2)
    empresa = models.IntegerField()
    fecha_pedido = models.DateField()
    cod_tipo_persona_ven = models.CharField(max_length=3)
    cod_persona_ven = models.CharField(max_length=14)
    cod_tipo_persona_cli = models.CharField(max_length=3)
    cod_persona_cli = models.CharField(max_length=14)
    observaciones = models.CharField(max_length=250, blank=True, null=True)
    cod_agencia = models.IntegerField()
    direccion_envio = models.CharField(max_length=250, blank=True, null=True)
    ciudad = models.CharField(max_length=30)
    cod_politica = models.IntegerField()
    transporte = models.CharField(max_length=30, blank=True, null=True)
    comprobante_manual = models.CharField(max_length=9)
    cod_liquidacion = models.CharField(max_length=9)
    valor_pedido = models.DecimalField(max_digits=14, decimal_places=2)
    es_aprobado_ven = models.CharField(max_length=1)
    es_aprobado_car = models.CharField(max_length=1)
    es_pendiente = models.CharField(max_length=1)
    es_bloqueado = models.CharField(max_length=1)
    es_anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    es_facturado = models.CharField(max_length=1)
    cod_bodega_despacho = models.IntegerField()
    telefono = models.BigIntegerField(blank=True, null=True)
    dias_validez = models.IntegerField()
    estado_anterior = models.CharField(max_length=3, blank=True, null=True)
    revisado = models.CharField(max_length=1, blank=True, null=True)
    financiamiento = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    es_venta_garantia = models.CharField(max_length=1, blank=True, null=True)
    es_pedido_repuestos = models.CharField(max_length=1, blank=True, null=True)
    codigo_transportista = models.IntegerField(blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    tipo_pedido = models.CharField(max_length=1, blank=True, null=True)
    ice = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    es_pedido_temporada = models.CharField(max_length=1, blank=True, null=True)
    tiene_ice = models.CharField(max_length=1, blank=True, null=True)
    cod_pedido_ejecutivo = models.CharField(max_length=9, blank=True, null=True)
    usuario_ejecutivo = models.CharField(max_length=30, blank=True, null=True)
    zona_geografica = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_pedidos_cabeceras'
        unique_together = (('cod_pedido', 'cod_tipo_pedido', 'empresa'),)


class StPedidosCabecerasP(models.Model):
    cod_pedido = models.CharField(primary_key=True, max_length=9)
    cod_tipo_pedido = models.CharField(max_length=2)
    empresa = models.ForeignKey('StVendedoresP', models.DO_NOTHING, db_column='empresa')
    cod_vendedor = models.ForeignKey('StVendedoresP', models.DO_NOTHING, db_column='cod_vendedor')
    cod_tipo_persona = models.ForeignKey('StVendedoresP', models.DO_NOTHING, db_column='cod_tipo_persona')
    fecha_visita = models.DateField()
    fecha_pedido = models.DateField()
    cod_politica = models.IntegerField()
    cod_cliente = models.CharField(max_length=14)
    direccion_envio = models.CharField(max_length=150)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    ciudad = models.CharField(max_length=30)
    observaciones = models.CharField(max_length=150, blank=True, null=True)
    bodega = models.IntegerField()
    transporte = models.CharField(max_length=30, blank=True, null=True)
    comprobante_manual = models.CharField(max_length=9, blank=True, null=True)
    es_enviado = models.BooleanField()
    valor_pedido = models.DecimalField(max_digits=14, decimal_places=2)
    es_pedido_repuestos = models.CharField(max_length=1, blank=True, null=True)
    codigo_transportista = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_pedidos_cabeceras_p'
        unique_together = (('cod_pedido', 'cod_tipo_pedido', 'empresa', 'fecha_visita', 'fecha_pedido', 'cod_vendedor'),)


class StPedidosCabecerasVendedor(models.Model):
    cod_pedido = models.CharField(max_length=9)
    cod_tipo_pedido = models.CharField(max_length=2)
    empresa = models.IntegerField()
    fecha_pedido = models.DateField()
    cod_tipo_persona_ven = models.CharField(max_length=3)
    cod_persona_ven = models.CharField(max_length=14)
    cod_tipo_persona_cli = models.CharField(max_length=3)
    cod_persona_cli = models.CharField(max_length=14)
    observaciones = models.CharField(max_length=250, blank=True, null=True)
    cod_agencia = models.IntegerField()
    direccion_envio = models.CharField(max_length=250, blank=True, null=True)
    ciudad = models.CharField(max_length=30)
    cod_politica = models.IntegerField()
    transporte = models.CharField(max_length=30, blank=True, null=True)
    comprobante_manual = models.CharField(max_length=9)
    cod_liquidacion = models.CharField(max_length=9)
    valor_pedido = models.DecimalField(max_digits=14, decimal_places=2)
    es_aprobado_ven = models.CharField(max_length=1)
    es_aprobado_car = models.CharField(max_length=1)
    es_pendiente = models.CharField(max_length=1)
    es_bloqueado = models.CharField(max_length=1)
    es_anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    es_facturado = models.CharField(max_length=1)
    cod_bodega_despacho = models.IntegerField()
    telefono = models.BigIntegerField(blank=True, null=True)
    dias_validez = models.IntegerField()
    estado_anterior = models.CharField(max_length=3, blank=True, null=True)
    revisado = models.CharField(max_length=1, blank=True, null=True)
    financiamiento = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    es_venta_garantia = models.CharField(max_length=1, blank=True, null=True)
    es_pedido_repuestos = models.CharField(max_length=1, blank=True, null=True)
    codigo_transportista = models.IntegerField(blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    tipo_pedido = models.CharField(max_length=1, blank=True, null=True)
    ice = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    es_pedido_temporada = models.CharField(max_length=1, blank=True, null=True)
    tiene_ice = models.CharField(max_length=1, blank=True, null=True)
    cod_pedido_ejecutivo = models.CharField(max_length=9, blank=True, null=True)
    usuario_ejecutivo = models.CharField(max_length=30, blank=True, null=True)
    secuencia_ejecutivo = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'st_pedidos_cabeceras_vendedor'
        unique_together = (('secuencia_ejecutivo', 'cod_pedido', 'cod_tipo_pedido', 'empresa'),)


class StPedidosDespachos(models.Model):
    cod_pedido = models.OneToOneField(StPedidosCabeceras, models.DO_NOTHING, db_column='cod_pedido', primary_key=True)
    cod_tipo_pedido = models.ForeignKey(StPedidosCabeceras, models.DO_NOTHING, db_column='cod_tipo_pedido')
    empresa = models.ForeignKey('StTransportistas', models.DO_NOTHING, db_column='empresa')
    estado_pedido = models.CharField(max_length=1)
    es_anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    zona_geografica = models.CharField(max_length=15, blank=True, null=True)
    codigo_transportista = models.ForeignKey('StTransportistas', models.DO_NOTHING, db_column='codigo_transportista', blank=True, null=True)
    enviado_a_bodega = models.CharField(max_length=1, blank=True, null=True)
    cod_agencia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_pedidos_despachos'
        unique_together = (('cod_pedido', 'cod_tipo_pedido', 'empresa'),)


class StPedidosDespachosDetalle(models.Model):
    cod_pedido = models.OneToOneField(StPedidosDespachos, models.DO_NOTHING, db_column='cod_pedido', primary_key=True)
    secuencia = models.IntegerField()
    cod_tipo_pedido = models.ForeignKey(StPedidosDespachos, models.DO_NOTHING, db_column='cod_tipo_pedido')
    empresa = models.ForeignKey(StPedidosDespachos, models.DO_NOTHING, db_column='empresa')
    cod_producto = models.CharField(max_length=14)
    cantidad_enviada = models.DecimalField(max_digits=9, decimal_places=2)
    cantidad_despachada = models.DecimalField(max_digits=9, decimal_places=2)
    es_anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_pedidos_despachos_detalle'
        unique_together = (('cod_pedido', 'secuencia', 'cod_tipo_pedido', 'empresa'),)


class StPedidosDetalles(models.Model):
    cod_pedido = models.OneToOneField(StPedidosCabeceras, models.DO_NOTHING, db_column='cod_pedido', primary_key=True)
    secuencia = models.IntegerField()
    cod_tipo_pedido = models.ForeignKey(StPedidosCabeceras, models.DO_NOTHING, db_column='cod_tipo_pedido')
    empresa = models.ForeignKey(StPedidosCabeceras, models.DO_NOTHING, db_column='empresa')
    cod_producto = models.CharField(max_length=14)
    cantidad_pedida = models.DecimalField(max_digits=9, decimal_places=2)
    cantidad_despachada = models.DecimalField(max_digits=9, decimal_places=2)
    es_pendiente = models.CharField(max_length=1)
    es_anulado = models.CharField(max_length=1)
    precio = models.DecimalField(max_digits=14, decimal_places=2)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cod_tipo_producto = models.CharField(max_length=1, blank=True, null=True)
    cod_agencia = models.IntegerField()
    color = models.CharField(max_length=15, blank=True, null=True)
    num_cuotas = models.IntegerField()
    plazo = models.IntegerField()
    financiamiento = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    precio_lista = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    precio_descontado = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porcentaje_interes = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    valor_iva = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    valor_linea = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cantidad_producida = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    ice = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    valor_tarifa = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    peso = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_pedidos_detalles'
        unique_together = (('cod_pedido', 'secuencia', 'cod_tipo_pedido', 'empresa'),)


class StPedidosDetallesP(models.Model):
    cod_pedido = models.OneToOneField(StPedidosCabecerasP, models.DO_NOTHING, db_column='cod_pedido', primary_key=True)
    cod_tipo_pedido = models.ForeignKey(StPedidosCabecerasP, models.DO_NOTHING, db_column='cod_tipo_pedido')
    secuencia = models.IntegerField()
    empresa = models.ForeignKey(StPedidosCabecerasP, models.DO_NOTHING, db_column='empresa')
    fecha_visita = models.ForeignKey(StPedidosCabecerasP, models.DO_NOTHING, db_column='fecha_visita')
    fecha_pedido = models.ForeignKey(StPedidosCabecerasP, models.DO_NOTHING, db_column='fecha_pedido')
    cod_vendedor = models.ForeignKey(StPedidosCabecerasP, models.DO_NOTHING, db_column='cod_vendedor')
    cod_producto = models.CharField(max_length=14)
    cantidad_pedida = models.DecimalField(max_digits=9, decimal_places=2)
    es_pendiente = models.CharField(max_length=1)
    color = models.CharField(max_length=15)
    numero_cuotas = models.IntegerField()
    precio = models.DecimalField(max_digits=14, decimal_places=2)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    plazo = models.IntegerField()
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    financiamiento = models.DecimalField(max_digits=14, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'st_pedidos_detalles_p'
        unique_together = (('cod_pedido', 'cod_tipo_pedido', 'empresa', 'secuencia', 'fecha_visita', 'fecha_pedido', 'cod_vendedor'),)


class StPedidosDetallesVendedor(models.Model):
    cod_pedido = models.ForeignKey(StPedidosCabecerasVendedor, models.DO_NOTHING, db_column='cod_pedido')
    secuencia = models.IntegerField()
    cod_tipo_pedido = models.ForeignKey(StPedidosCabecerasVendedor, models.DO_NOTHING, db_column='cod_tipo_pedido')
    empresa = models.ForeignKey(StPedidosCabecerasVendedor, models.DO_NOTHING, db_column='empresa')
    cod_producto = models.CharField(max_length=14)
    cantidad_pedida = models.DecimalField(max_digits=9, decimal_places=2)
    cantidad_despachada = models.DecimalField(max_digits=9, decimal_places=2)
    es_pendiente = models.CharField(max_length=1)
    es_anulado = models.CharField(max_length=1)
    precio = models.DecimalField(max_digits=14, decimal_places=2)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cod_tipo_producto = models.CharField(max_length=1, blank=True, null=True)
    cod_agencia = models.IntegerField()
    color = models.CharField(max_length=15, blank=True, null=True)
    num_cuotas = models.IntegerField()
    plazo = models.IntegerField()
    financiamiento = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    precio_lista = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    precio_descontado = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    porcentaje_interes = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    valor_iva = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    valor_linea = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cantidad_producida = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    ice = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    secuencia_ejecutivo = models.OneToOneField(StPedidosCabecerasVendedor, models.DO_NOTHING, db_column='secuencia_ejecutivo', primary_key=True)

    class Meta:
        managed = False
        db_table = 'st_pedidos_detalles_vendedor'
        unique_together = (('secuencia_ejecutivo', 'cod_pedido', 'secuencia', 'cod_tipo_pedido', 'empresa'),)


class StPedidosObservaciones(models.Model):
    cod_pedido = models.OneToOneField(StPedidosCabeceras, models.DO_NOTHING, db_column='cod_pedido', primary_key=True)
    cod_tipo_pedido = models.ForeignKey(StPedidosCabeceras, models.DO_NOTHING, db_column='cod_tipo_pedido')
    tipo_observacion = models.CharField(max_length=3)
    empresa = models.ForeignKey(StPedidosCabeceras, models.DO_NOTHING, db_column='empresa')
    observacion = models.CharField(max_length=3000, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    fecha_observacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_pedidos_observaciones'
        unique_together = (('cod_pedido', 'cod_tipo_pedido', 'tipo_observacion', 'empresa'),)


class StPerfilRiesgo(models.Model):
    empresa = models.IntegerField()
    tipo_comprobante = models.CharField(max_length=2)
    cod_registro = models.CharField(max_length=9)
    cod_cliente = models.CharField(max_length=14)
    nom_cliente = models.CharField(max_length=50, blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    puntuacion_tot = models.DecimalField(max_digits=6, decimal_places=2)
    puntuacion_cli50 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    puntuacion_prod50 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_perfil_riesgo'


class StPermisosRepoExcel(models.Model):
    usuario_oracle = models.CharField(max_length=20)
    reporte = models.CharField(primary_key=True, max_length=10)
    activo = models.CharField(max_length=1)
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'st_permisos_repo_excel'
        unique_together = (('reporte', 'empresa', 'usuario_oracle'),)


class StProductosCuotaCero(models.Model):
    cod_producto = models.CharField(primary_key=True, max_length=14)
    empresa = models.IntegerField()
    es_anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_productos_cuota_cero'
        unique_together = (('cod_producto', 'empresa'),)


class StProductosP(models.Model):
    cod_producto = models.CharField(primary_key=True, max_length=14)
    empresa = models.IntegerField()
    nombre = models.CharField(max_length=200)
    cod_unidad = models.CharField(max_length=8)
    precio = models.DecimalField(max_digits=14, decimal_places=2)
    stock = models.DecimalField(max_digits=14, decimal_places=2)
    activo = models.CharField(max_length=1, blank=True, null=True)
    numero_cuotas = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'st_productos_p'
        unique_together = (('cod_producto', 'empresa'),)


class StProductosRemplazos(models.Model):
    cod_producto = models.CharField(primary_key=True, max_length=14)
    empresa = models.IntegerField()
    cod_producto_remplazo = models.CharField(max_length=14)
    es_anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    precio_generado = models.CharField(max_length=1, blank=True, null=True)
    precio_jaher = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_electropolis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_productos_remplazos'
        unique_together = (('cod_producto', 'cod_producto_remplazo', 'empresa'),)


class StReciboCobranzaCab(models.Model):
    cod_recibo = models.CharField(primary_key=True, max_length=9)
    cod_tipo_recibo = models.CharField(max_length=2)
    empresa = models.IntegerField()
    fecha = models.DateField()
    cod_tipo_persona_ven = models.CharField(max_length=3)
    cod_persona_ven = models.CharField(max_length=14)
    cod_tipo_persona_cli = models.CharField(max_length=3)
    cod_persona_cli = models.CharField(max_length=14)
    observaciones = models.CharField(max_length=250, blank=True, null=True)
    ciudad = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    cod_agencia = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    procesado = models.CharField(max_length=1)
    cod_recibo_ejecutivo = models.CharField(max_length=9, blank=True, null=True)
    usuario_ejecutivo = models.CharField(max_length=30, blank=True, null=True)
    es_cheque = models.CharField(max_length=1, blank=True, null=True)
    secuencia_ejecutivo = models.IntegerField(blank=True, null=True)
    cod_tipo_recibo_ejecutivo = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_recibo_cobranza_cab'
        unique_together = (('cod_recibo', 'cod_tipo_recibo', 'empresa'),)


class StReciboCobranzaCabEjec(models.Model):
    cod_recibo = models.CharField(max_length=9)
    cod_tipo_recibo = models.CharField(max_length=2)
    empresa = models.IntegerField()
    fecha = models.DateField()
    cod_tipo_persona_ven = models.CharField(max_length=3)
    cod_persona_ven = models.CharField(max_length=14)
    cod_tipo_persona_cli = models.CharField(max_length=3)
    cod_persona_cli = models.CharField(max_length=14)
    observaciones = models.CharField(max_length=250, blank=True, null=True)
    ciudad = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    cod_agencia = models.IntegerField()
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    procesado = models.CharField(max_length=1)
    secuencia_ejecutivo = models.IntegerField(primary_key=True)
    usuario_ejecutivo = models.CharField(max_length=30, blank=True, null=True)
    es_cheque = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_recibo_cobranza_cab_ejec'
        unique_together = (('secuencia_ejecutivo', 'cod_recibo', 'cod_tipo_recibo', 'empresa'),)


class StReciboCobranzaCheques(models.Model):
    cod_recibo = models.OneToOneField(StReciboCobranzaCab, models.DO_NOTHING, db_column='cod_recibo', primary_key=True)
    secuencia = models.IntegerField()
    cod_tipo_recibo = models.ForeignKey(StReciboCobranzaCab, models.DO_NOTHING, db_column='cod_tipo_recibo')
    empresa = models.ForeignKey(StReciboCobranzaCab, models.DO_NOTHING, db_column='empresa')
    cheque_deposito = models.CharField(max_length=14)
    cod_banco = models.CharField(max_length=3)
    cuenta_corriente = models.CharField(max_length=15)
    fecha_deposito = models.DateField()
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_recibo_cobranza_cheques'
        unique_together = (('cod_recibo', 'secuencia', 'cod_tipo_recibo', 'empresa'),)


class StReciboCobranzaChequesEje(models.Model):
    cod_recibo = models.ForeignKey(StReciboCobranzaCabEjec, models.DO_NOTHING, db_column='cod_recibo')
    secuencia = models.IntegerField()
    cod_tipo_recibo = models.ForeignKey(StReciboCobranzaCabEjec, models.DO_NOTHING, db_column='cod_tipo_recibo')
    empresa = models.ForeignKey(StReciboCobranzaCabEjec, models.DO_NOTHING, db_column='empresa')
    cheque_deposito = models.CharField(max_length=14)
    cod_banco = models.CharField(max_length=3)
    cuenta_corriente = models.CharField(max_length=15)
    fecha_deposito = models.DateField()
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    secuencia_ejecutivo = models.OneToOneField(StReciboCobranzaCabEjec, models.DO_NOTHING, db_column='secuencia_ejecutivo', primary_key=True)

    class Meta:
        managed = False
        db_table = 'st_recibo_cobranza_cheques_eje'
        unique_together = (('secuencia_ejecutivo', 'cod_recibo', 'secuencia', 'cod_tipo_recibo', 'empresa'),)


class StReciboCobranzaDet(models.Model):
    cod_recibo = models.CharField(primary_key=True, max_length=9)
    secuencia = models.IntegerField()
    cod_tipo_recibo = models.CharField(max_length=2)
    empresa = models.IntegerField()
    cod_comprobante = models.CharField(max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    tipo_retencion = models.CharField(max_length=1, blank=True, null=True)
    retencion = models.CharField(max_length=9, blank=True, null=True)
    valor_retencion = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    observacion = models.CharField(max_length=500, blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    valor_factura = models.DecimalField(max_digits=14, decimal_places=2)
    valor_abona = models.DecimalField(max_digits=14, decimal_places=2)
    valor_reclamo = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    motivo_reclamo = models.CharField(max_length=700, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_recibo_cobranza_det'
        unique_together = (('cod_recibo', 'secuencia', 'cod_tipo_recibo', 'empresa'),)


class StReciboCobranzaDetEjec(models.Model):
    cod_recibo = models.CharField(max_length=9)
    secuencia = models.IntegerField()
    cod_tipo_recibo = models.CharField(max_length=2)
    empresa = models.IntegerField()
    cod_comprobante = models.CharField(max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    tipo_retencion = models.CharField(max_length=1, blank=True, null=True)
    retencion = models.CharField(max_length=9, blank=True, null=True)
    valor_retencion = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    observacion = models.CharField(max_length=500, blank=True, null=True)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    valor_factura = models.DecimalField(max_digits=14, decimal_places=2)
    valor_abona = models.DecimalField(max_digits=14, decimal_places=2)
    valor_reclamo = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    motivo_reclamo = models.CharField(max_length=700, blank=True, null=True)
    secuencia_ejecutivo = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'st_recibo_cobranza_det_ejec'
        unique_together = (('secuencia_ejecutivo', 'cod_recibo', 'secuencia', 'cod_tipo_recibo', 'empresa'),)


class StTipoProforma(models.Model):
    cod_comprobante = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    empresa = models.IntegerField()
    tipo_proforma = models.CharField(max_length=1)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_tipo_proforma'
        unique_together = (('cod_comprobante', 'tipo_comprobante', 'empresa'),)


class StTiposRetencion(models.Model):
    codigo_tipo_retencion = models.IntegerField(primary_key=True)
    empresa = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_tipos_retencion'
        unique_together = (('codigo_tipo_retencion', 'empresa'),)


class StTiposVisitasP(models.Model):
    cod_tipo_visita = models.CharField(primary_key=True, max_length=14)
    empresa = models.IntegerField()
    tipo_visita = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'st_tipos_visitas_p'
        unique_together = (('cod_tipo_visita', 'empresa'),)


class StTransportistas(models.Model):
    codigo_transportista = models.IntegerField(primary_key=True)
    codigo_empresa = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    cedula = models.CharField(max_length=14, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=9, blank=True, null=True)
    calcula_tarifa = models.CharField(max_length=1, blank=True, null=True)
    kilos_precio_fijo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    calcula_con_formula = models.CharField(max_length=1, blank=True, null=True)
    calcula_valor_x_categoria = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_transportistas'
        unique_together = (('codigo_transportista', 'codigo_empresa'),)


class StTransportistasTarifas(models.Model):
    codigo_transportista = models.OneToOneField(StTransportistas, models.DO_NOTHING, db_column='codigo_transportista', primary_key=True)
    zona_geografica = models.CharField(max_length=14)
    codigo_empresa = models.ForeignKey(StTransportistas, models.DO_NOTHING, db_column='codigo_empresa')
    porcentaje_tarifa_principal = models.DecimalField(max_digits=5, decimal_places=2)
    valor_tarifa_principal = models.DecimalField(max_digits=12, decimal_places=2)
    porcentaje_tarifa_secundaria = models.DecimalField(max_digits=5, decimal_places=2)
    valor_tarifa_secundaria = models.DecimalField(max_digits=12, decimal_places=2)
    porcentaje_tarifa_especial = models.DecimalField(max_digits=5, decimal_places=2)
    valor_tarifa_especial = models.DecimalField(max_digits=12, decimal_places=2)
    tipo_tarifa = models.CharField(max_length=1)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_transportistas_tarifas'
        unique_together = (('codigo_transportista', 'zona_geografica', 'codigo_empresa'),)


class StUsuarioAsterisk(models.Model):
    codigo_usuario = models.CharField(primary_key=True, max_length=30)
    cod_agencia = models.IntegerField()
    empresa = models.IntegerField()
    cod_asterisk = models.CharField(max_length=14)
    canal_usuario = models.CharField(max_length=10, blank=True, null=True)
    observacion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_usuario_asterisk'
        unique_together = (('codigo_usuario', 'cod_agencia', 'empresa', 'cod_asterisk'),)


class StVendedorZonaP(models.Model):
    cod_vendedor = models.CharField(primary_key=True, max_length=14)
    cod_tipo_persona = models.CharField(max_length=3)
    empresa = models.IntegerField()
    cod_modelo = models.CharField(max_length=8)
    cod_zona = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'st_vendedor_zona_p'
        unique_together = (('cod_vendedor', 'cod_tipo_persona', 'cod_modelo', 'cod_zona', 'empresa'),)


class StVendedoresP(models.Model):
    cod_vendedor = models.CharField(primary_key=True, max_length=14)
    cod_tipo_persona = models.CharField(max_length=3)
    empresa = models.IntegerField()
    nombre = models.CharField(max_length=255)
    estado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_vendedores_p'
        unique_together = (('cod_vendedor', 'cod_tipo_persona', 'empresa'),)


class StVendedoresProductosP(models.Model):
    cod_vendedor = models.OneToOneField(StVendedoresP, models.DO_NOTHING, db_column='cod_vendedor', primary_key=True)
    cod_tipo_persona = models.ForeignKey(StVendedoresP, models.DO_NOTHING, db_column='cod_tipo_persona')
    empresa = models.ForeignKey(StVendedoresP, models.DO_NOTHING, db_column='empresa')
    cod_producto = models.ForeignKey(StProductosP, models.DO_NOTHING, db_column='cod_producto')
    es_enviado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_vendedores_productos_p'
        unique_together = (('cod_vendedor', 'cod_tipo_persona', 'empresa', 'cod_producto'),)


class StVentasCheques(models.Model):
    cod_secuencia = models.OneToOneField('StVentasChequesCab', models.DO_NOTHING, db_column='cod_secuencia', primary_key=True)
    cheque = models.CharField(max_length=20)
    cod_persona_ban_ven = models.ForeignKey('StVentasChequesCab', models.DO_NOTHING, db_column='cod_persona_ban_ven')
    cod_tipo_persona_ban_ven = models.ForeignKey('StVentasChequesCab', models.DO_NOTHING, db_column='cod_tipo_persona_ban_ven')
    cod_persona = models.CharField(max_length=14)
    cod_tipo_persona = models.CharField(max_length=3)
    cod_banco_cheque = models.CharField(max_length=3)
    empresa = models.ForeignKey('StVentasChequesCab', models.DO_NOTHING, db_column='empresa')
    estado = models.BooleanField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_ventas_cheques'
        unique_together = (('cod_secuencia', 'cheque', 'cod_persona_ban_ven', 'cod_tipo_persona_ban_ven', 'cod_persona', 'cod_tipo_persona', 'cod_banco_cheque', 'empresa'),)


class StVentasChequesCab(models.Model):
    cod_secuencia = models.IntegerField(primary_key=True)
    cod_persona_ban_ven = models.CharField(max_length=14)
    cod_tipo_persona_ban_ven = models.CharField(max_length=3)
    empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='empresa')
    fecha_venta = models.DateField()
    estado = models.CharField(max_length=1)
    cod_tipo_negociacion = models.ForeignKey(CoTiposNegociaciones, models.DO_NOTHING, db_column='cod_tipo_negociacion')
    valor_negociacion = models.DecimalField(max_digits=13, decimal_places=2)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    es_negociacion_cerrada = models.CharField(max_length=1, blank=True, null=True)
    numero_operacion_banco = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_ventas_cheques_cab'
        unique_together = (('cod_secuencia', 'cod_persona_ban_ven', 'cod_tipo_persona_ban_ven', 'empresa'),)


class StVentasChequesCabOrg(models.Model):
    cod_secuencia = models.IntegerField(primary_key=True)
    cod_persona_ban_ven = models.CharField(max_length=14)
    cod_tipo_persona_ban_ven = models.CharField(max_length=3)
    empresa = models.ForeignKey(AdEmpresas, models.DO_NOTHING, db_column='empresa')
    fecha_venta = models.DateField()
    estado = models.CharField(max_length=1)
    cod_tipo_negociacion = models.ForeignKey(CoTiposNegociaciones, models.DO_NOTHING, db_column='cod_tipo_negociacion')
    valor_negociacion = models.DecimalField(max_digits=13, decimal_places=2)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_ventas_cheques_cab_org'
        unique_together = (('cod_secuencia', 'cod_persona_ban_ven', 'cod_tipo_persona_ban_ven', 'empresa'),)


class StVentasChequesOrg(models.Model):
    cod_secuencia = models.OneToOneField(StVentasChequesCabOrg, models.DO_NOTHING, db_column='cod_secuencia', primary_key=True)
    cheque = models.CharField(max_length=20)
    cod_persona_ban_ven = models.ForeignKey(StVentasChequesCabOrg, models.DO_NOTHING, db_column='cod_persona_ban_ven')
    cod_tipo_persona_ban_ven = models.ForeignKey(StVentasChequesCabOrg, models.DO_NOTHING, db_column='cod_tipo_persona_ban_ven')
    cod_persona = models.CharField(max_length=14)
    cod_tipo_persona = models.CharField(max_length=3)
    cod_banco_cheque = models.CharField(max_length=3)
    empresa = models.ForeignKey(StVentasChequesCabOrg, models.DO_NOTHING, db_column='empresa')
    estado = models.BooleanField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    valor_original = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_ventas_cheques_org'
        unique_together = (('cod_secuencia', 'cheque', 'cod_persona_ban_ven', 'cod_tipo_persona_ban_ven', 'cod_persona', 'cod_tipo_persona', 'cod_banco_cheque', 'empresa'),)


class StVerificacionCampoD(models.Model):
    usuario = models.CharField(primary_key=True, max_length=20)
    cod_persona = models.CharField(max_length=14)
    fecha_ver_campo = models.DateField()
    hora_ver_campo = models.CharField(max_length=10, blank=True, null=True)
    codigo_comprobante = models.CharField(max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    tipo_persona = models.CharField(max_length=1)
    codigo_empresa = models.IntegerField()
    es_enviado = models.BooleanField(blank=True, null=True)
    longitud = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)
    latitud = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_verificacion_campo_d'
        unique_together = (('usuario', 'cod_persona', 'fecha_ver_campo', 'codigo_empresa'),)


class StVisitaP(models.Model):
    fecha = models.DateField(primary_key=True)
    empresa = models.ForeignKey(StTiposVisitasP, models.DO_NOTHING, db_column='empresa')
    cod_cliente = models.CharField(max_length=14)
    cod_vendedor = models.CharField(max_length=14)
    longitud = models.CharField(max_length=20)
    latitud = models.CharField(max_length=20)
    es_enviado = models.CharField(max_length=1)
    comentario = models.CharField(max_length=150, blank=True, null=True)
    cod_tipo_visita = models.ForeignKey(StTiposVisitasP, models.DO_NOTHING, db_column='cod_tipo_visita')

    class Meta:
        managed = False
        db_table = 'st_visita_p'
        unique_together = (('fecha', 'cod_cliente', 'cod_vendedor', 'empresa'),)


class StZonasDespachos(models.Model):
    codigo_zona = models.IntegerField(primary_key=True)
    codigo_empresa = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_zonas_despachos'
        unique_together = (('codigo_zona', 'codigo_empresa'),)


class StZonasDespachosCiudades(models.Model):
    codigo_zona = models.OneToOneField(StZonasDespachos, models.DO_NOTHING, db_column='codigo_zona', primary_key=True)
    zona_geografica = models.CharField(max_length=15)
    codigo_empresa = models.ForeignKey(StZonasDespachos, models.DO_NOTHING, db_column='codigo_empresa')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_zonas_despachos_ciudades'
        unique_together = (('codigo_zona', 'zona_geografica', 'codigo_empresa'),)


class StZonasTransportistas(models.Model):
    codigo_transportista = models.OneToOneField(StTransportistas, models.DO_NOTHING, db_column='codigo_transportista', primary_key=True)
    codigo_zona = models.ForeignKey(StZonasDespachos, models.DO_NOTHING, db_column='codigo_zona')
    codigo_empresa = models.ForeignKey(StZonasDespachos, models.DO_NOTHING, db_column='codigo_empresa')
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_zonas_transportistas'
        unique_together = (('codigo_transportista', 'codigo_zona', 'codigo_empresa'),)


class StaCcRespuestasCampanias(models.Model):
    cod_cliente = models.CharField(primary_key=True, max_length=14)
    codigo_campania = models.IntegerField()
    codigo_area = models.IntegerField()
    codigo_empresa = models.IntegerField()
    observacion = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sta_cc_respuestas_campanias'
        unique_together = (('cod_cliente', 'codigo_campania', 'codigo_area', 'codigo_empresa'),)


class StaCmdt(models.Model):
    cedula = models.CharField(max_length=14, blank=True, null=True)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono1 = models.CharField(max_length=20, blank=True, null=True)
    telefono2 = models.CharField(max_length=20, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sta_cmdt'


class StaNotasVenta(models.Model):
    cod_comprobante = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'sta_notas_venta'


class StaProductosRemplazos(models.Model):
    cod_producto = models.CharField(max_length=14, blank=True, null=True)
    cod_producto_remplazo = models.CharField(max_length=14, blank=True, null=True)
    precio_jaher = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_electropolis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    unico = models.CharField(max_length=1, blank=True, null=True)
    generado = models.CharField(max_length=1, blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sta_productos_remplazos'


class StaTempClientes(models.Model):
    cod_cliente = models.CharField(max_length=14)
    observacion = models.CharField(max_length=50, blank=True, null=True)
    cod_agencia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sta_temp_clientes'


class StaTempComprobante(models.Model):
    empresa = models.IntegerField()
    tipo_comprobante = models.CharField(max_length=2)
    cod_comprobante = models.CharField(primary_key=True, max_length=9)
    periodo = models.IntegerField()
    cod_persona = models.CharField(max_length=14, blank=True, null=True)
    prioridad = models.IntegerField()
    es_asignado = models.BooleanField(blank=True, null=True)
    mensaje_error = models.CharField(max_length=1000, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    prioridad_ant = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sta_temp_comprobante'
        unique_together = (('cod_comprobante', 'tipo_comprobante', 'periodo', 'prioridad', 'empresa'),)


class StaTempInteragua(models.Model):
    ciclo = models.CharField(max_length=3, blank=True, null=True)
    sector = models.IntegerField(blank=True, null=True)
    ruta = models.IntegerField(blank=True, null=True)
    manzana = models.CharField(max_length=50, blank=True, null=True)
    secuencia = models.IntegerField(blank=True, null=True)
    piso = models.IntegerField(blank=True, null=True)
    departamento = models.IntegerField(blank=True, null=True)
    cat_sector = models.IntegerField(blank=True, null=True)
    cat_manzana = models.IntegerField(blank=True, null=True)
    cat_lote = models.IntegerField(blank=True, null=True)
    cat_division = models.IntegerField(blank=True, null=True)
    cat_phv = models.IntegerField(blank=True, null=True)
    cat_phh = models.IntegerField(blank=True, null=True)
    cat_numero = models.IntegerField(blank=True, null=True)
    cuenta = models.CharField(max_length=14)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    ref_direccion = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    est_pto_consumo = models.IntegerField(blank=True, null=True)
    tip_pto_consumo = models.IntegerField(blank=True, null=True)
    actividad = models.CharField(max_length=10, blank=True, null=True)
    abastecimiento = models.IntegerField(blank=True, null=True)
    tipo_uso = models.IntegerField(blank=True, null=True)
    tipo_construccion = models.IntegerField(blank=True, null=True)
    est_guia = models.IntegerField(blank=True, null=True)
    diam_guia = models.CharField(max_length=2, blank=True, null=True)
    fecha_inst_guia = models.DateField(blank=True, null=True)
    fecha_insp_guia = models.DateField(blank=True, null=True)
    material_de_guia = models.IntegerField(blank=True, null=True)
    llave_de_control = models.IntegerField(blank=True, null=True)
    est_medidor = models.IntegerField(blank=True, null=True)
    diam_medidor = models.CharField(max_length=2, blank=True, null=True)
    marca_med = models.IntegerField(blank=True, null=True)
    modelo_med = models.IntegerField(blank=True, null=True)
    tipo_med = models.IntegerField(blank=True, null=True)
    numero_med = models.CharField(max_length=30, blank=True, null=True)
    fecha_inst_med = models.DateField(blank=True, null=True)
    fecha_insp_med = models.DateField(blank=True, null=True)
    estado_de_la_caja = models.IntegerField(blank=True, null=True)
    ubicacion_de_caja = models.IntegerField(blank=True, null=True)
    desecha = models.IntegerField(blank=True, null=True)
    f_alternativa = models.IntegerField(blank=True, null=True)
    descarga = models.IntegerField(blank=True, null=True)
    infra_de_alcant_en_sector = models.CharField(max_length=2, blank=True, null=True)
    caja_prev_para_domicilio = models.CharField(max_length=2, blank=True, null=True)
    lect_actual = models.IntegerField(blank=True, null=True)
    lect_anterior = models.IntegerField(blank=True, null=True)
    consumo = models.CharField(max_length=6, blank=True, null=True)
    reliquidacion = models.IntegerField(blank=True, null=True)
    consumo_comunal = models.IntegerField(blank=True, null=True)
    tipo_facturabilidad = models.CharField(max_length=4, blank=True, null=True)
    promedio_historico = models.IntegerField(blank=True, null=True)
    promedio_sector = models.IntegerField(blank=True, null=True)
    calle1 = models.CharField(max_length=100, blank=True, null=True)
    calle2 = models.CharField(max_length=100, blank=True, null=True)
    calle3 = models.CharField(max_length=100, blank=True, null=True)
    dir_esquina = models.CharField(max_length=2, blank=True, null=True)
    saguan = models.CharField(max_length=2, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    dir_manzana = models.CharField(max_length=50, blank=True, null=True)
    dir_solar = models.CharField(max_length=50, blank=True, null=True)
    dir_km = models.CharField(max_length=50, blank=True, null=True)
    dir_via = models.CharField(max_length=50, blank=True, null=True)
    dir_bloque = models.CharField(max_length=50, blank=True, null=True)
    dir_condominio = models.CharField(max_length=50, blank=True, null=True)
    dir_piso = models.CharField(max_length=50, blank=True, null=True)
    dir_depto = models.CharField(max_length=50, blank=True, null=True)
    dir_oficina = models.CharField(max_length=50, blank=True, null=True)
    dir_local = models.CharField(max_length=50, blank=True, null=True)
    villa = models.CharField(max_length=50, blank=True, null=True)
    dir_referencia = models.CharField(max_length=100, blank=True, null=True)
    numero_personas = models.IntegerField(blank=True, null=True)
    numero_familias = models.IntegerField(blank=True, null=True)
    numero_pisos = models.IntegerField(blank=True, null=True)
    numero_unid_vivienda = models.IntegerField(blank=True, null=True)
    numero_unidad_no_habit = models.IntegerField(blank=True, null=True)
    alcantarillado_pluvial = models.CharField(max_length=2, blank=True, null=True)
    bombeo = models.CharField(max_length=2, blank=True, null=True)
    actualizado_censo = models.CharField(max_length=1, blank=True, null=True)
    propiedad_regularizada = models.CharField(max_length=6, blank=True, null=True)
    facturas_adeudadas = models.IntegerField(blank=True, null=True)
    facturas_emitidas = models.IntegerField(blank=True, null=True)
    saldo_adeudado = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    observacion_1 = models.CharField(max_length=10, blank=True, null=True)
    observacion_2 = models.CharField(max_length=10, blank=True, null=True)
    plan_expan_agua = models.CharField(max_length=10, blank=True, null=True)
    plan_expan_alcanta = models.CharField(max_length=10, blank=True, null=True)
    valor_factura = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    filtrado = models.CharField(max_length=100, blank=True, null=True)
    num_filtro = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sta_temp_interagua'


class StaTempRegistroCivil(models.Model):
    cedula = models.CharField(max_length=14, blank=True, null=True)
    operacion = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=300, blank=True, null=True)
    cedula_cony = models.CharField(max_length=14, blank=True, null=True)
    nombre_cony = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sta_temp_registro_civil'


class StaTempRegistroCivilClie(models.Model):
    cedula = models.CharField(max_length=14, blank=True, null=True)
    nombres = models.CharField(max_length=400, blank=True, null=True)
    provinciadomicilio = models.CharField(max_length=50, blank=True, null=True)
    cantondomicilio = models.CharField(max_length=50, blank=True, null=True)
    parroquiadomicilio = models.CharField(max_length=100, blank=True, null=True)
    barriodomicilio = models.CharField(max_length=300, blank=True, null=True)
    fechanacimiento = models.DateField(blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    telefono = models.CharField(max_length=40, blank=True, null=True)
    empresa = models.CharField(max_length=300, blank=True, null=True)
    empresafantasia = models.CharField(max_length=300, blank=True, null=True)
    provinciaempresa = models.CharField(max_length=50, blank=True, null=True)
    cantonempresa = models.CharField(max_length=50, blank=True, null=True)
    parroquiaempresa = models.CharField(max_length=100, blank=True, null=True)
    cedulaconyuge = models.CharField(max_length=14, blank=True, null=True)
    nombresconyuge = models.CharField(max_length=400, blank=True, null=True)
    fechanacimientoconyuge = models.DateField(blank=True, null=True)
    edadconyuge = models.IntegerField(blank=True, null=True)
    estadociv = models.CharField(max_length=50, blank=True, null=True)
    cargasfamiliares = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sta_temp_registro_civil_clie'


class StaTempRegistroCivilOpera(models.Model):
    cedula = models.CharField(max_length=14, blank=True, null=True)
    operacion = models.CharField(max_length=20, blank=True, null=True)
    producto = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    montoliquido = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    montobruto = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    saldo = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    plazo = models.IntegerField(blank=True, null=True)
    cuotaspagadas = models.IntegerField(blank=True, null=True)
    fechaaprobacion = models.DateField(blank=True, null=True)
    fechadesembolso = models.DateField(blank=True, null=True)
    en_promocion = models.CharField(max_length=2, blank=True, null=True)
    atrasopromedio = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    atrasomaximo = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sta_temp_registro_civil_opera'


class StaTempRegistroCivilProdu(models.Model):
    cedula = models.CharField(max_length=14, blank=True, null=True)
    producto = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sta_temp_registro_civil_produ'


class StaTempTarjetaCredito(models.Model):
    cedula = models.CharField(max_length=14, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=20, blank=True, null=True)
    apellido_materno = models.CharField(max_length=20, blank=True, null=True)
    nombre_uno = models.CharField(max_length=20, blank=True, null=True)
    nombre_dos = models.CharField(max_length=20, blank=True, null=True)
    direccion_domicilio = models.CharField(max_length=100, blank=True, null=True)
    telefono_domicilio = models.CharField(max_length=9, blank=True, null=True)
    direccion_trabajo = models.CharField(max_length=100, blank=True, null=True)
    telefono_trabajo = models.CharField(max_length=9, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    lugar_correspondencia = models.CharField(max_length=20, blank=True, null=True)
    ruc = models.CharField(max_length=14, blank=True, null=True)
    empresa = models.CharField(max_length=200, blank=True, null=True)
    estado_civil = models.CharField(max_length=15, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    actividad = models.CharField(max_length=20, blank=True, null=True)
    oficina = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sta_temp_tarjeta_credito'


class StaTempTelefonos(models.Model):
    telefono = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sta_temp_telefonos'


class StaValoresXCuotas(models.Model):
    cod_comprobante = models.CharField(primary_key=True, max_length=9)
    tipo_comprobante = models.CharField(max_length=2)
    cod_agencia = models.IntegerField()
    secuencia = models.IntegerField()
    empresa = models.IntegerField()
    valor_cuota = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    numero_cuotas = models.IntegerField(blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sta_valores_x_cuotas'
        unique_together = (('cod_comprobante', 'tipo_comprobante', 'cod_agencia', 'secuencia', 'empresa'),)


class SysImportSchema01(models.Model):
    process_order = models.FloatField(blank=True, null=True)
    duplicate = models.FloatField(blank=True, null=True)
    dump_fileid = models.FloatField(blank=True, null=True)
    dump_position = models.FloatField(blank=True, null=True)
    dump_length = models.FloatField(blank=True, null=True)
    dump_allocation = models.FloatField(blank=True, null=True)
    completed_rows = models.FloatField(blank=True, null=True)
    error_count = models.FloatField(blank=True, null=True)
    elapsed_time = models.FloatField(blank=True, null=True)
    object_type_path = models.CharField(max_length=200, blank=True, null=True)
    object_path_seqno = models.FloatField(blank=True, null=True)
    object_type = models.CharField(max_length=30, blank=True, null=True)
    in_progress = models.CharField(max_length=1, blank=True, null=True)
    object_name = models.CharField(max_length=500, blank=True, null=True)
    object_long_name = models.CharField(max_length=4000, blank=True, null=True)
    object_schema = models.CharField(max_length=30, blank=True, null=True)
    original_object_schema = models.CharField(max_length=30, blank=True, null=True)
    partition_name = models.CharField(max_length=30, blank=True, null=True)
    subpartition_name = models.CharField(max_length=30, blank=True, null=True)
    flags = models.FloatField(blank=True, null=True)
    property = models.FloatField(blank=True, null=True)
    completion_time = models.DateField(blank=True, null=True)
    object_tablespace = models.CharField(max_length=30, blank=True, null=True)
    size_estimate = models.FloatField(blank=True, null=True)
    object_row = models.FloatField(blank=True, null=True)
    processing_state = models.CharField(max_length=1, blank=True, null=True)
    processing_status = models.CharField(max_length=1, blank=True, null=True)
    base_process_order = models.FloatField(blank=True, null=True)
    base_object_type = models.CharField(max_length=30, blank=True, null=True)
    base_object_name = models.CharField(max_length=30, blank=True, null=True)
    base_object_schema = models.CharField(max_length=30, blank=True, null=True)
    ancestor_process_order = models.FloatField(blank=True, null=True)
    domain_process_order = models.FloatField(blank=True, null=True)
    parallelization = models.FloatField(blank=True, null=True)
    unload_method = models.FloatField(blank=True, null=True)
    granules = models.FloatField(blank=True, null=True)
    scn = models.FloatField(blank=True, null=True)
    grantor = models.CharField(max_length=30, blank=True, null=True)
    xml_clob = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    value_t = models.CharField(max_length=4000, blank=True, null=True)
    value_n = models.FloatField(blank=True, null=True)
    is_default = models.FloatField(blank=True, null=True)
    file_type = models.FloatField(blank=True, null=True)
    user_directory = models.CharField(max_length=4000, blank=True, null=True)
    user_file_name = models.CharField(max_length=4000, blank=True, null=True)
    file_name = models.CharField(max_length=4000, blank=True, null=True)
    extend_size = models.FloatField(blank=True, null=True)
    file_max_size = models.FloatField(blank=True, null=True)
    process_name = models.CharField(max_length=30, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)
    work_item = models.CharField(max_length=30, blank=True, null=True)
    object_number = models.FloatField(blank=True, null=True)
    completed_bytes = models.FloatField(blank=True, null=True)
    total_bytes = models.FloatField(blank=True, null=True)
    metadata_io = models.FloatField(blank=True, null=True)
    data_io = models.FloatField(blank=True, null=True)
    cumulative_time = models.FloatField(blank=True, null=True)
    packet_number = models.FloatField(blank=True, null=True)
    old_value = models.CharField(max_length=4000, blank=True, null=True)
    seed = models.FloatField(blank=True, null=True)
    last_file = models.FloatField(blank=True, null=True)
    user_name = models.CharField(max_length=30, blank=True, null=True)
    operation = models.CharField(max_length=30, blank=True, null=True)
    job_mode = models.CharField(max_length=30, blank=True, null=True)
    control_queue = models.CharField(max_length=30, blank=True, null=True)
    status_queue = models.CharField(max_length=30, blank=True, null=True)
    remote_link = models.CharField(max_length=4000, blank=True, null=True)
    version = models.FloatField(blank=True, null=True)
    db_version = models.CharField(max_length=30, blank=True, null=True)
    timezone = models.CharField(max_length=64, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    phase = models.FloatField(blank=True, null=True)
    guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    start_time = models.DateField(blank=True, null=True)
    block_size = models.FloatField(blank=True, null=True)
    metadata_buffer_size = models.FloatField(blank=True, null=True)
    data_buffer_size = models.FloatField(blank=True, null=True)
    degree = models.FloatField(blank=True, null=True)
    platform = models.CharField(max_length=101, blank=True, null=True)
    abort_step = models.FloatField(blank=True, null=True)
    instance = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_import_schema_01'
        unique_together = (('process_order', 'duplicate'),)


class SysImportSchema02(models.Model):
    process_order = models.FloatField(blank=True, null=True)
    duplicate = models.FloatField(blank=True, null=True)
    dump_fileid = models.FloatField(blank=True, null=True)
    dump_position = models.FloatField(blank=True, null=True)
    dump_length = models.FloatField(blank=True, null=True)
    dump_allocation = models.FloatField(blank=True, null=True)
    completed_rows = models.FloatField(blank=True, null=True)
    error_count = models.FloatField(blank=True, null=True)
    elapsed_time = models.FloatField(blank=True, null=True)
    object_type_path = models.CharField(max_length=200, blank=True, null=True)
    object_path_seqno = models.FloatField(blank=True, null=True)
    object_type = models.CharField(max_length=30, blank=True, null=True)
    in_progress = models.CharField(max_length=1, blank=True, null=True)
    object_name = models.CharField(max_length=500, blank=True, null=True)
    object_long_name = models.CharField(max_length=4000, blank=True, null=True)
    object_schema = models.CharField(max_length=30, blank=True, null=True)
    original_object_schema = models.CharField(max_length=30, blank=True, null=True)
    partition_name = models.CharField(max_length=30, blank=True, null=True)
    subpartition_name = models.CharField(max_length=30, blank=True, null=True)
    flags = models.FloatField(blank=True, null=True)
    property = models.FloatField(blank=True, null=True)
    completion_time = models.DateField(blank=True, null=True)
    object_tablespace = models.CharField(max_length=30, blank=True, null=True)
    size_estimate = models.FloatField(blank=True, null=True)
    object_row = models.FloatField(blank=True, null=True)
    processing_state = models.CharField(max_length=1, blank=True, null=True)
    processing_status = models.CharField(max_length=1, blank=True, null=True)
    base_process_order = models.FloatField(blank=True, null=True)
    base_object_type = models.CharField(max_length=30, blank=True, null=True)
    base_object_name = models.CharField(max_length=30, blank=True, null=True)
    base_object_schema = models.CharField(max_length=30, blank=True, null=True)
    ancestor_process_order = models.FloatField(blank=True, null=True)
    domain_process_order = models.FloatField(blank=True, null=True)
    parallelization = models.FloatField(blank=True, null=True)
    unload_method = models.FloatField(blank=True, null=True)
    granules = models.FloatField(blank=True, null=True)
    scn = models.FloatField(blank=True, null=True)
    grantor = models.CharField(max_length=30, blank=True, null=True)
    xml_clob = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    value_t = models.CharField(max_length=4000, blank=True, null=True)
    value_n = models.FloatField(blank=True, null=True)
    is_default = models.FloatField(blank=True, null=True)
    file_type = models.FloatField(blank=True, null=True)
    user_directory = models.CharField(max_length=4000, blank=True, null=True)
    user_file_name = models.CharField(max_length=4000, blank=True, null=True)
    file_name = models.CharField(max_length=4000, blank=True, null=True)
    extend_size = models.FloatField(blank=True, null=True)
    file_max_size = models.FloatField(blank=True, null=True)
    process_name = models.CharField(max_length=30, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)
    work_item = models.CharField(max_length=30, blank=True, null=True)
    object_number = models.FloatField(blank=True, null=True)
    completed_bytes = models.FloatField(blank=True, null=True)
    total_bytes = models.FloatField(blank=True, null=True)
    metadata_io = models.FloatField(blank=True, null=True)
    data_io = models.FloatField(blank=True, null=True)
    cumulative_time = models.FloatField(blank=True, null=True)
    packet_number = models.FloatField(blank=True, null=True)
    old_value = models.CharField(max_length=4000, blank=True, null=True)
    seed = models.FloatField(blank=True, null=True)
    last_file = models.FloatField(blank=True, null=True)
    user_name = models.CharField(max_length=30, blank=True, null=True)
    operation = models.CharField(max_length=30, blank=True, null=True)
    job_mode = models.CharField(max_length=30, blank=True, null=True)
    control_queue = models.CharField(max_length=30, blank=True, null=True)
    status_queue = models.CharField(max_length=30, blank=True, null=True)
    remote_link = models.CharField(max_length=4000, blank=True, null=True)
    version = models.FloatField(blank=True, null=True)
    db_version = models.CharField(max_length=30, blank=True, null=True)
    timezone = models.CharField(max_length=64, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    phase = models.FloatField(blank=True, null=True)
    guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    start_time = models.DateField(blank=True, null=True)
    block_size = models.FloatField(blank=True, null=True)
    metadata_buffer_size = models.FloatField(blank=True, null=True)
    data_buffer_size = models.FloatField(blank=True, null=True)
    degree = models.FloatField(blank=True, null=True)
    platform = models.CharField(max_length=101, blank=True, null=True)
    abort_step = models.FloatField(blank=True, null=True)
    instance = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_import_schema_02'
        unique_together = (('process_order', 'duplicate'),)


class SysImportSchema03(models.Model):
    process_order = models.FloatField(blank=True, null=True)
    duplicate = models.FloatField(blank=True, null=True)
    dump_fileid = models.FloatField(blank=True, null=True)
    dump_position = models.FloatField(blank=True, null=True)
    dump_length = models.FloatField(blank=True, null=True)
    dump_allocation = models.FloatField(blank=True, null=True)
    completed_rows = models.FloatField(blank=True, null=True)
    error_count = models.FloatField(blank=True, null=True)
    elapsed_time = models.FloatField(blank=True, null=True)
    object_type_path = models.CharField(max_length=200, blank=True, null=True)
    object_path_seqno = models.FloatField(blank=True, null=True)
    object_type = models.CharField(max_length=30, blank=True, null=True)
    in_progress = models.CharField(max_length=1, blank=True, null=True)
    object_name = models.CharField(max_length=500, blank=True, null=True)
    object_long_name = models.CharField(max_length=4000, blank=True, null=True)
    object_schema = models.CharField(max_length=30, blank=True, null=True)
    original_object_schema = models.CharField(max_length=30, blank=True, null=True)
    partition_name = models.CharField(max_length=30, blank=True, null=True)
    subpartition_name = models.CharField(max_length=30, blank=True, null=True)
    flags = models.FloatField(blank=True, null=True)
    property = models.FloatField(blank=True, null=True)
    completion_time = models.DateField(blank=True, null=True)
    object_tablespace = models.CharField(max_length=30, blank=True, null=True)
    size_estimate = models.FloatField(blank=True, null=True)
    object_row = models.FloatField(blank=True, null=True)
    processing_state = models.CharField(max_length=1, blank=True, null=True)
    processing_status = models.CharField(max_length=1, blank=True, null=True)
    base_process_order = models.FloatField(blank=True, null=True)
    base_object_type = models.CharField(max_length=30, blank=True, null=True)
    base_object_name = models.CharField(max_length=30, blank=True, null=True)
    base_object_schema = models.CharField(max_length=30, blank=True, null=True)
    ancestor_process_order = models.FloatField(blank=True, null=True)
    domain_process_order = models.FloatField(blank=True, null=True)
    parallelization = models.FloatField(blank=True, null=True)
    unload_method = models.FloatField(blank=True, null=True)
    granules = models.FloatField(blank=True, null=True)
    scn = models.FloatField(blank=True, null=True)
    grantor = models.CharField(max_length=30, blank=True, null=True)
    xml_clob = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    value_t = models.CharField(max_length=4000, blank=True, null=True)
    value_n = models.FloatField(blank=True, null=True)
    is_default = models.FloatField(blank=True, null=True)
    file_type = models.FloatField(blank=True, null=True)
    user_directory = models.CharField(max_length=4000, blank=True, null=True)
    user_file_name = models.CharField(max_length=4000, blank=True, null=True)
    file_name = models.CharField(max_length=4000, blank=True, null=True)
    extend_size = models.FloatField(blank=True, null=True)
    file_max_size = models.FloatField(blank=True, null=True)
    process_name = models.CharField(max_length=30, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)
    work_item = models.CharField(max_length=30, blank=True, null=True)
    object_number = models.FloatField(blank=True, null=True)
    completed_bytes = models.FloatField(blank=True, null=True)
    total_bytes = models.FloatField(blank=True, null=True)
    metadata_io = models.FloatField(blank=True, null=True)
    data_io = models.FloatField(blank=True, null=True)
    cumulative_time = models.FloatField(blank=True, null=True)
    packet_number = models.FloatField(blank=True, null=True)
    old_value = models.CharField(max_length=4000, blank=True, null=True)
    seed = models.FloatField(blank=True, null=True)
    last_file = models.FloatField(blank=True, null=True)
    user_name = models.CharField(max_length=30, blank=True, null=True)
    operation = models.CharField(max_length=30, blank=True, null=True)
    job_mode = models.CharField(max_length=30, blank=True, null=True)
    control_queue = models.CharField(max_length=30, blank=True, null=True)
    status_queue = models.CharField(max_length=30, blank=True, null=True)
    remote_link = models.CharField(max_length=4000, blank=True, null=True)
    version = models.FloatField(blank=True, null=True)
    db_version = models.CharField(max_length=30, blank=True, null=True)
    timezone = models.CharField(max_length=64, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    phase = models.FloatField(blank=True, null=True)
    guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    start_time = models.DateField(blank=True, null=True)
    block_size = models.FloatField(blank=True, null=True)
    metadata_buffer_size = models.FloatField(blank=True, null=True)
    data_buffer_size = models.FloatField(blank=True, null=True)
    degree = models.FloatField(blank=True, null=True)
    platform = models.CharField(max_length=101, blank=True, null=True)
    abort_step = models.FloatField(blank=True, null=True)
    instance = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_import_schema_03'
        unique_together = (('process_order', 'duplicate'),)


class SysImportSchema04(models.Model):
    process_order = models.FloatField(blank=True, null=True)
    duplicate = models.FloatField(blank=True, null=True)
    dump_fileid = models.FloatField(blank=True, null=True)
    dump_position = models.FloatField(blank=True, null=True)
    dump_length = models.FloatField(blank=True, null=True)
    dump_allocation = models.FloatField(blank=True, null=True)
    completed_rows = models.FloatField(blank=True, null=True)
    error_count = models.FloatField(blank=True, null=True)
    elapsed_time = models.FloatField(blank=True, null=True)
    object_type_path = models.CharField(max_length=200, blank=True, null=True)
    object_path_seqno = models.FloatField(blank=True, null=True)
    object_type = models.CharField(max_length=30, blank=True, null=True)
    in_progress = models.CharField(max_length=1, blank=True, null=True)
    object_name = models.CharField(max_length=500, blank=True, null=True)
    object_long_name = models.CharField(max_length=4000, blank=True, null=True)
    object_schema = models.CharField(max_length=30, blank=True, null=True)
    original_object_schema = models.CharField(max_length=30, blank=True, null=True)
    partition_name = models.CharField(max_length=30, blank=True, null=True)
    subpartition_name = models.CharField(max_length=30, blank=True, null=True)
    flags = models.FloatField(blank=True, null=True)
    property = models.FloatField(blank=True, null=True)
    completion_time = models.DateField(blank=True, null=True)
    object_tablespace = models.CharField(max_length=30, blank=True, null=True)
    size_estimate = models.FloatField(blank=True, null=True)
    object_row = models.FloatField(blank=True, null=True)
    processing_state = models.CharField(max_length=1, blank=True, null=True)
    processing_status = models.CharField(max_length=1, blank=True, null=True)
    base_process_order = models.FloatField(blank=True, null=True)
    base_object_type = models.CharField(max_length=30, blank=True, null=True)
    base_object_name = models.CharField(max_length=30, blank=True, null=True)
    base_object_schema = models.CharField(max_length=30, blank=True, null=True)
    ancestor_process_order = models.FloatField(blank=True, null=True)
    domain_process_order = models.FloatField(blank=True, null=True)
    parallelization = models.FloatField(blank=True, null=True)
    unload_method = models.FloatField(blank=True, null=True)
    granules = models.FloatField(blank=True, null=True)
    scn = models.FloatField(blank=True, null=True)
    grantor = models.CharField(max_length=30, blank=True, null=True)
    xml_clob = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    value_t = models.CharField(max_length=4000, blank=True, null=True)
    value_n = models.FloatField(blank=True, null=True)
    is_default = models.FloatField(blank=True, null=True)
    file_type = models.FloatField(blank=True, null=True)
    user_directory = models.CharField(max_length=4000, blank=True, null=True)
    user_file_name = models.CharField(max_length=4000, blank=True, null=True)
    file_name = models.CharField(max_length=4000, blank=True, null=True)
    extend_size = models.FloatField(blank=True, null=True)
    file_max_size = models.FloatField(blank=True, null=True)
    process_name = models.CharField(max_length=30, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)
    work_item = models.CharField(max_length=30, blank=True, null=True)
    object_number = models.FloatField(blank=True, null=True)
    completed_bytes = models.FloatField(blank=True, null=True)
    total_bytes = models.FloatField(blank=True, null=True)
    metadata_io = models.FloatField(blank=True, null=True)
    data_io = models.FloatField(blank=True, null=True)
    cumulative_time = models.FloatField(blank=True, null=True)
    packet_number = models.FloatField(blank=True, null=True)
    old_value = models.CharField(max_length=4000, blank=True, null=True)
    seed = models.FloatField(blank=True, null=True)
    last_file = models.FloatField(blank=True, null=True)
    user_name = models.CharField(max_length=30, blank=True, null=True)
    operation = models.CharField(max_length=30, blank=True, null=True)
    job_mode = models.CharField(max_length=30, blank=True, null=True)
    control_queue = models.CharField(max_length=30, blank=True, null=True)
    status_queue = models.CharField(max_length=30, blank=True, null=True)
    remote_link = models.CharField(max_length=4000, blank=True, null=True)
    version = models.FloatField(blank=True, null=True)
    db_version = models.CharField(max_length=30, blank=True, null=True)
    timezone = models.CharField(max_length=64, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    phase = models.FloatField(blank=True, null=True)
    guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    start_time = models.DateField(blank=True, null=True)
    block_size = models.FloatField(blank=True, null=True)
    metadata_buffer_size = models.FloatField(blank=True, null=True)
    data_buffer_size = models.FloatField(blank=True, null=True)
    degree = models.FloatField(blank=True, null=True)
    platform = models.CharField(max_length=101, blank=True, null=True)
    abort_step = models.FloatField(blank=True, null=True)
    instance = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_import_schema_04'
        unique_together = (('process_order', 'duplicate'),)


class T1(models.Model):
    owner = models.CharField(max_length=30, blank=True, null=True)
    object_name = models.CharField(max_length=128, blank=True, null=True)
    subobject_name = models.CharField(max_length=30, blank=True, null=True)
    object_type = models.CharField(max_length=19, blank=True, null=True)
    num_blocks = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't1'


class Tablename1(models.Model):
    text = models.CharField(max_length=2519, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tablename1'


class TempBancoRuminahui(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    identificacion = models.CharField(max_length=15, blank=True, null=True)
    tipo_identificacion = models.CharField(max_length=10, blank=True, null=True)
    num_cta = models.CharField(max_length=30, blank=True, null=True)
    cod_tipo_cta = models.CharField(max_length=30, blank=True, null=True)
    direccion_domicilio = models.CharField(max_length=200, blank=True, null=True)
    telefono_domicilio = models.CharField(max_length=15, blank=True, null=True)
    ciudad_domicilio = models.CharField(max_length=50, blank=True, null=True)
    direccion_trabajo = models.CharField(max_length=250, blank=True, null=True)
    telefono_trabajo = models.CharField(max_length=15, blank=True, null=True)
    ciudad_trabajo = models.CharField(max_length=50, blank=True, null=True)
    direccion_adicional = models.CharField(max_length=200, blank=True, null=True)
    telefono_adicional = models.CharField(max_length=15, blank=True, null=True)
    ciudad_adicional = models.CharField(max_length=50, blank=True, null=True)
    fecha_apertura = models.CharField(max_length=10, blank=True, null=True)
    agencia = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_banco_ruminahui'


class TempCampaniasCallcenterD(models.Model):
    cod_comprobante = models.CharField(max_length=9)
    numero_campania = models.IntegerField()
    periodo = models.IntegerField()
    codigo_call_center = models.IntegerField()
    tipo_comprobante = models.CharField(max_length=2)
    codigo_empresa = models.IntegerField()
    id_servidor = models.CharField(max_length=3)
    cod_tipo_persona = models.CharField(max_length=3)
    cod_persona = models.CharField(max_length=14)
    identificacion_cobrador_act = models.CharField(max_length=20)
    identificacion_cobrador_ori = models.CharField(max_length=20)
    codigo_segmento_cartera = models.IntegerField(blank=True, null=True)
    codigo_agencia = models.IntegerField()
    saldo_asignado = models.DecimalField(max_digits=18, decimal_places=2)
    tipo_campania = models.CharField(max_length=1)
    fecha_volver_a_llamar = models.DateField(blank=True, null=True)
    fecha_compromiso_pago = models.DateField(blank=True, null=True)
    dia_vencimiento = models.IntegerField(blank=True, null=True)
    carga_inicial = models.CharField(max_length=1)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    cliente_ubicado_si_no = models.CharField(max_length=1, blank=True, null=True)
    cliente_ubicado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_actualizacion_cod_etapa = models.DateField(blank=True, null=True)
    cnu_cod_etapa = models.BooleanField(blank=True, null=True)
    cnu_empresa = models.IntegerField(blank=True, null=True)
    cod_origen = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_campanias_callcenter_d'


class TempCredifacil(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    cedula = models.CharField(max_length=15, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    telefono1 = models.CharField(max_length=15, blank=True, null=True)
    telefono2 = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    telefono3 = models.CharField(max_length=15, blank=True, null=True)
    tipo_tarjeta = models.CharField(max_length=100, blank=True, null=True)
    nro_tarjeta = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_credifacil'


class TempEtafashion(models.Model):
    cedula = models.CharField(max_length=15, blank=True, null=True)
    cliente = models.CharField(max_length=200, blank=True, null=True)
    telefono1 = models.CharField(max_length=15, blank=True, null=True)
    telefono2 = models.CharField(max_length=15, blank=True, null=True)
    telefono3 = models.CharField(max_length=15, blank=True, null=True)
    telefono4 = models.CharField(max_length=15, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_etafashion'


class TempInteragua(models.Model):
    ciclo = models.CharField(max_length=10, blank=True, null=True)
    sector = models.IntegerField(blank=True, null=True)
    ruta = models.IntegerField(blank=True, null=True)
    manzana = models.CharField(max_length=150, blank=True, null=True)
    secuencia = models.IntegerField(blank=True, null=True)
    piso = models.IntegerField(blank=True, null=True)
    departamento = models.IntegerField(blank=True, null=True)
    cat_sector = models.IntegerField(blank=True, null=True)
    cat_manzana = models.IntegerField(blank=True, null=True)
    cat_lote = models.IntegerField(blank=True, null=True)
    cat_division = models.IntegerField(blank=True, null=True)
    cat_phv = models.IntegerField(blank=True, null=True)
    cat_phh = models.IntegerField(blank=True, null=True)
    cat_numero = models.IntegerField(blank=True, null=True)
    cuenta = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    ref_direccion = models.CharField(max_length=200, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    est_pto_consumo = models.IntegerField(blank=True, null=True)
    tip_pto_consumo = models.IntegerField(blank=True, null=True)
    actividad = models.CharField(max_length=20, blank=True, null=True)
    abastecimiento = models.IntegerField(blank=True, null=True)
    tipo_uso = models.IntegerField(blank=True, null=True)
    tipo_construccion = models.IntegerField(blank=True, null=True)
    est_guia = models.IntegerField(blank=True, null=True)
    diam_gui = models.CharField(max_length=20, blank=True, null=True)
    fecha_inst_guia = models.DateField(blank=True, null=True)
    fecha_insp_guia = models.DateField(blank=True, null=True)
    calle1 = models.CharField(max_length=200, blank=True, null=True)
    calle2 = models.CharField(max_length=200, blank=True, null=True)
    calle3 = models.CharField(max_length=200, blank=True, null=True)
    dir_esquina = models.CharField(max_length=20, blank=True, null=True)
    saguan = models.CharField(max_length=20, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    dir_manzana = models.CharField(max_length=200, blank=True, null=True)
    dir_solar = models.CharField(max_length=200, blank=True, null=True)
    dir_km = models.CharField(max_length=20, blank=True, null=True)
    dir_via = models.CharField(max_length=100, blank=True, null=True)
    dir_bloque = models.CharField(max_length=200, blank=True, null=True)
    dir_condominio = models.CharField(max_length=200, blank=True, null=True)
    dir_piso = models.CharField(max_length=200, blank=True, null=True)
    dir_depto = models.CharField(max_length=200, blank=True, null=True)
    dir_oficina = models.CharField(max_length=200, blank=True, null=True)
    dir_local = models.CharField(max_length=200, blank=True, null=True)
    villa = models.CharField(max_length=50, blank=True, null=True)
    dir_referencia = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_interagua'


class TempMulticobro(models.Model):
    tipo = models.CharField(max_length=2, blank=True, null=True)
    comprobante = models.CharField(max_length=9, blank=True, null=True)
    solicitud = models.CharField(max_length=15, blank=True, null=True)
    cedula = models.CharField(max_length=14, blank=True, null=True)
    cod_estado_cuota = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_multicobro'


class TempProdubanco(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    telefono_domicilio = models.CharField(max_length=15, blank=True, null=True)
    telefono_trabajo = models.CharField(max_length=15, blank=True, null=True)
    telefono_celular = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    cuneta = models.CharField(max_length=30, blank=True, null=True)
    subproducto = models.CharField(max_length=100, blank=True, null=True)
    fecha_apertura = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_produbanco'


class TempVisaPichincha(models.Model):
    numero_documento = models.CharField(max_length=20, blank=True, null=True)
    tarjeta_socio = models.CharField(max_length=20, blank=True, null=True)
    num_bin = models.IntegerField(blank=True, null=True)
    tipo_documento = models.CharField(max_length=10, blank=True, null=True)
    nombre_socio = models.CharField(max_length=250, blank=True, null=True)
    debito_automatico = models.CharField(max_length=1, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    direccion_socio = models.CharField(max_length=250, blank=True, null=True)
    lugar_trabajo = models.CharField(max_length=200, blank=True, null=True)
    prefijo1 = models.CharField(max_length=3, blank=True, null=True)
    telefono1 = models.CharField(max_length=15, blank=True, null=True)
    prefijo2 = models.CharField(max_length=3, blank=True, null=True)
    telefono2 = models.CharField(max_length=15, blank=True, null=True)
    prefijo3 = models.CharField(max_length=3, blank=True, null=True)
    telefono3 = models.CharField(max_length=15, blank=True, null=True)
    ciclo_facturacion = models.CharField(max_length=50, blank=True, null=True)
    fecha_ingreso = models.IntegerField(blank=True, null=True)
    fecha_corte = models.IntegerField(blank=True, null=True)
    cupo_corriente = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cupo_diferido = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cupo_total = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    estado_tarjeta = models.CharField(max_length=55, blank=True, null=True)
    status_socio = models.CharField(max_length=55, blank=True, null=True)
    substatus_socio = models.CharField(max_length=50, blank=True, null=True)
    cod_cancelacion = models.CharField(max_length=5, blank=True, null=True)
    cod_boletin = models.CharField(max_length=5, blank=True, null=True)
    estatus_boletin = models.CharField(max_length=3, blank=True, null=True)
    tipo_tarjeta = models.CharField(max_length=50, blank=True, null=True)
    tipo_socio = models.CharField(max_length=50, blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    producto = models.CharField(max_length=50, blank=True, null=True)
    canal = models.CharField(max_length=50, blank=True, null=True)
    subcanal = models.CharField(max_length=50, blank=True, null=True)
    mes_vig = models.IntegerField(blank=True, null=True)
    anio_vig = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_visa_pichincha'


class UserUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    image = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_user'


class UserUserGroups(models.Model):
    user = models.ForeignKey(UserUser, models.DO_NOTHING)
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_user_groups'
        unique_together = (('user', 'group_id'),)


class UserUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_user_user_permissions'


class VeIndiceRentabilidad(models.Model):
    periodo = models.IntegerField(primary_key=True)
    cod_producto = models.CharField(max_length=14)
    anio_mes_venta = models.IntegerField()
    forma_pago = models.CharField(max_length=3)
    plazo = models.IntegerField()
    codigo_agencia = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_agencia')
    codigo_canton = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_canton')
    codigo_provincia = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_provincia')
    codigo_region = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_region')
    cod_modelo_cat_linea = models.CharField(max_length=8)
    cod_item_cat_linea = models.CharField(max_length=3)
    cod_marca = models.IntegerField()
    tipo_cliente = models.CharField(max_length=50)
    codigo_nacion = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_nacion')
    codigo_empresa = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_empresa')
    nombre_producto = models.CharField(max_length=200)
    nombre_agencia = models.CharField(max_length=50)
    nombre_canton = models.CharField(max_length=50)
    nombre_provincia = models.CharField(max_length=100)
    nombre_region = models.CharField(max_length=300)
    nombre_linea = models.CharField(max_length=50)
    nombre_marca = models.CharField(max_length=50)
    costo_ventas = models.DecimalField(max_digits=30, decimal_places=2)
    precio_ventas = models.DecimalField(max_digits=30, decimal_places=2)
    costo_devoluciones = models.DecimalField(max_digits=30, decimal_places=2)
    precio_devoluciones = models.DecimalField(max_digits=30, decimal_places=2)
    costo_neto = models.DecimalField(max_digits=30, decimal_places=2)
    venta_neta = models.DecimalField(max_digits=30, decimal_places=2)
    utilidad = models.DecimalField(max_digits=30, decimal_places=2)
    mes_cerrado = models.CharField(max_length=1)
    fecha_ult_ejecucion = models.DateField()
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 've_indice_rentabilidad'
        unique_together = (('periodo', 'cod_producto', 'anio_mes_venta', 'forma_pago', 'plazo', 'codigo_agencia', 'codigo_canton', 'codigo_provincia', 'codigo_region', 'cod_modelo_cat_linea', 'cod_item_cat_linea', 'cod_marca', 'tipo_cliente', 'codigo_nacion', 'codigo_empresa'),)


class VeMovimientosGestiones(models.Model):
    secuencia = models.IntegerField(primary_key=True)
    codigo_cliente = models.CharField(max_length=14)
    codigo_empresa = models.IntegerField()
    codigo_comprobante_compr = models.CharField(max_length=9, blank=True, null=True)
    tipo_comprobante_compr = models.CharField(max_length=2, blank=True, null=True)
    codigo_empresa_compr = models.IntegerField(blank=True, null=True)
    codigo_tipo_gestion = models.CharField(max_length=10)
    codigo_area = models.IntegerField()
    tipo_mayor_detalle = models.CharField(max_length=1)
    fecha_llamar = models.DateField(blank=True, null=True)
    codigo_usuario_gestion = models.CharField(max_length=30)
    fecha_transaccion = models.DateField()
    observacion = models.CharField(max_length=2000, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    pct_codigo_cliente = models.CharField(max_length=14, blank=True, null=True)
    pct_codigo_campania = models.IntegerField(blank=True, null=True)
    pct_codigo_area = models.IntegerField(blank=True, null=True)
    pct_codigo_empresa = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 've_movimientos_gestiones'
        unique_together = (('secuencia', 'codigo_cliente', 'codigo_empresa'),)


class VeMovimientosGestionesRota(models.Model):
    secuencia = models.IntegerField(primary_key=True)
    codigo_cliente = models.CharField(max_length=14)
    codigo_empresa = models.IntegerField()
    codigo_comprobante_compr = models.CharField(max_length=9, blank=True, null=True)
    tipo_comprobante_compr = models.CharField(max_length=2, blank=True, null=True)
    codigo_empresa_compr = models.IntegerField(blank=True, null=True)
    codigo_tipo_gestion = models.ForeignKey(CcTiposGestiones, models.DO_NOTHING, db_column='codigo_tipo_gestion')
    codigo_area = models.ForeignKey(CcTiposGestiones, models.DO_NOTHING, db_column='codigo_area')
    tipo_mayor_detalle = models.CharField(max_length=1)
    fecha_llamar = models.DateField(blank=True, null=True)
    codigo_usuario_gestion = models.ForeignKey(AdUsuarios, models.DO_NOTHING, db_column='codigo_usuario_gestion')
    fecha_transaccion = models.DateField()
    observacion = models.CharField(max_length=2000, blank=True, null=True)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    pct_secuencia = models.ForeignKey(CcPersonasCampaniasTeleRot, models.DO_NOTHING, db_column='pct_secuencia', blank=True, null=True)
    pct_codigo_cliente = models.ForeignKey(CcPersonasCampaniasTeleRot, models.DO_NOTHING, db_column='pct_codigo_cliente', blank=True, null=True)
    pct_codigo_campania = models.ForeignKey(CcPersonasCampaniasTeleRot, models.DO_NOTHING, db_column='pct_codigo_campania', blank=True, null=True)
    pct_codigo_area = models.ForeignKey(CcPersonasCampaniasTeleRot, models.DO_NOTHING, db_column='pct_codigo_area', blank=True, null=True)
    pct_codigo_empresa = models.ForeignKey(CcPersonasCampaniasTeleRot, models.DO_NOTHING, db_column='pct_codigo_empresa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 've_movimientos_gestiones_rota'
        unique_together = (('secuencia', 'codigo_cliente', 'codigo_empresa'),)


class VeObjMensualesXAgencias(models.Model):
    periodo = models.IntegerField(primary_key=True)
    cod_agencia = models.IntegerField()
    empresa = models.IntegerField()
    valor_objetivo = models.DecimalField(max_digits=20, decimal_places=2)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 've_obj_mensuales_x_agencias'
        unique_together = (('periodo', 'cod_agencia', 'empresa'),)


class VeObjXSemanaXAgencias(models.Model):
    semana = models.IntegerField(primary_key=True)
    periodo = models.ForeignKey(VeObjMensualesXAgencias, models.DO_NOTHING, db_column='periodo')
    cod_agencia = models.ForeignKey(VeObjMensualesXAgencias, models.DO_NOTHING, db_column='cod_agencia')
    empresa = models.ForeignKey(VeObjMensualesXAgencias, models.DO_NOTHING, db_column='empresa')
    dias_x_semana = models.IntegerField()
    porcentaje_obj_x_semana = models.DecimalField(max_digits=5, decimal_places=2)
    valor_obj_x_semana = models.DecimalField(max_digits=20, decimal_places=2)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 've_obj_x_semana_x_agencias'
        unique_together = (('semana', 'periodo', 'cod_agencia', 'empresa'),)


class VeObjetivosXAgencias(models.Model):
    periodo = models.IntegerField(primary_key=True)
    codigo_agencia = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_agencia')
    codigo_canton = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_canton')
    codigo_provincia = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_provincia')
    codigo_region = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_region')
    codigo_nacion = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_nacion')
    codigo_empresa = models.ForeignKey(AdAgenciasXCantones, models.DO_NOTHING, db_column='codigo_empresa')
    valor_objetivo_mensual = models.DecimalField(max_digits=30, decimal_places=2)
    valor_objetivo_diario = models.DecimalField(max_digits=30, decimal_places=2)
    anulado = models.CharField(max_length=1)
    adicionado_por = models.CharField(max_length=30)
    fecha_adicion = models.DateField()
    modificado_por = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 've_objetivos_x_agencias'
        unique_together = (('periodo', 'codigo_agencia', 'codigo_canton', 'codigo_provincia', 'codigo_region', 'codigo_nacion', 'codigo_empresa'),)


class WuTestTable(models.Model):
    blob = models.BinaryField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wu_test_table'

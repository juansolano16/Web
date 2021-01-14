### tareas a ejecutar ####
from datetime import datetime, timedelta

from config.wsgi import *
from core.inventario.clases.bodegaVirtual import BodegaProveedor, BodegaBajajC
from core.inventario.models.bodegas.models import VtReservaBv


def readB(nom = '/MASSLINE/', path = 2):
    bodega = BodegaProveedor()
    reg = bodega.actualizaProdProv(prov = nom, path_ = path)
    return reg


def genRep(pdias = 0):
    print('>>>>>>>>>>>> GENERANDO REPORTE PROVEEDOR >>>>>>>>>>>>>>>>>>>>>>')
    resultado = []
    pfecha = datetime.now() - timedelta(days=pdias)
    bodega = BodegaProveedor()
    prov = VtReservaBv.objects.values('proveedor', 'email','fecha_aprobacion').filter(fecha_aprobacion=pfecha).distinct()
    for p in prov:
        #resultado.append(bodega.genReporte(ruc_proveedor=p['proveedor'], correo_prov=['juansolano@mastermoto.com.ec',], fecha = p['fecha_aprobacion']))
        resultado.append(bodega.genReporte(ruc_proveedor=p['proveedor'], correo_prov=p['email'].split(','), fecha = p['fecha_aprobacion']))
    if resultado: return resultado
    return 'Sin Datos'


def actualizarBodBajaj():
    bodega = BodegaBajajC()
    return bodega.actualizar()


def print_result(task):
    print(task.result)
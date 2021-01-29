### tareas a ejecutar ####
from datetime import datetime, timedelta

from config.wsgi import *
from core.facturacion.clases.Ventas import VentasUnno
from core.facturacion.modelos.comprobante.models import VtVentaMotor1


def genRep(pdias = 0):
    print('>>>>>>>>>>>> GENERANDO REPORTE PROVEEDOR >>>>>>>>>>>>>>>>>>>>>>')
    ventas = VentasUnno()
    pfecha = datetime.now() - timedelta(days=pdias)
    reg = None
    if VtVentaMotor1.objects.filter(fecha_venta=pfecha).exists():
        prov, correo = VtVentaMotor1.objects.values_list('proveedor', 'email').filter(fecha_venta=pfecha).distinct()[0]
        reg = ventas.genReporte(ruc_proveedor=prov, correo_prov=correo.split(','), pfecha=pfecha)
    if reg: return reg
    return 'Sin Datos'



def print_result(task):
    print(task.result)
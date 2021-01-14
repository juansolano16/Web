### tareas a ejecutar ####
from datetime import datetime

from config.wsgi import *
from core.facturacion.clases.Ventas import VentasUnno
from core.facturacion.modelos.comprobante.models import VtVentaMotor1


def genRep():
    print('>>>>>>>>>>>> GENERANDO REPORTE PROVEEDOR >>>>>>>>>>>>>>>>>>>>>>')
    ventas = VentasUnno()
    reg = None
    if VtVentaMotor1.objects.filter(fecha_venta=datetime.now()).exists():
        prov, correo = VtVentaMotor1.objects.values_list('proveedor', 'email').filter(fecha_venta=datetime.now()).distinct()[0]
        reg = ventas.genReporte(ruc_proveedor=prov, correo_prov=correo.split(','))
    if reg: return reg
    return 'Sin Datos'



def print_result(task):
    print(task.result)
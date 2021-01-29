import shutil

from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import get_template

from config import settings
from datetime import datetime

from config.settings import path_bodegaV
from core.clases_general import reportes
from core.facturacion.modelos.comprobante.models import VtVentaMotor1


class VentasUnno():

    def genReporte(self, ruc_proveedor, correo_prov, pfecha):
        data = {}
        try:
            path = settings.BASE_DIR + '/core/facturacion/reportes/jasper/'
            base = 'UNNOPARTSDB'
            parametros = {'FDESDE': pfecha.strftime('%d/%m/%Y'),
                          'FHASTA': pfecha.strftime('%d/%m/%Y'),
                          'RUC': ruc_proveedor}
            rep = reportes.ReporteJasper(path, base)
            file_path = rep.generarReporte('ReporteVentas', parametros, extencion='xlsx')

            template = get_template('correo/correoProveedor.html')
            content = template.render({
                'user': 'juan',
            })
            message = EmailMultiAlternatives('Productos Venta Diaria Unnoparts',
                                             'This is an important message.',
                                             settings.EMAIL_HOST_USER,  # Remitente
                                             correo_prov)  # Destinatario
            message.attach_alternative(content, 'text/html')
            message.attach_file(file_path)
            message.attach_file(self.genArchivoPlano(ruc_proveedor, pfecha))
            message.send()
            data['ok'] = 'ok'
        except Exception as e:
            data['error'] = str(e)
        return (data)

    def genArchivoPlano(self, ruc, pfecha):
        path = settings.BASE_DIR + "/core/TmpReportes/Ventas" + pfecha.strftime('%d_%m_%Y') + '.txt'
        file = open(path, "w")
        caracter = chr(9)
        # MOTOR 1 #######################
        if ruc == '1792014166001':
            cabecera = 1
            for reg in VtVentaMotor1.objects.filter(fecha_venta=pfecha):
                file.write(reg.cod_prov + chr(9) +
                       reg.numero_serie + chr(9) +
                       reg.chasis + chr(9) +
                       'CONSIGNACION' + chr(9) +
                       reg.agencia + chr(9) +
                       str(reg.cod_agencia) + chr(9) +
                       reg.fecha_venta.strftime('%d/%m/%Y') +
                       "\n"
                       )
                cabecera = cabecera + 1
        file.close()
        return path
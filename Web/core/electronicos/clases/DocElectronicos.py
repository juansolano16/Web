from xml.dom import minidom
import codecs
import chardet
from os import remove, rename

from core.clases_general.Utilities import get_random_string
import config.settings as setting
from core.clases_general.reportes import ReporteJasper
from core.inventario.models.producto.models import Producto, StProdPackingList


class ride():

    def readXmlRide(self, file, output):
        f = open(file, "r")

        encoding = f.encoding
        tmp = f.read()
        vfirmado = 'S' if tmp.find('<numeroAutorizacion>') >= 0 else 'N'

        if vfirmado == 'S':
            try:
                mydoc = minidom.parse(codecs.open(file, "r", encoding))
            except:
                mydoc = minidom.parse(codecs.open(file, "r", 'utf-8'))
            estado = mydoc.getElementsByTagName('estado')[0].firstChild.data
            numeroAutorizacion = mydoc.getElementsByTagName('numeroAutorizacion')[0].firstChild.data
            fechaAutorizacion = mydoc.getElementsByTagName('fechaAutorizacion')[0].firstChild.data
            comprobante = mydoc.getElementsByTagName('comprobante')[0].firstChild.data
            # print('%s %s %s' % (estado, numeroAutorizacion, fechaAutorizacion))
        else:
            estado = 'No Autorizado'
            numeroAutorizacion = "1"
            fechaAutorizacion = ''
            comprobante = tmp

        # Para cambiar detalles en caso de Moto
        comprobante = self.changeDetAdi(comprobante)

        output = output + get_random_string(20) + '.xml'
        file1 = codecs.open(output, "w", "utf-8")
        file1.write(comprobante)
        file1.close()

        return {'estado': estado,
                'autorizacion': numeroAutorizacion,
                'fechaaut': fechaAutorizacion,
                'file': output}

    def removeXmlTmp(self, file):
        remove(file)

    def changeDetAdi(self, comprobante):
        try:
            tmp = minidom.parseString(comprobante)
            for prod in tmp.getElementsByTagName('codigoPrincipal'):
                # Para determinar si el producto es Moto
                if Producto.objects.filter(empresa=2, cod_producto=prod.firstChild.data, cod_marca=1).exists():
                    # Para obtener detalles del producto
                    detAdis = prod.parentNode.getElementsByTagName('detallesAdicionales')[0]
                    for detAdi in detAdis.getElementsByTagName('detAdicional'):
                        key, value = detAdi.getAttribute('nombre'), detAdi.getAttribute('valor')
                        if key == 'Chasis':
                            p = StProdPackingList.objects.get(empresa=2, cod_producto=prod.firstChild.data, cod_chasis=value)
                            det = self.genDetAdicional(p)
                            break
                    # Para eliminar detalles adiciones
                    for d in detAdis.getElementsByTagName('detAdicional'):
                        detAdis.removeChild(d)

                    # Genera nuevo detalle
                    detAdi = tmp.createElement("detAdicional")
                    detAdi.setAttribute("nombre", "Descripcion Adicional")
                    detAdi.setAttribute("valor", det)
                    detAdis.appendChild(detAdi)
                    return tmp.toxml()
            return comprobante
        except Exception as e:
            return comprobante

    def genDetAdicional(self, product):
        val = """CHASIS={};MOTOR={};RAMV={};AÑO={};CILINDRAJE={};COLOR={};ORIGEN={};MODELO={};TONELAJE={};EJES={};RUEDAS={};PASAJEROS={};"""\
            .format(product.cod_chasis,
                     product.cod_motor,
                     product.camvcpn,
                     product.anio,
                     product.color,
                     product.cilindraje,
                     product.origen,
                     product.modelo,
                     product.tonelaje,
                     product.ejes,
                     product.ruedas,
                     product.pasajeros)
        return val


class rideFac():

    def changeNameRide(self, nombre, file):
        xml = nombre.replace('\\', '/')
        xml = xml.split('/')[-1]

        nom_tmp = file.replace('\\', '/')
        nom_tmp = nom_tmp.split('/')[-1]

        pdf = 'RIDE_' + xml.replace('xml', 'pdf')
        pdf = file.replace(nom_tmp, pdf)

        try:
            remove(pdf)
        except:
            pass

        rename(file, pdf)
        return pdf

    def genPDF(self, file, output_=None, change_name='S'):
        try:
            c_ride = ride()
            output_xml_tmp = setting.BASE_DIR + '/core/TmpReportes/'
            data = c_ride.readXmlRide(file, output_xml_tmp)
            datafile_ = '"' + data['file'] + '"'

            path = setting.BASE_DIR + '/core/electronicos/reportes/jasper/'
            base = 'UNNOPARTSDB'
            param = {
                'FECHA_AUT': data['fechaaut'],
                'NUM_AUT': data['autorizacion'] if data['fechaaut'] else 'Sin Autorización',
                'CLAVE_ACC': data['autorizacion'],
                'SUBREPORT_DIR': path,
                'IMAGE_DIR': path + 'imagenes/'
            }
            rep = ReporteJasper(path, base)
            fac = rep.xml_to_pdf(reporte='FACTURA', data_file=datafile_, xml_path='/factura', parametros=param,
                                 output=output_)
            c_ride.removeXmlTmp(data['file'])
            if change_name == 'S': fac = self.changeNameRide(file, fac)
            return (fac)
        except Exception as e:
            return ('error: ' + str(e))

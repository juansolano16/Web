from xml.dom import minidom
import codecs
import chardet
from os import remove, rename

from core.clases_general.Utilities import get_random_string
import config.settings as setting
from core.clases_general.reportes import ReporteJasper


class ride():

    def readXmlRide(self, file, output):
        f = open(file, "r")

        encoding = f.encoding
        tmp = f.read()
        vfirmado = 'S' if tmp.find('<numeroAutorizacion>') >= 0 else 'N'

        if vfirmado == 'S':
            try: mydoc = minidom.parse(codecs.open(file, "r", encoding))
            except: mydoc = minidom.parse(codecs.open(file, "r", 'utf-8'))
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

        output = output + get_random_string(20) + '.xml'
        file1 = codecs.open(output, "w", "utf-8")
        file1.write(comprobante)
        file1.close()

        return {'estado': estado,
                'autorizacion': numeroAutorizacion,
                'fechaaut': fechaAutorizacion,
                'file': output }

    def removeXmlTmp(self, file):
        remove(file)


class rideFac():

    def changeNameRide(self, nombre, file):
        xml = nombre.replace('\\','/')
        xml = xml.split('/')[-1]

        nom_tmp = file.replace('\\', '/')
        nom_tmp = nom_tmp.split('/')[-1]

        pdf = 'RIDE_' + xml.replace('xml', 'pdf')
        pdf = file.replace(nom_tmp, pdf)

        try: remove(pdf)
        except: pass

        rename(file, pdf)
        return pdf

    def genPDF(self, file, output_ = None):
        try:
            c_ride = ride()
            output_xml_tmp = setting.BASE_DIR + '/core/TmpReportes/'
            data = c_ride.readXmlRide(file, output_xml_tmp)
            datafile_ = '"' + data['file'] + '"'

            path = setting.BASE_DIR + '/core/electronicos/reportes/jasper/'
            base = 'UNNOPARTSDB'
            param = {
                'FECHA_AUT': data['fechaaut'],
                'NUM_AUT':  data['autorizacion'] if data['fechaaut'] else 'Sin Autorización',
                'CLAVE_ACC':  data['autorizacion'],
                'SUBREPORT_DIR': path,
                'IMAGE_DIR': path + 'imagenes/'
            }
            rep = ReporteJasper(path, base)
            fac = rep.xml_to_pdf(reporte='FACTURA', data_file=datafile_, xml_path='/factura', parametros=param, output=output_)
            c_ride.removeXmlTmp(data['file'])
            fac = self.changeNameRide(file, fac)
            return (fac)
        except Exception as e:
            return ('error: ' + str(e))
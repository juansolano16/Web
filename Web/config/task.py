# Use the schedule wrapper
import os

from django.db import connections


from config.wsgi import *

# from django.contrib.auth.hashers import make_password
#
# reg = ['ja10deagosto',
# 'jaalborada',
# 'jaambato',
# 'jaarenal',
# 'jaatacames',
# 'jaauviazogues',
# 'jaauviduran',
# 'jaauviempalme',
# 'jaauvigrancolombia',
# 'jaauvilamana',
# 'jaauvilatroncal',
# 'jaauvimanta',
# 'jaauviportoviejo',
# 'jaauvistodomingo',
# 'jababahoyo',
# 'jabiloxi',
# 'jabuenafe',
# 'jacalderon',
# 'jacalifornia',
# 'jacarmen',
# 'jacoca',
# 'jacomite',
# 'jaconcordia',
# 'jadaule',
# 'jaduran',
# 'jaempalme',
# 'jaesclusas',
# 'jagilramirez',
# 'jahuaquillas',
# 'jaibarra',
# 'jalago',
# 'jalalibertad',
# 'jalamana',
# 'jalatroncal',
# 'jamachala',
# 'jamanta',
# 'jamilagro',
# 'jamilagro2',
# 'janabon',
# 'janaranjal',
# 'japasaje',
# 'japedernales',
# 'japortoviejo',
# 'japuyo',
# 'jaquevedo',
# 'jaquininde',
# 'jasantodomingo',
# 'jasantodomingo2',
# 'jasantodomingo3',
# 'jashyris',
# 'jatallerelcoca',
# 'jatallerquevedo',
# 'jatallerquitonorte',
# 'jatena',
# 'javentanas',
# 'javillaflora']
#
# for i in reg:
#     password = make_password(i + '$$')
#     print(password)


from core.user.clases.usuario_oracle import CrearUserOracle
print(CrearUserOracle())

# from core.inventario.schedules.bodegaV import genRep
# print(genRep(1))


from core.inventario.models.prueba.model import TmpImagen
from django.http import FileResponse

# creating a bytes object
# res = bytes(test_string, 'utf-8')
# file_path = r'C:\Users\juansolano\Downloads\Cedulas.docx'
#
#
# p = open(file_path, 'rb').read()
#
# with connections['default'].cursor() as cur:
#     cur.callproc('stock.gen_IMG', [p])

#######################################################################
# from core.electronicos.clases.DocElectronicos import rideFac
#
# file = r'C:\Users\juansolano\OneDrive - Grupo Vazquez\Mastermoto\Python Web Services\SerWebDjango\Web\core\FACTURA_007-500-000002087.xml'
# # file = r'C:\Users\juansolano\OneDrive - Grupo Vazquez\Mastermoto\Python Web Services\SerWebDjango\Web\core\030-001A02K1001432.xml'
# # file = r'C:\Users\juansolano\OneDrive - Grupo Vazquez\Mastermoto\Python Web Services\SerWebDjango\Web\core\FACT-012-001A01Q1002511.xml'
# ride = rideFac()
# print(ride.genPDF(file))


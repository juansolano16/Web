from django.urls import path

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
from core.personal.views.empleado.views import liqEmpleado, listEmpleados, rhPersonalCreateView, rhPersonalUpdateView
from core.personal.views.encuestas.views import *
from core.personal.views.roles.views import *

app_name = 'personal'

urlpatterns = [
    path('readEncuesta/', readEncuestaCovid.as_view(), name='readEncuestaCovid'),
    path('resultadoEncuesta/', resultadoEncuesta.as_view(), name='resultadoEncuesta'),
    path('updateReEncuesta/<str:ced>/<str:id_ec>/', rEncuestaUpdateView.as_view(), name='updateReEncuesta'),

    path('genReporteG/', genReporteG, name='genReporteG'),
    path('genReporteR/', genReporteR, name='genReporteR'),

    path('gestionTurnosEmp/', gestionTurnosEmp.as_view(), name='gestionTurnosEmp'),

    ## ROL DE EMPLEADO ##
    path('rolEmpleado/', rolEmpleado.as_view(), name='rolEmpleado'),
    path('listRolDescargado/', listRolesDescargados.as_view(), name='listRolDescargado'),

    ## ROL DE BENFICIO SOCIAL ##
    path('rolDecimo/', rolDecimo.as_view(), name='rolDecimo'),

    ## FORMULARIOS EMPLEADO ##
    path('rhPersonalCreate/', rhPersonalCreateView.as_view(), name='rhPersonalCreate'),
    path('rhPersonalUpdateView/<str:pk>/', rhPersonalUpdateView.as_view(), name='rhPersonalUpdateView'),
    path('listEmpleados/', listEmpleados.as_view(), name='listEmpleados'),
    path('liqEmpleado/', liqEmpleado.as_view(), name='liqEmpleado'),
]

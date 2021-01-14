from django.urls import path
from core.Repositorio.views import *


app_name = 'repositorio'

urlpatterns = [
    path('RevistaUnno/', RevistaUnno, name='revistaUnno'),
]
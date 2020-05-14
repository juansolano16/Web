from django.shortcuts import render
from django.http import JsonResponse
from django.db import connections
import json


## PARA VISUALIZAR REST API
from rest_framework import viewsets
from .serializers import ProductoSerializer
from .models import vt_producto_web

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = vt_producto_web.objects.all().order_by('linea', 'sublinea', 'categoria', 'segmento', 'subsegmento')
    serializer_class = ProductoSerializer

# Create your views here.
def products(request):
	my_query = query_db('SELECT * FROM stock.vt_producto_web', ())
	data = {
		'name': 'Vitor',
		'location': 'Finland',
		'is_active': True,
		'count': 28
		}
	return JsonResponse(my_query, safe=False)


def query_db(query, args=(), one=False):
	with connections['oracle'].cursor() as cur:
	    cur.execute(query, args)
	    r = [dict((cur.description[i][0], value) \
	               for i, value in enumerate(row)) for row in cur.fetchall()]
	return (r[0] if r else None) if one else r	
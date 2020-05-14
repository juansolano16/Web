from rest_framework import serializers
from .models import vt_producto_web, StProductoDetalle, StProductoSerie


class DetProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StProductoDetalle
        fields = ('caracteristicas', 'detalle')


class ProductoSerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = StProductoSerie
        fields = ('cod_interno', 'color')        


class ProductoSerializer(serializers.ModelSerializer):
	#detalles = DetProductoSerializer( many=True, read_only=True,)
	detalles = serializers.StringRelatedField(many=True)
	series = ProductoSerieSerializer( many=True, read_only=True,)

	class Meta:
		model = vt_producto_web
		fields = ('linea', 'sublinea', 'categoria', 'segmento', 'subsegmento', 'cod_producto', 'producto', 'series', 'detalles')
		#depth = 3
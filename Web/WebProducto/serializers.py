from rest_framework import serializers
from .models import vt_producto_web, StProductoDetalle


class DetProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StProductoDetalle
        fields = ('caracteristicas', 'detalle')


class ProductoSerializer(serializers.ModelSerializer):
	#detalles = DetProductoSerializer( many=True, read_only=True,)
	detalles = serializers.StringRelatedField(many=True)

	class Meta:
		model = vt_producto_web
		fields = ('linea', 'sublinea', 'categoria', 'segmento', 'subsegmento', 'cod_producto', 'producto', 'detalles')
		#depth = 3
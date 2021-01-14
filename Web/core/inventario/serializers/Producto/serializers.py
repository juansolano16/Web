from drf_serializer_cache import SerializerCacheMixin
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from core.inventario.models.producto.models import vt_producto_web, StProductoDetalle, StProductoSerie, VtListaPrecio, \
    vt_producto_web_auvi, StProductoSerieAuvi


########## PRODUCTOS MASTERMOTO ##############
class ProductoSerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = StProductoSerie
        fields = ('cod_interno', 'color')


class ProductoSerializerMM(serializers.ModelSerializer):
    detalles = serializers.StringRelatedField(many=True)
    # series = ProductoSerieSerializer(many=True, read_only=True,)
    precio = serializers.StringRelatedField(many=True)

    series = SerializerMethodField()

    def get_series(self, obj):
        items = StProductoSerie.objects.filter(bodegav=obj.bodegav, cod_producto=obj.cod_producto) # Whatever your query may be
        serializer = ProductoSerieSerializer(instance=items, many=True)
        return serializer.data

    class Meta:
        model = vt_producto_web
        fields = (
        'linea', 'tipo', 'categoria', 'subcategoria', 'cod_producto', 'producto', 'precio', 'series', 'detalles')



########## PRODUCTOS AUVI ####################
class ProductoSerieAuviSerializer(SerializerCacheMixin, serializers.ModelSerializer):
    class Meta:
        model = StProductoSerieAuvi
        fields = ('cod_interno',)


class ProductoSerializerAuvi(SerializerCacheMixin, serializers.ModelSerializer):
    detalles = serializers.StringRelatedField(many=True)
    # series = ProductoSerieAuviSerializer(many=True, read_only=True)
    precio = serializers.StringRelatedField(many=True)

    series = SerializerMethodField()

    def get_series(self, obj):
        items = StProductoSerieAuvi.objects.filter(bodegav=obj.bodegav, cod_producto=obj.cod_producto) # Whatever your query may be
        serializer = ProductoSerieAuviSerializer(instance=items, many=True, read_only=True)
        return serializer.data

    class Meta:
        model = vt_producto_web_auvi
        fields = ('linea', 'sublinea', 'categoria', 'segmento', 'subsegmento', 'cod_producto', 'producto', 'precio', 'series',
                  'detalles',)

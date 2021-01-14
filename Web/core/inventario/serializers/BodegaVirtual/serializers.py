from rest_framework import serializers

from core.inventario.models.bodegas.models import VtReservaBv


class VentaBodegaVitualSerializer(serializers.ModelSerializer):
    FechaVenta = serializers.CharField(source='fecha_aprobacion')

    class Meta:
        model = VtReservaBv
        fields = ('cod_agencia', 'agencia', 'numero_serie', 'chasis', 'cod_persona', 'nombre_persona', 'e_mailh', 'tipo_venta', 'FechaVenta')

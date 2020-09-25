from api.models import Usuario, Producto, Compra, Factura, Earnings
from rest_framework import serializers


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'dni_cif', 'address', 'number', 'via', 'city', 'province']


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['unit_price', 'name']


class CompraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Compra
        fields = ['product', 'name', 'user']


class FacturaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Factura
        fields = ['purchases']


class EarningsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Earnings
        fields = ['total', 'total_iva', 'unique_clients', 'avg_profit']
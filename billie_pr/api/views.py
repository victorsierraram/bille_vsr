from api.models import Usuario, Producto, Compra, Factura, Earnings
from rest_framework import viewsets
from api.serializers import UsuarioSerializer, ProductoSerializer, CompraSerializer, FacturaSerializer, EarningsSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Usuarios to be viewed or edited.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    """avg_profitavg_profit
    API endpoint that allows Productos to be viewed or edited.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    

class CompraViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Compras to be viewed or edited.
    """
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer


class FacturaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Facturas to be viewed or edited.
    """
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class EarningsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Earnings to be viewed.
    """
    queryset = Earnings.objects.all()
    serializer_class = EarningsSerializer


from django.db import models

# Create your models here.
class Usuario(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dni_cif = models.CharField(max_length=9)
    address = models.CharField(max_length=255)
    number = models.IntegerField()
    via = models.CharField(max_length=9)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)

class Producto(models.Model):
    name = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=10 ,decimal_places=2)

class Compra(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    number = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, blank=True)

class Factura(models.Model):
    purchases = models.ManyToManyField(Compra)
    total = models.DecimalField(max_digits=10 ,decimal_places=2)

class Earnings(models.Model):
    total = models.DecimalField(max_digits=10 ,decimal_places=2)
    total_iva = models.DecimalField(max_digits=10 ,decimal_places=2)
    unique_clients = models.IntegerField()
    avg_profit = models.DecimalField(max_digits=10 ,decimal_places=2)

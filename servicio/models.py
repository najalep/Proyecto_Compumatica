from django.db import models
from datetime import datetime
# Create your models here.

class Client(models.Model):
    names = models.CharField(max_length=150, null=False, blank=False, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, null=False, blank=False, verbose_name='Apellidos')
    cedula = models.CharField(max_length=10, null=False, blank=False, unique=True, verbose_name='Cedula')
    birthday = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')

    def __str__(self):
        return '{}'.format(self.names)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']



class Area(models.Model):
    names = models.CharField(max_length=150, null=False, blank=False, verbose_name='Nombres')

    def __str__(self):
        return '{}'.format(self.names)

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'
        ordering = ['id']



class Empleado(models.Model):
    names = models.CharField(max_length=150, null=False, blank=False, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, null=False, blank=False, verbose_name='Apellidos')
    cedula = models.CharField(max_length=10, null=False, blank=False, unique=True, verbose_name='Cedula')
    birthday = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    area = models.ForeignKey(Area, on_delete= models.CASCADE, verbose_name='Area' )

    def __str__(self):
        return '{}'.format(self.names)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['id']


class Categoria(models.Model):
    names = models.CharField(max_length=150, null=False, blank=False, verbose_name='Nombres')

    def __str__(self):
        return '{}'.format(self.names)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']



class Marca(models.Model):
    names = models.CharField(max_length=150, null=False, blank=False, verbose_name='Nombres')

    def __str__(self):
        return '{}'.format(self.names)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['id']


class Articulo(models.Model):
    code = models.CharField(max_length=150, null=False, blank=False, unique=True, verbose_name='Codigo')
    device = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    names = models.CharField(max_length=150, null=False, blank=False, verbose_name='Nombres')
    brand = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name='Marca')
    pvp = models.DecimalField(default=0.00, max_digits=9, null=False, blank=False, decimal_places=2, verbose_name='Precio')


    def __str__(self):
        return '{}/{}'.format(self.code, self.device)

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['id']



class Factura(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.names



    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Factura, on_delete=models.CASCADE)
    arti = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.arti.code


    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']





















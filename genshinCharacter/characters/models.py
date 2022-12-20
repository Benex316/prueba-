from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Personaje(models.Model):
    id_personaje=models.AutoField(db_column='id_personaje', primary_key=True)
    fecha_cumpleaños=models.DateField(blank=True, null=True)
    nombre=models.CharField(max_length=20, blank=True)
    edad=models.CharField(max_length=10, blank=True, null=True)
    region=models.CharField(max_length=20, blank=False, null=False)
    vision=models.CharField(max_length=10, blank=False, null=False)
    afiliacion=models.CharField(max_length=20, blank=True)
    constelacion=models.CharField(max_length=30, blank=False, null=False)
    genero = models.CharField(max_length=10, blank=True, null=True) 
    foto  = models.ImageField(upload_to='fotos', blank=True, null=True)


    def __str__(self):
        return str(self.id_personaje)+", "+str(self.fecha_cumpleaños)+", "\
                +self.nombre+", "+self.edad+", "+self.region+", "+self.region+", "+self.vision+", "\
                +self.afiliacion+", "+self.constelacion+", "+self.genero+", "+self.foto.__str__()


    def cargarFoto(instance, filename):
        return "fotos/foto_{0}_{1}".format(instance.id_personaje, filename)

class Usuario(models.Model):
    id_cuenta=models.AutoField(db_column='id_cuenta', primary_key=True)
    nombre=models.CharField(max_length=30, blank=False)
    contraseña=models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.id_cuenta+", "+self.nombre+", "+self.contraseña
    
class carroCompra(models.Model):
    id_compra=models.AutoField(db_column='id_producto', primary_key=True)
    fotoCompra  = models.ImageField(upload_to='fotos', blank=True, null=True)
    productoCompra = models.CharField(max_length=99, blank=False)
    descripcionCompra=models.CharField(max_length=999, blank=False)
    precioCompra = models.CharField(max_length=99, blank=False)
    stockCompra = models.CharField(max_length=99, blank=False)
    

    def __str__(self):
        return str(self.id_compra)+", "+self.fotoCompra.__str__()+", "+self.productoCompra+", "+self.descripcionCompra+", "+self.precioCompra+", "+self.stockCompra 
    

    
class Producto(models.Model):
    id_producto=models.AutoField(db_column='id_producto', primary_key=True)
    foto  = models.ImageField(upload_to='fotos', blank=True, null=True)
    producto = models.CharField(max_length=99, blank=False)
    descripcion=models.CharField(max_length=999, blank=False)
    precio = models.CharField(max_length=99, blank=False)
    stock = models.CharField(max_length=99, blank=False)

    def __str__(self):
        return str(self.id_producto)+", "+self.foto.__str__()+", "+self.producto+", "+self.descripcion+", "+self.precio+", "+self.stock 
    
       
class Venta(models.Model):
    id_venta=models.AutoField(db_column="id_venta", primary_key=True)
    productoVenta=models.CharField(max_length=99, blank=False)
    precioVenta=models.CharField(max_length=99, blank=False)
    stockComprado=models.CharField(max_length=99, blank=False)

    def __str__(self):
        return str(self.id_venta)+", "+self.productoVenta+", "+self.precioVenta+", "+self.stockComprado

class Cliente(models.Model):
    id_ClienteVenta=models.AutoField(db_column="id_ClienteVenta", primary_key=True)
    cliente=models.CharField(max_length=99, blank=False)


    def __str__(self):
        return str(self.id_ClienteVenta)+", "+self.cliente

class Detalle(models.Model):
    id_descripcion=models.AutoField(db_column="id_descripcion", primary_key=True)
    descripcionVenta=models.CharField(max_length=99, blank=False)
    
    def __str__(self):
        return str(self.id_descripcion)+", "+self.descripcionVenta

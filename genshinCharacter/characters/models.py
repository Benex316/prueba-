from django.db import models

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
                +str(self.nombre)+", "+str(self.edad)+", "+str(self.region)+", "+str(self.region)+", "+str(self.vision)+", "\
                +str(self.afiliacion)+", "+str(self.constelacion)+", "+str(self.genero)+", "+self.foto.__str__()


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
    foto  = models.ImageField(upload_to='fotos', blank=True, null=True)
    producto = models.CharField(max_length=99, blank=False)
    descripcion=models.CharField(max_length=999, blank=False)
    precio = models.CharField(max_length=99, blank=False)
    stock = models.CharField(max_length=99, blank=False)

    def __str__(self):
        return self.id_compra+", "+self.foto.__str__()+", "+self.producto+", "+self.descripcion+", "+self.precio+", "+self.stock 
    

    
class Producto(models.Model):
    id_producto=models.AutoField(db_column='id_producto', primary_key=True)
    foto  = models.ImageField(upload_to='fotos', blank=True, null=True)
    producto = models.CharField(max_length=99, blank=False)
    descripcion=models.CharField(max_length=999, blank=False)
    precio = models.CharField(max_length=99, blank=False)
    stock = models.CharField(max_length=99, blank=False)

    def __str__(self):
        return self.id_producto+", "+self.foto.__str__()+", "+self.producto+", "+self.descripcion+", "+self.precio+", "+self.stock 
    
            

    

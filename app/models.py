from django.db import models

# Create your models here.

class clientes(models.Model):
    codigo=models.CharField(primary_key=True, max_length=15)
    p_nombre=models.CharField(max_length=50)
    s_nombre=models.CharField(max_length=50)
    apellido_p=models.CharField(max_length=50)
    apellido_m=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    correo=models.CharField(max_length=50)
    clave=models.CharField(max_length=16)
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.p_nombre, self.apellido_p)
    
class habitacion(models.Model):
    num_habitacion = models.CharField(primary_key=True, max_length=15)
    tipo = models.CharField(max_length=20)
    precio = models.CharField(max_length=20)
    estado_ocupacion = models.CharField(max_length=20)
    capacidad = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=20)

class Reserva(models.Model):
    num_reserva = models.CharField(primary_key=True, max_length=15)
    fecha_entrada = models.CharField(max_length=20)
    fecha_salida = models.CharField(max_length=20)
    estado_reserva = models.CharField(max_length=20)
    cliente = models.ForeignKey('Clientes', on_delete=models.CASCADE)
    nro_personas = models.CharField(max_length=20)
    estado_pago = models.CharField(max_length=20)
    medio_pago = models.CharField(max_length=20)
    comentario = models.CharField(max_length=20)


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
    
    ESTADO_CHOICES = (
        ('Ocupada', 'Ocupada'),
    )
    
    estado_ocupacion = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    estado_seleccionado = models.CharField(max_length=20, choices=ESTADO_CHOICES, blank=True, null=True)
    capacidad = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=20)

class reserva(models.Model):
    num_reserva = models.AutoField(primary_key=True)
    fecha_entrada = models.DateField(max_length=20)
    fecha_salida = models.DateField(max_length=20)
    estado_reserva = models.CharField(max_length=20)
    cliente = models.ForeignKey('clientes', on_delete=models.CASCADE)
    nro_personas = models.CharField(max_length=20)



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


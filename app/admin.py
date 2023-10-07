from django.contrib import admin
from .models import clientes, habitacion , reserva

# Register your models here.

admin.site.register(clientes)
admin.site.register(habitacion)
admin.site.register(reserva)



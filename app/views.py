from django.shortcuts import render, redirect
from .models import clientes, habitacion
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def pagPrincipal(request):
    return render (request,"app/pagPrincipal.html")

def pagLogin(request):
    return render (request,"app/pagLogin.html")

def pagBase(request):
    return render (request,"app/pagBase.html")

def pagADM(request):
    clientesList = clientes.objects.all()
    return render(request, "app/pagADM.html", {"clientes":clientesList} )

def pagHabitacion(request):
    habitacionList = habitacion.objects.all()
    return render(request, "app/pagHabitacion.html", {"habitacion":habitacionList} )

def pagRegistro(request):
    codigo = request.POST['txtCodigo']
    nombre1 = request.POST['txtNombre1']
    nombre2 = request.POST['txtNombre2']
    apellido1 = request.POST['txtApellido1']
    apellido2 = request.POST['txtApellido2']
    direccion = request.POST['txtDireccion']
    correo = request.POST['txtCorreo']
    clave = request.POST['txtClave']

    nuevos_clientes = clientes.objects.create(codigo=codigo,p_nombre=nombre1,s_nombre=nombre2,apellido_p=apellido1,apellido_m=apellido2,direccion=direccion,correo=correo,clave=clave)
    return redirect('pagADM')

def pagEliminar(request, id):
    e_clientes = clientes.objects.get(codigo=id)
    e_clientes.delete()
    return redirect('pagADM')

def pagEditar(request, id):
    e_clientes = clientes.objects.get(codigo=id)
    return render(request, "app/pagEditar.html", {"clientes": e_clientes})

def pagEdicion(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    correo = request.POST['txtCorreo']

    e_clientes = clientes.objects.get(codigo=codigo)
    e_clientes.codigo = codigo
    e_clientes.p_nombre = nombre
    e_clientes.correo = correo
    e_clientes.save()
    return redirect('pagADM')

def pagRegistroH(request):
    numero = request.POST['txtNumH']
    tipo = request.POST['txtTipo']
    precio = request.POST['txtPrecio']
    estado = request.POST['txtOcupacion']
    capacidad = request.POST['txtCapacidad']
    descripcion = request.POST['txtDescripcion']

    nueva_habitacion = habitacion.objects.create(num_habitacion=numero,tipo=tipo,precio=precio,estado_ocupacion=estado,capacidad=capacidad,descripcion=descripcion)
    return redirect('pagHabitacion')

def pagEliminarH(request, id):
    e_habitacion = habitacion.objects.get(num_habitacion=id)
    e_habitacion.delete()
    return redirect('pagHabitacion')

def pagEditarH(request, id):
    a_habitacion = habitacion.objects.get(num_habitacion=id)
    return render(request, "app/pagEditarH.html", {"habitacion": a_habitacion})

def pagEdicionH(request):
    numero = request.POST['txtNumH']
    tipo = request.POST['txtTipo']
    estado = request.POST['txtOcupacion']

    e_habitacion = habitacion.objects.get(num_habitacion=numero)
    e_habitacion.num_habitacion = numero
    e_habitacion.tipo = tipo
    e_habitacion.estado_ocupacion = estado
    e_habitacion.save()
    return redirect('pagHabitacion')


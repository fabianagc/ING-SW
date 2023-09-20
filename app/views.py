from django.shortcuts import render, redirect
from .models import clientes
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm




def pagLogin(request):
    return render (request,"app/pagLogin.html")

def pagPrincipal(request):
    return render (request,"app/pagPrincipal.html")

def pagBase(request):
    return render (request,"app/pagBase.html")

def pagADM(request):
    clientesList = clientes.objects.all()
    return render(request, "app/pagADM.html", {"clientes":clientesList} )

def pagRegistro(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    correo = request.POST['txtCorreo']

    nuevos_clientes = clientes.objects.create(codigo=codigo,p_nombre=nombre,correo=correo)
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


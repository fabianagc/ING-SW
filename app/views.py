from django.shortcuts import render, redirect
from .models import clientes, habitacion, reserva
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages

def pagPrincipal(request):
    return render (request,"app/pagPrincipal.html")

def pagUregistro(request):
    reservaList = reserva.objects.all()
    return render(request, "app/pagUregistro.html", {"reserva":reservaList} )

def pagPanel(request):
    return render (request,"app/pagPanel.html")

def pagFecha(request):
    return render (request,"app/pagFecha.html")

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


def pagLogin(request):
    if request.method == 'POST':
        try:
            user = clientes.objects.get(correo=request.POST['correo'], clave=request.POST['clave'])
            print("Usuario=", user)
            request.session['correo'] = user.correo
            request.session['codigo'] = user.codigo
            return render(request, 'app/pagPrincipal.html')
        except clientes.DoesNotExist as e:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos..!')
    return render(request, 'app/pagLogin.html')

def pagLogout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Has cerrado sesión con éxito.')
        return redirect('pagLogin')  
    messages.warning(request, 'La solicitud de cierre de sesión debe ser mediante POST.')
    return redirect('pagLogin') 

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
    nombre = request.POST['txtNombre1']
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


def pagCheck(request):
    if request.method == 'POST':

        habitaciones_ids = request.POST.getlist('habitaciones_seleccionadas')
        nuevo_estado = 'reservado' 
        fecha_entrada = request.session.get('fecha_seleccionada_1')
        fecha_salida = request.session.get('fecha_seleccionada_2')
        codigo_cliente = request.session.get('codigo')
        nro_personas = request.POST.get('number', '') 

        try:
            cliente = clientes.objects.get(codigo=codigo_cliente)
            nueva_reserva = reserva(
                fecha_entrada=fecha_entrada,
                fecha_salida=fecha_salida,
                estado_reserva=nuevo_estado,
                cliente=cliente, 
                nro_personas=nro_personas
            )
            nueva_reserva.save()
            reserva_reciente = reserva.objects.filter(cliente=cliente).order_by('-num_reserva').first()

            todas_habitaciones = habitacion.objects.all()
            for habitacion_obj in todas_habitaciones:
                if habitacion_obj.num_habitacion in habitaciones_ids:
                    habitacion_obj.estado_ocupacion = nuevo_estado
                    habitacion_obj.save()

            habitaciones = habitacion.objects.all()

            return render(request, "app/pagConfirmacion.html", {"reservas": [reserva_reciente]})

        except clientes.DoesNotExist:

            pass

    habitaciones = habitacion.objects.all()
    return render(request, "app/pagCheck.html", {"habitaciones": habitaciones})



def pagFecha(request):
    if request.method == 'POST':
        fecha_actual = datetime.now().date()
        fecha_seleccionada_1 = request.POST['fecha_1']
        fecha_seleccionada_2 = request.POST['fecha_2']

        request.session['fecha_actual'] = str(fecha_actual)  # Convertir a cadena
        request.session['fecha_seleccionada_1'] = fecha_seleccionada_1
        request.session['fecha_seleccionada_2'] = fecha_seleccionada_2
        
        return redirect('pagCheck')

    return render(request, "app/pagFecha.html")

    
def pagConfirmacion(request):

    codigo_usuario = request.session.get('codigo')
    reservas = reserva.objects.filter(cliente__codigo=codigo_usuario)
    reservas = reserva.objects.all()
    
    return render(request, "app/pagConfirmacion.html", {"reservas": reservas})

def pagRegistroR(request):
    num_reserva = request.POST['txtReserva']
    fecha1 = request.POST['txtFechaE']
    fecha2 = request.POST['txtFechaS']
    estado = request.POST['txtEstado']
    cliente = request.POST['txtCliente']
    nro_personas = request.POST['txtPersonas']

    nuevas_reservas = reserva.objects.create(num_reserva=num_reserva,fecha_entrada=fecha1,fecha_salida=fecha2,estado_reserva=estado,cliente=cliente,nro_personas=nro_personas)
    return redirect('pagUregistro')

def pagEliminarR(request, id):
    e_reserva = reserva.objects.get(num_reserva=id)
    e_reserva.delete()
    return redirect('pagEliminarR')

def pagEditarR(request, id):
    a_reserva = reserva.objects.get(num_reserva=id)
    return render(request, "app/pagEditarR.html", {"reserva": a_reserva})

def pagEdicionR(request):
    num_reserva = request.POST['txtReserva']
    fecha1 = request.POST['txtFechaE']
    fecha2 = request.POST['txtFechaS']
    estado = request.POST['txtEstado']
    cliente = request.POST['txtCliente']
    nro_personas = request.POST['txtPersonas']

    e_reserva = reserva.objects.get(num_reserva=num_reserva)
    e_reserva.num_reserva = num_reserva
    e_reserva.fecha_entrada = fecha1
    e_reserva.fecha_salida = fecha2
    e_reserva.estado_reserva = estado
    e_reserva.cliente = cliente
    e_reserva.nro_personas = nro_personas
    e_reserva.save()
    return redirect('pagUregistro')
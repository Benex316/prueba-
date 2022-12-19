from django.shortcuts import render, redirect
from .models import Personaje, Usuario, carroCompra, Producto
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

        messages.success(request, "Tu cuenta ha sido creada exitosamente")
        return redirect('index')


    else:
        form = UserCreationForm()

        
    return render(request, "characters/register.html", {'form': form})





def index(request):
    print("Estoy en el Index")
    context = {}
    return render(request, 'characters/index.html', context)


def quienesSomos(request):
    print("QuienesSomos")
    context = {}
    return render(request, 'characters/quienesSomos.html', context)


def colaborador(request):
    print("Se esta en la colaboración")
    context = {}
    return render(request, 'characters/colaboradores.html', context)


def crud_personajes(request):

    print("hola  estoy en crud_alumnes...")
    personaje = Personaje.objects.all()  # select * from Alumne
    context = {'personaje': personaje}
    return render(request, 'characters/agregarPersonaje.html', context)


def agregarPersonaje(request):
    print("Estoy en agregar personaje")
    context = {}
    if request.method == "POST":
        print("Post")
        opcion = request.POST.get("opcion", "")
        print("opcion="+opcion)

        # Listar
        if opcion == "Editar" or opcion == "Volver":
            personaje = Personaje.objects.all()
            context = {'personaje': personaje}
            print("Enviando a List")
            return render(request, "characters/listarPersonaje.html", context)

        # Agregar

        if opcion == "Agregar":
            nombre = request.POST["nombre"]
            cumpleaños = request.POST["cumpleaños"]
            edad = request.POST["edad"]
            region = request.POST["region"]
            vision = request.POST["vision"]
            afiliacion = request.POST["afiliacion"]
            constelacion = request.POST["constelacion"]
            genero = request.POST["genero"]
            foto = request.FILES["foto"]

            if region != "" and vision != "" and constelacion != "":

                personaje = Personaje()

                personaje.nombre = nombre
                personaje.fecha_cumpleaños = cumpleaños
                personaje.edad = edad
                personaje.region = region
                personaje.vision = vision
                personaje.afiliacion = afiliacion
                personaje.genero = genero
                personaje.foto = foto

                personaje.save()

                context = {'mensaje': "Guardado"}

            else:
                context = {
                    'mensaje': "Error, no se pudo guardar, los datos estan vacios"}

        # Actualizar

        if opcion == "Actualizar":
            nombre = request.POST["nombre"]
            cumpleaños = request.POST["cumpleaños"]
            print("Cumpleaños= ", cumpleaños)
            edad = request.POST["edad"]
            region = request.POST["region"]
            vision = request.POST["vision"]
            afiliacion = request.POST["afiliacion"]
            constelacion = request.POST["constelacion"]
            genero = request.POST["genero"]
            foto = request.FILES.get("foto", False)

            if region != "" and vision != "" and constelacion != "":
                personaje = Personaje(
                    nombre, cumpleaños, edad, region, vision, afiliacion, constelacion, genero, foto)

                personaje.save()

                context = {'personaje': personaje,
                           'mensaje': "Personaje actualizado"}

            else:
                context = {
                    'mensaje': "Error, no se ha podido actualizar, verifique los datos"}

            return render(request, "characters/editarPersonaje.html", context)

    return render(request, "characters/agregarPersonaje.html", context)


def personaje_edit(request, pk):
    mensajes = []
    errores = []

    context = {}
    personaje = Personaje.objects.all()

    personaje = Personaje.objects.get(id_personaje=pk)

    context = {}

    if personaje:
        print("Se encontro al personaje")
        mensajes.append("Datos eliminados")

        context = {'personaje': personaje,
                   'mensajes': mensajes, 'errores': errores}

        return render(request, 'characters/editarPersonaje.html', context)

    return render(request, 'characters/listarPersonaje.html', context)


def personaje_del(request, pk):
    mensajes = []
    errores = []
    personaje = Personaje.objects.all()
    try:
        personaje = Personaje.objects.get(id_personaje=pk)
        context = {}
        if personaje:
            personaje.delete()
            mensajes.append("Datos elimiados")

            context = {'personaje': personaje,
                       'mensajes': mensajes, 'errores': errores}

            return render(request, 'characters/listarPersonaje.html', context)

    except:
        print("Error, Personaje no existe")

        errores.append("Personaje no encontrado")

        context = {'personaje': personaje,
                   'mensajes': mensajes, 'errores': errores}

        return render(request, 'characters/listarPersonaje.html', context)


def listarPersonaje(request):
    print("hola  estoy en personaje...")
    personaje = Personaje.objects.all()
    context = {'personaje': personaje}
    return render(request, 'characters/listarPersonaje.html', context)


def personajes(request):
    print("hola  estoy en personaje...")
    personaje = Personaje.objects.all()
    context = {'personaje': personaje}
    return render(request, "characters/personajes.html", context)


def administracion(request):
    print("Adminisración")
    context = {}
    return render(request, 'characters/administracion.html', context)


def producto(request):
    personaje = Personaje.objects.all()
    context = {'personaje': personaje}
    return render(request, 'characters/producto.html', context)


def carrito(request):
    print("carrito")
    personaje = Personaje.objects.all()
    context = {'personaje':personaje}
    return render(request, 'characters/carrito.html', context)



def agregarCarrito(request):
    print("Estoy en el carrito culiao")
    context = {}
    if request.method=="POST":
        print("Estoy dentro del post")
        opcion=request.method.GET("opcion", " ")
        print("opcion"+ opcion)
        if opcion == "agregarProducto":
            print("Mandemos la wea")
            producto = request.POST["producto"]
            descripcion = request.POST["descripcion"]
            precio = request.POST["precio"]
            stock = request.POST["stock"]
            foto = request.FILE["foto"]

            if producto != "" and descripcion != "" and precio != "" and stock != "" and foto!="":
                añadirCarrito=carroCompra(producto, descripcion, precio, stock, foto)
                
                añadirCarrito.save()

                context={'mensaje': 'Guardado'}

            return render(request,"characters/producto.html", context)


def AgregarProductos(request):
    print("Estoy en productos")
    context = {}
    return render(request, 'characters/agregarProducto.html', context)

def agregarProducto(request):
    print("Estoy en el carrito culiao")
    context={}
    if request.method=="POST":
        print("Estoy dentro del post")
        opcion = request.POST.get("opcion", "")
        print("opcion="+opcion)
        if opcion == "agregarProducto":
            print("Mandemos la wea")
            producto = request.POST["producto"]
            descripcion = request.POST["descripcion"]
            precio = request.POST["precio"]
            stock = request.POST["stock"]
            foto = request.FILE["foto"]

            if producto != "" and descripcion != "" and precio != "" and stock != "" and foto!="":
                añadirCarrito=Producto(producto, descripcion, precio, stock, foto)
                
                añadirCarrito.save()

                context={'mensaje': 'Guardado'}

    return render(request,'characters/agregarProducto.html', context)


def agregarUsuario(request):
    print("Estoy en agregar personaje")
    context = {}
    if request.method == "POST":
        print("Post")
        opcion = request.POST.get("opcion", "")
        print("opcion="+opcion)

        if opcion == "Agregar":
            nombre = request.POST["nombre"]
            contraseña = request.POST["contraseña"]

            if nombre != "" and contraseña != "":
                usuario = Usuario

                usuario.nombre = nombre
                usuario.contraseña = contraseña

                usuario.save()

                context = {'mensaje': "Guardado"}

            else:
                context = {
                    'mensaje': "Error, no se pudo guardar, los datos estan vacios"}

        return render(request, "characters/crearUsuario.html", context)

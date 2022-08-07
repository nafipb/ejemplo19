from django.shortcuts import render
from django.http import HttpResponse
from Fio.models import Curso, Estudiante, Profesor, Entregable
from Fio.forms import CursoFormulario

# Create your views here.
def inicio(request):
    context = {
        "mensaje": "Se constante en tu trabajo",
        "mensaje_bienvenida": "Bienvenidos a esta pagina"
    }
    return render(request, "Fio/index.html", context)

def estudiantes(request):
    estudiantes = Estudiante.objects.all ()
    
    context = {
        "mensaje": "Se constante en tu trabajo",
        "mensaje_bienvenida": "Estos son nuestros Estudiantes por cada clase",
        "cursos": estudiantes
    }
    return render(request, "Fio/estudiantes.html", context)

def cursos(request):
    cursos = Curso.objects.all ()

    context = {
        "mensaje": "Se constante en tu trabajo",
        "mensaje_bienvenida": "Todos nuestros cursos al mejor precio",
        "cursos": cursos
    }
    return render(request, "Fio/cursos.html", context)

def profesor (request):
    profesor = Profesor.objects.all()
    context = {
        "mensaje": "Se constante en tu trabajo",
        "mensaje_bienvenida": "Este es el plantel de nuestros docentes",
        "cursos": profesor
    }
    return render(request, "Fio/profesor.html", context)

def entregables(request):
    entregables = Entregable.objects.all()
    context = {
        "mensaje": "Se constante en tu trabajo",
        "mensaje_bienvenida": "Estos son nuestros profesores por cada clase",
        "cursos": entregables
    }
    return render(request, "Fio/profesor.html", context)

def crear_curso(request):
    if request.method == "GET":
        formulario = CursoFormulario()
        return render(request, "Fio/formulario.html",{"formulario":formulario})
    else:
        nombre= request.POST["nombre"]
        camada= request.POST["camada"]
        curso= Curso(nombre=nombre, camada=camada)
        curso.save()
        return render(request, "Fio/index.html")
def crear_estudiante(request):
        if request.method == "GET":
            return render(request, "Fio/formestudiantes.html")
        else:
            nombre= request.POST["nombre"]
            apellido= request.POST["apellido"]
            email= request.POST["email"]
            estudiante= Estudiante(nombre=nombre, apellido=apellido, email=email )
            estudiante.save()
            return render(request, "Fio/index.html")

def fake_login(request):
    if request.method == "GET":
        return render(request, "Fio/login.html")
    else:
        username= request.POST["username"]
        password= request.POST["password"]

    if username == "admin" and password == "12345":
        return HttpResponse("Bienvenido admin")
    
    else:
        return HttpResponse("No te conozco")
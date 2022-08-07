from django.shortcuts import render
from django.http import HttpResponse
from Fio.models import Curso, Estudiante, Profesor, Entregable
from Fio.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario

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
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data
            print(data)
            nombre = data.get("nombre")
            camada = data.get("camada")
            curso= Curso(nombre=nombre, camada=camada)
            curso.save()

            return render(request, "Fio/index.html")
        else:
            return HttpResponse("Formulario no valido")

def crear_profesor(request):
    if request.method == "GET":
        formulario = ProfesorFormulario()
        return render(request, "Fio/formprofesores.html",{"formulario":formulario})
    else:
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data
            print(data)
            nombre = data.get("nombre")
            apellido = data.get("apellido")
            email = data.get("email")
            profesion = data.get("profesion")
            profesor= Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profesor.save()

            return render(request, "Fio/index.html")
        else:
            return HttpResponse("Formulario no valido")

def crear_estudiante(request):
        if request.method == "GET":
            formulario = EstudianteFormulario()
            return render(request, "Fio/formestudiantes.html",{"formulario":formulario})
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

def formulario_busqueda(request):
    return render(request, "Fio/formulario_busqueda.html")

def buscar(request):

    curso_nombre = request.GET.get("curso", None)
    camada = request.GET.get("camada", None)

    if not curso_nombre:
        return HttpResponse("No indicaste ningun nombre")

    cursos_lista = Curso.objects.filter(nombre__icontains=curso_nombre)

    if camada:
        cursos_lista = cursos_lista.filter(camada=camada)
    return render(request, "Fio/resultado_busqueda.html", {"cursos": cursos_lista})
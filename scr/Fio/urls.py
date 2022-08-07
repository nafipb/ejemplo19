from django.urls import path
from Fio.views import *

urlpatterns = [
    path("",inicio, name= "inicio"),
    path("cursos/", cursos, name= "cursos"),
    path("estudiantes/", estudiantes, name= "estudiantes"),
    path("profesores/", profesor, name= "profesor"),
    path("entregables/", entregables, name= "entregables"),
    path("curso/crear/",crear_curso, name= "curso_crear"),
    path("estudiante/crear",crear_estudiante, name="estudiante_crear"),
    path("profesor/crear",crear_profesor,name="profesor_crear"),
    path("formulario/",formulario_busqueda,name="formulario_busqueda"),
    path("resultados/", buscar, name="buscar_curso"),
    path("login/",fake_login, name= "login_falso")
]
from django.forms import Form, IntegerField, CharField, EmailField


class CursoFormulario(Form):
    nombre = CharField()
    camada = IntegerField()
    
class EstudianteFormulario(Form):
    nombre = CharField()
    apellido= CharField()
    email= EmailField()

class ProfesorFormulario(Form):
    nombre = CharField()
    apellido= CharField()
    email= EmailField() 
    profesion= CharField() 
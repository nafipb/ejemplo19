from django.forms import Form, IntegerField, CharField


class CursoFormulario(Form):
    nombre = CharField()
    camada = IntegerField()
    
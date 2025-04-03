from django.shortcuts import render

# Create your views here.

def index(request):
    personas = [
        {"nombre": "Homero", "apellido": "Simpson", "descripcion": "Padre"},
        {"nombre": "Marge", "apellido": "Simpson", "descripcion": "Madre"},
        {"nombre": "Bart", "apellido": "Simpson", "descripcion": "Hijo"},
        {"nombre": "Lisa", "apellido": "Simpson", "descripcion": "Hija"},
        {"nombre": "Maggie", "apellido": "Simpson", "descripcion": "Hija"},
        {"nombre": "Ned", "apellido": "Flanders", "descripcion": "Vecino"},
        {"nombre": "Montgomery", "apellido": "Burns", "descripcion": "Jefe"},
        {"nombre": "Seymour", "apellido": "Skinner", "descripcion": "Director"}
    ]
    contexto = {"personas" : personas}
    return render(request , "datos/index.html" , context = contexto)
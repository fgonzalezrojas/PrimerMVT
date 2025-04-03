from django.shortcuts import render

# Create your views here.

def index(request):
    personas = [
        {"nombre" : "Homero" , "apellido" : "Simpson" , "descripcion" : "Padre"},
    ]
    contexto = {"personas" : personas}
    return render(request , "datos/index.html" , context = contexto)
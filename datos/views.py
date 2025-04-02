from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"mensaje" : "Despues lo completo"}
    return render(request , "datos/index.html" , context)
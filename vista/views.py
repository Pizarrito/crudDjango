from django.shortcuts import render
from .models import ventas

# Create your views here.

def list(request):
    datosListado = ventas.objects.all()
    return render(request,'datos.html',{"ventas":datosListado})

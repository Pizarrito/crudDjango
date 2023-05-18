from django.shortcuts import render
from django.db.models import Sum
from .models import ventas

# Create your views here.

def list(request):
    datosListado = ventas.objects.all()
    resultado = ventas.objects.aggregate(total_cantidad=Sum("cantidad"))
    resultado2 = ventas.objects.aggregate(total_gramos=Sum("gramos_unidad"))
    
    return render(request,'datos.html',{"ventas":datosListado,"resultado":resultado,"resultado2":resultado2})


from django.shortcuts import render
from .models import Carreras, Pensum

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def carreras_view(request):
    carreras = Carreras.objects.all()
    context = {
        'carreras': carreras
    }
    return render(request, 'carreras.html', context)

def carreras_detail(request,carrera_id):
    carrera = Carreras.objects.get(id=carrera_id)
    pensums = carrera.pensum_set.all()
    context = {
        'carrera': carrera,
        'pensums': pensums
    }
    return render(request, 'carreras_view.html', context)    

def instalaciones(request):
    return render(request, 'instalaciones.html') 

def noticias(request):
    return render(request, 'actividades.html')      
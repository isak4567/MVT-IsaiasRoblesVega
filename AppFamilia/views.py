from django.shortcuts import render
from datetime import datetime
from AppFamilia.models import Familia
from django.http import HttpResponse

# Create your views here.
def familia(request, nombre, edad, fecha):
    
    fam1 = Familia(nombre = nombre, edad = int(edad), fecha = fecha)
    fam1.save()

    return HttpResponse(f"""
        <div> 
            <h2> Integrante agregado: </h2>
            <p> -Nombre del Integrante:               {fam1.nombre} </p>
            <p> -Edad del Integrante:                 {fam1.edad} </p>
            <p> -Fecha de nacimiento del Integrante:  {fam1.fecha} </p>
        </div>
    """)

def lista_familia (request):

    lista = Familia.objects.all()

    return render (request, "list_familia.html", {"lista_familia": lista})


def vista_prueba (request):

    return HttpResponse("vista prueba")

def vista_prueba1html (request):

    return render(request, "prueba1.html")

def vista_prueba2html (request):

    return render(request, "prueba2.html")

def vista_prueba3html (request):

    return render(request, "prueba3.html")

def vista_prueba4html (request):

    return render(request, "prueba4.html")

def vista_prueba5html (request):

    if request.method == 'post':

        fam1 = Familia(nombre = request.post['nombre del input'], edad = int(request.post['nombre del input']), fecha = request.post['nombre del input'])
        
        fam1.save()



    return render(request, "prueba5.html")

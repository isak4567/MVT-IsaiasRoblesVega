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
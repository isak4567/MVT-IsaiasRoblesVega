from django.urls import path

from .views import familia, lista_familia, vista_prueba, vista_prueba1html, vista_prueba2html, vista_prueba3html, vista_prueba4html, vista_prueba5html

urlpatterns = [
    path('agregando_f/<nombre>/<edad>/<fecha>', familia),
    path('listando_f/', lista_familia, name="familia"),
    path('vista_P/', vista_prueba),
    path('', vista_prueba1html, name="Inicio"),
    path('vista_Practca2/', vista_prueba2html, name="Servicios"),
    path('vista_Practca3/', vista_prueba3html, name="Quienes"),
    path('vista_Practca4/', vista_prueba4html, name="Preguntas"),
    path('vista_Practca5/', vista_prueba5html, name="Contacto"),
]

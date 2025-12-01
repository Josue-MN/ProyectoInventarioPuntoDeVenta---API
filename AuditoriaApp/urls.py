from django.urls import path
from AuditoriaApp import views

# Lista de rutas (URL patterns) que pertenecen a esta aplicación.
urlpatterns = [
    
    # Ruta que apunta a la vista "AuditoriaData".
    # Cuando el usuario ingrese a "/auditorias/", se ejecutará la función correspondiente.
    path(
        'auditorias/', views.AuditoriaData, name='auditorias')
]


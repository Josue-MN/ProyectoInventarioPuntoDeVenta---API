"""
URL configuration for ProyectoInventarioPuntoDeVenta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

# Lista de rutas principales de la aplicación Django
urlpatterns = [
    # Ruta principal del login
    # Todas las URLs definidas en LoginApp.urls se incluirán aquí
    # Al acceder a la raíz del sitio ("/") se manejarán las vistas de LoginApp
    path('', include('ProInvPunDeVenAPI.urls')),
]


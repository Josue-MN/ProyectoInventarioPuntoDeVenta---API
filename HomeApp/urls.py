from django.urls import path, include
from HomeApp.views import renderTemplateHome  # Importa la view que renderiza el template del home
from CrudProductosApp import views           # Importa views de la app CrudProductosApp
from CrudCategoriaProductoApp import views          # Importa views de la app CrudCategoriasApp
from CrudBodegasApp import views              # Importa views de la app CrudBodegaApp

# Lista de rutas para la aplicación HomeApp y sus secciones relacionadas
urlpatterns = [
    # Ruta raíz de HomeApp ('/')
    # Al acceder a la raíz de HomeApp, se ejecuta la view renderTemplateHome
    path('', renderTemplateHome, name='home'),

    # Rutas para CRUD de productos
    # Todas las URLs definidas en CrudProductosApp.urls se incluirán bajo /crudproductos/
    path('', include("CrudProductosApp.urls")),

    # Rutas para CRUD de categorías
    # Todas las URLs definidas en CrudCategoriasApp.urls se incluirán bajo /crudcategorias/
    path('', include("CrudCategoriaProductoApp.urls")),

    # Rutas para CRUD de bodegas
    # Todas las URLs definidas en CrudBodegaApp.urls se incluirán bajo /crudbodegas/
    path('', include("CrudBodegasApp.urls")),
]

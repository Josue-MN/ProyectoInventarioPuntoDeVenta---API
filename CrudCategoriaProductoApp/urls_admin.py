from django.urls import path
from CrudCategoriaProductoApp import views
# Lista de rutas para la aplicación CrudCategoiaApp

# Lista de rutas (URL patterns) de la aplicación CRUD de categorias solo par admin.
urlpatterns = [

    path('crud-categoriaProducto/', views.categoriaProductoData, name='admin-crud-categoria'),

    path('crud-categoriaProducto/registro-categoriaProducto/', views.categoriaProductoRegistracionView, name='admin-registrar-categoria'),

    path('crud-categoriaProducto/detalle-categoriaProducto/<int:IdCategoriaProducto>', views.detalleCategoriaProducto, name='admin-detalle-categoria'),

    path('crud-categoriaProducto/actualizar-categoriaProducto/<int:IdCategoriaProducto>', views.actualizarCategoriaProducto, name='admin-actualizar-categoria'),

    path('crud-categoriaProducto/confirmar-eliminar/<int:IdCategoriaProducto>', views.confirmarEliminar, name='admin-confirmar-eliminar-categoria'),

    path('crud-categoriaProducto/eliminar-categoriaProducto/<int:IdCategoriaProducto>', views.eliminarCategoriaProducto, name='admin-eliminar-categoria'),

]   


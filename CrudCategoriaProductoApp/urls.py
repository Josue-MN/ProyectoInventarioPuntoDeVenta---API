from django.urls import path
from CrudCategoriaProductoApp import views
# Lista de rutas para la aplicación CrudCategoiaApp


# Lista de rutas (URL patterns) de la aplicación CRUD de categorias solo para otro tipo de usuario.
urlpatterns = [

    path('crud-categoriaProducto/', views.categoriaProductoData, name='crud-categoria'),

    path('crud-categoriaProducto/registro-categoriaProducto/', views.categoriaProductoRegistracionView, name='registrar-categoria'),

    path('crud-categoriaProducto/detalle-categoriaProducto/<int:IdCategoriaProducto>', views.detalleCategoriaProducto, name='detalle-categoria'),

    path('crud-categoriaProducto/actualizar-categoriaProducto/<int:IdCategoriaProducto>', views.actualizarCategoriaProducto, name='actualizar-categoria'),

    path('crud-categoriaProducto/confirmar-eliminar/<int:IdCategoriaProducto>', views.confirmarEliminar, name='confirmar-eliminar-categoria'),

    path('crud-categoriaProducto/eliminar-categoriaProducto/<int:IdCategoriaProducto>', views.eliminarCategoriaProducto, name='eliminar-categoria'),

]   


from django.urls import path
from django.contrib import admin
from ProInvPunDeVenAPI import views

urlpatterns = [
    path('bodegas/', views.BodegasList.as_view()),
    path('bodegas/<int:pk>', views.BodegasDetail.as_view()),
    path('cargos/', views.CargosList.as_view()),
    path('cargos/<int:pk>', views.CargosDetail.as_view()),
    path('categoriaP/', views.CategoriaProductoList.as_view()),
    path('categoriaP/<int:pk>', views.CategoriaProductoDetail.as_view()),
    path('empleados/', views.EmpleadosList.as_view()),
    path('empleados/<int:pk>', views.EmpleadosDetail.as_view()),
    path('productos/', views.ProductosList.as_view()),
    path('productos/<int:pk>', views.ProductosDetail.as_view()),
    path('usuarios/', views.UsuariosList.as_view()),
    path('usuarios/<int:pk>', views.UsuariosDetail.as_view()),
]
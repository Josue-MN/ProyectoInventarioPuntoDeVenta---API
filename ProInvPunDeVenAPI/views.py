from django.shortcuts import render
from ProInvPunDeVenAPI.serializers import *
from ProInvPunDeVenAPI.models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, viewsets
from django.http import Http404

# Create your views here.
class BodegasList(generics.ListCreateAPIView):
    queryset = Bodegas.objects.all()
    serializer_class = BodegasSerializer
class BodegasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bodegas.objects.all()
    serializer_class = BodegasSerializer
class BodegasViewSets(viewsets.ModelViewSet):
    queryset = Bodegas.objects.all()
    serializer_class = BodegasSerializer
    
class CargosList(generics.ListCreateAPIView):
    queryset = Cargos.objects.all()
    serializer_class = CargosSerializer
class CargosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cargos.objects.all()
    serializer_class = CargosSerializer
class CargosViewSets(viewsets.ModelViewSet):
    queryset = Cargos.objects.all()
    serializer_class = CargosSerializer

class CategoriaProductoList(generics.ListCreateAPIView):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer
class CategoriaProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer
class CategoriaProductoViewSets(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer

class EmpleadosList(generics.ListCreateAPIView):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer
class EmpleadosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer
class EmpleadosViewSets(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer

class ProductosList(generics.ListCreateAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
class ProductosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
class ProductosViewSets(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

class UsuariosList(generics.ListCreateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
class UsuariosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
class UsuariosViewSets(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
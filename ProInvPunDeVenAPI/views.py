from django.shortcuts import render
from ProInvPunDeVenAPI.serializers import *
from ProInvPunDeVenAPI.models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.
class BodegasList(APIView):
    def get(self, request):
        bodegas = Bodegas.objects.all()
        serializer = BodegasSerializer(bodegas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BodegasSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
class BodegasDetail(APIView):
    def get_object(self, pk):
        try:
            return Bodegas.objects.get(pk=pk)
        except Bodegas.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        bodega = self.get_object(pk)
        serializer = BodegasSerializer(bodega)
        return Response(serializer.data)
    
    def put(self, request, pk):
        bodega = self.get_object(pk)
        serializer = BodegasSerializer(bodega, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        bodega = self.get_object(pk)
        bodega.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CargosList(APIView):
    def get(self, request):
        cargos = Cargos.objects.all()
        serializer = CargosSerializer(cargos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CargosSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            
class CargosDetail(APIView):
    def get_object(self, pk):
        try:
            return Cargos.objects.get(pk=pk)
        except Cargos.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        cargo = self.get_object(pk)
        serializer = CargosSerializer(cargo)
        return Response(serializer.data)
    
    def put(self, request, pk):
        cargo = self.get_object(pk)
        serializer = CargosSerializer(cargo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, pk):
        cargo = self.get_object(pk)
        cargo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    

class CategoriaProductoList(APIView):
    def get(self, request):
        categoriaP = CategoriaProducto.objects.all()
        serializer = CategoriaProductoSerializer(categoriaP, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategoriaProductoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
class CategoriaProductoDetail(APIView):
    def get_object(self, pk):
        try:
            return CategoriaProducto.objects.get(pk=pk)
        except CategoriaProducto.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        categoriaP = self.get_object(pk)
        serializer = CategoriaProductoSerializer(categoriaP)
        return Response(serializer.data)
    
    def put(self, request, pk):
        categoriaP = self.get_object(pk)
        serializer = CategoriaProductoSerializer(categoriaP, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, pk):
        categoriaP = self.get_object(pk)
        categoriaP.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class EmpleadosList(APIView):
    def get(self, request):
        empleados = Empleados.objects.all()
        serializer = EmpleadosSerializer(empleados, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EmpleadosSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
class EmpleadosDetail(APIView):
    def get_object(self, pk):
        try:
            return Empleados.objects.get(pk=pk)
        except Empleados.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        empleados = self.get_object(pk)
        serializer = EmpleadosSerializer(empleados)
        return Response(serializer.data)
    
    def put(self, request, pk):
        empleados = self.get_object(pk)
        serializer = EmpleadosSerializer(empleados, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, pk):
        empleados = self.get_object(pk)
        empleados.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ProductosList(APIView):
    def get(self, request):
        productos = Productos.objects.all()
        serializer = ProductosSerializer(productos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductosSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
class ProductosDetail(APIView):
    def get_object(self, pk):
        try:
            return Productos.objects.get(pk=pk)
        except Productos.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        productos = self.get_object(pk)
        serializer = ProductosSerializer(productos)
        return Response(serializer.data)
    
    def put(self, request, pk):
        productos = self.get_object(pk)
        serializer = ProductosSerializer(productos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, pk):
        productos = self.get_object(pk)
        productos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class UsuariosList(APIView):
    def get(self, request):
        usuarios = Usuarios.objects.all()
        serializer = UsuariosSerializer(usuarios, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UsuariosSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
class UsuariosDetail(APIView):
    def get_object(self, pk):
        try:
            return Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        usuarios = self.get_object(pk)
        serializer = UsuariosSerializer(usuarios)
        return Response(serializer.data)
    
    def put(self, request, pk):
        usuarios = self.get_object(pk)
        serializer = UsuariosSerializer(usuarios, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, pk):
        productos = self.get_object(pk)
        productos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
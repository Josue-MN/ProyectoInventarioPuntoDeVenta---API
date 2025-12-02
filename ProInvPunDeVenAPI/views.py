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
        
    def get(self, rquest, pk):
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

    

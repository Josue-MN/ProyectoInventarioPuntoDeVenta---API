from django.shortcuts import render
from ProInvPunDeVenAPI.serializers import *
from ProInvPunDeVenAPI.models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, viewsets
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class BodegasViewSets(viewsets.ModelViewSet):
    queryset = Bodegas.objects.all()
    serializer_class = BodegasSerializer
    
class CargosViewSets(viewsets.ModelViewSet):
    queryset = Cargos.objects.all()
    serializer_class = CargosSerializer

class CategoriaProductoViewSets(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer

class EmpleadosViewSets(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer

class ProductosViewSets(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

class UsuariosViewSets(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer



class logoutView(APIView):
    #ESPECIFICA QUE SOLO LOS USARIOS CON PERMISO PUEDEN USAR ESTA CLASE
    permission_classes = [IsAuthenticated]

    def post(self, request):
        #SE OBTIENE EL TOKEN REFRESH QU ENVIA EL USUARIO
        refresh = request.data.get("refresh")

        # SI NO HAY UN TOKEN, SE ENVIA UN ERROR DE QUE EL TOKEN ES REQUERIDO
        if not refresh:
            return Response({"Detalle": "Refresh token es requerido"},status=status.HTTP_400_BAD_REQUEST)
        try:
            #A PARTIR DEL TOKEN OBTENIDO SE CREA UNO PARA LUEGO AGREGARLO 
            #A LA LISTA NEGRA Y DEJAR DICHO TOKEN INUTILIZABLE
            token = RefreshToken(refresh)
            token.blacklist()

            #CIERRE DE SESION EXITOSO
            return Response({"Detalle": "Cierre de sesion"}, status=status.HTTP_200_OK)
        except Exception:
            #RETORNA QUE HAY UN ERROR POR EL TOKEN INVALIDO
            return Response({"Detalle": "Token invalido"}, status=status.HTTP_400_BAD_REQUEST)

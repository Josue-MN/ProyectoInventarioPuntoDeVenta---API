from django.shortcuts import render
from ProInvPunDeVenAPI.serializers import *
from ProInvPunDeVenAPI.models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

#SE IMPORTAN LAS CLASES DE REST_FRAMEWROK PARA CREAR UNA RUTA DE CIERRE DE SESION MEDIANTE
#LA APIVIEW, SI ESTA AUTHENTICADO(ISAUTHENTICATED) Y LOS TOKEN DE REFRESCO (REFRESHTOKEN)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

##SE IMPORTA LOS PERMISOS PARA ACCEDER A LAS VISTAS Y LA CLASES OR PARA COMPARAR DICHOS PERMISOS Y VER CUAL CORRESPONDE
##SEGUN EL CARGO DEL USUARIO
from ProInvPunDeVenAPI.permissions import *

from ProInvPunDeVenAPI.views_auditoria import *

# Create your views here.
class BodegasViewSets(viewsets.ModelViewSet):
    queryset = Bodegas.objects.all()
    serializer_class = BodegasSerializer
    permission_classes = [EsUsuarioAdmin | EsUsuarioBasicos | EsUsuarioBodeguero]

    # -------------------------
    # Crear (POST)
    # -------------------------
    def perform_create(self, serializer):
        nueva_bodega = serializer.save()  # Guarda la nueva bodega
        RegistrarAuditoriaBodega(self.request, nueva_bodega, "REGISTRAR")  # Auditoría
    # -------------------------
    # Actualizar (PUT / PATCH)
    # -------------------------
    def perform_update(self, serializer):
        bodega_actualizada = serializer.save()  # Actualiza la bodega
        RegistrarAuditoriaBodega(self.request, bodega_actualizada, "ACTUALIZAR")  # Auditoría
    # -------------------------
    # Eliminar (DELETE)
    # -------------------------
    def perform_destroy(self, instance):
        RegistrarAuditoriaBodega(self.request, instance, "ELIMINAR")  # Auditoría antes de borrar
        instance.delete()  # Borra la audtoria
    
class CargosViewSets(viewsets.ModelViewSet):
    queryset = Cargos.objects.all()
    serializer_class = CargosSerializer
    permission_classes = [EsUsuarioAdmin]

    # -------------------------
    # Crear (POST)
    # -------------------------
    def perform_create(self, serializer):
        nuevo_cargo = serializer.save()  # Guarda la nueva bodega
        RegistrarAuditoriaCargo(self.request, nuevo_cargo, "REGISTRAR")  # Auditoría
    # -------------------------
    # Actualizar (PUT / PATCH)
    # -------------------------
    def perform_update(self, serializer):
        cargo_actualizado = serializer.save()  # Actualiza la bodega
        RegistrarAuditoriaCargo(self.request, cargo_actualizado, "ACTUALIZAR")  # Auditoría
    # -------------------------
    # Eliminar (DELETE)
    # -------------------------
    def perform_destroy(self, instance):
        RegistrarAuditoriaCargo(self.request, instance, "ELIMINAR")  # Auditoría antes de borrar
        instance.delete()  # Borra la audtoria

class CategoriaProductoViewSets(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer
    permission_classes = [EsUsuarioAdmin | EsUsuarioBasicos]

    # -------------------------
    # Crear (POST)
    # -------------------------
    def perform_create(self, serializer):
        nueva_categoria = serializer.save()  # Guarda la nueva bodega
        RegistrarAuditoriaCategoria(self.request, nueva_categoria, "REGISTRAR")  # Auditoría
    # -------------------------
    # Actualizar (PUT / PATCH)
    # -------------------------
    def perform_update(self, serializer):
        categoria_actualizada = serializer.save()  # Actualiza la bodega
        RegistrarAuditoriaCategoria(self.request, categoria_actualizada, "ACTUALIZAR")  # Auditoría
    # -------------------------
    # Eliminar (DELETE)
    # -------------------------
    def perform_destroy(self, instance):
        RegistrarAuditoriaCategoria(self.request, instance, "ELIMINAR")  # Auditoría antes de borrar
        instance.delete()  # Borra la audtoria

class EmpleadosViewSets(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer
    permission_classes = [EsUsuarioAdmin]

    # -------------------------
    # Crear (POST)
    # -------------------------
    def perform_create(self, serializer):
        nuevo_empleado = serializer.save()  # Guarda la nueva bodega
        RegistrarAuditoriaEmpleado(self.request, nuevo_empleado, "REGISTRAR")  # Auditoría
    # -------------------------
    # Actualizar (PUT / PATCH)
    # -------------------------
    def perform_update(self, serializer):
        empleado_actualizado = serializer.save()  # Actualiza la bodega
        RegistrarAuditoriaEmpleado(self.request, empleado_actualizado, "ACTUALIZAR")  # Auditoría
    # -------------------------
    # Eliminar (DELETE)
    # -------------------------
    def perform_destroy(self, instance):
        RegistrarAuditoriaEmpleado(self.request, instance, "ELIMINAR")  # Auditoría antes de borrar
        instance.delete()  # Borra la audtoria

class ProductosViewSets(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    permission_classes = [EsUsuarioAdmin | EsUsuarioBasicos]

    # -------------------------
    # Crear (POST)
    # -------------------------
    def perform_create(self, serializer):
        nuevo_producto = serializer.save()  # Guarda la nueva bodega
        RegistrarAuditoriaProducto(self.request, nuevo_producto, "REGISTRAR")  # Auditoría
    # -------------------------
    # Actualizar (PUT / PATCH)
    # -------------------------
    def perform_update(self, serializer):
        producto_actualizado = serializer.save()  # Actualiza la bodega
        RegistrarAuditoriaProducto(self.request, producto_actualizado, "ACTUALIZAR")  # Auditoría
    # -------------------------
    # Eliminar (DELETE)
    # -------------------------
    def perform_destroy(self, instance):
        RegistrarAuditoriaProducto(self.request, instance, "ELIMINAR")  # Auditoría antes de borrar
        instance.delete()  # Borra la audtoria

class UsuariosViewSets(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = [EsUsuarioAdmin]

    # -------------------------
    # Crear (POST)
    # -------------------------
    def perform_create(self, serializer):
        nuevo_usuario = serializer.save()  # Guarda la nueva bodega
        RegistrarAuditoriaUsuario(self.request, nuevo_usuario, "REGISTRAR")  # Auditoría
    # -------------------------
    # Actualizar (PUT / PATCH)
    # -------------------------
    def perform_update(self, serializer):
        usuario_actualizado = serializer.save()  # Actualiza la bodega
        RegistrarAuditoriaUsuario(self.request, usuario_actualizado, "ACTUALIZAR")  # Auditoría
    # -------------------------
    # Eliminar (DELETE)
    # -------------------------
    def perform_destroy(self, instance):
        RegistrarAuditoriaUsuario(self.request, instance, "ELIMINAR")  # Auditoría antes de borrar
        instance.delete()  # Borra la audtoria

class AuditoriaBodegasViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = AuditoriaBodega.objects.all()
    serializer_class = AuditoriasBodegasSerializer
    permission_classes = [EsUsuarioAdmin]
class AuditoriaCargosViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = AuditoriaCargo.objects.all()
    serializer_class = AuditoriasCargosSerializer
    permission_classes = [EsUsuarioAdmin]
class AuditoriaCategoriaProductoViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = AuditoriaCategoria.objects.all()
    serializer_class = AuditoriasCategoriaProductoSerializer
    permission_classes = [EsUsuarioAdmin]
class AuditoriaEmpleadosViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = AuditoriaEmpleado.objects.all()
    serializer_class = AuditoriasEmpleadosSerializer
    permission_classes = [EsUsuarioAdmin]
class AuditoriaProductosViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = AuditoriaProducto.objects.all()
    serializer_class = AuditoriasProductosSerializer
    permission_classes = [EsUsuarioAdmin]
class AuditoriaUsuariosViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = AuditoriaUsuario.objects.all()
    serializer_class = AuditoriasUsuariosSerializer
    permission_classes = [EsUsuarioAdmin]
class authuserViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = auth_user.objects.all()
    serializer_class = authuserSerializer
    permission_classes = [EsUsuarioAdmin]



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

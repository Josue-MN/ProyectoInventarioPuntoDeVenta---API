from rest_framework import serializers
from ProInvPunDeVenAPI.models import *

class BodegasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodegas
        fields = '__all__'

class CargosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargos
        fields = '__all__'

class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = '__all__'

class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = '__all__'

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'



class AuditoriasBodegasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditoriaBodega
        fields = '__all__'

class AuditoriasCargosSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditoriaCargo
        fields = '__all__'

class AuditoriasCategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditoriaCategoria
        fields = '__all__'

class AuditoriasEmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditoriaEmpleado
        fields = '__all__'

class AuditoriasProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditoriaProducto
        fields = '__all__'

class AuditoriasUsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditoriaUsuario
        fields = '__all__'
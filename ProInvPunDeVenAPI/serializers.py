from rest_framework import serializers
from ProInvPunDeVenAPI import models

class BodegasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bodegas
        fields = '__all__'

class CargosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cargos
        fields = '__all__'

class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoriaProducto
        fields = '__all__'

class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Empleados
        fields = '__all__'

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Productos
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuarios
        fields = '__all__'



class AuditoriasBodegasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuditoriaBodega
        fields = '__all__'

class AuditoriasCargosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuditoriaCargo
        fields = '__all__'

class AuditoriasCategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuditoriaCategoria
        fields = '__all__'

class AuditoriasEmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuditoriaEmpleado
        fields = '__all__'

class AuditoriasProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuditoriaProducto
        fields = '__all__'

class AuditoriasUsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuditoriaUsuario
        fields = '__all__'
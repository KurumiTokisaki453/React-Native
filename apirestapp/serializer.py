from rest_framework import serializers
from .models import *

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

class CuentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuentas
        fields = '__all__'

class SesionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sesiones
        fields = '__all__'

class PaqueteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paquete
        fields = '__all__'

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'

class DestinosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinos
        fields = '__all__'

class UsuariofinalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuariofinal
        fields = '__all__'

class DestinofinalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinofinal
        fields = '__all__'

class NroseguimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nroseguimiento
        fields = '__all__'

class SaveseguimientosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saveseguimientos
        fields = '__all__'

class AsignacionenvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignacionenvio
        fields = '__all__'

class DestinoinicialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinoinicial
        fields = '__all__'

class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = '__all__'









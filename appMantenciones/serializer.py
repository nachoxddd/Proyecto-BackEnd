from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    PerfilUsuario,
    Taller,
    Vehiculo,
    AsignacionVehiculo,
    Incidente,
    Mantencion,
    HistorialEstado
)


class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUsuario
        fields = ('__all__')


class TallerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taller
        fields = ('__all__')


class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ('__all__')


class AsignacionVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionVehiculo
        fields = ('__all__')


class IncidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidente
        fields = ('__all__')


class MantencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantencion
        fields = ('__all__')


class HistorialEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialEstado
        fields = (
            'id',
            'entidad_afectada',
            'vehiculo',
            'mantencion',
            'usuario_responsable',
            'estado_anterior',
            'estado_nuevo',
            'motivo_cambio',
            'created_at'
        )
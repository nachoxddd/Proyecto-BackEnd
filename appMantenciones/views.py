from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    PerfilUsuario,
    Taller,
    Vehiculo,
    AsignacionVehiculo,
    Incidente,
    Mantencion,
    HistorialEstado
)
from .serializer import (
    PerfilUsuarioSerializer,
    TallerSerializer,
    VehiculoSerializer,
    AsignacionVehiculoSerializer,
    IncidenteSerializer,
    MantencionSerializer,
    HistorialEstadoSerializer
)


# Vista de página de inicio (creada en el punto 8)
def bienvenida(request):
    return render(request, 'appMantenciones/.html')


# Vistas Basadas en Clases (CBV - ModelViewSet) para el CRUD de la API
class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer


class TallerViewSet(viewsets.ModelViewSet):
    queryset = Taller.objects.all()
    serializer_class = TallerSerializer


class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer


class AsignacionVehiculoViewSet(viewsets.ModelViewSet):
    queryset = AsignacionVehiculo.objects.all()
    serializer_class = AsignacionVehiculoSerializer


class IncidenteViewSet(viewsets.ModelViewSet):
    queryset = Incidente.objects.all()
    serializer_class = IncidenteSerializer


class MantencionViewSet(viewsets.ModelViewSet):
    queryset = Mantencion.objects.all()
    serializer_class = MantencionSerializer


class HistorialEstadoViewSet(viewsets.ModelViewSet):
    queryset = HistorialEstado.objects.all()
    serializer_class = HistorialEstadoSerializer

def home(request):
    return render(request, 'appMantenciones/index.html')
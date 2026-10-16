from django.urls import path, include
from rest_framework import routers
from appMantenciones import views

enrutador = routers.DefaultRouter()

enrutador.register(r'perfiles', views.PerfilUsuarioViewSet)
enrutador.register(r'talleres', views.TallerViewSet)
enrutador.register(r'vehiculos', views.VehiculoViewSet)
enrutador.register(r'asignaciones', views.AsignacionVehiculoViewSet)
enrutador.register(r'incidentes', views.IncidenteViewSet)
enrutador.register(r'mantenciones', views.MantencionViewSet)
enrutador.register(r'historial-estados', views.HistorialEstadoViewSet)

urlpatterns = [
    path('', include(enrutador.urls))
]
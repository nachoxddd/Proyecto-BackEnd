from django.contrib import admin
from .models import (
    PerfilUsuario,
    Taller,
    Vehiculo,
    AsignacionVehiculo,
    Incidente,
    Mantencion,
    HistorialEstado
)

admin.site.register(PerfilUsuario)
admin.site.register(Taller)
admin.site.register(Vehiculo)
admin.site.register(AsignacionVehiculo)
admin.site.register(Incidente)
admin.site.register(Mantencion)
admin.site.register(HistorialEstado)

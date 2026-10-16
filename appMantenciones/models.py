from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class PerfilUsuario(models.Model):
    ROLES = [
        ('ADMIN', 'Administrador de Flota'),
        ('CONDUCTOR', 'Conductor'),
        ('TALLER', 'Encargado de Taller'),
        ('AUDITOR', 'Auditor / Reportes'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario de Sistema')
    rut = models.CharField('RUT', max_length=12, unique=True, null=False)
    telefono = models.CharField('Teléfono', max_length=20, null=False)
    rol = models.CharField('Perfil de Acceso', max_length=15, choices=ROLES, default='CONDUCTOR', null=False)
    licencia_clase = models.CharField('Clase de Licencia', max_length=10, null=True, blank=True)
    fecha_vencimiento_licencia = models.DateField('Vencimiento Licencia', null=True, blank=True)
    activo = models.BooleanField('Usuario Activo', default=True)
    created_at = models.DateTimeField('Fecha Creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)

    def __str__(self):
        return f"{self.usuario.get_full_name() or self.usuario.username} - {self.get_rol_display()}"


class Taller(models.Model):
    nombre = models.CharField('Nombre del Taller', max_length=100, null=False)
    rut_empresa = models.CharField('RUT Empresa', max_length=12, unique=True, null=False)
    direccion = models.CharField('Dirección', max_length=150, null=False)
    telefono = models.CharField('Teléfono Contacto', max_length=20, null=False)
    email = models.EmailField('Correo Electrónico', max_length=100, null=False)
    es_interno = models.BooleanField('Es Taller Interno', default=False)
    encargado = models.ForeignKey(
        PerfilUsuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Usuario Encargado'
    )
    activo = models.BooleanField('Taller Habilitado', default=True)
    created_at = models.DateTimeField('Fecha Creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)

    def __str__(self):
        return f"{self.nombre} ({self.rut_empresa})"


class Vehiculo(models.Model):
    ESTADOS_VEHICULO = [
        ('DISPONIBLE', 'Disponible'),
        ('EN_RUTA', 'En Ruta / Asignado'),
        ('EN_MANTENCION', 'En Mantención'),
        ('FUERA_SERVICIO', 'Fuera de Servicio / Excepcional'),
        ('DE_BAJA', 'Dado de Baja'),
    ]

    patente = models.CharField('Patente', max_length=10, unique=True, null=False)
    marca = models.CharField('Marca', max_length=50, null=False)
    modelo = models.CharField('Modelo', max_length=50, null=False)
    anio = models.IntegerField('Año Fabricación', null=False)
    numero_chasis = models.CharField('Número de Chasis (VIN)', max_length=50, unique=True, null=False)
    kilometraje_actual = models.IntegerField('Kilometraje Actual (km)', default=0, null=False)
    kilometraje_proxima_mantencion = models.IntegerField('Km Próxima Mantención', default=10000, null=False)
    fecha_vencimiento_revision = models.DateField('Vencimiento Revisión Técnica', null=False)
    estado = models.CharField('Estado Operativo', max_length=20, choices=ESTADOS_VEHICULO, default='DISPONIBLE', null=False)
    # Separación de información pública (visible para conductores/talleres) y privada (solo administración)
    observaciones_publicas = models.TextField('Observaciones Generales (Público)', max_length=500, null=True, blank=True)
    notas_administrativas_privadas = models.TextField('Notas de Gerencia / Costos (Privado)', max_length=500, null=True, blank=True)
    created_at = models.DateTimeField('Fecha Creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)

    def __str__(self):
        return f"{self.patente} - {self.marca} {self.modelo} ({self.get_estado_display()})"


class AsignacionVehiculo(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, verbose_name='Vehículo')
    conductor = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, verbose_name='Conductor Asignado')
    fecha_inicio = models.DateTimeField('Fecha y Hora de Salida', null=False)
    fecha_termino = models.DateTimeField('Fecha y Hora de Regreso', null=True, blank=True)
    km_inicial = models.IntegerField('Kilometraje Inicial', null=False)
    km_final = models.IntegerField('Kilometraje Final', null=True, blank=True)
    destino_motivo = models.CharField('Destino o Motivo de Operación', max_length=150, null=False)
    observaciones = models.TextField('Observaciones del Viaje', max_length=300, null=True, blank=True)
    activa = models.BooleanField('Asignación en Curso', default=True)
    created_at = models.DateTimeField('Fecha Creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)

    def __str__(self):
        return f"Ruta {self.vehiculo.patente} - {self.conductor.rut}"


class Incidente(models.Model):
    GRAVEDAD_CHOICES = [
        ('LEVE', 'Leve (No impide circular)'),
        ('MEDIA', 'Media (Requiere revisión pronta)'),
        ('GRAVE', 'Grave / Situación Excepcional (Inmoviliza el vehículo)'),
    ]

    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, verbose_name='Vehículo Afectado')
    reportado_por = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, verbose_name='Reportado Por')
    fecha_incidente = models.DateTimeField('Fecha y Hora del Incidente', null=False)
    gravedad = models.CharField('Nivel de Gravedad', max_length=10, choices=GRAVEDAD_CHOICES, default='LEVE', null=False)
    descripcion = models.TextField('Descripción de la Situación Excepcional', max_length=500, null=False)
    ubicacion = models.CharField('Ubicación del Evento', max_length=150, null=False)
    resuelto = models.BooleanField('Incidente Resuelto', default=False)
    es_confidencial = models.BooleanField('Reporte Privado / Confidencial', default=False)
    created_at = models.DateTimeField('Fecha Creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)

    def __str__(self):
        return f"Incidente {self.vehiculo.patente} ({self.get_gravedad_display()})"


class Mantencion(models.Model):
    TIPOS_MANTENCION = [
        ('PREVENTIVA', 'Mantención Preventiva'),
        ('CORRECTIVA', 'Mantención Correctiva'),
        ('URGENCIA', 'Reparación por Situación Excepcional'),
    ]

    ESTADOS_MANTENCION = [
        ('PROGRAMADA', 'Programada'),
        ('EN_PROCESO', 'En Taller / En Proceso'),
        ('ESPERA_REPUESTOS', 'En Espera de Repuestos'),
        ('FINALIZADA', 'Finalizada / Entregada'),
        ('CANCELADA', 'Cancelada'),
    ]

    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, verbose_name='Vehículo')
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE, verbose_name='Taller Asignado')
    incidente_asociado = models.ForeignKey(
        Incidente,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Incidente Origen (Opcional)'
    )
    tipo = models.CharField('Tipo de Mantención', max_length=15, choices=TIPOS_MANTENCION, default='PREVENTIVA', null=False)
    estado = models.CharField('Estado de Mantención', max_length=20, choices=ESTADOS_MANTENCION, default='PROGRAMADA', null=False)
    fecha_ingreso = models.DateField('Fecha de Ingreso', null=False)
    fecha_salida_estimada = models.DateField('Fecha Salida Estimada', null=False)
    fecha_salida_real = models.DateField('Fecha Salida Real', null=True, blank=True)
    km_al_ingreso = models.IntegerField('Kilometraje al Ingreso', null=False)
    descripcion_trabajo = models.TextField('Detalle técnico del trabajo (Público)', max_length=500, null=False)
    costo_repuestos = models.DecimalField('Costo Repuestos ($)', max_digits=10, decimal_places=2, default=0.00)
    costo_mano_obra = models.DecimalField('Costo Mano de Obra ($)', max_digits=10, decimal_places=2, default=0.00)
    costo_total = models.DecimalField('Costo Total ($)', max_digits=10, decimal_places=2, default=0.00)
    observacion_interna_privada = models.TextField('Auditoría de Costos / Factura (Privado)', max_length=300, null=True, blank=True)
    created_at = models.DateTimeField('Fecha Creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)

    def __str__(self):
        return f"OT #{self.id} - {self.vehiculo.patente} ({self.get_tipo_display()})"


class HistorialEstado(models.Model):
    ENTIDADES = [
        ('VEHICULO', 'Vehículo'),
        ('MANTENCION', 'Orden de Mantención'),
        ('INCIDENTE', 'Incidente'),
    ]

    entidad_afectada = models.CharField('Entidad Modificada', max_length=15, choices=ENTIDADES, null=False)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Vehículo Relacionado')
    mantencion = models.ForeignKey(Mantencion, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Mantención Relacionada')
    usuario_responsable = models.ForeignKey(PerfilUsuario, on_delete=models.SET_NULL, null=True, verbose_name='Usuario Responsable')
    estado_anterior = models.CharField('Estado Anterior', max_length=30, null=False)
    estado_nuevo = models.CharField('Estado Nuevo', max_length=30, null=False)
    motivo_cambio = models.TextField('Justificación para Auditoría', max_length=300, null=False)
    created_at = models.DateTimeField('Fecha Exacta del Evento', auto_now_add=True)

    def __str__(self):
        return f"Auditoría {self.entidad_afectada}: {self.estado_anterior} a {self.estado_nuevo}"
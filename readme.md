Control de Vehículos y Mantenciones
Empresa con flota necesita digitalizar la gestión de vehículos y mantenimiento. Actualmente gran parte de la información se mantiene distribuida en distintos registros, lo que dificulta el seguimiento de operaciones, la generación de reportes y la coordinación entre los distintos actores involucrados. El sistema deberá centralizar la información relevante y ofrecer mecanismos que permitan mantener datos históricos consistentes.
Los conductores y talleres interactuarán diariamente con la plataforma realizando operaciones que afectan el estado de los registros. Será necesario almacenar antecedentes históricos, controlar situaciones excepcionales, validar reglas de negocio y facilitar consultas complejas utilizando diferentes criterios de búsqueda. Determinados eventos producirán cambios de estado que deberán quedar registrados para efectos de auditoría y seguimiento.
La organización requiere además indicadores de gestión que permitan analizar tendencias, actividad reciente, utilización de recursos y comportamiento de los usuarios. El diseño deberá considerar distintos perfiles de acceso, información pública y privada, relaciones de dependencia entre los datos y procesos que involucren múltiples entidades conectadas entre sí. La descripción entrega suficiente contexto para que el equipo de desarrollo identifique actores, entidades, relaciones, restricciones, reglas de integridad y posibles escenarios de uso.

El sistema fue desarrollado utilizando:

- Python
- Django 6.1.1
- Django REST Framework 3.18.3
- MySQL (WampServer)
- python-decouple
- Git y GitHub

Para ejecutar el proyecto, es necesario disponer de Python y un servidor MySQL.

**1. Crear el entorno virtual:**

"python -m venv venv"

**2. Activar el entorno virtual en Windows:**

"venv\Scripts\activate"

**3. Instalar las dependencias:**

"python -m pip install -r requirements.txt"

El proyecto utiliza una base de datos llamada "bd_control_vehiculos".

En la carpeta "sql" se incluyen los scripts necesarios:

- "crear_db.sql": crea la base de datos.
- "crear_usuario.sql": crea el usuario de MySQL.
- "asignar_permisos.sql": asigna los privilegios necesarios.

Los scripts deben ejecutarse en ese orden y las credenciales deben configurarse de acuerdo con el entorno donde se ejecutará el proyecto.

Crear un archivo ".env" en la carpeta raíz del proyecto, junto al archivo "manage.py".

Se deben configurar las siguientes variables:

- "SECRET_KEY"
- "DB_NAME"
- "DB_USER"
- "DB_PASSWORD"
- "DB_HOST"
- "DB_PORT"

El archivo ".env.example" sirve como plantilla de configuración.

Para crear las tablas de la base de datos, ejecutar:

"python manage.py migrate"

Para cargar los datos iniciales incluidos en el proyecto, ejecutar:

"python manage.py loaddata datos_iniciales.json"

## Crear usuario administrador

Para crear una cuenta que permita acceder al panel administrativo de Django, ejecutar:

"python manage.py createsuperuser"

Ingresar el nombre de usuario, correo y contraseña solicitados.

## Ejecutar el proyecto

Iniciar el servidor de desarrollo:

"python manage.py runserver"

Acceder a la aplicación:

http://127.0.0.1:8000/

Panel administrativo:

http://127.0.0.1:8000/admin/

## API REST

La aplicación "appMantenciones" implementa operaciones CRUD mediante Django REST Framework.

Los métodos HTTP disponibles son:

- **GET:** consultar registros.
- **POST:** crear registros.
- **PUT:** actualizar registros.
- **PATCH:** modificar parcialmente registros.
- **DELETE:** eliminar registros o desactivarlos mediante eliminación lógica, según el modelo.

Ejemplo de endpoint:

"http://127.0.0.1:8000/appMantenciones/talleres/"


from django.contrib import admin
from django.urls import path
from appMantenciones.views import home  # <-- Importar tu vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),       # <-- Conectar la ruta vacía al home
]
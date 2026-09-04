from django.contrib import admin
from django.urls import path
from appMantenciones import views  # <-- Importar tu vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),       # <-- Conectar la ruta vacía al home
]
from django.contrib import admin
from .models import Perro, UsuarioAdoptante
@admin.register(Perro)
class PerroAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'raza', 'vacunado', 'estado']
    list_filter = ['vacunado', 'estado','edad', 'tamaño']

admin.site.register(UsuarioAdoptante)

# Register your models here.

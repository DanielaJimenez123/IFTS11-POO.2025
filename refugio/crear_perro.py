import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "refugio.settings")
django.setup()

from adopciones.models import Perro, UsuarioAdoptante

# Obtener o crear el perro
perro, creado = Perro.objects.get_or_create(
    nombre="Paco",
    defaults={
        'raza': 'caniche',
        'tamaño': 'S',
        'edad': 7,
        'peso': 5,
        'estado_salud': 'buena',
        'vacunado': True,
        'estado': 'disponible',
        'temperamento': 'amigable'
    }
)

usuario, creado_u = UsuarioAdoptante.objects.get_or_create(
    nombre="Valentina",
    apellido="Pasieka",
    dni=12345678,
    defaults={
        'email': 'valentina@gmail.com',
        'telf': '1160000000',
        'preferencias': 'caniche'
    }
)


if perro not in usuario.historial_adopciones.all():
    usuario.historial_adopciones.add(perro)
    print(f" {usuario.nombre} adoptó a {perro.nombre}, Raza: {perro.raza}")


perro.cambiar_estado('adoptado')
perro.save()

print("Estado actualizado:", perro.estado)

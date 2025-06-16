from django.db import models
class Perro(models.Model):
    DOG_SIZE = [
        ('S','Pequeño'),
        ('M', 'Mediano'),
        ('L', ' Grande'),
        ('XL', 'Extra Grande'),
    ]
    
    DOG_ESTADO=[
        ('disponible', 'Disponible'),
        ('reservado', 'Reservado'),
        ('adoptado', 'Adoptado')
    ]
    DOG_ESTADO_SALUD = [
        ('buena', 'Buena'),
        ('moderada', 'Moderada'),
        ('requiere_atencion', 'Requiere atención '),
    ]
    DOG_TEMPERAMENTO = [
        ('amigable', 'Amigable'),
        ('agresivo', 'Agresivo'),
        ('nervioso','Nervioso'),
        ('jugueton', 'Juguetón'),
        ('tranquilo', 'Tranquilo')
    ]
    nombre = models.CharField(max_length= 100)
    tamaño = models.CharField(max_length=2, choices=DOG_SIZE)
    estado = models.CharField(max_length=15, choices= DOG_ESTADO)
    raza =  models.CharField(max_length = 100)
    edad = models.IntegerField()
    peso = models.IntegerField()
    estado_salud = models.CharField(max_length = 20, choices = DOG_ESTADO_SALUD)
    vacunado = models.BooleanField()
    temperamento =  models.CharField(max_length = 20, choices = DOG_TEMPERAMENTO)
    def __str__(self):
      return f"{self.nombre} {self.raza}"
    def cambiar_estado(self,nuevo_estado):
        if nuevo_estado in dict(self.DOG_ESTADO):
            self.estado = nuevo_estado
            print("Estado actualizado") 
        else:
            print("Estado inválido")
class UsuarioAdoptante(models.Model):
    PREFERENCIAS_CHOICES = [
        ('caniche','Caniche'),
        ('pitbull', 'Pitbull'),
        ('labrador', 'Labrador'),
        ('doverman','Doverman'),
        ('callejero', 'Callejero'),
        ('otro', 'Otro')
    ]
    class Meta:
        verbose_name = "Usuario adoptante"
        verbose_name_plural = "Usuarios adoptantes"
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni= models.IntegerField()
    email= models.EmailField(max_length=100)
    telf= models.CharField(max_length=15)
    preferencias= models.CharField(max_length= 50,choices= PREFERENCIAS_CHOICES)
    historial_adopciones= models.ManyToManyField('Perro', blank=True)
    

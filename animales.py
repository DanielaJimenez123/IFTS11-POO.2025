class Perro:
    def __init__(self,nombre,raza,edad, tamaño,peso,estado_salud, vacunado,estado,temperamento,id):
        self.nombre= nombre
        self.raza=raza
        self.edad=edad
        self.tamaño=tamaño
        self.peso= peso
        self.estado_salud= estado_salud
        self.vacunado=vacunado
        self.estado= estado
        self.temperamento= temperamento
        self.id= id
    def cambiarEstado(self,nuevo_estado):
        if nuevo_estado in ['disponible', 'reservado', 'adoptado']:
            self.estado = nuevo_estado
            print("Estado actualizado")
        else:
            print("Estado inválido")
    def mostrarInformacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Tamaño: {self.tamaño} cm")
        print(f"Peso: {self.peso} kg")
        print(f"Estado de salud: {self.estado_salud}")
        print(f"Vacunado: {self.vacunado}")
        print(f"Estado: {self.estado}")
        print(f"Temperamento: {self.temperamento}")
        print(f"ID: {self.id}")
perro1 = Perro("Paco","caniche",12,50, 20,"bueno",True,"Disponible","Tranquilo", 3443)
perro1.mostrarInformacion()
class UsuarioAdoptante:
    def __init__(self,nombre,dni,email,preferencias,historial_adopciones):
        self.nombre= nombre
        self.dni= dni
        self.email= email
        self.preferencias= preferencias
        self.historial_adopciones=historial_adopciones
    def registrarse(self,nombre,dni,apellido,email):
        self.nombre= nombre
        self.dni = dni
        self.email= email
        print(f"nombre. {self.nombre}", f"apellido: {self.apellido}", f"email: {self.email}", f"Telf: {self.telf}")


        

       


        

        
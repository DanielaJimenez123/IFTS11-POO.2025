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
perro1 = Perro("Paco","caniche",12,50, 20,"bueno",True,"disponible","Tranquilo", 3443)
perro1.mostrarInformacion()
class UsuarioAdoptante:                        
    def __init__(self,nombre,apellido,dni,email,telf,preferencias,historial_adopciones):
        self.nombre= nombre
        self.apellido=apellido
        self.dni= dni
        self.email= email
        self.telf= telf
        self.preferencias= preferencias
        self.historial_adopciones=historial_adopciones

    def modificarDatos(self,nuevo_nombre,nuevo_apellido,nuevo_dni,nuevo_email,nuevo_telf, nueva_preferencia):
        self.nombre= nuevo_nombre
        self.apellido= nuevo_apellido
        self.dni= nuevo_dni
        self.email= nuevo_email
        self.telf= nuevo_telf
        self.preferencias= nueva_preferencia
        print("Datos actualizados correctamente")
    def mostrarDatosUsuario(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print( f"Dni: {self.dni}")
        print(f"Email: {self.email}")
        print(f"Telf: {self.telf}")
        print( f"Preferencias: {self.preferencias}")
        if self.historial_adopciones:
            print("Perros adoptados:")
            for perro in self.historial_adopciones:
                print(perro.nombre, perro.raza)
        else:
            print("Aún no ha adoptado ningún perro")
    def verHistorial(self):
        print(self.historial_adopciones)
    def __str__(self):
      return f"{self.nombre} {self.apellido} - {self.email}"


#usuario1= UsuarioAdoptante("Daniela","Jiménez",9523846,"danielaji@gmail.com",11347284,"caniche",[])
#usuario1.mostrarDatosUsuario()
#usuario1.modificarDatos("Dani","Miranda",9624866,"lita@gmail.com",116611763, "pitbull")
#usuario1.historial_adopciones.append(perro1)
#usuario1.mostrarDatosUsuario()
class SistemaAdopcion:
    def __init__(self):
        self.perros=[]
        self.usuarios= []
    def cargarPerro(self,nuevo_perro):
        self.perros.append(nuevo_perro)
        print(f"{self.perros}")
    def eliminarPerros(self, nombre):

         for perro in self.perros:
             if perro.nombre == nombre:
               self.perros.remove(perro)
               print(f"Perro {nombre} eliminado.")
               break
         else:
    
            print("No se encontró un perro con ese nombre.")
         print(f"{self.perros}")
    def registrarUsuario(self,nuevo_usuario):
        self.usuarios.append(nuevo_usuario)
    def postularPerro(self,id):
        for perro in self.perros:
            if perro.id == id:
                if perro.estado== "disponible":
                    perro.cambiarEstado("reservado")
                    print(f"Perro {id} reservado con éxito!")
                    return perro
                else:
                    print(f"Este perro {id} se encuentra resservado, no es posible postularse")
                    return None
        print(f"No se encontró ningun perro con el ID {id}")
        return None
    def confirmarAdopcion(self,perro_id,usuario_dni):
        perro_encontrado= None
        usuario_encontrado= None
        for perro in self.perros:
            if perro.id== perro_id:
                if perro.estado == ("reservado"):
                    perro.cambiarEstado("adoptado")
                    perro_encontrado = perro
                    break
        if perro_encontrado is None:
                raise ValueError(f"No se encontró un perro reservado con ID {perro_id}.")
        for usuario in self.usuarios:
            if usuario.dni == usuario_dni:
                usuario_encontrado= usuario
                break
        if usuario_encontrado is None:
             raise ValueError(f"No se encontró un usuario con DNI {usuario_dni}.")
        if perro_encontrado and usuario_encontrado:
             usuario_encontrado.historial_adopciones.append(perro_encontrado)
             print(f"Adopción confirmada: {perro_encontrado.nombre} fue adoptado por {usuario_encontrado.nombre}")
    def sugerirPerro(self,dni):
        for usuario in self.usuarios:
            if usuario.dni== dni:
                usuario.preferencias
                preferencias= usuario.preferencias
        for perro in self.perros:
            if perro.estado ==("disponible"):
                if perro.raza == preferencias and perro.estado == "disponible":
                   print(f"Se sugiere el perro: {perro.nombre}")
                   
                

        
    



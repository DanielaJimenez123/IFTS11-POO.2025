class Mascotas:
    def __init__(self,nombre, edad, raza):
        self.nombre= nombre
        self.edad= edad
        self.raza= raza
class Perros(Mascotas):
    def __init__(self, nombre, edad,raza, sonido):
        super().__init__(nombre, edad,raza)
        self.sonido= sonido
    def ladrar(self):
        print(f"{self.nombre} dice: {self.sonido}")
mi_perro= Perros("Paco", 5,"caniche", "guau!")
mi_perro.ladrar()
class Gatos(Mascotas):
    def __init__(self, nombre, edad, raza,sonido):
        super().__init__(nombre, edad,raza)
        self.sonido= sonido
    def maullar(self):
        print(f"{self.nombre} dice: {self.sonido}")
mi_gato= Gatos(" Mi gato Michi",3,"siames","miiiiiaaauuu")
mi_gato.maullar()
class Estudiante:
    def __init__(self,nombre, edad,nota_final):
        self.nombre= nombre
        self.edad= edad
        self.nota_final= nota_final
    def aprobo(self):
        return self.nota_final >= 6
       
estudiante1= Estudiante("Daniela",32,5)
print(estudiante1.aprobo())

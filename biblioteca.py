class Libro:
    def __init__(self,titulo,autor,paginas):
        self.titulo=titulo
        self.autor=autor
        self.paginas=paginas
    def info(self):
        print(f"{self.titulo},{self.autor}, {self.paginas}")
libro1= Libro("Cien años de soledad","Gabriel Garcia Marquez", 563)
libro1.info()
class Estudiante:
    def __init__(self,nombre, edad,nota_final):
        self.nombre= nombre
        self.edad= edad
        self.nota_final= nota_final
    def aprobo(self):
        if self.nota_final == 6:
            return True
        else:
            return False
estudiante1= Estudiante("Daniela",32,"6")
estudiante1.aprobo()
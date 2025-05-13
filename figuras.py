class Figura:
    def __init__(self,nombre,area):
        self.nombre= nombre
        self.area= area 
    def mostrarArea(self):
        if self.area is not None:
            print(round(self.area,2))

class Triangulo(Figura):
    def __init__(self, nombre,altura,base):
        self.altura= altura
        self.base= base
        area= (base*altura)/2
        super().__init__(nombre, area)
class Cuadrado(Figura):
    def __init__(self, nombre,lado):
        self.lado=lado
        area= lado*lado
        super().__init__(nombre, area)
import math
class Circulo(Figura):
    def __init__(self, nombre,radio):
        self.radio= radio
        area = math.pi *(radio*radio)
        super().__init__(nombre, area)
t= Triangulo("triangulo bonito",10,5)
c= Cuadrado("Cuadrado1",10)
c1= Circulo("Circulo vicioso",10)
t.mostrarArea()
c.mostrarArea()
c1.mostrarArea()
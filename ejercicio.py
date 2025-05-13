class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    def __add__(self, otra_fraccion):
    
        numerador_resultado = (self.numerador * otra_fraccion.denominador) + (self.denominador * otra_fraccion.numerador)
        denominador_resultado = (self.denominador * otra_fraccion.denominador)

        return Fraccion(numerador_resultado, denominador_resultado)
    def __sub__(self,otra_fraccion):
        numerador_resultado=(self.numerador * otra_fraccion.denominador)-(self.denominador*otra_fraccion.numerador)
        denominador_resultado=(self.denominador*otra_fraccion.denominador)
        return Fraccion(numerador_resultado, denominador_resultado)
    def __mul__(self,otra_fraccion):
        numerador_resultado= self.numerador * otra_fraccion.numerador
        denominador_resultado= self.denominador * otra_fraccion.denominador
        return Fraccion(numerador_resultado, denominador_resultado)
    def __truediv__(self,otra_fraccion):
        numerador_resultado= self.numerador* otra_fraccion.denominador
        denominador_resultado= self.denominador* otra_fraccion.numerador
        return Fraccion(numerador_resultado, denominador_resultado)
         #ef mostrar(self):
        #print(f"{self.numerador}/{self.denominador}".replace("/1", ""))

    def mostrar(self):
        if self.denominador == 1:
            print(self.numerador)
        else:
            print(f"{self.numerador}/{self.denominador}")
f1=Fraccion(8,2)
f2= Fraccion(3,3)
resultado= f1-f2
resultado.mostrar()

    



        
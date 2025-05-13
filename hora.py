class Hora:
    def __init__(self,hora,minuto,segundo):
        self.hora= hora
        self.minuto= minuto
        self.segundo= segundo
    def __add__(self,otra_hora):
        resultado_hora= self.hora+ otra_hora.hora
        resultado_minuto= self.minuto + otra_hora.minuto
        resultado_segundo= self.segundo + otra_hora.segundo
        if resultado_segundo > 60:
            resultado_segundo-=60
            resultado_minuto += 1 
        if resultado_minuto >= 60:
            resultado_minuto -= 60
            resultado_hora += 1 
        if resultado_hora >= 24:
            resultado_hora -= 24
        return Hora(resultado_hora, resultado_minuto, resultado_segundo)
    def mostrar(self):
        print(f"{self.hora:02}:{self.minuto:02}:{self.segundo:02}")
h1=Hora(24,2,35)
h2= Hora(16,3,30)
resultado= h1+h2
resultado.mostrar()
        

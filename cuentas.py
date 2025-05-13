class Cuenta:
    def __init__(self,nro_cuenta,nombre,saldo,estado_cuenta):
        self.nro_cuenta= nro_cuenta
        self.nombre= nombre
        self.saldo=saldo
        self.estado_cuenta= estado_cuenta
    def montoSuma(self,ingreso):
        self.saldo += ingreso
        return self.saldo
    def montoRetiro(self,retiro):
        self.saldo -= retiro
        return self.saldo
    def mostrarInformacion(self):
         print(f"N° de cuenta: {self.nro_cuenta}")
         print(f"Titular: {self.nombre}")
         print(f"Saldo: ${self.saldo}")
         print(f"Estado: {self.estado_cuenta}")
class CuentaMayor(Cuenta):
    def __init__(self, nro_cuenta, nombre, saldo, estado_cuenta):
        super().__init__(nro_cuenta, nombre, saldo, estado_cuenta)
    def mayorDeEdad(self,edad):
        self.edad=edad
        if self.edad > 18:
            return "Si es mayor de edad"
        else:
            return "Es menor de edad"
class CuentaMenor(Cuenta):
    def __init__(self, nro_cuenta, nombre, saldo, estado_cuenta):
        super().__init__(nro_cuenta, nombre, saldo, estado_cuenta)
class CuentaEstudiante(Cuenta):
    def __init__(self, nro_cuenta, nombre, saldo, estado_cuenta):
        super().__init__(nro_cuenta, nombre, saldo, estado_cuenta)
cM= CuentaMayor(3155,"Daniela Jiménez",38000,"Activa")
cmenor= CuentaMenor(5789,"Gustavo Passieka",15000,"activa")
cE= CuentaEstudiante(3189,"Emily Sanchez",20000,"activa")
cM.montoRetiro(3000)
cmenor.montoSuma(10000)
cE.montoSuma(1000)

cM.mostrarInformacion()
cmenor.mostrarInformacion()
cE.mostrarInformacion()

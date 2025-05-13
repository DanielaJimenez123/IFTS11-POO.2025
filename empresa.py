class Empleado:
    def __init__(self,nombre,apellido,telf,email,dni,sueldo):
        self.nombre= nombre
        self.apellido=apellido
        self.telf= telf
        self.email= email
        self.dni= dni
        self.sueldo=sueldo
class Depto_Sistemas(Empleado):
    def __init__(self, nombre, apellido, telf, email, dni, sueldo,area_sistemas,tiene_titulo,tiene_compu,personas_a_cargo):
        self.area_sistemas= area_sistemas
        self.tiene_titulo = tiene_titulo
        self.tiene_compu= tiene_compu
        self.personas_a_cargo = personas_a_cargo
        super().__init__(nombre, apellido, telf, email, dni, sueldo)
class Programador(Depto_Sistemas):
    def __init__(self, nombre, apellido, telf, email, dni, sueldo, area_sistemas, tiene_titulo, tiene_compu, personas_a_cargo,lenguaje_progra,categoria,cantidad_vencio_sistema):
        self.lenguaje_progra= lenguaje_progra
        self.categoria= categoria
        self.cantidad_vencio_sistema = cantidad_vencio_sistema
        super().__init__(nombre, apellido, telf, email, dni, sueldo, area_sistemas, tiene_titulo, tiene_compu, personas_a_cargo)
    def mostrarInformacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"telf: {self.telf}")
        print(f"Email: {self.email}")
        print(f"Dni: {self.dni}")
        print(f"Sueldo $: {self.sueldo}")
        print(f"Area Sistemas: {self.area_sistemas}")
        print(f"Tiene título: {"Si" if self.tiene_titulo else "No"}")
        print(f"Tiene computadora: {"Si" if self.tiene_compu else "No"}")
        print(f"Cantidad de personas a cargo:{self.personas_a_cargo}")
        print(f"Lenguaje progrmacón que usa:{self.lenguaje_progra}")
        print(f"Categoria Programador:{self.categoria}")
        print(f"Cantidad de veces que tumbo al sistema: {self.cantidad_vencio_sistema}")
p1=Programador("Daniela","Jiménez",1134727823,"danielajimirandagmail.com",257898,38000,"Finanzas",False, True,4,"Python","Junior",3)

p1.mostrarInformacion()
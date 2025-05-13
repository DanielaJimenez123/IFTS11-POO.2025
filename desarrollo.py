class Ambiente:
    def __init__(self,sistema_operativo,ram,base_datos,app,):
        self.sistema_operativo= sistema_operativo
        self.ram= ram
        self.base_datos= base_datos
        self.app= app
    def verificar_despliegue(self):
        if self.sistema_operativo == "Linux" and self.ram ==4 and  self.base_datos=="postgresql" and self.app =="openjdk":
            print("El despliegue se puede realizar")
        else:
            print("El despligue no se puede realizar")

                 

        

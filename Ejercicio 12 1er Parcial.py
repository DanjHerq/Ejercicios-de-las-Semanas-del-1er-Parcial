from Ejercio_11_1er_Parcial import Cargo

class Empleado:
    secuencia=0
    def __init__(self,nomb="",sue="",carg=None):
        
        self.codigo=self.generarCodigo()
        self.nombre=nomb
        self.sueldo=sue
        self.cargoEmp=carg
        
    def generarCodigo(self):
        Empleado.secuencia=Empleado.secuencia+1
        return Empleado.secuencia
    
    def mostrar(self):
        print("Codigo:{} Nombre:{} Cargo({}):".format(self.codigo,self.nombre,self.cargo.Emp.codigo,self.cargoEmp.descr))
                
cargo1 = Cargo("Estudiante")    
emp1 = Empleado("Daniel", 1994, cargo1)
emp1.mostrar()
emp2 = Empleado("Jesús", 1999, cargo1)
emp2.mostrar()     

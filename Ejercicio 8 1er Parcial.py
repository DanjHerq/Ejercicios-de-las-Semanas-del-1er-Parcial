class Condicion:
    def __init__(self,num1,num2):
        self.numero1=num1
        self.numero2=num2
        numero= self.numero1+self.numero2
        self.numero3=numero
    def Condicion(self):
        if self.numero1 == self.numero2:
            print ("El 1er número: {} y el 2do número: {} son iguales".format(self.numero1,self.numero2))
        elif self.numero1 < self.numero3:
            print("El 1er número: {} es menor que el 3er número: {}".format(self.numero1,self.numero3))
        else:
            print("No son iguales")
    print("Fin del método")            
condi1=Condicion(8,18)
print(condi1.numero3)
print(condi1.Condicion())
            
            
                    
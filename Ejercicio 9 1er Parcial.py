class Ciclo:
    def __init__(self,num=10):
        self.numero=num
        
    def usowhile(self):
        caracter=""
        while caracter not in ("a","e","i","o","u"):
            caracter=input("Ingrese la vocal: ").lower()
        print("Felicitaciones el caracter {} es una vocal".format(caracter))       
    
ciclo1= Ciclo()
ciclo1.usowhile()    
    
        
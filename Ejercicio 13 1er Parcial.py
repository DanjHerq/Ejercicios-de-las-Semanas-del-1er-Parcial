class Buscador:
    def __init__(self,datos):
        self.lista= datos
    
    def recorrerelemento(self):
        for elemento in self.lista:
            print(elemento,end=" ")
        
        for ele in self.lista[::-1]:
            print(elemento,end=" ")
        
        print()
        for pos,elemento in enumerate(self.lista):
            print("[{}]={}  ".format(pos,elemento))
        print()
        
        for pos in range(len(self.lista)-1,-1,-1):
            print("[{}]={}  ".format(pos,self.lista[pos]))
        
    def buscar(self,buscador):
        for pos,elemento in enumerate(self.lista):
            if elemento==buscador:
                break
        return pos
               
datos = [5,6,4,9,3,7]
buscador=7
search=buscador(datos)
search.recorrerele()
x=4
R=search.buscar(x)
if R !=1:
    print("El número {} se encuentra en la posición [{}] de la lista {} ".format(x,R,search.lista))
else:
    print("El número {} no se encuentra en la lista {} ".format(x,search.lista))



numerosbuscador=(3,8,7,6,4)
respuesta={}
for valor in numerosbuscador:
    resp=search.buscar(x)
    if resp !=-1: respuesta[x]=resp
print(respuesta)
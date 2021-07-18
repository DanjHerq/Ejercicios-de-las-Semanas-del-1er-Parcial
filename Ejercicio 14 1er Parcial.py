class Ordenar:
    def __init__(self,lista):
        self.lista=lista
        
    def recorrerElemento(self):
        for elemento in self.lista:
            print(elemento)
            
    def recorrerPosicion(self):        
        for posicion,elemento in enumerate(self.lista):
            print(posicion,elemento)    
    
    def recorrerRange(self):
        for posicion in range(len(self.lista)):
            print(posicion,self.lista[posicion])
    
    def buscar(self,buscado):
        enc=False
        for posicion,elemento in enumerate(self.lista):
            if elemento == buscado:
                enc=True
                break
        if enc == True:return posicion
        else:return -1 

    def ordenarAsc(self):
        for posicion in range(len(self.lista)):
            for sig in range(posicion+1,len(self.lista)):
                if self.lista[posicion] > self.lista[sig]:
                   aux = self.lista[posicion]
                   self.lista[posicion]=self.lista[sig]
                   self.lista[sig]=aux


            
    def ordenarDes(self):
        for posicion,elemento in enumerate(self.lista):
            for sig in range(posicion+1,len(self.lista)):
                if elemento < self.lista[sig]:
                    aux = self.lista[posicion]
                    self.lista[posicion]=self.lista[sig]
                    self.lista[sig]= aux
                    
    def primer(self):
        return self.lista[0]
    
    def primerEliminado(self):
        primer = self.lista[0]
        auxlista = []
        for posicion in range(1,len(self.lista)):
            auxlista.append(self.lista[posicion])
        self.lista=auxlista
        return primer
    
    def primerEliminado2(self):
        primer = self.lista[0]
        self.lista = self.lista[1:]
        return primer
    
    def ultimo(self):
        return self.lista[-1]
    
    def ultimoEliminado(self):
        ultimo = self.lista[-1]
        auxlista = []
        for posicion in range(0,len(self.lista)-1):
            auxlista.append(self.lista[posicion])
        self.lista=auxlista
        return ultimo
    
    def ultimoEliminado2(self):
         ultimo = self.lista[-1]
         self.lista = self.lista[0:-1]
         return ultimo
     
    def inserta(self):
        self.ordenarAsc()
        
 

lista = [2,3,1,5,8,10]
inserta= 4
ord1= Ordenar(lista)
print(ord1.lista)
print(ord1.ultimoEliminado())
print(ord1.lista)
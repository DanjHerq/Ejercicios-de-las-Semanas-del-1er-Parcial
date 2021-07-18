class añadir:
    def __init__(self,cifras):
        self.terminos=cifras
        
    def ordennumAsc(self):
        for posicion in range(0,len(self.terminos)-1):
            for sig in range(posicion+1,len(self.terminos)):
                if self.terminos[posicion]>self.terminos[sig]:
                    anexo=self.terminos[posicion]
                    self.terminos[posicion]=self.terminos[sig]
                    self.terminos[sig]=anexo
    
    def añadirnum(self,numero):
        self.ordennumAsc()
        anexo=[]
        for posicion,elemento in enumerate(self.terminos):
            if numero<elemento:
                anexo.append(numero)
                break
        self.terminos=cifras
        self.terminos=self.terminos[0:posicion]+anexo+self.terminos[posicion:]
        
    def añadirnum2(self,numero):
        self.ordennumAsc()
        anexo=[]
        for posicion,elemento in enumerate(self.terminos):
            if numero<elemento:
                break
        self.terminos=cifras
        for i in range(posicion):
            anexo.append(self.terminos[i])
        anexo.append(numero)
        for k in range(posicion,len(self.terminos)):
            anexo.append(self.terminos[k])
        self.terminos=anexo
        
    def añadir2dometodo(self,num):
        self.terminos=cifras
        self.terminos.append(num)
        self.ordennumAsc()
        
    def eliminar(self,num):
        conf=False
        for posicion,elemento in enumerate(self.terminos):
            if num==elemento:
                conf=True
                break
        if conf:
            self.terminos=cifras
            self.terminos=self.terminos[0:posicion]+self.terminos[posicion+1:]
        return conf
       
cifras=[7,3,8,10,21,9]
agregar=añadir(cifras)
print(agregar.añadirnum(11))
print(agregar.terminos)
print(agregar.añadirnum2(6))
print(agregar.terminos)
print(agregar.añadir2metodo(15))
print(agregar.terminos)

if agregar.eliminar(10)==True:
    print("El número ingresado si se encontro en la lista y a sido eliminado",agregar.terminos)
else:
    print("El número ingresado no se encontro en la lista, por lo tanto que queda intacta",agregar.terminos)
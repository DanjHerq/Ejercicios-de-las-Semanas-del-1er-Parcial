class logica:
    def __init__(self):
        pass
    
    def par(self,numero):
        res=numero%2
        if res == 0:
            print("El número: {} es Par".format(numero))
        else:
            print("El número: {} es Impar".format(numero))
    
    def par2dometodo(self,numero):
        res = numero%2
        return res
    
    def divisores(self,termino):
        divisores=[]
        for divisor in range(1,termino):
            res = termino%divisor
            if res == 0:
                divisores.append(divisor)
        return divisores
    
    def perfecto(self,namber):
        acu=0
        for divisor in range(1,namber):
            res = namber%divisor
            if res==0:
                acu=acu+divisor
        return acu

algoritmo=logica()
numero=int(input("Ingrese un número: "))
algoritmo.par(numero)
conjunto=[2,1,5,7,8,10,6]
pares=[]
impares={}
for num in conjunto:
    if algoritmo.par2dometodo(num)==0:
        pares.append(num)
    else:
        impares[num]="Impar"
print("Los números pares del conjunto son: ",pares)
print("Los número impares del conjunto son los siguientes: ",impares)

termino = int(input("Ingrese el número para determinar sus divisores: "))
print(algoritmo.divisores(termino))

namber= int(input("Ingrese un número para descubrir si es perfecto: "))
if algoritmo.perfecto(namber)==namber:
    print("El número si es perfecto")
else:
    print("El número no es perfecto")
    
grupo=[5,2,6,30,28,10,74]
for per in grupo:
    if algoritmo.perfecto(per)==per:
        print(num," perfecto ") 
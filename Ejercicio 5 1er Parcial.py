#Funciones sin retorno
def vocales(Frase):
    for car in Frase:
        if car in ("a","e","i","o","u"):
            print(car)
 #Llamada a la Función
 oracion= input("Ingrese una oración: ")
 vocales(oracion.lower())
 #Función con retorno de valores
 def Promedio (Notas):
     summ=0
     for n in Notas:
         summ += n
     return summ / len(Notas)
 #Llamada a la Función
Listadenotas= [2,4,6,8,10]
prom= promedio(Listadenotas)
print ("Promedio: {} = {} ".format(Listadenotas,prom))
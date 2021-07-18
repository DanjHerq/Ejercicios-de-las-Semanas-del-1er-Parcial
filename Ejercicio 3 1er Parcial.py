# Uso del While Infinito
c=1
while True:
    print(c)
    break
# While de Validación
Vocal= input("Ingrese una vocal: ")
while Vocal not in ("a","e","i","o","u"):
    if Vocal==".":
        break
    Vocal=input("Vocal:")
print("Su vocal o punto es: {}" .format(Vocal))        

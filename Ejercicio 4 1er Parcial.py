# for range(v) – range(vi,vf)  - range(vi,vf,inc)
Frase= input("Ingrese una frase: ")
for Indice in range(len(Frase)):
    print(Indice, "=", Frase[Indice])

# for in cadena - in(tupla) – in[lista]  
for car in Frase:
    if car in ("a","e","i","o","u","A","E","I","O","U"):
        if car in ["A","E","I","O","U"]:
            continue
        else:
            cvoc=cvoc+1
print("cantidad de vocales: {}".format(cvoc))

# Comprehension – [var for var in datos condicion]
[car for car in["a","e","i","o","u"] if car not in("a","i","o")]
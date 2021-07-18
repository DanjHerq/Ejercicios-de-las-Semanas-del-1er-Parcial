# Tuplas – Listas - Diccionarios
usuario = ("Danj","1994","dhenriquez@unemi.edu.ec")
materias = ["Python","PHP","POO","Sistemas Operativos"]
Estudiante = {"nombre":"Daniel Jesús","edad": 26,"facultad": "faci"}
print(usuario[0],materias[1],Estudiante['nombre'])
print(usuario[0:2],Estudiante.keys(),Estudiante.values())
materias.append("Estructura de datos")
Estudiante["sexo"], Estudiante["edad"]="Masculino", 26
print(materias,Estudiante)
#tupla,lista,diccionario=(),[],{}
# Recorridos tuplas y listas con in
for valor in usuario: print(valor)
# Recorridos listas con enumerate
for i, c in enumerate(materias): print(i,':',c)
# Recorridos diccionario con items
for c, v in Estudiante.items(): print(c,':',v)
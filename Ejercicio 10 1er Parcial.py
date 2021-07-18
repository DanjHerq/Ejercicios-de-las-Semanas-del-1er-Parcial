class For:
    def __init__(self):
        pass
  
    def usoFor(self):
        # ciclo repetitivo de incrementos o decremetos se ejecuta por verdadero
        nombre = "Daniel"
        datos=["Daniel",26,True]
        # pos     0    1   2
        numeros=(2,5.6,4,1)
        estudiante = {'nombre': 'Daniel', 'edad': 26, 'fac': 'faci'}
        listaNotas = [(70,80),(40,80),(100,80)]
        listaAlumnos=[{"nombre":"Daniel","final":140},{"nombre":"Jesús","final":120},{"nombre":"Katherine","final":180}]
        
        #'''version1'''
        listaNotas = [(70,80,20,40),(40,80,50),(100,80,20),(20,40)]
        acum=0
        cont=0
        for notas in listaNotas:
            print(notas)
            acumparcial=0
            contparcial=0
            for nota in notas:
                acumparcial +=nota
                contparcial +=1
                cont=cont+1
            print(acumparcial/contparcial)
        print(acum/cont)
       
        # '''versión2'''
        listaNotas = [(60,80,20,40),(40,80,50),(100,80,20),(20,40)]
        acum,cont=0,0
        for notas in listaNotas:
            print(notas)
            acumparcial=0
            for nota in notas:
                acumparcial +=nota
            cont=cont+len(notas)
            acum=acum+acumparcial    
            print("TotalParcial:{} PromParcial:{}".format(acumparcial,acumparcial/len(notas)))
        print("TotalGeneral:{} PromGeneral:{}".format(acum,acum/cont))  
        
bucle = For()
bucle.usoFor()   
 

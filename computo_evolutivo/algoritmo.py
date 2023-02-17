# algoritmo evolutivo 1  15/02/2023
#
import random
import math
import statistics

def aptitud_funcion(x):
    return ((x*x*x - (10*(x*x)) - x + 1) * (math.sin(x)))



def iniciar(tamanio, poblacion):
    for i in range(tamanio):
        temp = [0,0]
        # individuo i
        temp[0] = random.uniform(-9, 16)
        # temp[0] = 11

        # aptitud del individuo i
        temp[1] = aptitud_funcion(temp[0])
        poblacion.append(temp)



def ordena(poblacion):
    for i in range(len(poblacion)):
        for j in range(0, int(len(poblacion))-i-1):
            # ordena de mayor a menor
            if poblacion[j][1] < poblacion[j+1][1]:
                poblacion[j], poblacion[j+1] = poblacion[j+1], poblacion[j]
    

def evalua(poblacion):
    # evalua con la función de aptitud a los nuevos individuos
    for i in range(int(len(poblacion))):
        poblacion[i][1] = aptitud_funcion(poblacion[i][0])
    



def generacion_hijos(poblacion):
    # Haciendo una cruza de la primera mitad de elementos
    
    for i in range(int(len(poblacion)/2)):
        otro = random.randint(0, int(len(poblacion)/2))
        poblacion[i+(int(len(poblacion)/2))][0] = (poblacion[i][0] + \
        poblacion[otro][0])/2 
    
    # evalua con la funcion de aptitud a los nuevos individuos
    for i in range(int(len(poblacion))):
        poblacion[i][1] = aptitud_funcion(poblacion[i][0])
      


def mutacion(poblacion):
    # genera un cambio en los hijos (la mitad "inferior" del arreglo de
    # poblacion)
    for i in range(int(len(poblacion)/2), int(len(poblacion))):
        # mutación de los hijos
        poblacion[i][0] = poblacion[i][0] + random.normalvariate(0, 0.1)
        # para no salirnos del rango
        if poblacion[i][0] < -10:
            poblacion[i][0] = 10
        if poblacion[i][0] > 16:
            poblacion[i][0] = 16


def main(repeticiones, tamanio):
    pob = []
    # Genera población inicial
    iniciar(tamanio, pob)
    # Imprime
    print("Poblacion inicial :")
    for i in pob:
        print(i)
    # Generaciones
    generacion = 0

    #for i in range(repeticiones): 
    while(pob[0][1] < 871.99):
        # Ordena por aptitud
        ordena(pob)

        # Genera hijos
        generacion_hijos(pob) 

        # mutacion
        mutacion(pob)
        evalua(pob)
        ordena(pob)
        
        generacion = generacion + 1
    print("Población final :")
    for i in pob:
        print(i)
    return generacion

# main(repeticiones, tamaño_de_poblacion)
gens = []
for i in range(1):
    # ignorar "1000"
    gens.append(main(1000, 20))

# promedio
print("Resultados: ", gens)
print("Promedio", statistics.mean(gens))
print("Desv estandar: ", statistics.pstdev(gens))

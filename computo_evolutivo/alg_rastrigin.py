# Optimizacion de la función de Rastrigin
# 17/02/2023
# Ángel Emmanuel Pérez Geovanni

import random
import math
import statistics

# Recibe un individuo de la forma [[a1,a2,a3], p]
# donde "p" es la aptitud
def aptitud_func(x):
    a = 10 * int(len(x[0])) 
    b = 0
    for i in x[0]:
        b = b + (i**2 - (10 * math.cos(2*math.pi*i)))
    # valor de la aptitud (p)
    x[1] = a + b



# Devuelve una lista del tipo [[[a1,a2,a3],p], [[a1,a2,a3],p], ... ]
# tamanio <- tamaño de la población
# long_individuo <- tamaño del individuo (número de variables)
def iniciar(tamanio, long_individuo):
    ind_x = [0 for s in range(long_individuo)]
    ind_xy = [ind_x, "aptitud"]
    poblacion = [ind_xy for s in range(tamanio)]
    for i in poblacion:
        # genera los valores de X "aleatoriamente"
        for j in range(len(i[0])):
            # genera un número aleatorio entre -5.12 y 5.12 para el vector
            i[0][j] = random.uniform(-5.12, 5.12)
        print(i[0])
        # calcula valor de la aptitud
        aptitud_func(i)
    # regresa la lista de individuos evaluada
    return poblacion



# recibe una población y la ordena de menor a mayor (minimización) de acuerdo a
# su aptitud
def ordena(poblacion):
    for i in range(int(len(poblacion))):
        for j in range(0, int(len(poblacion)) - i - 1):
            # compara (bubble sort)
            if poblacion[j][1] > poblacion[j+1][1]:
                # intercambio si poblacion[j+1] es menor (sube al inicio)
                poblacion[j], poblacion[j+1] = poblacion[j+1], poblacion[j]



# Evalua toda la poblacion con la funcion de aptitud
def evalua(poblacion):
    for i in poblacion:
        aptitud_func(i)



# Técnica de media aritmética para el cruce
# recibe dos individuos y genera un hijo
# calcula su aptitud
def cruce_media_aritmetica(a, b):
    vector = [5 for i in range(len(a))]
    hijo_nuevo = ["vector","aptitud"]
    # Por cada elemento del individuo
    for i in range(len(a)):
        vector[i] = (a[0][i] + b[0][i])/2
    # coloca el vector al hijo
    hijo_nuevo[0] = vector
    # evalua aptitud de nuevo hijo
    aptitud_func(hijo_nuevo)    
    # devuelve hijo nuevo
    return hijo_nuevo
    


# Para crear una nueva generación de hijos con la mitad de individuos mejor
# adaptados, sustituyendo a los menos adaptados (mitad inferior)
# Realiza por medio de media aritmética de pares de individuos
def generacion_hijos(poblacion):
    mitad_pob = int(len(poblacion)/2)
    # para la mitad superior (primera mitad) de la lista de individuos
    for i in range(mitad_pob):
        # escoje una pareja de las más aptas (de la mitad superior)
        pareja = random.randint(0 , mitad_pob)
        # realiza el cruce de individuo y pareja y acomoda en la sección de
        # hijos
        poblacion[i + mitad_pob] = cruce_media_aritmetica(poblacion[i], poblacion[pareja])
    # NOTA: Los individuos nuevos ya están evaluados pero no acomodados en la
    # población



def mutacion(poblacion, rango=2):
    # Hará mutar la mitad de la poblacion
    # dependiendo si rango = 0, se mutará a toda la población
    # si rango = 1, se mutará a los padres (primera mitad <<superior>>)
    # si rango = 2 o cualquier otro, se mutará a la segunda mitad (hijos)
    if rango == 0:
        inicio = 0
        fin = int(len(poblacion))
    elif rango == 1:
        inicio = 0 
        fin = int(len(poblacion)/2)
    else:
        inicio = int(len(poblacion)/2)
        fin = int(len(poblacion))
    # inicia mutacion
    # para cada individuo
    for i in range(inicio, fin):
        # para cada elemento "j" del vector del individuo "i"
        for j in poblacion[i][0]:
            # Aplica suma de número aleatorio de distribución normal
            j = j + random.normalvariate(0, 0.01)



# imprime la población
def imprime_pob(poblacion):
    print("Individuo\t\tAptitud")
    for i in range(len(poblacion)):
        print(i, "\t", poblacion[i][0], "\t", poblacion[i][1])



# Evolución, función principal
def main(tamanio_pob, tamanio_vector, repeticiones=0):
    # inicia población
    pob = iniciar(tamanio_pob, tamanio_vector)

    # ordena la poblacion inicial, no es necesario evaluar, la función de
    # iniciar ya la evaluó
    ordena(pob)
    n_generaciones = 0

    # imprime poblacion
    print("Población inicial :")
    imprime_pob(pob)

    # Inicia el ciclo de evolución
    # depende si repeticiones es igual a 0 (cero) se buscará que el valor de la
    # aptitud del mejor individuo se acerque a cero (~ 0.0001)
    if repeticiones == 0:
        while pob[0][1] > 0.01:
            # Ordena para empezar
            ordena(pob)

            # generacion y evaluacion de hijos nuevos
            generacion_hijos(pob)
            # ordena hijos nuevos
            ordena(pob)

            # mutación de la mitad inferior, en este caso
            mutacion(pob)
            evalua(pob)
            ordena(pob)

            # suma de una nueva generacion a la cuenta
            n_generaciones = n_generaciones + 1

        print("Poblacion final: ")
        imprime_pob(pob) 
    else:
        for i in range(repeticiones):
            # Ordena para empezar
            ordena(pob)

            # generacion y evaluacion de hijos nuevos
            generacion_hijos(pob)
            # ordena hijos nuevos
            ordena(pob)

            # mutación de la mitad inferior, en este caso
            mutacion(pob)
            evalua(pob)
            ordena(pob)

        print("Poblacion final: ")
        imprime_pob(pob) 

#main
main(20, 10)

         







#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#● Crear una lista con los pares y otra con los impares.
#● Mostrar cuántos números tiene cada lista.

#Importamos la libreria random 

import random

#Creamos la lista vacia para luego cargar los valores al azar
listaRandom = []
#Creamos las listas de impares e pares vacias
listaPar = []
listaImpar = []



#Realizamos una iteracion
for i in range(0,15):
    #Generamos el número entre 1 y 100 
    num = random.randint(1, 100) 
    # Agregamos a la lista usando append 
    listaRandom.append(num) 


#Recorremos la lista random y verificamos si el numero que encuentra en la posicion es par o impar
#Realizamos una iteracion
for i in range(len(listaRandom)):
    if listaRandom[i] % 2 == 0:
        listaPar.append(listaRandom[i])
    else:
        listaImpar.append(listaRandom[i])

#Contamos cuantos numeros tiene cada lista
cantPar = len(listaPar)
cantImpar = len(listaImpar)

#Imprimimos la cantidad de numeros que tiene cada lista
print(f"La cantidad de numeros pares es: {cantPar}")
print(f"La cantidad de numeros impares es: {cantImpar}")
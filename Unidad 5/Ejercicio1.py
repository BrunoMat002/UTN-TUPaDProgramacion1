#1) Crear una lista con las notas de 10 estudiantes.
#● Mostrar la lista completa.
#● Calcular y mostrar el promedio.
# #● Indicar la nota más alta y la más baja.

listaNotas = [3.45,5.50,10,8.50,9.50,2.50,6,4.50,7,8]

#Realizamos una iteracion para mostrar todas las notas
#Recorremos la lista y calculamos el promedio
#Inicializamos dos variables para poder calcular los promedios
cantTotalNotas = 0
valorFinalNotas = 0
#Inicializmaos dos variables para saber cual es la nota mas alta y cual la mas baja.
#Al maximo lo inicializamos con un valor bajo y al minimo lo inicializamos con un valor alto
max = -1
min = 11


for i in range(len(listaNotas)):
    #Lo realizamos todo en una misma iteracion para no volver hacerlo mas veces.
    #Obtenemos amvos valores
    cantTotalNotas += 1
    valorFinalNotas += listaNotas[i]
    #Verificamos si el valor de la lista en dicha posicion(i) es mayor o menor que los valores de las variables max y min.
    if listaNotas[i] > max:
        max = listaNotas[i]
    if listaNotas[i] < min:
        min = listaNotas[i]

    #Mostramos las notas
    print(listaNotas[i])

#Realizamos el calculo del promedio
promedio = valorFinalNotas // cantTotalNotas

#Imprimimos todo lo que pide el ejercicio
print(f"El promedio de las notas es: {promedio}")

print(f"La nota mas alta es: {max} y la nota mas baja es: {min}")



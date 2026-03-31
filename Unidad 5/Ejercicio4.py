#4) Dada una lista con valores repetidos:
#● Crear una nueva lista sin elementos repetidos.
#datos = [1,3,5,3,7,1,9,5,3]
#● Mostrar el resultado.

#Datos que da el enunciado
datos = [1,3,5,3,7,1,9,5,3]

#Inicializamos una lista que guardara los elementos no repetidos

listaNueva = []

#Realizamos una iteracion
for i in range(len(datos)):
    #Verificamos si el numero esta en la lista nueva, si no lo esta lo agregamos
    if datos[i] not in listaNueva:
        listaNueva.append(datos[i])

#Imprimimos la lista nueva.
print(listaNueva)
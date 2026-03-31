#2) Pedir al usuario que cargue 5 productos en una lista.
#● Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#● Preguntar al usuario qué producto desea eliminar y actualizar la lista


#Inicializamos una lista vacia

listaProductos = []

#Le pedimos al usuario que cargue la lista y realizamos una iteracion para que cargue 5 elementos

for i in range(0,5):
    producto = input("Ingrese un producto: ")
    listaProductos.append(producto)


#Ordenamos los elementos de la lista usando el sorted()

listaOrdenada = sorted(listaProductos)

#Verificamos que los elementos queden ordenados de manera alfabetica
print(listaOrdenada)

#Le preguntamos al usuario que producto desea eliminar y actualizamos la lista
eliminar = input("Ingrese el nombre del producto que desee eliminar: ")

#Eliminamos dicho producto
listaOrdenada.remove(eliminar)

#Verificamos si se elimino el elemento
print(listaOrdenada)
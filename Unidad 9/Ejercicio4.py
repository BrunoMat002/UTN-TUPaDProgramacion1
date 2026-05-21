#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
#una lista llamada productos, donde cada elemento sea un diccionario con claves:
#nombre, precio, cantidad.



#Inicializamos una lista donde vamos a guardar todos los productos
productos = []

#Abrimos el archivo para lectura
with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")

        producto = {
            "nombre": datos[0],
            "precio": datos[1],
            "cantidad": datos[2]
        }

        productos.append(producto)

#Mostramos la lista final
print(productos)
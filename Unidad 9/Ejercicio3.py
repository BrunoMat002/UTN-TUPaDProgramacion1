#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente.

#Abrimos el archivo productos.txt y hacemos que lea cada linea
with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        #Procesa cada uno con strip(elimina cosas invisibles) y split(divide el texto en partes y al agregarle "," lo separamos en coma)
        datos = linea.strip().split(",")

        nombre = datos[0]
        precio = datos[1]
        cantidad = datos[2]
        #Imprimimos como nos pide el ejercicio.
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

#Pedimos al usuairo que ingrese un nuevo producto
print("Ingrese un nuevo producto:")

nombre_nuevo = input("Nombre: ")
precio_nuevo = input("Precio: ")
cantidad_nuevo = input("Cantidad: ")

#Lo agregamos al archivo sin borrar lo anterior
with open("productos.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{nombre_nuevo},{precio_nuevo},{cantidad_nuevo}\n")
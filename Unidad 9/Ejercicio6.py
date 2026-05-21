#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
#productos actualizados desde la lista.

#Inicializamos una lista vacia
productos = []

#Leemos el archivo y cargamos en la lista
with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")

        if len(datos) == 3:
            producto = {
                "nombre": datos[0],
                "precio": datos[1],
                "cantidad": datos[2]
            }
            productos.append(producto)

#agregamos un producto nuevo
nombre = input("Nombre: ")
precio = input("Precio: ")
cantidad = input("Cantidad: ")

#Lo agregamos a la lista
productos.append({
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad
})

#Sobrescribimos el archivo con la lista actualizada
with open("productos.txt", "w", encoding="utf-8") as archivo:
    for p in productos:
        linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
        archivo.write(linea)

print("Archivo actualizado correctamente.")
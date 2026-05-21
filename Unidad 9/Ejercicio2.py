#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
#formato:
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30

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
#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
#no existe, mostrar un mensaje de error.

#Pedimos al usuario que ingrese el nombre del producto para buscar

buscar = input("Ingrese el nombre del producto: ").strip().lower()

#Inicializamos una variable en False
encontrado = False

#Abrumos el archivo

with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")

        nombre = datos[0].strip()
        precio = datos[1].strip()
        cantidad = datos[2].strip()

        #Verificamos si se encuentra e imprimimos los datos
        if nombre.lower() == buscar:
            print("\nProducto encontrado:")
            print("Nombre:", nombre)
            print("Precio:", precio)
            print("Cantidad:", cantidad)
            encontrado = True
            break
    #Si no se encontro
    if not encontrado:
        print("Error: el producto no existe. ")
#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario: 
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.


#Armamos un diccionario con las claves y valores

diccionario_herramientas={"martillo" : 10, "destornillador" : 4, "alicate" : 5, "serrucho" : 3}

#Realizamos un menu para que el usuario elija lo que quiera hacer

#Inicializamos una variable para desplazarnos en el menu
opcion = 0

while opcion != 4:
    print("\n 1. --Consultar el stock--")
    print("\n 2. --Agregar unidades al stock--")
    print("\n 3. --Agregar un nuevo producto--")
    print("\n 4. --Salir del Menu--")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        #Consultamos el stock de un producto
        producto = input("Ingrese el nombre del producto a consultar: ").lower()
        if producto in diccionario_herramientas:
            # Si existe, accedemos al valor mediante la clave 
            print(f"El stock actual de {producto} es: {diccionario_herramientas[producto]}")
        else:
            print(f"El producto '{producto}' no se encuentra en el inventario.")

    elif opcion == 2:
        #Agregamos unidades al stock si el producto ya existe
        producto = input("Ingrese el producto al que desea sumar stock: ").lower()
        if producto in diccionario_herramientas:
            cantidad = int(input(f"¿Cuantas unidades desea sumar a {producto}?: "))
            diccionario_herramientas[producto] += cantidad
            print(f"Stock actualizado. Nuevo total de {producto}: {diccionario_herramientas[producto]}")
        else:
            print("Error: El producto no existe. Use la opcion 3 para darlo de alta.")

    elif opcion == 3:
        #Agregamos un nuevo producto si no existe
        nuevo_producto = input("Ingrese el nombre del nuevo producto: ").lower()
        if nuevo_producto in diccionario_herramientas:
            print("Ese producto ya existe. Si desea sumar stock, use la opcion 2.")
        else:
            stock_inicial = int(input(f"Ingrese el stock inicial para {nuevo_producto}: "))
            diccionario_herramientas[nuevo_producto] = stock_inicial
            print(f"Producto '{nuevo_producto}' agregado con exito.")

    elif opcion == 4:
        print("Saliendo del sistema de inventario...")
    else:
        print("Opcion no valida. Por favor, elija una opcion del 1 al 4.")
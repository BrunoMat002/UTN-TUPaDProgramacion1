
#===============================================================================================================================================
#  FUNCIONES AUXILIARES
#===============================================================================================================================================
def normalizar_nombre(nombre):
    #Esta funcion la utilizaremos para limpiar los espacios y estandarizar a minusculas,permitiendo comparar nombres segun la consigna 
    #(ej. " Martillo " -> "martillo").
    return nombre.strip().lower()
#===============================================================================================================================================
def existe_herramienta(inventario, nombre):
    #Con esta funcion verificaremos si la herramienta se encuentra en el inventario o no
    nombre_buscado = normalizar_nombre(nombre)
    for item in inventario:
        if normalizar_nombre(item["herramienta"]) == nombre_buscado:
            return True
    return False
#===============================================================================================================================================
#===============================================================================================================================================



#===============================================================================================================================================
#  PROGRAMA PRINCIPAL
#===============================================================================================================================================

# Carga de Herramientas 
def cargar_herramientas(inventario):
    if len(inventario) > 0:
        print("\nEl inventario ya contiene productos. Para agregar nuevos use la opcion 5.")
        return

    while True:
        try:
            cantidad_a_cargar = int(input("\n¿Cuantas herramientas desea cargar inicialmente?: "))
            if cantidad_a_cargar <= 0:
                print("Error: La cantidad de herramientas a cargar debe ser un numero entero mayor que cero.")
                continue
            break
        except ValueError:
            print("Error: Debe ingresar un numero entero valido.")

    cargadas = 0
    while cargadas < cantidad_a_cargar:
        print(f"\n--- Cargando herramienta {cargadas + 1} de {cantidad_a_cargar} ---")
        
        nombre = input("Nombre de la herramienta: ")
        if not nombre.strip():
            print("Error de validacion: El nombre de la herramienta no puede estar vacio.")
            continue
        #Verificamos que no sea un numero
        if not nombre.replace(" ", "").isalpha():
            print("Error de validacion: El nombre de la herramienta solo debe contener letras.")
            continue

        if existe_herramienta(inventario, nombre):
            print("Error de validacion: Esta herramienta ya esta registrada en el inventario.")
            continue

        # Bucle interno exclusivo para validar el stock sin perder el nombre de la herramienta
        while True:
            try:
                stock_inicial = int(input("Stock inicial: "))
                if stock_inicial < 0:
                    print("Error: El stock inicial puede ser cero o mayor, pero nunca negativo.")
                    continue
                break  # Stock correcto, salimos del bucle del stock
            except ValueError:
                print("Error: El stock debe ser un numero entero valido.")

        # Si llegó acá, tanto el nombre como el stock son válidos
        nueva_herramienta = {
            "herramienta": nombre.strip(),
            "cantidad": stock_inicial
        }
        inventario.append(nueva_herramienta)
        cargadas += 1
        print(f"¡{nombre.strip()} cargada con exito.")
#===============================================================================================================================================
#Ver Inventario
#Mostramos el listado completo de herramientas y cuatas hay
def Visualizar_inventario(inventario):
    if len(inventario) == 0:
        print("\nNo hay herramientas cargadas en el inventario.")
        return

    print("\n========= LISTADO DE INVENTARIO =========")
    for item in inventario:
        print(f"- Producto: {item['herramienta']} | Unidades: {item['cantidad']}")
    print("=========================================")

#===============================================================================================================================================
#Consultar stock de las herramientas
def Consulta_stock(inventario):
    #Verificamos que esten cargadas las herramientas
    if len(inventario) == 0:
        print("\n No hay herramientas cargadas en el inventario.")
        return

    nombre_buscar = input("\nIngrese el nombre de la herramienta a consultar: ")
    nombre_normalizado = normalizar_nombre(nombre_buscar)
    
    encontrado = False
    for item in inventario:
        if normalizar_nombre(item["herramienta"]) == nombre_normalizado:
            print(f"\nHerramienta: {item['herramienta']} | Stock Disponible: {item['cantidad']}")
            encontrado = True
            break
            
    if not encontrado:
        print(f"\nLa herramienta {nombre_buscar.strip()} no se encuentra en el catalogo.")

#===============================================================================================================================================
#Stock agotado
def Agotados(inventario):
    #Verificamos que las herramientas esten cargadas en el inventario
    if len(inventario) == 0:
        print("\nNo hay herramientas cargadas en el inventario.")
        return

    print("\n========= PRODUCTOS AGOTADOS (STOCK 0) =========")
    conteo_agotados = 0
    #Si tienen stock 0 informar
    for item in inventario:
        if item["cantidad"] == 0:
            print(f"- {item['herramienta']} esta AGOTADO.")
            conteo_agotados += 1
            
    if conteo_agotados == 0:
        print("No se encontraron productos agotados en el sistema.")
    print("=================================================")
#===============================================================================================================================================
#Agregar un nuevo producto
def Nuevo_producto(inventario):
    #Aseguramos que el usuario realice el primer paso antes que el 5
    if len(inventario) == 0:
        print("Primero debe realizar la carga inicial utilizando la opcion 1.")
        return
    print("\n--- Alta de un Único Nuevo Producto ---")
    #Verificamos que el usuario ingrese correctamente un nombre
    try:
        nombre = input("Nombre de la nueva herramienta: ")
        if not nombre.strip():
            raise ValueError("El nombre de la herramienta no puede estar vacio.")
        
        if not nombre.replace(" ", "").isalpha():
            raise ValueError("El nombre de la herramienta solo debe contener letras.")
        
        if existe_herramienta(inventario, nombre):
            raise ValueError("Esta herramienta ya existe en el inventario.")

        try:
            stock_inicial = int(input("Stock inicial: "))
            if stock_inicial < 0:
                raise ValueError("El stock inicial no puede ser negativo.")
        except ValueError as e:
            if "invalid literal for int()" in str(e):
                raise ValueError("El stock debe ser un numero entero valido.")
            else:
                raise e

        # Agregamos al final de la lista si paso los filtros
        inventario.append({"herramienta": nombre.strip(), "cantidad": stock_inicial})
        print(f"¡Producto {nombre.strip()} dado de alta correctamente!")
    #Si ocurrio algun error volvemos al menu principal
    except ValueError as e:
        print(f"\nNo se pudo agregar el producto: {e}")
        print("Regresando al menu principal.")

#===============================================================================================================================================
#Actualizar el stock
def Actualizar_stock(inventario):
    
    #Verificamos que este cargado el inventario
    if len(inventario) == 0:
        print("\nNo hay herramientas cargadas. No se pueden realizar movimientos de stock.")
        return

    nombre_buscar = input("\nIngrese el nombre de la herramienta a modificar: ")
    nombre_normalizado = normalizar_nombre(nombre_buscar)

    # Buscamos la herramienta e identificamos su indice
    indice_encontrado = -1
    for i in range(len(inventario)):
        if normalizar_nombre(inventario[i]["herramienta"]) == nombre_normalizado:
            indice_encontrado = i
            break

    if indice_encontrado == -1:
        print(f"La herramienta {nombre_buscar.strip()} no existe en el catalogo.")
        return

    # Si existe, procedemos al submenu de movimiento
    print(f"\nProducto seleccionado: {inventario[indice_encontrado]['herramienta']} (Stock actual: {inventario[indice_encontrado]['cantidad']})")
    print("1. Registrar Ingreso (Reposicion)")
    print("2. Registrar Venta (Disminucion)")
    
    #verificamos que el usuaroi ingrese correctamente una opcion
    try:
        tipo_movimiento = int(input("Seleccione el tipo de movimiento: "))
        if tipo_movimiento not in [1, 2]:
            raise ValueError("Opcion de movimiento invalida (Debe ser 1 o 2).")

        cantidad_mov = int(input("Ingrese la cantidad (entero mayor a cero): "))
        if cantidad_mov <= 0:
            raise ValueError("La cantidad ingresada debe ser un numero mayor a cero.")

        if tipo_movimiento == 1:
            # Ingreso
            inventario[indice_encontrado]['cantidad'] += cantidad_mov
            print(f"¡Ingreso registrado! Nuevo stock de {inventario[indice_encontrado]['herramienta']}: {inventario[indice_encontrado]['cantidad']}")
        
        elif tipo_movimiento == 2:
            # Venta (Validar que no quede en negativo)
            stock_actual = inventario[indice_encontrado]["cantidad"]
            if stock_actual - cantidad_mov < 0:
                raise ValueError(f"Venta rechazada. Stock insuficiente. Solamente hay {stock_actual} unidades disponibles.")
            
            inventario[indice_encontrado]["cantidad"] -= cantidad_mov
            print(f"¡Venta registrada! Nuevo stock de {inventario[indice_encontrado]['herramienta']}: {inventario[indice_encontrado]['cantidad']}")

    except ValueError as e:
        if "invalid literal for int()" in str(e):
            print("Debe ingresar un numero entero valido para las cantidades y opciones.")
        else:
            print(f"Movimiento cancelado: {e}")
#===============================================================================================================================================
# Menu

def menu(inventario):

    #Hacemos un menu interactivo que mientras el usuario no ingrese la opcion 7 (salida) se se debera desplegar una vez mas el menu
    #Inicializamos la una variable con la que nos desplazaremos atravez del menu
    
    opcion = 0
    
    while opcion != 7:
        print("--MENU--")
        print("-"*60)
        print("Eliga una de las siguientes opciones: ")
        print("-"*60)
        print("1.Carga de Herramientas")
        print("2.Visualizacion de inventario")
        print("3.Consulta de stock")
        print("4.Reporte de agotados")
        print("5.Alta de nuevo producto")
        print("6.Actualizacion de stock")
        print("7.Salir")
        #Verificamos que el usuario ingrese algunos de los valores correctos
        try:
            opcion = int(input("Opcion: "))
            if opcion == 1:
                cargar_herramientas(inventario)
            elif opcion == 2:
                Visualizar_inventario(inventario)
            elif opcion == 3:
                Consulta_stock(inventario)
            elif opcion == 4:
                Agotados(inventario)
            elif opcion == 5:
                Nuevo_producto(inventario)
            elif opcion == 6:
                Actualizar_stock(inventario)
            elif opcion == 7:
                print("El sistema Finalizo!!.")
            else:
                print("Opcion fuera de rango. Por favor, elija un numero del 1 al 7.")
                
        except ValueError:
            print("Entrada invalida. Debe ingresar un numero entero.")
            # Reseteamos la opcion para asegurar que el bucle continue sin problemas
            opcion = 0    

#===============================================================================================================================================

inventario = []

menu(inventario)
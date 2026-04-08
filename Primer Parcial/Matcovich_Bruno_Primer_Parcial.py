#l programa debe presentar un menú interactivo persistente con las siguientes opciones:



#Inicializamos las listas y variables que necesitamos
listaHerramientas = []
listaCantidadHerramientas = []
listaCero = []
opcion = ""

while opcion != "8":
    #Creamos lo que sera el menu interactivo
    print("\n--Menu--")

    print("\n 1. Cargar Inicial de Herramientas")
    print("\n 2. Carga de Existencias ")
    print("\n 3. Visualización de Inventario ")
    print("\n 4. Consulta de Stock (existencias) ")
    print("\n 5. Reporte de Agotados ")
    print("\n 6. Alta de Nuevo Producto")
    print("\n 7. Actualización de Stock (Venta/Ingreso) ")
    print("\n 8. Salir ")

    PriOpcion = input("\n Eliga una de las siguientes opciones: ")

    #Verificamos si el usuario ingreso correctamente un numero
    while not PriOpcion.isdigit() or int(PriOpcion) < 1 or int(PriOpcion) >8:
        print("\n Ingrese un numero valido (entre el 1 y el 8): ")
        PriOpcion = input("\n Eliga una de las siguientes opciones: ")


    #Convertimos a integer la variable priOpcion
    opcion =int(PriOpcion)

#1. Carga Inicial de Herramientas: Registrar los nombres de las herramientas que se
#pondrán a la venta. Se debe preguntar al usuario la cantidad de herramientas a cargar
#y se debe usar una estructura pertinente. En caso de nombre vacío o duplicado se
#debe seguir pidiendo hasta que sea correcto respetando la cantidad de herramientas
#que el usuario indicó antes de la carga.


    #Si es 1 
    if opcion == 1:
        print("\n Ingrese la cantidad de herramientas para subir: ")
        totalHerramientasPri = input (" ")
        #Verificamos que el usuario ingrese un numero y que sea distinto a 0 o si es negatico
        while not totalHerramientasPri.isdigit() or int(totalHerramientasPri) == 0:
            print("\n No ah ingresado un numero o el numero es menor a 0, intente nuevamente: ")
            totalHerramientasPri = input (" ")
        #Convertimos a integer la variable cantHerramientasPri    
        cantHerramientas =int(totalHerramientasPri)
        #Inicializamos una variable que utilizaremos como contadora
        cargados = 0

        while cargados < cantHerramientas:    
            nombreHerramienta =input("\n Ingrese el nombre de la herramienta: ")
            #Verificamos que haya ingresado un string
            if nombreHerramienta == "" or not nombreHerramienta.isalpha():
                print("\n No ah ingresado un nombre valido, porfavor intente nuevamente: ")
            #Verificamos si la herramienta esta en la lista
            elif nombreHerramienta in listaHerramientas:
                print(f"La herramienta {nombreHerramienta} ya esta registrada")
            else:
                #Agregamos la herramienta a la lista y aumentamos el contador
                listaHerramientas.append(nombreHerramienta)
                cargados += 1


    #2. Carga de Existencias: Ingresar la cantidad de unidades para cada herramienta
    #registrada previamente, respetando el orden de ingreso. Cuando el usuario ingresa
    #existencias, el sistema debe mostrar por pantalla el nombre de la herramienta.
    elif opcion == 2:
        #Verificamos que la lista no este vacia
        if len(listaHerramientas) == 0:
            print("\n Primero ingrese herramientas para este paso")
            continue
        # Inicializamos dos valores, con los cuales verificaremos que se cargue solo las nuevas cantidades
        # de las herramientas que no tengamos ya cargadas en las listas.
        inicio = len(listaCantidadHerramientas)
        fin = len(listaHerramientas)

        if inicio == fin:
            print("\n Todas las herramientas ya tienen stock cargado.")
        else: 
        #Recorremos toda la lista cargada e ingresamos en otra lista la cantidad de herramientas que posee
            for i in range(inicio, fin):
                totalHerramientasPri = input(f"Ingrese la cantidad de {listaHerramientas[i]} que tiene: ")
                #Verificamos que el usuario ingrese un numero
                while not totalHerramientasPri.isdigit():
                    print("\n ingrese un numero porfavor: ")
                    totalHerramientasPri = input(f"Ingrese la cantidad de {listaHerramientas[i]} que tiene: ")
                totalHerramientas =int(totalHerramientasPri)
                listaCantidadHerramientas.append(totalHerramientas)
                

    #3. Visualización de Inventario: Mostrar el listado completo de herramientas junto a su stock actual.
    elif opcion == 3:
        #Verificamos que los inventarios esten cargados
        if len(listaHerramientas) == 0 or len(listaCantidadHerramientas) == 0:
            print("\n Primero debe cargar herramientas y sus cantidades para poder visualizarlas")
            continue
        #Mostramos en pantalla ambas listas
        for i in range(len(listaHerramientas)):
            print(f"Usted tiene: -- {listaCantidadHerramientas[i]} {listaHerramientas[i]} -- ")

    #4. Consulta de Stock (existencias): Buscar una herramienta por su nombre y mostrar
    #cuántas unidades hay disponibles.
    elif opcion == 4:
        #Verificamos que se hayan cargados elementos en la lista
        if len(listaHerramientas) == 0:
            print("\n Primero debe cargar herramientas para poder visualizarlas")
            continue
        #Pedimos al usuario que ingrese la herramienta
        consulta = input("\n Ingrese el nombre de la herramienta que quiere buscar: ")
        #Verificamos que ingrese un string, y no un 0 o este vacio
        while consulta == "" or not consulta.isalpha():
            print("\n Ingrese por favor un nombre valido: ")
            consulta = input("\n Ingrese el nombre de la herramienta que quiere buscar: ")
        #Verificamos en la lista si esta ese nombre
        if consulta in listaHerramientas:
            indice = listaHerramientas.index(consulta)
            #Accedemos directamente al valor en la lista de cantidades usando ese índice 
            unidades = listaCantidadHerramientas[indice]
    
            print(f"Resultado de la búsqueda:")
            print(f"Herramienta: {consulta}")
            print(f"Unidades disponibles: {unidades}")
        else:
            # Si el valor no está presente, el operador 'in' retorna False 
            print(f"Error: La herramienta '{consulta}' no se encuentra en el inventario.")
    #5. Reporte de Agotados: Listar únicamente aquellos productos cuyo stock sea igual a cero.
    elif opcion == 5:
        #verificamos que se hayan cargados las cantidades de herramientas
        if len(listaCantidadHerramientas) == 0:
            print("\n Primero se deben agregar las cantidades de herramientas")
            continue
        #recorremos la lista de cantidades de herramientas
        for i in range(len(listaCantidadHerramientas)):
            if listaCantidadHerramientas[i] == 0:
                listaCero.append(listaHerramientas[i])
        #Al final mostramos las herramientas que tienen stock 0
        if len(listaCero) > 0:
            print(f"Las herramientas que tienen stock 0 son: {listaCero} ")
        else:
            print("\n No hay productos agotados actualmente.")
    
    #6. Alta de Nuevo Producto: Permitir agregar solo una nueva herramienta al final de las
    #listas con su stock inicial. En caso de nombre vacío, nombre duplicado o valor de
    #existencia negativo se debe volver al menú principal mostrando por pantalla el motivo
    elif opcion == 6:
        #primero veirifcamos que este cargada la lista de herramientas
        if len(listaHerramientas) == 0:
            print("\n Primero debe de ingresar herramientas.")
            continue
        #Pedimos al usuario que ingrese la nueva herramienta
        nueva_Herramienta = input("\n Ingrese el nombre de la nueva herramienta: ")
        #Verificamos todos los casos de error
        if nueva_Herramienta == "" or not nueva_Herramienta.isalpha():
            print("\n Usted a dejado el espacio en blanco o ah ingresado un nombre no valido, por favor ingrese un nombre de manera correcta.")
            continue
        elif nueva_Herramienta in listaHerramientas:
            print(f"la herramienta {nueva_Herramienta}, ya se encuentra en la lista, porfavor ingrese una nueva herramienta.")
            continue
        
        
        #Agregamos su cantidad en stock
        cant_Nueva_Herramienta_Pri =input(f"Ingrese la cantidad de {nueva_Herramienta}, que posee: ")
        if not cant_Nueva_Herramienta_Pri.isdigit():
            print("\n El valor deberia ser numerico, no puede contener letras, porfavor ingrese un valor correcto")
            continue
        cant_Nueva_Herramienta=int(cant_Nueva_Herramienta_Pri)
        #Verificamos que el numero ingresado no es negativo
        if cant_Nueva_Herramienta < 0:
            print("\n El numero de stock no puede ser negativo, por favor ingrese un valor valido.")
            continue

        #Solo si todo esta bien agregamos en ambas listas.
        listaHerramientas.append(nueva_Herramienta)
        listaCantidadHerramientas.append(cant_Nueva_Herramienta)
    #7. Actualización de Stock (Venta/Ingreso):
    #o Venta: Disminuir el stock tras validar que hay unidades suficientes.
    #o Ingreso: Aumentar el stock por reposición de mercadería.
    elif opcion == 7:
        #Verificamos que ambas listas esten cargadas
        if len(listaCantidadHerramientas) == 0 or len(listaHerramientas) == 0:
            print("\n Primero debe cargar herramientas y sus cantidades. ")
            continue
        print("1. Venta")
        print("2. Ingreso")
        opcion_2_pri = (input("\n Ingrese algunas de las opciones: "))
        #Verificamos que el usuario haya ingresado algunas de las opciones validas.
        while not opcion_2_pri.isdigit() or(opcion_2_pri != "1" and opcion_2_pri != "2"):
            print("\n Por favor ingrese una valor valido 1 0 2:")
            opcion_2_pri = input("\n Ingrese algunas de las opciones: ")
        
        opcion_2 = int(opcion_2_pri)
        
        if opcion_2 == 1:
            #Pedimos al usuario que ingrese una herramienta para vender
            Herramienta_Vendida = input("\n Ingrese la herramienta que vendera: ")
            #Verificamos que dicha herramienta este registrada en las listas
            while  Herramienta_Vendida not in listaHerramientas:
                print("\n Por favor ingrese una herramienta que se encuentre en el listado: ")
                print(listaHerramientas)
                Herramienta_Vendida = input("\n Ingrese la herramienta que vendera: ")
            indice_2 = listaHerramientas.index(Herramienta_Vendida)
            #Verificamos que tenga stock superior a 0
            if listaCantidadHerramientas[indice_2] > 0:
                listaCantidadHerramientas[indice_2] -= 1
            else:
                print(f"No se puede realizar la venta, {Herramienta_Vendida} tiene stock agotado.")    
        else:
            #Pedimos al usuario que ingrese la herramienta que quiere ingresar al stock
            Herramienta_ingreso = input("\n Ingrese el nombre de la herramienta para reponer stock: ")

            #Verificamos que la herramienta se encuentre en la lista
            while Herramienta_ingreso not in listaHerramientas:
                print(f"{Herramienta_ingreso} no se encuentra")
                print(f"Herramientas disponibles: {listaHerramientas}")
                Herramienta_ingreso = input("\n Ingrese el nombre de la herramienta para reponer stock: ")         
                
            indice_3 = listaHerramientas.index(Herramienta_ingreso)
            
            #Pedimos al usuario que ingrese una cantidad 
            cant_pri = input("\n Ingrese la cantidad que desea sumar el stock: ")

            #Verificamos que lo que ingrese el usuario sea un numero
            while not cant_pri.isdigit():
                print("\n Ingrese un valor numero entero. ")
                cant_pri = input("\n Ingrese la cantidad que desea sumar el stock: ")
            
            unidades_nue = int(cant_pri)
            #Sumamos las nuevas cantidades

            listaCantidadHerramientas[indice_3] += unidades_nue



    elif opcion == 8:
        print("\n Salio del sistema. ")
        break






#l programa debe presentar un menú interactivo persistente con las siguientes opciones:



#Inicializamos las listas y variables que necesitamos
listaHerramientas = []
listaCantidadHerramientas = []
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
            print("Primero ingrese herramientas para este paso")
            continue
        # Inicializamos dos valores, con los cuales verificaremos que se cargue solo las nuevas cantidades
        # de las herramientas que no tengamos ya cargadas en las listas.
        inicio = len(listaCantidadHerramientas)
        fin = len(listaHerramientas)

        if inicio == fin:
            print("Todas las herramientas ya tienen stock cargado.")
        else: 
        #Recorremos toda la lista cargada e ingresamos en otra lista la cantidad de herramientas que posee
            for i in range(inicio, fin):
                totalHerramientasPri = input(f"Ingrese la cantidad de {listaHerramientas[i]} que tiene: ")
                #Verificamos que el usuario ingrese un numero
                while not totalHerramientasPri.isdigit():
                    print("ingrese un numero porfavor: ")
                    totalHerramientasPri = input(f"Ingrese la cantidad de {listaHerramientas[i]} que tiene: ")
                totalHerramientas =int(totalHerramientasPri)
                listaCantidadHerramientas.append(totalHerramientas)
                

    #3. Visualización de Inventario: Mostrar el listado completo de herramientas junto a su stock actual.
    elif opcion == 3:
        #Verificamos que los inventarios esten cargados
        if len(listaHerramientas) == 0 or len(listaCantidadHerramientas) == 0:
            print("Primero debe cargar herramientas y sus cantidades para poder visualizarlas")
            continue
        #Mostramos en pantalla ambas listas
        for i in range(len(listaHerramientas)):
            print(f"Usted tiene: -- {listaCantidadHerramientas[i]} {listaHerramientas[i]} -- ")

    elif opcion == 8:
        break






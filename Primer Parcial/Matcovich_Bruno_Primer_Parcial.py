#l programa debe presentar un menú interactivo persistente con las siguientes opciones:
#1. Carga Inicial de Herramientas: Registrar los nombres de las herramientas que se
#pondrán a la venta. Se debe preguntar al usuario la cantidad de herramientas a cargar
#y se debe usar una estructura pertinente. En caso de nombre vacío o duplicado se
#debe seguir pidiendo hasta que sea correcto respetando la cantidad de herramientas
#que el usuario indicó antes de la carga.


#Inicializamos una lista vacia para guardar las herramientas

listaHerramientas = []
PriOpcion = ""

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

if opcion == 1:
    print("\n Ingrese la cantidad de herramientas para subir: ")
    cantHerramientasPri = input (" ")
    #Verificamos que el usuario ingrese un numero
    while not cantHerramientasPri.isdigit() or int(cantHerramientasPri) == 0:
        print("\n No ah ingresado un numero o el numero es menor a 0, intente nuevamente: ")
        cantHerramientasPri = input (" ")
    #Convertimos a integer la variable cantHerramientasPri    
    cantHerramientas =int(cantHerramientasPri)
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
            listaHerramientas.append(nombreHerramienta)
            cargados += 1

#ignorar este print
print(listaHerramientas)



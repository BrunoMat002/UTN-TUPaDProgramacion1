#l programa debe presentar un menú interactivo persistente con las siguientes opciones:
#1. Carga Inicial de Herramientas: Registrar los nombres de las herramientas que se
#pondrán a la venta. Se debe preguntar al usuario la cantidad de herramientas a cargar
#y se debe usar una estructura pertinente. En caso de nombre vacío o duplicado se
#debe seguir pidiendo hasta que sea correcto respetando la cantidad de herramientas
#que el usuario indicó antes de la carga.



#Creamos lo que sera el menu interactivo

print("\n--Menu--")

print("\n 1. Cargar Herramienta ")

PriOpcion = input("\n Eliga una de las siguientes opciones: ")

#Verificamos si el usuario ingreso correctamente un numero
while not PriOpcion.isdigit():
    print("\nNo ah ingresado un numero, intente nuevamente.")
    PriOpcion = input("\n Eliga una de las siguientes opciones: ")


#Convertimos a integer la variable priOpcion
opcion =int(PriOpcion)

if opcion == 1:
    print("\nIngrese la cantidad de herramientas para subir: ")
    cantHerramientasPri = input (" ")
    #Verificamos que el usuario ingrese un numero
    while not cantHerramientasPri.isdigit():
        print("\nNo ah ingresado un numero intente nuevamente: ")
        cantHerramientasPri = input (" ")
    #Convertimos a integer la variable cantHerramientasPri    
    cantHerramientas =int(cantHerramientasPri)
    for i in range(cantHerramientas):
        nombreHerramienta =input("\nIngrese el nombre de la herramienta: ")
        #Verificamos que haya ingresado un string
        while not nombreHerramienta.isalpha():
            print("\nNo ah ingresado un nombre valido, porfavor intente nuevamente: ")
            nombreHerramienta =input("\nIngrese el nombre de la herramienta: ")
        
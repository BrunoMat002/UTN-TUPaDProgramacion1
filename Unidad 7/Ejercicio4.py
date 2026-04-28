#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe. 

#Inicializamos un diccionario vacio

contactos = {}

#Realizamos un for para que el usuario cargue los contactos

for i in range(5):
    #Guardamos los valores en dos variables
    nombre=input("Ingrese el nombre del contacto: ")
    numero = int(input(f"Ingrese el numero para {nombre}: "))

    #Colocamos los valores en el diccionario
    contactos[nombre] = numero

#Le decimos al usuario que ingrese el nombre que quiera buscar
busqueda=input("Ingrese un nombre que quiera mostras: ")
#Verificamos si el nombre se encuentra en el diccionario
if busqueda in contactos:
    #Mostramos el numero
    print(f"Su teléfono es: {contactos[busqueda]}")
#Si no se encuentra informamos
else:
    print(f"El contacto '{busqueda}' no se encuentra en la lista.")


#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#● Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#● Mostrar la lista final actualizada.


#Creamos una lista con los nombres de los estudiantes

listaNombres = ["Fernando", "Luis", "Lucas", "Matias", "Bruno","Nicolas","Enzo", "Nacho"]

#Preguntamos al usuario si quiere agregar a otro estudiante o si quiere eliminar una que existe

print("\n ---MENU---")
print("\n 1. Agregar Alumno")
print("\n 2. Eliminar alumno existente")

iniOpcion = input("\n Ingrese una opcion(1 o 2): ")

opcion = int(iniOpcion)

#Verificamos que la opcion se ingrese correctamente

while opcion != 1 and opcion != 2:
    print("Error: Opción incorrecta.")
    iniOpcion = input("Ingrese nuevamente alguna opción correcta (1 o 2): ")
    opcion = int(iniOpcion)

if opcion == 1:
    nombre= input("Ingrese el nuevo nombre del alumno: ")
    listaNombres.append(nombre)
elif opcion == 2:
    #Le mostramos al usuario los nombres de los alumnos
    print(listaNombres)
    print("\n")
    borrar = input("ingrese el nombre del alumno que quiere eliminar: ") 
    listaNombres.remove(borrar)


#Informamos la lista final

print(listaNombres)
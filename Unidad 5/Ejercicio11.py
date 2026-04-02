#11) Crear una lista con los nombres de 10 estudiantes.
#● Solicitar al usuario que ingrese un nombre a buscar.
#● Indicar si el nombre se encuentra en la lista.
#● Mostrar la posición en la que aparece.
#● Si no se encuentra, informar que no está en la lista.

# Lista de estudiantes
estudiantes = [
    "Ana", "Bruno", "Carla", "Diego", "Sol", 
    "Facundo", "Micaela", "Tomas", "Martin", "Juan"
]

# Pedir nombre al usuario
nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")

# Convertimos a minúsculas para comparar sin errores
estudiantes_lower = [e.lower() for e in estudiantes]

# Buscar
if nombre_buscar.lower() in estudiantes_lower:
    posicion = estudiantes_lower.index(nombre_buscar.lower())
    
    print(f"El estudiante '{estudiantes[posicion]}' se encuentra en la lista.")
    print(f"Aparece en la posición (orden): {posicion + 1}")
else:
    print(f"El estudiante '{nombre_buscar}' no está en la lista.")
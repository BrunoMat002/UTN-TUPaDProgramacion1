#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#● Inicializarlo con guiones "-" representando casillas vacías.
#● Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#● Mostrar el tablero después de cada jugada.


# Crear tablero 3x3
matriz = [["-"] * 3 for i in range(3)]

turno = "X"

for jugada in range(9):

    # Mostrar tablero
    print("\nTablero:")
    for fila in matriz:
        print(fila)

    print(f"\nTurno del jugador {turno}")

    fila = int(input("Ingrese fila (0-2): "))
    columna = int(input("Ingrese columna (0-2): "))

    # Validar que esté libre
    if matriz[fila][columna] == "-":
        matriz[fila][columna] = turno

        # Cambiar turno
        if turno == "X":
            turno = "O"
        else:
            turno = "X"
    else:
        print(" Esa posición ya está ocupada. Intentá de nuevo.")
        continue

# Mostrar tablero final
print("\nTablero final:")
for fila in matriz:
    print(fila)

print("\nSe completó el juego")
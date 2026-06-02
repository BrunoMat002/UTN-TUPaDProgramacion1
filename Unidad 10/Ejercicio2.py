#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.

#Creo la función recursiva para calcular Fibonacci en la posición 'n'
def fibonacci(n):
    # Casos que n sea 0 o 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    #Sino suma de las dos posiciones anteriores
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#Verificamos que el usuario ingrese un numero
while True:
    try:
        posicion_maxima = int(input("Introduce la posición máxima de Fibonacci (entero >= 0): "))
        if posicion_maxima < 0:
            print("La posición no puede ser negativa. Inténtalo de nuevo.")
            continue
        break
    except ValueError:
        print("¡Error! Debes ingresar un número entero. Inténtalo de nuevo.")

#imprimimos los resultados
print(f"\nSerie de Fibonacci hasta la posición {posicion_maxima}:")
for i in range(0, posicion_maxima + 1):
    print(f"Posición {i}: {fibonacci(i)}")
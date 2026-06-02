#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario


# Realizo la función recursiva para calcular el factorial
def factorial(n):
    #si el numero es 0 o 1
    if n == 0 or n == 1:
        return 1
    #En caso contrario 
    else:
        return n * factorial(n - 1)

#Le pedimos el numero al usuario y lo convertimos a entero
limite = int(input("Introduce un número entero: "))

print(f"\nCalculando los factoriales desde 1 hasta {limite}:")
print("-" * 40)

# Utiliza la función para mostrar el factorial de todos los números enteros entre 1 y la variable limite
for i in range(1, limite + 1):
    resultado = factorial(i)
    print(f"El factorial de {i} es -> {resultado}") 
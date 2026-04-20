#7.Crear una función llamada operaciones_basicas(a, b) que reciba dos
#números como parámetros y devuelva una tupla con el resulta- do de
#sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re- sultados de
#forma clara.


# Definimos la función para que calcule y retorne los valores
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    # Retornamos los 4 resultados separados por comas para crear la tupla
    return suma, resta, multiplicacion, division

# Le pedimos al usuario que ingrese los numeros
num1 = int(input("Ingrese el número más grande: ")) 
num2 = int(input("Ingrese el número más chico: "))

# Llamamos a la función
resultados = operaciones_basicas(num1, num2)

# Imprimimos los resultados
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")
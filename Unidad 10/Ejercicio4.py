#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.

# Realizo la funcion recursiva para convertir decimal a binario
def decimal_a_binario(n):
    #si el número es 0 o 1, su binario es el mismo número
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    #llamamos a la función con la división entera  y sumamos el residuo al final de la cadena
    else:
        return decimal_a_binario(n // 2) + str(n % 2)



print("--- CONVERSOR RECURSIVO A BINARIO ---")

while True:
    try:
        numero_decimal = int(input("Introduce un número entero positivo: "))
        if numero_decimal < 0:
            print("Por favor, introduce un número que sea mayor o igual a 0.")
            continue
        break
    except ValueError:
        print("¡Error! Debes ingresar un número entero válido.")

#Calculamos el resultado 
resultado_binario = decimal_a_binario(numero_decimal)

print("-" * 45)
print(f"El número {numero_decimal} en binario es -> {resultado_binario}")
print("-" * 45)
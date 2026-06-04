#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
#No se puede convertir el número a string.
#Usá operaciones matemáticas (%, //) y recursión.
#Ejemplos:
#suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
#suma_digitos(9) → 9
#suma_digitos(305) → 8 (3 + 0 + 5)

#Realizo la Funcion recursiva para sumar los digitos de un numero entero
def suma_digitos(n):
    # Si el numero es de un solo digito, devolvemos el mismo numero
    if n < 10:
        return n
    # Tomamos el ultimo dígito + la suma de los digitos restantes
    else:
        ultimo_digito = n % 10
        resto_del_numero = n // 10
        return ultimo_digito + suma_digitos(resto_del_numero)


print("--- SUMADORA RECURSIVA DE DIGITOS ---")

while True:
    try:
        #Le pedimos al usuario que ingrese un numero
        numero = int(input("Introduce un numero entero positivo: "))
        if numero < 0:
            print("Por favor, introduce un numero mayor o igual a 0.")
            continue
        break
    except ValueError:
        print("¡Error! Debes ingresar un numero entero valido.")

# Calculamos la suma
resultado = suma_digitos(numero)

print("-" * 45)
print(f"La suma de los digitos de {numero} es -> {resultado}")
print("-" * 45)
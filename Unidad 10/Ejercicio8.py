#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número.
# Ejemplos:
#contar_digito(12233421, 2) → 3
#contar_digito(5555, 5) → 4 
#contar_digito(123456, 7) → 0



# Realizo la funcion recursiva para contar cuantas veces aparece un dígito en un numero
def contar_digito(numero, digito):
    # si el numero es de un solo digito, evaluamos directamente
    if numero < 10:
        return 1 if numero == digito else 0

    # Extraemos el ultimo digito y el resto del numero
    ultimo_digito = numero % 10
    resto_del_numero = numero // 10

    # Si el ultimo digito coincide, sumamos 1 al conteo de las llamadas restantes
    if ultimo_digito == digito:
        return 1 + contar_digito(resto_del_numero, digito)
    # Si no coincide, sumamos 0 (seguimos arrastrando el conteo anterior)
    else:
        return 0 + contar_digito(resto_del_numero, digito)


print("--- CONTADOR RECURSIVO DE UN DIGITO ---")

#Validacion del nuSmero principal
while True:
    try:
        #Le pedimos el usuario que ingrese un numero
        num_usuario = int(input("Introduce un numero entero positivo: "))
        if num_usuario < 0:
            print("Por favor, introduce un numero mayor o igual a 0.")
            continue
        break
    except ValueError:
        print("¡Error! Debes ingresar un numero entero valido.")

#Validacion del digito a buscar
while True:
    try:
        digito_buscar = int(input("Introduce el digito que deseas contar (0-9): "))
        if digito_buscar < 0 or digito_buscar > 9:
            print("El digito debe estar estrictamente entre 0 y 9.")
            continue
        break
    except ValueError:
        print("¡Error! Debes ingresar un solo numero entero.")

# Calculamos el resultado
coincidencias = contar_digito(num_usuario, digito_buscar)

print("-" * 55)
print(f"El digito {digito_buscar} aparece {coincidencias} veces dentro de {num_usuario}")
print("-" * 55)
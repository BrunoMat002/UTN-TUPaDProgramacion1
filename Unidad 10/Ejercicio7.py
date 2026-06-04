#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
#último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la
#pirámide.
# Ejemplos:
#contar_bloques(1) → 1 (1)
#contar_bloques(2) → 3 (2 + 1)
#contar_bloques(4) → 10 (4 + 3 + 2 + 1)


#Realizo la funcion recursiva para contar los bloques de la piramide
def contar_bloques(n):
    # Si la base es de 1 bloque, la piramide solo tiene ese bloque
    if n == 1:
        return 1
    # Bloques del nivel actual + los bloques de los niveles superiores
    else:
        return n + contar_bloques(n - 1)


print("--- CONTADOR RECURSIVO DE BLOQUES (PIRAMIDE) ---")

while True:
    try:
        #Le pedimos al usuario que introduzca el numero de bloques
        nivel_base = int(input("Introduce el numero de bloques en el nivel mas bajo (entero > 0): "))
        if nivel_base <= 0:
            print("La piramide debe tener al menos 1 bloque en su base. Intentalo de nuevo.")
            continue
        break
    except ValueError:
        print("¡Error! Debes ingresar un numero entero valido.")

# Calculamos el total de bloques
total_bloques = contar_bloques(nivel_base)

print("-" * 55)
print(f"Para una base de {nivel_base} bloques, la piramide completa usara -> {total_bloques} bloques")
print("-" * 55)
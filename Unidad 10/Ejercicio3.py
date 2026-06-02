#3) Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1)
#. Prueba esta función en un algoritmo general.

#Realizo la funcion recursiva para calcular la potencia (base^exponente)
def calcular_potencia(base, exponente):
    #cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    else:
        return base * calcular_potencia(base, exponente - 1)

# Verifico que el usuario ingrese un numero flotante o entero
while True:
    try:
        base = float(input("Introduce la base (número real): "))
        break
    except ValueError:
        print("¡Error! Por favor, introduce un número válido para la base.")

# Veirificamos que el exponente sea positivo
while True:
    try:
        exponente = int(input("Introduce el exponente (entero mayor o igual a 0): "))
        if exponente < 0:
            print("Para esta función recursiva, el exponente debe ser mayor o igual a 0.")
            continue
        break
    except ValueError:
        print("¡Error! El exponente debe ser un número entero.")

#Calculo e imprimo
resultado = calcular_potencia(base, exponente)

print("-" * 40)
print(f"Resultado: {base} elevado a la {exponente} es igual a -> {resultado}")
print("-" * 40)
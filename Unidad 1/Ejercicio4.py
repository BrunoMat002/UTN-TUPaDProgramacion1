# EJERCICIO 4
# Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

#Pedimos al usuario que ingrese el radio de un circulo

radio = float(input("Ingrese el radio de un circulo: "))

#Calculamos su area y perimetro

area = radio ** 2 * 3.14

perimetro = 2 * 3.14 * radio

#Imprimimos los resultados

print(f"El area del circulo es: {area}")

print(f"El perimetro del circulo es: {perimetro}")
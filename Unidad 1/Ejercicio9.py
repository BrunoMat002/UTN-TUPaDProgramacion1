#EJERCICIO 9

# Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

#Le pedimos al usuario que ingrese la temperatura en grados celcius

grados = float(input("Ingrese una temperatura en grados Celcius: "))

#Calculamos su equivalente en grados fahrenheit

TemperaturaF = 9/5 * grados + 32

#Imprimimos el valor final

print(f"El equivalente de {grados} grados Celcius es {TemperaturaF} grados fahrenheit")
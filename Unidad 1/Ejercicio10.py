#EJERCICIO 10

# Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

#Inicializamos dos variables para contar el total y luego el promedio
total = 0
promedio = 0

#Le pedimos al usuario que ingrese los 3 numeros
num1 =int(input("Ingrese un numero: "))
num2 =int(input("Ingrese otro numero: "))
num3 =int(input("Ingrese otro numero: "))

#Calculamos lo que pide el ejercicio

total = num1 + num2 + num3

promedio = total / 3

#Imprimimos el promedio final

print(f"El promedio es: {promedio}")
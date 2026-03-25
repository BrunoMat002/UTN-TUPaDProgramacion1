#EJERCICIO 7

# Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

#Le pedimos a un usuario que ingrese dos numeros distintos a 0

num1 = int(input("Ingrese un numero distinto de 0: "))

num2 = int(input("ingrese un segundo numero distinto a 0: "))

#Calculamos las diferentes operaciones

suma = num1 + num2
multiplicacion = num1 * num2


if num1 > num2:
    division = num1 / num2
    resta = num1 - num2
else:
    division = num2 / num1 
    resta = num2 - num1

#Imprimimos los resultados

print(f"La suma de ambos numeros es: {suma}")
print(f"La resta de ambos numeros es: {resta}")
print(f"La multiplicacion de ambos numeros es: {multiplicacion}")
print(f"La division de ambos numeros es: {division}")


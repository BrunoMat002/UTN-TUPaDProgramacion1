#3) Utilizando el código del ejercicio 1, mantener el código con los errores originales e incluir
#bloquestry-except para que la ejecución del programa no se frene al encontrar los errores.

a = 10

b = input("Introduce un número: ")

try:
    #Convierto el string en entero
    bFinal = int(b)
    result = a / bFinal 
    print(f"Resultado: {result}")
    #Verifico que ingrese un numero
except ValueError:
    print("Debera ingresar un numero valido. ")
    

numbers = [1, 2, 3]
try:
    print(numbers[5])  
except IndexError:
    #Informo que el valor esta fuera de rango
    print("El rango no es el correcto. ")
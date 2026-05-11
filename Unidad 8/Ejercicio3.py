#3) Utilizando el código del ejercicio 1, mantener el código con los errores originales e incluir
#bloquestry-except para que la ejecución del programa no se frene al encontrar los errores.

a = 10

b = input("Introduce un número: ")

try:
    bFinal = int(b)
    result = a / bFinal 
    print(f"Resultado: {result}")
except ZeroDivisionError:
    print("Ingrese otro numero que no sea 0. ")
except ValueError:
    print("Debera ingresar un numero valido. ")
    

numbers = [1, 2, 3]
try:
    print(numbers[5]) #Error: IndexError. numbers[5] no existe ya que la lista llega hasta el indice 2 que seria el valor 3. 
except IndexError:
    print("El rango no es el correcto. ")
#EJERCICIO 8

#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:

#Le pedimos al usuario que ingrese su altura y su peso

altura = float(input("Ingresa tu altura: "))
peso = float(input("Ingresa tu peso: "))

#Calculamos el valor del IMC

IMC = peso / altura ** 2

#Informamos el resultado

print(f"Tu indice de masa corporal es: {IMC} ")


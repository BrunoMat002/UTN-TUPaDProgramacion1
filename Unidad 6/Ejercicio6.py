#6. Crear una función llamada tabla_multiplicar(numero) que reciba un número
#como parámetro y imprima la tabla de multiplicar de ese número del 1 al
#10. Pedir al usuario el número y llamar a la función.

#Creamos la funcion

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(numero * i)

#Le pedimos al usuario que ingrese el numero

numero = int(input("Ingrese el numero que quiere saber su tabla: "))

#Llamamos a la funcion

tabla_multiplicar(numero)
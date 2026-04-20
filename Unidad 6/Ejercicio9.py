#9.Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una
#temperatura en grados Celsius y devuelva su equivalente en Fahrenheit.
#Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la
#función.


#Definimos la funcion

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#Le pedimos al usuario que ingrese la temperatura

grados = float(input("Ingrese la temperatura en grados Celsius: "))

#Llamamos a la funcion e imprimimos

print(f"La temperatura en Fahrenheit es: {celsius_a_fahrenheit(grados):.2f}")
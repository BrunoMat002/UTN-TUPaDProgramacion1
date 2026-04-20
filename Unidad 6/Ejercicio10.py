#10. Crear una función llamada calcular_promedio(a, b, c) que reciba tres
#números como parámetros y devuelva el promedio de ellos. Solicitar los
#números al usuario y mostrar el resultado usando esta función.

#Definimos la funcion

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

#Le pedimos al usuario que ingrese los numeros

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

#Llamamos a la funcion e imprimimos

print(f"El promedio de los tres números es: {calcular_promedio(num1, num2, num3):.2f}")
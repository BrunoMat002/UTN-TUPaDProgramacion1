#8.Crear una función llamada calcular_imc(peso, altura) que reciba el peso en
#kilogramos y la altura en metros, y devuelva el índice de masa corporal
#(IMC). Solicitar al usuario los datos y llamar a la fun- ción para mostrar el
#resultado con dos decimales.

#Definimos la funcion

def calcular_imc(p, a):
    return(p/(a**2))

#Le pedimos al usuario ingrese los valores

peso = float(input("Ingrese el peso en KG(KiloGramos): "))

altura = float(input("Ingrese la altura en M(metros):"))

#Llamamos a la funcion e imprimimos 

print(f"Su indice de masa corporal es: {calcular_imc(peso,altura): .2f}")
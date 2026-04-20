#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra- dio
#como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuel- va el
#perímetro del círculo. Solicitar el radio al usuario y llamar am- bas
#funciones para mostrar los resultados.

#Creamos las dos funciones

def calcular_area_circulo(radio):
    return (3.14 * (radio**2))

def calcular_perimetro_circulo(radio):
    return(2*3.14*radio)

#Le pedimos al usuario que ingrese el radio del circulo

radio = float(input("Ingrese el radio del circulo: "))

#Llamamos a las funciones e imprimimos los resultados

print (calcular_area_circulo(radio))

print (calcular_perimetro_circulo(radio))
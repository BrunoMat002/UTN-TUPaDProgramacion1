#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 


# Pedimos al usuario ingresar su nombre

nombre = input("Ingrese su nombre")

valores = [1,2,3]

opcion = int(input("Ingrese un numero(1, 2 o 3)"))

if opcion in valores:
    if opcion == 1:
        nombre = nombre.upper()
        print(nombre)
    elif opcion == 2:
        nombre = nombre.lower()
        print(nombre)
    else:
        nombre = nombre.title()
        print(nombre)
else:
    print("Ingresaste otro numero")
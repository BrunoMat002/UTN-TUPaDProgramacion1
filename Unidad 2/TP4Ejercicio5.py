#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

#Pedimos  que el usuario ingrese una contraseña

contraseña = input("Ingrese un contraseñaa entre 8 y 14 caracteres")

#Verificamos la cantidad de dijitos que tiene la variable uusando len()

cant = len(contraseña)

if cant >= 8 and cant <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese unaa contraseña entre 8 y 14 caracteres")
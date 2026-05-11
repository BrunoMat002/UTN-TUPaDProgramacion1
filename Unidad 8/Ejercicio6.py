#6) Escribir un programa que pida al usuario un número, y:
#● Si el valor ingresado es válido, lo imprima por pantalla.
#● Si el valor ingresado no es numérico, imprima por pantalla “Debe ingresar un número
#válido”.
#● Si contiene algún otro tipo de error, imprima por pantalla “Se produjo un error
#inesperado” junto con el error que surgió.


try:
    #Le pedimos al usuario que ingrese un numero
    numero = int(input("Ingrese un numero: "))
#Verificamos los casos posibles
except ValueError:
    print("Debe ingresar un número válido. ")
#Verificamos si hay otro tipo de error
except Exception as e:
    print(f"Se produjo un error inesperado: {type(e).__name__}")
else:
    #Si todo esta bien imprimo
    print(numero)
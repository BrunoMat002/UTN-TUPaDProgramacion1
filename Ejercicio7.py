#7) Repetir el ejercicio 6, pero añadiendo la posibilidad de que el usuario intente ingresar un
#nuevo número luego de encontrar un error.

#Utilizo un while True para que no 

while True:

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
        #Cortamos el while ya que es correcto
        break

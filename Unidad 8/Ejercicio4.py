#4) Repetir el ejercicio 3, pero usando excepciones múltiples que hagan alusión a lostipos de
#errores detectados.


a = 10


b = input("Introduce un número: ")

try:
    # Convierto el string a entero
    bFinal = int(b)
    
    # Realizo la división
    result = a / bFinal
    
    print(f"Resultado: {result}")

# Si el usuario ingresa 0
except ZeroDivisionError:
    print("Ingrese otro número distinto de 0.")

# Si el usuario no ingresa un número válido
except ValueError:
    print("Deberá ingresar un número válido.")

# Capturo cualquier otro error inesperado
except Exception as e:
    print(f"Ocurrió un error inesperado: {type(e).__name__}")


numbers = [1, 2, 3]

try:
    print(numbers[5])

# Si el índice no existe
except IndexError:
    print("Error: índice fuera de rango.")

# Capturo cualquier otro error inesperado
except Exception as e:
    print(f"Ocurrió un error inesperado: {type(e).__name__}")
#5) Repetir el ejercicio 4, pero esta vezincluyendo bloques else y finally.

a = 10

b = input("Introduce un número: ")

try:
    # Convierto el string a entero
    bFinal = int(b)
    
    # Realizo la división
    result = a / bFinal

# Si el usuario ingresa 0
except ZeroDivisionError:
    print("Ingrese otro número distinto de 0.")

# Si el usuario no ingresa un número válido
except ValueError:
    print("Deberá ingresar un número válido.")

# Capturo cualquier otro error inesperado
except Exception as e:
    print(f"Ocurrió un error inesperado: {type(e).__name__}")

# Se ejecuta solo si no hubo errores
else:
    print(f"Resultado: {result}")

# Se ejecuta siempre
finally:
    print("Fin de la operación.")


numbers = [1, 2, 3]

try:
    print(numbers[5])

# Si el índice no existe
except IndexError:
    print("Error: índice fuera de rango.")

# Capturo cualquier otro error inesperado
except Exception as e:
    print(f"Ocurrió un error inesperado: {type(e).__name__}")

# Se ejecuta solo si no hubo errores
else:
    print("Acceso a la lista realizado correctamente.")

# Se ejecuta siempre
finally:
    print("Fin del acceso a la lista.")
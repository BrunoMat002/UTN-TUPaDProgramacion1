#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
#lo es.
# Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed().

#Realizo la funcion recursiva para verificar si es palindromo
def es_palindromo(palabra):
    # Si tiene 0 o 1 letras, ya se comprobó todo con exito
    if len(palabra) <= 1:
        return True

    # Comparamos la primera letra [0] con la ultima [-1]
    if palabra[0] == palabra[-1]:
        # Si coinciden, recortamos los extremos y volvemos a evaluar
        # palabra[1:-1] toma el texto desde el segundo carácter hasta el penultimo
        return es_palindromo(palabra[1:-1])
    else:
        # Si en algun momento no coinciden, no es palindromo
        return False


# --- Algoritmo General con Validacion ---

print("--- DETECTOR RECURSIVO DE PALINDROMOS ---")

while True:
    # Pedimos la palabra y usamos .lower() para evitar problemas con mayusculas
    entrada = input("Introduce una palabra (sin espacios ni tildes): ").strip().lower()

    # verificamos que no este vacia y que solo contenga letras (sin numeros)
    if not entrada.isalpha():
        print("¡Error! Por favor, ingresa una unica palabra valida que contenga solo letras.")
        continue
    break

# Evaluamos la palabra con nuestra funcion
if es_palindromo(entrada):
    print(f"\n¡Confirmado! {entrada} ,si es un palindromo. ")
else:
    print(f"\nLa palabra {entrada}, no es un palindromo. ")
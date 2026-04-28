#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra. 

#Le pedimos al usuario una frase

frase = input("Ingrese una frase: ")

#Convertimos la frase en una lista de palabras (usando .split() que separa por espacios)
palabras_lista = frase.split()

#Obtenemos las palabras únicas usando un set

palabras_unicas = set(palabras_lista)

print(f"Palabras únicas: {palabras_unicas}")

#Creamos un diccionario para el recuento
recuento = {}

#Recorremos el set para contar cuántas veces aparece cada palabra en la lista original
for i in palabras_unicas:
    # Usamos .count() para saber la frecuencia y lo asignamos al diccionario
    recuento[i] = palabras_lista.count(i)

#imprimimos el resultado final
print(f"Recuento de palabras: {recuento}")
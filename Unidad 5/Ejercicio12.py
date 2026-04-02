#12) Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista.
#● Mostrar la lista original.
#● Mostrar la lista ordenada de menor a mayor.
#● Mostrar la lista ordenada de mayor a menor.
#● Investigar el uso de sorted() y del parámetro reverse.


# Inicializamos una lista vacía
numeros = []


#Ingreso de datos
print("--- Ingreso de 8 números enteros ---")
for i in range(8):
    valor = int(input(f"Ingrese el número para la posición {i+1}: "))
    numeros.append(valor)

# Mostrar lista original
print(f"\nLista original: {numeros}")

# Orden ascendente
lista_ascendente = sorted(numeros)
print(f"Lista ordenada (menor a mayor): {lista_ascendente}")

# Orden descendente
lista_descendente = sorted(numeros, reverse=True)
print(f"Lista ordenada (mayor a menor): {lista_descendente}")
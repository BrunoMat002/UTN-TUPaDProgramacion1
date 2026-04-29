#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores. 


#Definimos el diccionario 
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Brasil": "Brasilia"
}

#Inicializamos un diccionario vacio para el resultado
capitales_paises = {}

#Recorremos el original obteniendo clave (pais) y valor (capital)
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

#Imprimimos los resultados
print("Diccionario Original (Pais: Capital):")
print(paises_capitales)

print("\nDiccionario Invertido (Capital: Pais):")
print(capitales_paises)
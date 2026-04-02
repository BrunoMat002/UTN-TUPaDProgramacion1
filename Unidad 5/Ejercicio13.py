#13) Dada la siguiente lista de puntajes de un videojuego: puntajes = [450, 1200, 875, 990, 300, 1500, 640] 
#● Mostrar el puntaje más alto y el más bajo. 
#● Mostrar la lista ordenada de mayor a menor (ranking). 
#● Indicar en qué posición del ranking se encuentra el puntaje 990.

#Lista de puntajes
puntajes = [450, 1200, 875, 990, 300, 1500, 640]

#Ordenar de mayor a menor (ranking)
puntajes.sort(reverse=True)

#Puntaje más alto y más bajo
puntaje_alto = puntajes[0]
puntaje_bajo = puntajes[-1]

#Posición del puntaje 990
posicion_990 = puntajes.index(990) + 1

#Resultados
print(f"Puntaje más alto: {puntaje_alto}")
print(f"Puntaje más bajo: {puntaje_bajo}")
print(f"Ranking ordenado (mayor a menor): {puntajes}")
print(f"El puntaje 990 se encuentra en la posición {posicion_990} del ranking.")
#EJERCICIO 5

#Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale

#Le pedimos al usuario que ingrese una cantidad de segundos

seg = int(input("Ingrese una cantidad de segundos: "))

#Realizamos la cuanto para verificar cuantas horas equivale

horas = seg / 3600

#Imprimimos el resultado

print(f"{seg} segundos equivale a {horas} horas.")
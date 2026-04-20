#5.Crear una función llamada segundos_a_horas(segundos) que reciba una
#cantidad de segundos como parámetro y devuelva la cantidad de horas
#correspondientes. Solicitar al usuario los segundos y mos- trar el resultado
#usando esta función.

#Creamos la funcion 

def segundos_a_horas(segundos):
    return(segundos / 3600)

#Le pedimos al usuario que ingrese los segundos

segundos = int(input("Ingrese los segundos: "))

#llamamos e imprimimos el resultados

print(f"{segundos} segundos son {segundos_a_horas(segundos)} horas.")
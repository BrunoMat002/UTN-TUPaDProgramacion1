#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego,
#mostrá el promedio de cada alumno. 

#Inicializamos un diccionario 
alumnos = {}

#Usamos un bucle for para realizar la carga de 3 alumnos
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    
    #Le pedimos al usuario que ingrese las 3 notas 
    n1 = float(input(f"Ingrese nota 1 para {nombre}: "))
    n2 = float(input(f"Ingrese nota 2 para {nombre}: "))
    n3 = float(input(f"Ingrese nota 3 para {nombre}: "))
    
    #Guardamos las notas en una tupla
    notas_tupla = (n1, n2, n3)
    
    #Guardamos en el diccionario:
    alumnos[nombre] = notas_tupla

print("Resultados de Promedios")

#Recorremos el diccionario con .items() para calcular los promedios
for nombre, notas in alumnos.items():
    #Obtenemos el promedio
    promedio = sum(notas) / 3
    #Imprimimos el resultado
    print(f"Alumno: {nombre} | Promedio: {promedio:.2f}")
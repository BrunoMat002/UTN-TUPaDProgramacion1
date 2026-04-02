# Definimos dimensiones
filas = 7
columnas = 2
matriz = [[0] * columnas for i in range(filas)] 

# Cargamos los datos
print("--- Ingreso de Temperaturas de la Semana ---")
for i in range(filas): 
    print(f"Día {i + 1}:")
    matriz[i][0] = float(input("  Ingrese temperatura mínima: ")) 
    matriz[i][1] = float(input("  Ingrese temperatura máxima: "))

# Inicializamos las variables
suma_minimas = 0
suma_maximas = 0
max_amplitud = 0
dia_mayor_amplitud = 0

for i in range(filas):
    suma_minimas += matriz[i][0]
    suma_maximas += matriz[i][1]
    
    amplitud_hoy = matriz[i][1] - matriz[i][0]
    
    if i == 0 or amplitud_hoy > max_amplitud:
        max_amplitud = amplitud_hoy
        dia_mayor_amplitud = i + 1

# Obtenemos los promedios
promedio_min = suma_minimas / filas
promedio_max = suma_maximas / filas

# Imprimimos los resultados
print("\n=== Resumen Semanal ===")
print("Matriz (Mín, Máx):")
for fila in matriz:
    print(fila)

print(f"\nPromedio de mínimas: {promedio_min:.2f}°C") 
print(f"Promedio de máximas: {promedio_max:.2f}°C")
print(f"El día {dia_mayor_amplitud} tuvo la mayor amplitud térmica con {max_amplitud:.2f}°C")
#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
#● Mostrar el promedio de cada estudiante.
#● Mostrar el promedio de cada materia.

# Matriz de notas
matrizNotas = [
    [5,8,10],
    [8,8,9],
    [3,7,2],
    [10,9,6],
    [8,9,10]
]

# Promedio por estudiante
print("--- Promedios por Estudiante ---")
for i in range(len(matrizNotas)):
    sumaEstudiante = 0
    for j in range(len(matrizNotas[i])):
        sumaEstudiante += matrizNotas[i][j]
    
    promedioEst = sumaEstudiante / len(matrizNotas[i])
    print(f"Estudiante {i+1}: Promedio = {promedioEst:.2f}")

# Promedio por materia
print("\n--- Promedios por Materia ---")
cantidadEstudiantes = len(matrizNotas)
cantidadMaterias = len(matrizNotas[0])

for j in range(cantidadMaterias):
    sumaMateria = 0
    for i in range(cantidadEstudiantes):
        sumaMateria += matrizNotas[i][j]
    
    promedioMat = sumaMateria / cantidadEstudiantes
    print(f"Materia {j+1}: Promedio = {promedioMat:.2f}")
#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora


#Inicializamos la agenda con algunos eventos de ejemplo
agenda = {
    ("lunes", "10:00"): "ir al trabajo",
    ("martes", "15:00"): "Clase de inglés",
    ("viernes", "18:00"): "Gimnasio"
}

print("--- Consulta de Agenda ---")

#Solicitamos al usuario los datos para la busqueda
dia_busqueda = input("Ingrese el dia a consultar (ej: lunes): ").lower()
hora_busqueda = input("Ingrese la hora a consultar (ej: 10:00): ")

#Creamos la tupla de busqueda para usarla como clave
consulta = (dia_busqueda, hora_busqueda)

#Verificamos si la combinacion dia/hora existe usando el operador 'in' 
if consulta in agenda:
    # Si existe, accedemos al valor (el evento) asociado a esa clave 
    evento = agenda[consulta]
    print(f"Actividad programada para el {dia_busqueda} a las {hora_busqueda}: {evento}")
else:
    # Si la clave no esta en el diccionario, informamos al usuario
    print(f"No hay actividades registradas para el {dia_busqueda} a las {hora_busqueda}.")
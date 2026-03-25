#Contexto
#Hay 2 días de atención: Lunes y Martes.
#Cada día tiene cupos fijos:
#• Lunes: 4 turnos
#• Martes: 3 turnos
#Reglas
#1. Pedir nombre del operador (solo letras).
#2. Menú repetitivo hasta salir:
#1. Reservar turno
#2. Cancelar turno (por nombre)
#3. Ver agenda del día
#4. Ver resumen general
#5. Cerrar sistema
#3. Reservar:
#o Elegir día (1=Lunes, 2=Martes).
#o Pedir nombre del paciente (solo letras).
#o Verificar que no esté repetido en ese día (comparando con las variables
##o Guardar en el primer espacio libre (ej. lunes1, lunes2…).
#2. Cancelar:
#o Elegir día.
#o Pedir nombre del paciente (solo letras).
#o Si existe, cancelar y dejar el espacio vacío ("").
#5. Ver agenda del día:
#4
#Programación 1
#TECNICATURA UNIVERSITARIA
#EN PROGRAMACIÓN
##está vacío.
#6. Resumen general:
#o Turnos ocupados y disponibles por día.
#o Día con más turnos (o empate).
#Restricciones
#• ❌ No listas, no diccionarios, no sets, no tuplas.
#• ✅ Se permite usar "" como “vacío”.
#• ✅ Validaciones con .isalpha() y .isdigit() (sin try/except).

# Definimos las variables globales para los turnos 
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

# Pedimos al operar que ingrese el nombre y verificamos que sean todas letras
operador = input("Ingrese el nombre del operador: ")
while not operador.isalpha():
    print("Error: El nombre solo puede contener letras y no puede estar vacío.")
    operador = input("Ingrese el nombre del operador: ")

# Hacemos el menu
opcion = ""
while opcion != "5":
    print(f"\n--- AGENDA DE TURNOS (Operador: {operador}) ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    
    opcion = input("Elija una opción (1-5): ")
    
    # Verificamos que ingrese un numero
    while not opcion.isdigit():
        print("Error: Ingrese un número válido.")
        opcion = input("Elija una opción (1-5): ")
    
    # Realizamos lo que pide cada punto
    if opcion == "1":
        dia = input("Seleccione día (1=Lunes, 2=Martes): ")
        while dia not in ["1", "2"]:
            print("Error: Opción de día inválida.")
            dia = input("Seleccione día (1=Lunes, 2=Martes): ")
        
        paciente = input("Nombre del paciente: ")
        while not paciente.isalpha():
            print("Error: Ingrese un nombre válido (solo letras).")
            paciente = input("Nombre del paciente: ")
            
        if dia == "1":
            # Verificamos si ya existe el nombre para evitar repetidos
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print(f"Error: {paciente} ya tiene un turno asignado el Lunes.")
            elif lunes1 == "": lunes1 = paciente; print("Turno reservado: Lunes - Turno 1")
            elif lunes2 == "": lunes2 = paciente; print("Turno reservado: Lunes - Turno 2")
            elif lunes3 == "": lunes3 = paciente; print("Turno reservado: Lunes - Turno 3")
            elif lunes4 == "": lunes4 = paciente; print("Turno reservado: Lunes - Turno 4")
            else: print("Lo sentimos, no hay más cupos para el Lunes.")
        else:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print(f"Error: {paciente} ya tiene un turno asignado el Martes.")
            elif martes1 == "": martes1 = paciente; print("Turno reservado: Martes - Turno 1")
            elif martes2 == "": martes2 = paciente; print("Turno reservado: Martes - Turno 2")
            elif martes3 == "": martes3 = paciente; print("Turno reservado: Martes - Turno 3")
            else: print("Lo sentimos, no hay más cupos para el Martes.")

    elif opcion == "2":
        dia = input("Día del turno a cancelar (1=Lunes, 2=Martes): ")
        paciente = input("Nombre del paciente a cancelar: ")
        
        encontrado = False
        if dia == "1":
            if lunes1 == paciente: lunes1 = ""; encontrado = True
            elif lunes2 == paciente: lunes2 = ""; encontrado = True
            elif lunes3 == paciente: lunes3 = ""; encontrado = True
            elif lunes4 == paciente: lunes4 = ""; encontrado = True
        elif dia == "2":
            if martes1 == paciente: martes1 = ""; encontrado = True
            elif martes2 == paciente: martes2 = ""; encontrado = True
            elif martes3 == paciente: martes3 = ""; encontrado = True
            
        if encontrado:
            print(f"El turno de {paciente} ha sido cancelado con éxito.")
        else:
            print("No se encontró ningún paciente con ese nombre en el día seleccionado.")

    elif opcion == "3":
        dia = input("Ver agenda de (1=Lunes, 2=Martes): ")
        if dia == "1":
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        else:
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    elif opcion == "4":
        # Contamos cuántos están ocupados
        ocupados_l = 0
        if lunes1 != "": ocupados_l += 1
        if lunes2 != "": ocupados_l += 1
        if lunes3 != "": ocupados_l += 1
        if lunes4 != "": ocupados_l += 1
        
        ocupados_m = 0
        if martes1 != "": ocupados_m += 1
        if martes2 != "": ocupados_m += 1
        if martes3 != "": ocupados_m += 1
        
        print(f"Lunes: {ocupados_l} ocupados / {4 - ocupados_l} disponibles.")
        print(f"Martes: {ocupados_m} ocupados / {3 - ocupados_m} disponibles.")
        
        # Determinar día con más turnos
        if ocupados_l > ocupados_m:
            print("Día con más turnos: Lunes")
        elif ocupados_m > ocupados_l:
            print("Día con más turnos: Martes")
        else:
            print("Día con más turnos: Empate entre Lunes y Martes")

    elif opcion == "5":
        print("Cerrando el sistema de agenda. ¡Buen trabajo!")
    else:
        print("Error: Opción fuera de rango (1-5).")
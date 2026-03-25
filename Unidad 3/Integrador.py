#Ejercicio 1— “Caja del Kiosco”
#Objetivo: Simular una compra con validaciones y cálculo de total.
#Requisitos
#1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while).
#2. Pedir cantidad de productos a comprar (número entero positivo, validar con
#.isdigit() en while).
#3. Por cada producto (usar for):
#o Pedir precio (entero, validar .isdigit()).
#o Pedir si tiene descuento S/N (validar con while, aceptar s o n en
#cualquier mayuscula/minuscula).
#o Si tiene descuento: aplicar 10% al precio de ese producto.
#4. Al final mostrar:
#o Total sin descuentos
#o Total con descuentos
#o Ahorro total
#o Promedio por producto (usar float y formatear con :.2f, ejem:
#x = 3.14159
#print(f"{x:.2f}"))

#Le pedimos al usuario que ingrese su nombre

nom = input("Ingrese su nombre")

#Verificamos que sean solo letras y si no lo son informar al usuario. 
while not nom.isalpha():
    print("Error: Solo se permiten letras y el campo no puede estar vacio.")
    nom = input("Ingrese su nombre: ")

#Pedimos al usuario que ingrese la cantidad de prodcutos que va a comprar

entradaCant = input("Ingrese la cantidad de productos: " )

#Verificamos que sea solo un numero, en caso contrario informar y que vuelva a ingreserlo

while not entradaCant.isdigit():
    print("Error: Solo se permiten numeros y el campo no puede estar vacio.")
    entradaCant = input("Ingrese la cantidad de productos")

cantProductos = int(entradaCant)

#Inicializamos contadores
totalSinDescuento = 0

totalConDescuento = 0

#Por cada producto pedimos y validamos el precio, si tiene descuento
for i in range(cantProductos):
    pInput = input("Ingrese el precio del producto")
    #Validamos si es un numero entero
    while not pInput.isdigit():
        print("Error: Solo se permiten numeros y el campo no puede estar vacio.")
        pInput = input("Ingrese el precio del producto")
    precio = int(pInput)

    totalSinDescuento += precio
    
    descuento = input("¿El producto tiene un descuento? (S/N): ").lower()
    #Verificamos si el usuario ingrese s o n
    while descuento != "s" and descuento != "n":
        print("Error: Ingrese 's' para afirmativo o 'n' para negativo.")
        descuento = input("¿El producto tiene un descuento? (S/N): ").lower()

    #Verificamos si tiene descuento el producto o no
    if descuento == "s":
        precioFinal = precio * 0.90
        print("Se realizo el descuento de 10%")
    else:
        precioFinal = precio
    
    totalConDescuento += precioFinal

#Realizamos los calculos finales e imprimimos lo que pide la consigna
ahorroTotal = totalSinDescuento - totalConDescuento
promedio = totalConDescuento / cantProductos

print("-" * 30)
print(f"Cliente: {nom}")
print(f"Total sin descuentos: ${totalSinDescuento}")
print(f"Total con descuentos: ${totalConDescuento:.2f}")
print(f"Ahorro total: ${ahorroTotal:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")





#Ejercicio 2 — “Acceso al Campus y Menú Seguro”
#Requisitos
#1. Definir credenciales fijas en el código:
#o usuario correcto: "alumno"
#4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
#1. Ver estado de inscripción (mostrar “Inscripto”)
#2. Cambiar clave (pedir nueva clave y confirmación; deben
#coincidir)
#3. Mostrar mensaje motivacional (1 frase)
#4. Salir
#5. Validación del menú:
#o Debe ser número (.isdigit())
#o Debe estar entre 1 y 4
#Cambio de clave
#• La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no,
#rechazar

#Definimos las credenciales fijas y variables de control iniciales
usuarioCorrecto = "alumno"
claveCorrecta = "python123"
intentos = 0
accesoConcedido = False

# Iniciamos el bucle de login (máximo 3 intentos)
# Mientras los intentos sean menores a 3 y no hayamos entrado todavía
while intentos < 3 and accesoConcedido == False:
    intentos += 1
    print(f"\nIntento {intentos}/3")
    
    # Pedimos los datos al usuario
    usuIngresado = input("Usuario: ")
    claIngresada = input("Clave: ")

    # Verificamos si las credenciales coinciden usando operadores relacionales ==
    if usuIngresado == usuarioCorrecto and claIngresada == claveCorrecta:
        print("Acceso concedido.")
        accesoConcedido = True # Cambiamos el booleano para salir del bucle y entrar al menú
    else:
        print("Error: credenciales inválidas.")

# Verificamos si se bloqueó la cuenta por fallar los 3 intentos
if accesoConcedido == False:
    print("\nCuenta bloqueada")
else:
    #Si el acceso fue concedido, entramos al menú repetitivo (while)
    opcion = ""
    while opcion != "4":
        print("\n--- MENÚ DE CAMPUS ---")
        print("1) Ver estado de inscripción")
        print("2) Cambiar clave")
        print("3) Mostrar mensaje motivacional")
        print("4) Salir")
        
        # Pedimos la opción como texto para validar con .isdigit()
        opcion = input("Elija una opción: ")
        
        # Validación del menú: debe ser número
        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = input("Opción: ")
        
        # Validación del rango: debe estar entre 1 y 4
        if int(opcion) < 1 or int(opcion) > 4:
            print("Error: opción fuera de rango.")
        
        # Ejecutamos las acciones según la opción elegida
        elif opcion == "1":
            print("Estado: Inscripto")
            
        elif opcion == "2":
            # Proceso de cambio de clave
            nueva_clave = input("Nueva clave (mínimo 6 caracteres): ")
            
            # Validamos el largo de la clave con len() según la consigna
            while len(nueva_clave) < 6:
                print("Error: la clave es muy corta (mínimo 6).")
                nueva_clave = input("Nueva clave: ")
            
            confirmacion = input("Confirme su nueva clave: ")
            
            # Verificamos que ambas coincidan
            if nueva_clave == confirmacion:
                claveCorrecta = nueva_clave
                print("Clave cambiada con éxito.")
            else:
                print("Error: Las claves no coinciden. Intente nuevamente.")
                
        elif opcion == "3":
            print("Mensaje: 'El éxito es la suma de pequeños esfuerzos repetidos día tras día'.")
            
        elif opcion == "4":
            print("Cerrando sesión")

#Ejercicio 3
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

       
       
#Ejercicio 4 
        #Historia
#Eres un agente que intenta abrir una bóveda con 3 cerraduras.
#Cuentas con energía y tiempo limitados; si logras abrir las 3 antes de que se agoten, ganas.
#Variables iniciales (No se piden por teclado):
#energia = 100
#tiempo = 12
#cerraduras_abiertas = 0
#alarma = False
#codigo_parcial = ""
#Validaciones obligatorias:
#No usar try/except.
#Validar el nombre del agente con .isalpha() en un while.
#Validar opciones del menú y cualquier número pedido con .isdigit() en un while.
#Regla anti-spam (Muy importante):
#Si eliges "Forzar cerradura" (opción 1) 3 veces seguidas:
#Se cobra el costo normal (-20 energía, -2 tiempo).
#NO abre la cerradura.
#Se activa la alarma automáticamente (alarma = True).
#Elegir la opción 2 o 3 corta esta racha.
#Menú de acciones
#El juego continúa mientras energia > 0, tiempo > 0, cerraduras_abiertas < 3 y no esté bloqueado por la alarma.
#Forzar cerradura (Costo: -20 energía, -2 tiempo):
#Si la energía es menor a 40, hay "riesgo de alarma": pedir un número del 1 al 3. Si el usuario elige 3, alarma = True.
#Si no hay alarma, se abre 1 cerradura.
#Aplica la regla anti-spam.
#Hackear panel (Costo: -10 energía, -3 tiempo):
#Usar un for de 4 pasos mostrando el progreso.
#En cada paso, sumar una letra al codigo_parcial (ej: "A").
#Si len(codigo_parcial) >= 8, se abre 1 cerradura automáticamente (si faltan).
#Descansar (Costo: +15 energía (máx 100), -1 tiempo):
#Si la alarma está encendida (alarma == True), se restan 10 de energía extra.
#Regla de bloqueo por alarma
#:
#Si alarma == True y tiempo <= 3 y aún no se abrió la bóveda, el sistema se bloquea y pierdes.
#Condiciones de fin
#:
#VICTORIA: cerraduras_abiertas == 3.
#DERROTA: energia <= 0 o tiempo <= 0.
#DERROTA (Bloqueo): Si se activa el bloqueo por alarma y tiempo agotado.



# Variables iniciales (fijas según la consigna)
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
# Contador interno para la regla anti-spam
forzar_seguidas = 0  

# Registro del agente con validación 
nombreAgente = input("Ingrese su nombre agente: ")
while not nombreAgente.isalpha():
    print("Error: El nombre solo puede contener letras y no puede estar vacío.")
    nombreAgente = input("Ingrese su nombre agente: ")

# Bucle principal del juego: se repite mientras haya recursos y no se gane
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    
    # REGLA DE BLOQUEO: Si hay alarma y el tiempo es crítico (<= 3), se pierde automáticamente 
    if alarma == True and tiempo <= 3:
        print("\n¡SISTEMA BLOQUEADO! La alarma y el tiempo agotado han sellado la bóveda.")
        break

    # Mostrar estado actual al agente 
    print(f"\n{'='*20} ESTADO ACTUAL {'='*20}")
    print(f"Agente: {nombreAgente} | Cerraduras: {cerraduras_abiertas}/3")
    print(f"Energía: {energia} | Tiempo: {tiempo} | Alarma: {'ON' if alarma else 'OFF'}")
    print(f"Código parcial: '{codigo_parcial}'")
    
    # Menú de acciones
    print("\nAcciones disponibles:")
    print("1) Forzar cerradura (-20 energía, -2 tiempo)")
    print("2) Hackear panel (-10 energía, -3 tiempo)")
    print("3) Descansar (+15 energía, -1 tiempo)")
    
    # Validación de la opción elegida 
    validarOpcion = input("Elija una opción: ")
    while not validarOpcion.isdigit():
        print("Error: Ingrese un número válido.")
        validarOpcion = input("Elija una opción: ")
    
    opcion = int(validarOpcion)
    
    if opcion == 1:
        # Costo base de la acción
        energia -= 20
        tiempo -= 2
        forzar_seguidas += 1

        # Regla anti Spam: 3 veces seguidas activa alarma y no abre nada 
        if forzar_seguidas == 3:
            print("¡AVISO! La cerradura se trabó por forzarla demasiado. ALARMA ACTIVADA.")
            alarma = True
        else:
            # Riesgo de alarma si la energía es baja (< 40)
            if energia < 40:
                print("¡RIESGO! Estás muy cansado y haces ruido.")
                riesgo = input("Para mantener el sigilo, elige un número (1-3): ")
                while not riesgo.isdigit():
                    riesgo = input("Error: elige un número: ")
                if int(riesgo) == 3:
                    alarma = True
                    print("¡Activaste los sensores! Alarma encendida.")
            
            # Si no saltó la alarma, se abre una cerradura
            if not alarma:
                cerraduras_abiertas += 1
                print("¡Click! Has abierto una cerradura.")

    elif opcion == 2:
        # Hackear panel: corta la racha de forzar
        energia -= 10
        tiempo -= 3
        forzar_seguidas = 0
        
        print("Iniciando bypass del sistema...")
        # Uso obligatorio de bucle FOR para el progreso 
        for i in range(4):
            print(f"Hackeando... paso {i+1}/4")
            codigo_parcial += "A"
        
        # Validación de longitud de código
        if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("¡Código completado! Una cerradura se ha liberado.")
                # Se limpia para un posible nuevo hackeo
                codigo_parcial = "" 

    elif opcion == 3:
        # Descansar: recupera energía
        forzar_seguidas = 0
        tiempo -= 1
        energia += 15
        if energia > 100: 
            energia = 100
        
        # Penalización si la alarma está encendida
        if alarma:
            energia -= 10
            print("No puedes descansar bien con el ruido de la alarma. -10 energía.")
        else:
            print("Has recuperado fuerzas en silencio.")

    else:
        print("Opción fuera de rango. Pierdes el turno por dudar.")

#Resultados Finales
if cerraduras_abiertas == 3:
    print(f"\n¡VICTORIA! El agente {nombreAgente} ha burlado la seguridad y abierto la bóveda.")
elif energia <= 0:
    print(f"\nDERROTA. {nombreAgente} se ha desmayado por agotamiento.")
elif tiempo <= 0:
    print(f"\nDERROTA. Se acabó el tiempo y los refuerzos te han atrapado.")



#Ejercicio 5 — “Escape Room:"La Arena del
#Gladiador"
#1. Descripción del Escenario
#Vas a desarrollar un simulador de batalla por turnos en Python. El programa enfrentará a un
#usuario (Gladiador) contra un oponente controlado por la computadora (Enemigo). El
#Este ejercicio evalúa el uso de variables (int, float, string, boolean), estructuras de
#control (if/elif/else), ciclos (while y for) y validación de datos estricta.
#2. Requerimientos Técnicos
#A. Tipos de Datos
#Debes utilizar obligatoriamente los siguientes tipos de datos para las variables del juego:
#• • String: Para el nombre del jugador.
#• • Int: Para los Puntos de Vida (HP) y cantidad de pociones.
#• • Float: Para el cálculo del daño (ej: un golpe crítico multiplica el ataque por 1.5). 

#• • Boolean: Para controlar si el juego sigue activo o quién tiene el turno.
#B. Reglas de Validación (¡Importante!)
#• • No está permitido usar bloques try / except.
#• • Para validar texto, debes usar el método .isalpha() dentro de un ciclo while.
#• • Para validar números, debes usar el método .isdigit() dentro de un ciclo
#while.
#3. Flujo del Programa
#Paso 1: Configuración del Personaje
#El programa inicia pidiendo el nombre del Gladiador.
#• • Validación: El nombre solo puede contener letras. Si el usuario ingresa números,
#símbolos o lo deja vacío, el programa debe decir "Error: Solo se permiten letras" y volver a
#preguntar hasta que sea válido.
#Paso 2: Inicialización de Estadísticas
#El programa debe definir las variables iniciales (sin preguntar al usuario):
#• • Vida del Gladiador: 100 (int)
#• • Vida del Enemigo: 100 (int)
#• • Pociones de Vida: 3 (int)
#• • Daño base "Ataque Pesado": 15 (int)
#• • Daño base del enemigo: 12 (int)
#• • Turno Gladiador : True (booleano)
#Paso 3: El Ciclo de Combate
#El juego entra en un ciclo que se repite mientras ambos combatientes tengan más de 0
#puntos de vida.
#Turno del Jugador:
#Muestra la vida actual de ambos y las pociones restantes. Luego, ofrece un menú con 3
#opciones:
#1. Ataque Pesado
#2. Ráfaga Veloz (Requiere uso de for)
#3. Curar
#• Validación del Menú: El programa debe pedir la opción al usuario. 1. Verificar que lo
#ingresado sea un número (.isdigit()).
#2. Verificar que el número sea 1, 2 o 3.
#o Si falla alguna validación, mostrar mensaje de error y volver a pedir.
#Lógica de las Acciones:
#Acción A: Ataque Pesado (Opción 1)
#• • Calcula el daño final. Si la vida del enemigo es menor a 20 puntos, el jugador
#realiza un "Golpe Crítico" multiplicando su daño base por 1.5 (resultado float).
#• • Resta el daño a la vida del enemigo.
#• • Muestra un mensaje: "¡Atacaste al enemigo por X puntos de daño!"
#Acción B: Ráfaga Veloz (Opción 2)
#• • Esta acción realiza una serie de golpes rápidos. Debes implementar un bucle for.
# • El bucle debe repetirse 3 veces (usando range).
#• • Dentro del bucle, en cada repetición: 1. Resta 5 puntos de daño a la vida del enemigo.
#• 2. Muestra el mensaje: " > Golpe conectado por 5 de daño".
#•
#Acción C: Curar (Opción 3) 
#• • Si tienes pociones (> 0): Suma 30 puntos a tu vida y resta 1 poción.
#• • Si NO tienes pociones: Muestra "¡No quedan pociones!" y pierdes el turno (el
#enemigo ataca igual).
#Turno del Enemigo:
#Justo después de tu acción, el enemigo ataca automáticamente.
#• • Resta el daño base del enemigo (12) a tu vida.
#• • Muestra un mensaje: "¡El enemigo te atacó por 12 puntos de daño!"
#Paso 4: Fin del Juego
#Cuando el ciclo termine (porque la vida de alguno llegó a 0 o menos), debes evaluar:
#• • Si vida_jugador > 0: Mostrar "¡VICTORIA! [Nombre] ha ganado la batalla."
#• • Si vida_jugador <= 0: Mostrar "DERROTA. Has caído en combate." 



# Pedimos el nombre y validamos que sean solo letras y no esté vacío
nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras")
    nombre = input("Nombre del Gladiador: ")

# Definimos los tipos de datos según la consigna 
vida_gladiador = 100       
vida_enemigo = 100         
pociones = 3               
ataque_pesado_base = 15    
ataque_enemigo_base = 12   
juego_activo = True        

print("\n=== INICIO DEL COMBATE ===")


# Se repite mientras ambos tengan más de 0 puntos de vida 

while vida_gladiador > 0 and vida_enemigo > 0:
    # Mostramos estado actual
    print(f"\n{nombre} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz (Bucle for)")
    print("3. Curar")
    
    # Validación del menú 
    opcion_input = input("Opción: ")
    while not opcion_input.isdigit() or (int(opcion_input) < 1 or int(opcion_input) > 3):
        print("Error: Ingrese un número válido (1, 2 o 3).")
        opcion_input = input("Opción: ")
    
    opcion = int(opcion_input)
    
    if opcion == 1:
        # Acción A: Ataque Pesado
        daño = float(ataque_pesado_base) 
        
        # Si la vida del enemigo es baja, se realiza un golpe crítico
        if vida_enemigo < 20:
            daño = ataque_pesado_base * 1.5
            print("¡GOLPE CRÍTICO!")
        
        vida_enemigo -= int(daño)
        print(f"¡Atacaste al enemigo por {daño} puntos de daño!")
        
    elif opcion == 2:
        # Acción B: Ráfaga Veloz 
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print(" > Golpe conectado por 5 de daño")
            
    elif opcion == 3:
        # Acción C: Curar 
        if pociones > 0:
            vida_gladiador += 30
            pociones -= 1
            print(f"Te has curado. Pociones restantes: {pociones}")
        else:
            # Si no hay pociones, se informa y se pierde la acción (pero el enemigo ataca igual)
            print("¡No quedan pociones! Pierdes el turno.")

    #Enemigo

    # Ataca automáticamente si todavía tiene vida después de la acción del jugador 
    if vida_enemigo > 0:
        vida_gladiador -= ataque_enemigo_base
        print(f">> ¡El enemigo te atacó por {ataque_enemigo_base} puntos de daño!")

#Fin del Juego 
if vida_gladiador > 0:
    print(f"\n¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print(f"\nDERROTA. {nombre} ha caído en combate.")
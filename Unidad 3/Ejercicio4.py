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
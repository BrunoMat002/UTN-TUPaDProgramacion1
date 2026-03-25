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
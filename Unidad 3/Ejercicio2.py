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
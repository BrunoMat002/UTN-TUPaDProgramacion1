#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”. 

#Pedimos al usuario que ingrese su nota

nota = int(input("Ingrese su nota"))

# Verificamos que la nota sea mayor o igual a 6

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
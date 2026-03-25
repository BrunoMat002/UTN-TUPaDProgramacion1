#Actividades 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
 


#Pedir al usuario que ingrese su edad

edad = int(input("Ingresa tu edad: "))


if edad >= 18:
    print("Es mayor de edad")
else:
    print(f"Usted no es mayor de edad ya que tiene:{edad}")
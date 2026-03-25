#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#• Niño/a: menor de 12 años.
#• Adolescente: mayor o igual que 12 años y menor que 18 años.
#• Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#• Adulto/a: mayor o igual que 30 años. 



#Pedir al usuario que ingrese su edad

edad = int(input("Ingrese su edad"))

#Verificamos  que categoria pertenece

if edad >= 0 and edad < 12:
    print("Usted es un/a niño/a")
elif edad >=12 and edad < 18:
    print("Usted es un/a adolescente")
elif edad >= 18 and edad < 30:
    print("Usted es un adulto/a joven")
else:
    print("Usted es un adulto")    
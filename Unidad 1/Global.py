#EJERCICIO 1
#Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”


#imprimimos el texto "Hola Mundo!"

print("Hola Mundo!")


#Ejercicio 2
# Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

#Pedimos al usuario que ingrese su nombre

nombre = input("Ingresa tu nombre: ")

#Imprimimos el saludo con el nombre ingresado

print(f"Hola {nombre}!")


#EJERCICIO 3
# Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla

#Pedimos al usuario que ingrese los diferentes datos que pide el ejercicio

nom = input("Ingrese su nombre: ")

ape = input("Ingrese su apellido: ")

edad =  input("Ingrese su edad: ")

lugar = input("Ingrese su lugar de residencia: ")

#Una vez ingresados todos los elementos imprimimos la oracion completa

print(f"Soy {nom} {ape}, tengo {edad} años y vivo en {lugar}")

# EJERCICIO 4
# Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

#Pedimos al usuario que ingrese el radio de un circulo

radio = float(input("Ingrese el radio de un circulo: "))

#Calculamos su area y perimetro

area = radio ** 2 * 3.14

perimetro = 2 * 3.14 * radio

#Imprimimos los resultados

print(f"El area del circulo es: {area}")

print(f"El perimetro del circulo es: {perimetro}")

#EJERCICIO 5

#Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale

#Le pedimos al usuario que ingrese una cantidad de segundos

seg = int(input("Ingrese una cantidad de segundos: "))

#Realizamos la cuanto para verificar cuantas horas equivale

horas = seg / 3600

#Imprimimos el resultado

print(f"{seg} segundos equivale a {horas} horas.")

#EJERCICIO 6
# Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

#Le pedimos al usuario que ingrese un numero

num = int(input("ingrese un numero: "))

#Caculamos se tabla de multiplicar

uno = num * 1
dos = num * 2
tres = num *3
cuatro = num *4
cinco = num *5
seis = num *6
siete = num *7
ocho = num *8
nueve = num *9
diez = num *10

#Imprimimos los resultados
print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)
print(seis)
print(siete)
print(ocho)
print(nueve)
print(diez)

#EJERCICIO 7

# Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

#Le pedimos a un usuario que ingrese dos numeros distintos a 0

num1 = int(input("Ingrese un numero distinto de 0: "))

num2 = int(input("ingrese un segundo numero distinto a 0: "))

#Calculamos las diferentes operaciones

suma = num1 + num2
multiplicacion = num1 * num2


if num1 > num2:
    division = num1 / num2
    resta = num1 - num2
else:
    division = num2 / num1 
    resta = num2 - num1

#Imprimimos los resultados

print(f"La suma de ambos numeros es: {suma}")
print(f"La resta de ambos numeros es: {resta}")
print(f"La multiplicacion de ambos numeros es: {multiplicacion}")
print(f"La division de ambos numeros es: {division}")

#EJERCICIO 8

#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:

#Le pedimos al usuario que ingrese su altura y su peso

altura = float(input("Ingresa tu altura: "))
peso = float(input("Ingresa tu peso: "))

#Calculamos el valor del IMC

IMC = peso / altura ** 2

#Informamos el resultado

print(f"Tu indice de masa corporal es: {IMC} ")


#EJERCICIO 9

# Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

#Le pedimos al usuario que ingrese la temperatura en grados celcius

grados = float(input("Ingrese una temperatura en grados Celcius: "))

#Calculamos su equivalente en grados fahrenheit

TemperaturaF = 9/5 * grados + 32

#Imprimimos el valor final

print(f"El equivalente de {grados} grados Celcius es {TemperaturaF} grados fahrenheit")

#EJERCICIO 10

# Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

#Inicializamos dos variables para contar el total y luego el promedio
total = 0
promedio = 0

#Le pedimos al usuario que ingrese los 3 numeros
num1 =int(input("Ingrese un numero: "))
num2 =int(input("Ingrese otro numero: "))
num3 =int(input("Ingrese otro numero: "))

#Calculamos lo que pide el ejercicio

total = num1 + num2 + num3

promedio = total / 3

#Imprimimos el promedio final

print(f"El promedio es: {promedio}")
#3.Crear una función llamada informacion_personal(nombre, apellido, edad,
#residencia) que reciba cuatro parámetros e imprima: “Soy [nombre]
#[apellido], tengo [edad] años y vivo en [residencia]”. Pe- dir los datos al
#usuario y llamar a esta función con los valores in- gresados.


#Creamos la funcion informacionPersonal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivio en {residencia}" )

#Pedimos al usuario que ingrese lo que pide el enunciado
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")

#LLamamos a la funcion e imprimimos los valores que ingresa el usuario
informacion_personal(nombre, apellido, edad, residencia)
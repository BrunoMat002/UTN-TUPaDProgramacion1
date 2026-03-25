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
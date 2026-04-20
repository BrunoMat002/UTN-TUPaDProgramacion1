# 2. Crear una función llamada saludar_usuario(nombre) que reciba como
# parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si
# se llama con saludar_usuario("Marcos"), deberá de- volver: “Hola Marcos!”.
# Llamar a esta función desde el programa principal solicitando el nombre al
# usuario.


#Realizamos la funcion
def saludar_usuario(nombre):
    return (f"Hola {nombre}!")


#Le pedimos al usuario que ingrese un nombre
nombre = input("Ingrese su nombre: ")
#Imprimimos el mensaje
print(saludar_usuario(nombre))


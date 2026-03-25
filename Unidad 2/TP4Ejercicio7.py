#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla. 

#Solicitamos al usuario ingresar un frase
frase = input("Ingrese una frase o palabra: ")

# 2. Definimos las vocales
vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"

# Verificamos si el último carácter de la frase está en nuestra lista de vocales
if frase[-1] in vocales:
    frase = frase + "!"

# 4. Imprimimos el resultado 
print(f"resultado:  {frase}")

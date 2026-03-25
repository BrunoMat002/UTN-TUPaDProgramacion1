#Ejercicio 1— “Caja del Kiosco”
#Objetivo: Simular una compra con validaciones y cálculo de total.
#Requisitos
#1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while).
#2. Pedir cantidad de productos a comprar (número entero positivo, validar con
#.isdigit() en while).
#3. Por cada producto (usar for):
#o Pedir precio (entero, validar .isdigit()).
#o Pedir si tiene descuento S/N (validar con while, aceptar s o n en
#cualquier mayuscula/minuscula).
#o Si tiene descuento: aplicar 10% al precio de ese producto.
#4. Al final mostrar:
#o Total sin descuentos
#o Total con descuentos
#o Ahorro total
#o Promedio por producto (usar float y formatear con :.2f, ejem:
#x = 3.14159
#print(f"{x:.2f}"))

#Le pedimos al usuario que ingrese su nombre

nom = input("Ingrese su nombre")

#Verificamos que sean solo letras y si no lo son informar al usuario. 
while not nom.isalpha():
    print("Error: Solo se permiten letras y el campo no puede estar vacio.")
    nom = input("Ingrese su nombre: ")

#Pedimos al usuario que ingrese la cantidad de prodcutos que va a comprar

entradaCant = input("Ingrese la cantidad de productos: " )

#Verificamos que sea solo un numero, en caso contrario informar y que vuelva a ingreserlo

while not entradaCant.isdigit():
    print("Error: Solo se permiten numeros y el campo no puede estar vacio.")
    entradaCant = input("Ingrese la cantidad de productos")

cantProductos = int(entradaCant)

#Inicializamos contadores
totalSinDescuento = 0

totalConDescuento = 0

#Por cada producto pedimos y validamos el precio, si tiene descuento
for i in range(cantProductos):
    pInput = input("Ingrese el precio del producto")
    #Validamos si es un numero entero
    while not pInput.isdigit():
        print("Error: Solo se permiten numeros y el campo no puede estar vacio.")
        pInput = input("Ingrese el precio del producto")
    precio = int(pInput)

    totalSinDescuento += precio
    
    descuento = input("¿El producto tiene un descuento? (S/N): ").lower()
    #Verificamos si el usuario ingrese s o n
    while descuento != "s" and descuento != "n":
        print("Error: Ingrese 's' para afirmativo o 'n' para negativo.")
        descuento = input("¿El producto tiene un descuento? (S/N): ").lower()

    #Verificamos si tiene descuento el producto o no
    if descuento == "s":
        precioFinal = precio * 0.90
        print("Se realizo el descuento de 10%")
    else:
        precioFinal = precio
    
    totalConDescuento += precioFinal

#Realizamos los calculos finales e imprimimos lo que pide la consigna
ahorroTotal = totalSinDescuento - totalConDescuento
promedio = totalConDescuento / cantProductos

print("-" * 30)
print(f"Cliente: {nom}")
print(f"Total sin descuentos: ${totalSinDescuento}")
print(f"Total con descuentos: ${totalConDescuento:.2f}")
print(f"Ahorro total: ${ahorroTotal:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
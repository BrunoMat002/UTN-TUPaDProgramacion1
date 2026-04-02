#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# Mostrar el total vendido por cada producto.
#● Mostrar el día con mayores ventas totales.
#● Indicar cuál fue el producto más vendido en la semana.


#Definimos dimensiones e inicializamos la matriz con ceros
cant_productos = 4
cant_dias = 7
matriz_ventas = [[0] * cant_dias for i in range(cant_productos)]

#Carga de datos
print("--- Ingreso de Ventas Semanales ---")
for i in range(cant_productos):
    print(f"Producto {i + 1}:")
    for j in range(cant_dias):
        matriz_ventas[i][j] = float(input(f"  Ventas día {j + 1}: "))

#Totales por producto
print("\n--- Totales por Producto ---")
totales_productos = []
for i in range(cant_productos):
    suma_producto = 0
    for j in range(cant_dias):
        suma_producto += matriz_ventas[i][j]
    totales_productos.append(suma_producto)
    print(f"Producto {i + 1}: Total vendido = {suma_producto:.2f}")

#Día con mayores ventas
max_ventas_dia = -1
dia_ganador = 0

for j in range(cant_dias):
    total_dia = 0
    for i in range(cant_productos):
        total_dia += matriz_ventas[i][j]
    
    if total_dia > max_ventas_dia:
        max_ventas_dia = total_dia
        dia_ganador = j + 1

print(f"\nEl día con mayores ventas fue el Día {dia_ganador} con {max_ventas_dia:.2f}")

#Producto más vendido
max_ventas_prod = -1
prod_ganador = 0

for i in range(len(totales_productos)):
    if totales_productos[i] > max_ventas_prod:
        max_ventas_prod = totales_productos[i]
        prod_ganador = i + 1

print(f"El producto más vendido fue el Producto {prod_ganador} con {max_ventas_prod:.2f} unidades.")
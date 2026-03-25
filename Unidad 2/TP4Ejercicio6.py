#6) Escribir un programa que solicite al usuario el consumo mensual de energía eléctrica en
# kilovatios (kWh) e indique la categoría del consumo según el siguiente criterio:
# • Menor que 150 kWh: “Consumo bajo”.
# • Entre 150 y 300 kWh (inclusive): “Consumo medio”.
# • Mayor que 300 kWh: “Consumo alto”.



#Pedimos al usuario que ingrese el consumo mensuaal de energia electrica

consumo = int(input("Ingrese su consumo mensual de energia electrica en kilovatios(kWh)"))

#Verificamos en que categoria se encuentra

if consumo <= 150:
    print("Consumo bajo")
elif consumo > 150 and consumo <= 300:
    print("Consumo medio")
else:
    print("Consumo alto")
if consumo >= 500:
    print("Considere medidas de ahorro energetico")
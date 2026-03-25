# 1. Solicitamos los datos al usuario
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ")
mes = input("¿Qué mes es?: ")
dia = int(input("¿Qué día es?: "))

# 2. Convertimos el mes a número para facilitar las comparaciones
meses = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, 
    "mayo": 5, "junio": 6, "julio": 7, "agosto": 8, 
    "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}

m = meses[mes]

# 3. Determinamos el periodo del año basado en la tabla
# Periodo 1: 21 Dic al 20 Mar
if (m == 12 and dia >= 21) or (m <= 2) or (m == 3 and dia <= 20):
    norte, sur = "Invierno", "Verano"

# Periodo 2: 21 Mar al 20 Jun
elif (m == 3 and dia >= 21) or (m <= 5) or (m == 6 and dia <= 20):
    norte, sur = "Primavera", "Otoño"

# Periodo 3: 21 Jun al 20 Sep
elif (m == 6 and dia >= 21) or (m <= 8) or (m == 9 and dia <= 20):
    norte, sur = "Verano", "Invierno"

# Periodo 4: 21 Sep al 20 Dic
else:
    norte, sur = "Otoño", "Primavera"

# 4. Imprimimos el resultado según el hemisferio elegido
if hemisferio == "N":
    print(f"Usted se encuentra en: {norte}")
else:
    print(f"Usted se encuentra en: {sur}")
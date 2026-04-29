#7) Se recibe el registro diario de asistencia a una capacitación en forma de lista.
#En dicha lista pueden aparecer nombres repetidos, ya que una misma persona pudo haber
#asistido en más de una jornada.
#• Mostrá la lista original de asistencias.
#• Generá un conjunto (set) a partir de la lista y mostrar los empleados que asistieron al
#menos una vez (sin repetir nombres).
#• Indicá cuántas veces asistió cada empleado a la capacitación.

#Definimos la lista original (segun el ejemplo del PDF)
asistencias = ["Ana", "Luis", "Ana", "Maria", "Luis", "Pedro", "Ana"]

#Mostramos la lista original de asistencias
print(f"Lista original de asistencias: {asistencias}")

#Generamos un conjunto (set) a partir de la lista para ver los nombres unicos
empleados_unicos = set(asistencias)
print(f"Empleados que asistieron al menos una vez: {empleados_unicos}")

# • Indicamos cuantas veces asistio cada empleado a la capacitacion
print("Reporte de Frecuencias")
for empleado in empleados_unicos:
    #Usamos el metodo .count() sobre la lista original para saber la frecuencia
    cantidad = asistencias.count(empleado)
    print(f"El empleado {empleado} asistió {cantidad} veces.")
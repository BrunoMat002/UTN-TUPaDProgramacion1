#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios. 


#Utilizamos el diccionario del punto anterior
precios_frutas = {"Banana": 1330, "Anana": 2500, "Melon": 2800, "Uva": 1450, "Naranja": 1200, "Manzana": 1700, "Pera": 2300}

#Para crear una lista que solo contenga solamente las frutas utilizaremos el metodo .keys()
#Ya que solo queremos la clave y no el value o valor

nombre_frutas = list(precios_frutas.keys())

#Imprimimos la lista para verificar que se realizo correctamente

print(nombre_frutas)
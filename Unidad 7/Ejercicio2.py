#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

#Utilizamos el diccionario de precios_frutas del punto anterior
precios_frutas = {"Banana" : 1200, "Anana" : 2500, "Melon" : 3000, "Uva" : 1450, "Naranja" : 1200, "Manzana" : 1500, "Pera" : 2300 }


#Para actualizar simplemente volvemos a escribir los nuevos valores

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melon"] = 2800

#Imprimimos el diccionario para verificar los resultados

print(precios_frutas)
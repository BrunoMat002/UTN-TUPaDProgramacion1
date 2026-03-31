#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha
#(el último pasa a ser el primero).

#Generamos la lista con los numeros

lista = [15,10,32,44,56,69,72]


#Sacamos el ultimo digito y lo guardamos
ultimo = lista.pop() # [2]

# Lo insertamos en la posición 0
lista.insert(0, ultimo) # [3]

#Imprimimmos la lista modificada
print(f"Lista Final: {lista}") 

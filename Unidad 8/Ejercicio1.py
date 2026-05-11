#1) Identifica los errores del código usando comentarios (#) en las líneas afectadas. Indica el tipo
#de error y una breve explicación de por qué ocurre.
#Ejemplo: c = a / b # Error: TypeError. 'b' es un string y no permite la división[cite: 14].

a = 10

b = input("Introduce un número: ")

result = a / b #Error: TypeError. "b" es un string por lo tanto no se puede utilizar para realizar la division

print(f"Resultado: {result}")

numbers = [1, 2, 3]

print(numbers[5]) #Error: IndexError. numbers[5] no existe ya que la lista llega hasta el indice 2 que seria el valor 3. 

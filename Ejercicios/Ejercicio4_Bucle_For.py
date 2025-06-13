# Ejercicio 4: Bucle for

# Pedir número 
numero = int(input("Ingresa un número: "))

# Imprimir números del 1 hasta el número escrito
for i in range(1, numero + 1): # Se pone + 1, para que imprima tambien el número que hace de límite
    print(i)

for i in range(numero, 0, -2): # Hace un decremento de 2 en 2, hasta llegar al 0 sin incluirlo, 
    print(i)                   # si quiero incluirlo tengo que poner 0 - 1 
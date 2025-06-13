# Ejercicio 2. Operaciones Matemáticas
# Pedir 2 números al usuario.
# Sumar, restar, multiplicar y dividir esos números.
# Finalmente imprimir el resultado de cada operaciones.

numero1 = float(input("Escribe el primer número: "))
numero2 = float(input("Escribe el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"La suma {numero1} + {numero2} es: {suma}")
print(f"La resta {numero1} - {numero2} es: {resta}")
print(f"La multiplicacion {numero1} * {numero2} es: {multiplicacion}")
print(f"La division {numero1} / {numero2} es: {division}")
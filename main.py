print("¡Mi primer script en Python funciona en VS Code!")

# Aprendiendo Python

# Ejercicio 1

# Pedir datos al usuario
nombre = input("¿Como te llamas? ")
edad = int(input("¿Cuantos años tienes? "))

# Imprimir un mensaje por pantalla
print(f"Hola {nombre}, tienes {edad} años.")

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

# Ejercicio 3: Condiciones (if/elif/else)
# Pida al usuario que ingrese una edad.
# Según la edad, imprimirá:
# “Eres un niño” si tiene menos de 13 años
# “Eres un adolescente” si tiene de 13 a 17 años
# “Eres un adulto” si tiene 18 o más

edad = int(input("Ingresa una edad: "))

if edad < 13:
    print("Eres un niño.")
elif edad >= 13 and edad < 18: 
    print("Eres un adolescente.")
else:
    print("Eres un adulto.")


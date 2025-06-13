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
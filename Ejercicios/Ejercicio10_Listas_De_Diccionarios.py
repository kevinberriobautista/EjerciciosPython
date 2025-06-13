# Ejercicio 10: Listas de diccionarios

# Creo una lista de diccionarios
personas = [
    {"nombre": "Kevin", "edad": 23, "ciudad": "Almería"},
    {"nombre": "Antonio", "edad": 32, "ciudad": "Granada"},
    {"nombre": "Raul", "edad": 56, "ciudad": "Toledo"}
]

# Recorro la lista e imprimo la información de cada persona
print("Personas: \n")

for persona in personas: 
    print(f"Nombre: {persona["nombre"]}")
    print(f"Edad: {persona["edad"]}")
    print(f"Ciudad: {persona["ciudad"]}")
    print("\n")
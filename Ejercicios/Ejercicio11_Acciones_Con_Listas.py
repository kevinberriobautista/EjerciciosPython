# Ejercicio 11: Buscar, actualizar o eliminar en una lista de diccionarios

# Creo una lista de diccionarios
personas = [
    {"nombre": "Kevin", "edad": 23, "ciudad": "Almería"},
    {"nombre": "Antonio", "edad": 32, "ciudad": "Granada"},
    {"nombre": "Raul", "edad": 56, "ciudad": "Toledo"}
]

# Buscar a "Kevin" en la lista
for persona in personas:
    if persona["nombre"] == "Kevin":
        print("Persona encontrada: ")
        print(persona)
        break

print("-" * 20)

# Actualizar la ciudad de "Antonio"
for persona in personas:
    if persona["nombre"] == "Antonio":
        persona["ciudad"] = "Sevilla"
        print("Ciudad de Antonio actualizada: ")
        print(persona)
        break

print("-" * 20)

# Eliminar a "Raul" de la lista
for i, persona in enumerate(personas): # Lo hago con enumerate para que me devuelva la posición en la lista de la persona
    if persona["nombre"] == "Raul":
        del personas[i]
        print("Raul ha sido eliminado.")
        break

print("-" * 20)

# Imprimo la lista actualizada despues de todas la operaciones
print("Lista final: ")
for persona in personas: 
    print(persona)
    print("\n")

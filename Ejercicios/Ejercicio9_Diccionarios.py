# Ejercicio 9: Diccionarios

persona = {
    "nombre": "Kevin",
    "edad": 23,
    "ciudad": "Almería"
}

# Imprimir toda la informacion
print("Datos de la persona: \n", persona)

# Acceder a un valor en particular
print("Nombre: ", persona["nombre"])

# Agregar un nuevo campo
persona["profesion"] = "programador"

print("Datos actualizados: ", persona)

# Modificar un valor
persona["ciudad"] = "Aguadulce"

print("Ciudad actualizada: ")
print(persona)
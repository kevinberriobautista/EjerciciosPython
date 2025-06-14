# Ejercicio 15: Filtrar en JSON

import json

def filtrar_JSON(archivo_json, edad_minima=None, ciudad=None):
    # Filtra las personas en el JSON según la edad o la ciudad
    with open(archivo_json, encoding='utf-8') as file:
        personas = json.load(file)

    personasFiltradas = []
    for persona in personas:
        # IMPORTANTE --> Si se cumplen las 2 condiciones, se ejecuta el continue que hace que no se ejecute el resto del for, de esa manera se filtra
        # Si la edad minima no es nula y la edad de la persona es menor que la edad minima continua
        if edad_minima is not None and persona["edad"] < edad_minima:
            continue 
        # Si la ciudad no es nula y la ciudad es diferente a la escrita
        if ciudad is not None and persona["ciudad"].lower() != ciudad.lower():
            continue
        # Añado las personas que no cumplen los if
        personasFiltradas.append(persona)
    return personasFiltradas

# Uso de la función
mayoresde40 = filtrar_JSON("personas.json", edad_minima=40)
print("\nPersonas mayores de 40: ")
for persona in mayoresde40:
    print(persona)

almerienses = filtrar_JSON("personas.json", ciudad="Almería")
print("\nPersonas de Almería: ")
for persona in almerienses:
    print(persona)
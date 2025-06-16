# Ejercicio 16: Actualizar CSV o JSON

# CSV

import csv

def actualizar_csv(archivo_csv, nombre, nuevo_valor): 
    personas = []

    with open(archivo_csv, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['nombre'].lower() == nombre.lower():
                row.update(nuevo_valor) # nuevo_valor es un diccionario
            personas.append(row)

    fieldnames = ['nombre', 'edad', 'ciudad']

    with open(archivo_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for persona in personas:
            writer.writerow(persona)

# Ejemplo de uso: 
actualizar_csv('personas.csv', 'Antonio', {"ciudad": "Valencia", "edad": "60"})
print("Registro actualizado en CSV.")

# JSON

import json

def actualizar_json(archivo_json, nombre, nuevo_valor):
    with open(archivo_json, encoding='utf-8') as file:
        personas = json.load(file)

    for persona in personas:
        if persona["nombre"].lower() == nombre.lower():
            persona.update(nuevo_valor)

    with open(archivo_json, 'w', encoding='utf-8') as file:
        json.dump(personas, file, ensure_ascii=False, indent=4)

# Ejemplo de uso
actualizar_json('personas.json', 'Raul', {"ciudad": "Madrid", "edad": 50})
print("Registro actualizado en JSON.")
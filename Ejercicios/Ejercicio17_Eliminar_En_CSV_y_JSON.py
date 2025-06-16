# Ejercicio 17: Eliminar en CSV y JSON

# CSV: eliminar a una perosna en CSV

import csv

def eliminar_csv(archivo_csv, nombre):
    personas = []

    with open(archivo_csv, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['nombre'].lower() != nombre.lower(): # Si el nombre no coincide con el nombre que entra por parametro, entonces entra en personas[]
                personas.append(row)

    fieldnames = ['nombre', 'edad', 'ciudad']

    with open(archivo_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for persona in personas:
            writer.writerow(persona)

# Ejemplo de uso:
eliminar_csv('personas.csv', 'Antonio')
print("Registro eliminado en CSV.")

# JSON

import json

def eliminar_json(archivo_json, nombre):
    with open(archivo_json, encoding='utf-8') as file:
        personas = json.load(file)

    # Esto es lo que se llama una list comprehension o comprensión de listas en Python
    # Es una forma más compacta de crear una nueva lista a partir de otra en una sola línea de código
    # persona delante del for significa qué vas a guardar en la nueva lista
    # En la nueva lista entras todas la personas que no coincidan con el nombre introducido por parámetro
    personas = [persona for persona in personas if persona['nombre'].lower() != nombre.lower()]

    with open(archivo_json, 'w', encoding='utf-8') as file:
        json.dump(personas, file, ensure_ascii=False, indent=4)

# Ejemplo de uso:
eliminar_json('personas.json', 'Antonio')
print("Registro eliminado en JSON.")
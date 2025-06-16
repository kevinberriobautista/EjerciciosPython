# Ejercicio 18: Agregar nuevos registros al CSV o al JSON.

# CSV

import csv

def agregar_csv(archivo_csv, nuevo_registro):
    fieldnames = ['nombre', 'edad', 'ciudad']

    # mode='a' --> añade al final del archivo
    with open(archivo_csv, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(nuevo_registro)

# Ejemplo de uso:
agregar_csv('personas.csv', {"nombre": "Antonio", "edad": "60", "ciudad": "Galicia"})
print("Registro agregado en CSV.")

# JSON

import json

def agregar_json(archivo_json, nuevo_registro):
    with open(archivo_json, encoding='utf-8') as file:
        personas = json.load(file)

    personas.append(nuevo_registro)

    with open(archivo_json, 'w', encoding='utf-8') as file:
        json.dump(personas, file, ensure_ascii=False, indent=4)

# Ejemplo de uso:
agregar_json('personas.json', {"nombre": "Antonio", "edad": 60, "ciudad": "Galicia"})
print("Registro agregado en JSON.")
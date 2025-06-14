# Ejercicio 14: Pasar de CSV a JSON

import csv
import json

def csv_a_json(archivo_csv, archivo_json):
    personas = []
    with open(archivo_csv, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["edad"] = int(row["edad"]) # Covertir el texto a int
            personas.append(row)

    with open(archivo_json, 'w', encoding='utf-8') as file:
        # json.dump sirve para convertir un objeto de Python en JSON
        # personas --> lista de diccionario
        # file --> es el archivo abierto en modo escritura ('w') donde se guardará el resultado
        # ensure_ascii=False --> Deja los acentos o la ñ tal cual están, sin transformarlos en Unicode
        # indent=4 --> es la identación necesario apra que el json sea lo mejor legible posible
        json.dump(personas, file, ensure_ascii=False, indent=4)

# Uso de la función
csv_a_json("personas.csv", "personas.json")
print("Datos guradados en personas.json")
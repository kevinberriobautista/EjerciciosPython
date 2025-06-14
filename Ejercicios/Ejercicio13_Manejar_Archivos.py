# Ejercicio 13: Manejar archivos (leer y guardar)

# Vamos a guardar la información en un CSV o TXT, así cuando cerremos el programa podemos recuperar lo que hicimos
import csv

def guardar_en_csv(filename, personas):
    # Guardar una lista de personas en un csv
    # newline='' evita que aparezcan lineas en blanco en Windows
    # encoding='utf-8' acepta acentos y la ñ sin problema
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        # Define que encabezados o columnas tiene el CSV y tiene que coincidir con las claves del diccionario
        fieldnames = ["nombre", "edad", "ciudad"]
        # csv.DictWriter es un obejto capaz de escribit diccionarios en CSV
        # Se le dice que cada diccionario tiene que tener esos fieldnames
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # Escribe el encabezado del archivo, es decir, la primera linea
        writer.writeheader()
        # Por cada persona(un diccionario) en personas
        for persona in personas:
            # Escribe una linea en el CSV con los datos de ese diccionario
            writer.writerow(persona)

def leer_desde_csv(filename):
    #Leer el CSV y cargar en una lista de diccionarios
    personas = []
    try:
        with open(filename, newline='', encoding='utf-8') as file:
            # csv.DictReader(file) es un objeto que convierte cada línea en un diccionario, utilizando como claves el encabezado de la primera línea
            reader = csv.DictReader(file)
            # Recorre cada linea con sus claves
            for row in reader:
                # CSV deja todo como texto, así que podemos parsear la edad a int
                row["edad"] = int(row["edad"])
                # Añado cada diccionario a la lista de personas
                personas.append(row)
    # Esto evita que el código falle si el CSV aún no existe y así simplemente devolverá personas como lista vacía
    except FileNotFoundError:
        pass
    # Devuelve la lista de diccionarios
    return personas

# Uso de las funciones

# Creo una lista de diccionarios
personas = [
    {"nombre": "Kevin", "edad": 23, "ciudad": "Almería"},
    {"nombre": "Antonio", "edad": 32, "ciudad": "Granada"},
    {"nombre": "Raul", "edad": 56, "ciudad": "Toledo"}
]

# Guardo la información en el csv
guardar_en_csv("personas.csv", personas)

# Leo lo que hay guardado en el csv
personas_csv = leer_desde_csv("personas.csv")
print("Personas cargadas: ")
for persona in personas_csv:
    print(f"\n{persona}")
# Ejercicio 19: CRUD básico en CSV

import csv

# Muestra por pantalla los registros en el CSV
def listar(archivo_csv):
    with open(archivo_csv, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Nombre: {row["nombre"]} | Edad: {row['edad']} | Ciudad: {row['ciudad']}\n")

# Añade un usuario
def agregar(archivo_csv): 
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    ciudad = input("Ingrese su ciudad: \n")
    nuevo = {"nombre": nombre, "edad": edad, "ciudad": ciudad}

    fieldnames = ['nombre', 'edad', 'ciudad']

    with open(archivo_csv, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(nuevo)

    print("Registro añadido con éxito.\n")

# Elimina un usuario
def eliminar(archivo_csv):
    nombre = input("Introduzca el nombre que desea eliminar: \n")
    personas = []

    with open(archivo_csv, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['nombre'].lower() != nombre.lower():
                personas.append(row)

    fieldnames = ['nombre', 'edad', 'ciudad']

    with open(archivo_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for persona in personas:
            writer.writerow(persona)
    
    print("Registro eliminado con éxito!")

# Menú

def menu(archivo_csv):
    while True:
        print("\n1. Listar")
        print("2. Agregar")
        print("3. Eliminar")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar(archivo_csv)
        elif opcion == "2":
            agregar(archivo_csv)
        elif opcion == "3":
            eliminar(archivo_csv)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, inténtelo de nuevo.")


# 
if __name__ == "__main__":
    menu('personas.csv')
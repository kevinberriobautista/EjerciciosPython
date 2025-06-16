# Ejercicio 21: menú CRUD pero con SQLite

import sqlite3

def crear_tabla():
    # Creo la tabla si no exite
    with sqlite3.connect('personas.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS persona (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                edad INTEGER,
                ciudad TEXT
            )
        ''')
        conexion.commit()

# Agregar usuario a la tabla
def agregar():
    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad: "))
    ciudad = input("Ingrese ciudad: ")

    with sqlite3.connect('personas.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO persona (nombre, edad, ciudad) VALUES (?, ?, ?)
        ''', (nombre, edad, ciudad))
        conexion.commit()
    print("Registro agregado con éxito.")

# Borrar usuario de la tabla
def eliminar():
    id_eliminar = int(input("Ingrese el ID a eliminar: "))
    with sqlite3.connect('personas.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('DELETE FROM persona WHERE id = ?', (id_eliminar,))
        conexion.commit()
    print("Registro eliminado.")

# Listar usuarios
def listar():
    with sqlite3.connect('personas.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM persona')
        for row in cursor.fetchall():
            print(f"ID:{row[0]} | Nombre:{row[1]} | Edad:{row[2]} | Ciudad:{row[3]}")

# Actualizar usuario (el campo que se deje vacio no se modifica)
def actualizar():
    # Pido el id del ussuairo que quiero actualizar
    id_modificar = int(input("Ingrese el ID a modificar: (los parametros en blanco no se modificarán)"))

    with sqlite3.connect('personas.db') as conn:
        cursor = conn.cursor()

         # Traer datos actuales del usuario
        cursor.execute('SELECT nombre, edad, ciudad FROM persona WHERE id = ?', (id_modificar,))
        fila = cursor.fetchone() # Meto los datos del usuario en fila

        if fila is None:
            print("No existe registro con ese ID.")
            return
        
        nombre_actual, edad_actual, ciudad_actual = fila

        # Pido los valores a modificaqr al usuario
        nombre = input(f"Ingrese nuevo nombre [{nombre_actual}]: ")
        edad = input(f"Ingrese nueva edad [{edad_actual}]: ")
        ciudad = input(f"Ingrese nueva ciudad [{ciudad_actual}]: ")

        # Si el input está vacío, conservar valor actual
        nombre = nombre if nombre.strip() != '' else nombre_actual
        edad = int(edad) if edad.strip() != '' else edad_actual
        ciudad = ciudad if ciudad.strip() != '' else ciudad_actual

        # Actualizo el usuario
        cursor.execute('''
            UPDATE persona
            SET nombre = ?, edad = ?, ciudad = ?
            WHERE id = ?
        ''', (nombre, edad, ciudad, id_modificar))
        conn.commit()

        print("Registro actualizado correctamente.")

# Buscar a personas por nombre o ciudad
def buscar():
    # Pido nombre o ciudad
    campo = input("Buscar por (nombre/ciudad): ").strip().lower()
    if campo not in ['nombre', 'ciudad']:
        print("Campo inválido. Debe ser 'nombre' o 'ciudad'.")
        return

    # Ahora pido el nombre o la ciudad por la que voy a filtrar
    valor = input(f"Ingrese el {campo} a buscar: ").strip()

    with sqlite3.connect('personas.db') as conn:
        cursor = conn.cursor()
        query = f"SELECT * FROM persona WHERE {campo} LIKE ?"
        cursor.execute(query, ('%' + valor + '%',)) # Los % se utilizan por el LIKE
        resultados = cursor.fetchall()

        if resultados:
            for row in resultados:
                print(f"ID:{row[0]} | Nombre:{row[1]} | Edad:{row[2]} | Ciudad:{row[3]}")
        else:
            print("No se encontraron resultados.")


# Menú de opciones
def menu():
    crear_tabla()
    while True:
        print("\n1. Listar")
        print("2. Agregar")
        print("3. Eliminar")
        print("4. Actualizar")
        print("5. Buscar")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar()
        elif opcion == "2":
            agregar()
        elif opcion == "3":
            eliminar()
        elif opcion == "4":
            actualizar()
        elif opcion == "5":
            buscar()
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")



if __name__ == "__main__":
    menu()
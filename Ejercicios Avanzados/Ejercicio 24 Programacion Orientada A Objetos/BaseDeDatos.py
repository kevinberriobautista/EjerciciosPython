# Ejercicio 24: Clase que maneja toda la base de datos

import sqlite3

class BaseDeDatos:
    def __init__(self, nombre_db="personas_poo.db"):
        self.nombre_db = nombre_db
        self.crear_tabla()

    def conexion_db(self):
        return sqlite3.connect(self.nombre_db)

    def crear_tabla(self):
        with self.conexion_db() as conexion:
            cursor = conexion.cursor()
            cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Persona (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT,
                        edad INTEGER,
                        ciudad TEXT
                    )
            ''')
            conexion.commit()

    def agregar_persona(self, persona):
        with self.conexion_db() as conexion:
            cursor = conexion.cursor()
            cursor.execute('''
                INSERT INTO Persona (nombre, edad, ciudad) VALUES (?, ?, ?)
            ''', persona.to_tuple()) # Con el metodo to_tuple tartabamos los datos para la base de datos
            conexion.commit()

    def eliminar_persona(self, id):
        with self.conexion_db() as conexion:
            cursor = conexion.cursor()
            cursor.execute('DELETE FROM Persona WHERE id = ?', (id,))
            conexion.commit()

    def actualizar_persona(self, id, nombre=None, edad=None, ciudad=None):
        with self.conexion_db() as conexion:
            cursor = conexion.cursor()
            cursor.execute('SELECT nombre, edad, ciudad FROM Persona WHERE id = ?', (id,))
            actual = cursor.fetchone()
            nombre = nombre if nombre is not None else actual[0]
            edad = edad if edad is not None else actual[1]
            ciudad = ciudad if ciudad is not None else actual[2]

            cursor.execute('''
                UPDATE Persona SET nombre = ?, edad = ?, ciudad = ? WHERE id = ?
            ''', (nombre, edad, ciudad, id))
            conexion.commit

    def buscar_personas(self, nombre=None, ciudad=None):
        with self.conexion_db() as conexion:
            cursor = conexion.cursor()
            if nombre:
                cursor.execute('SELECT * FROM Persona WHERE nombre LIKE ?', ('%' + nombre + '%',))
            elif ciudad:
                cursor.execute('SELECT * FROM Persona WHERE ciudad LIKE ?', ('%' + ciudad + '%',))
            else:
                return []
            
            return cursor.fetchall()
        
    def listar_personas(self):
        with self.conexion_db() as conexion:
            cursor = conexion.cursor()
            cursor.execute('SELECT * FROM Persona')
            return cursor.fetchall()
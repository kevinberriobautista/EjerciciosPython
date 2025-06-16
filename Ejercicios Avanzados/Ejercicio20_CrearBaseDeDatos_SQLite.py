# INFORMACIÓN
# SQLite es una base de datos ligera, sin tener que instalar un motor externo como MySQL o Postgres.
# Toda la base de datos se guarda en un solo fichero .db en tu computadora.
# Esto la hace muy fácil de transportar, copiar o mover junto con tu aplicación.
import sqlite3

# Conectar o crear base de datos, sqlite3.connect() se encarga de crear o encontrar personas.db
conexion = sqlite3.connect('personas.db')
# sqlite3.cursor() proporciona un objeto para ejecutar SQL
cursor = conexion.cursor()

# Crear tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS persona (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        edad INTEGER,
        ciudad TEXT
    )
''')

# Agregar registros
cursor.execute('''
    INSERT INTO persona (nombre, edad, ciudad) VALUES ('Kevin', 23, 'Almería')
''')

# commit() confirma los cambios en la base de datos
conexion.commit()

# Listar registros
cursor.execute('SELECT * FROM persona')
# fetchall() trae devulve los registros que encontró
for row in cursor.fetchall():
    print(row)

# Cerrar conexión
conexion.close()

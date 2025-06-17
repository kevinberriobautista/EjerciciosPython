# Ejercicio 23: CRUD personas mejorado

import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog

# Creo la tabla persona si no existe
def crear_tabla():
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

# Muestra en el widget de texto la lista de personas en la base de datos
def listar_personas(text):
    with sqlite3.connect('personas.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM persona")
        filas = cursor.fetchall()
        text.delete('1.0', tk.END)
        for row in filas:
            text.insert(tk.END, f"ID:{row[0]} | Nombre:{row[1]} | Edad:{row[2]} | Ciudad:{row[3]}\n")

# Agrega una nueva persona solicitando datos al usuario
def agregar_persona():
    nombre = simpledialog.askstring("Agregar", "Ingrese nombre:")
    if not nombre:
        return
    try:
        edad = int(simpledialog.askstring("Agregar", "Ingrese edad:"))
    except (ValueError, TypeError):
        messagebox.showerror("Error", "Edad inválida.")
        return
    ciudad = simpledialog.askstring("Agregar", "Ingrese ciudad:")
    if not ciudad:
        return

    with sqlite3.connect('personas.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO persona (nombre, edad, ciudad) VALUES (?, ?, ?)", (nombre, edad, ciudad))
        conexion.commit()
    messagebox.showinfo("Éxito", "Persona añadida.")

# Elimina a una persona en base a su ID
def eliminar_persona():
    try:
        id_eliminar = int(simpledialog.askstring("Eliminar", "Ingrese ID a eliminar:"))
    except (ValueError, TypeError):
        messagebox.showerror("Error", "ID inválido.")
        return
    
    with sqlite3.connect('personas.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM persona WHERE id = ?", (id_eliminar,))
        conexion.commit()
    messagebox.showinfo("Éxito", "Persona eliminada.")

# Modifica los datos de una persona en base a su ID
def actualizar_persona():
    try:
        id_modificar = int(simpledialog.askstring("Actualizar", "Ingrese ID a modificar:"))
    except (ValueError, TypeError):
        messagebox.showerror("Error", "ID inválido.")
        return
    
    with sqlite3.connect('personas.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, edad, ciudad FROM persona WHERE id = ?", (id_modificar,))
        fila = cursor.fetchone()
        if not fila:
            messagebox.showinfo("Información", "ID no encontrado.")
            return
    
    nombre = simpledialog.askstring("Actualizar", f"Ingrese nuevo nombre [{fila[0]}]:")
    nombre = nombre if nombre and nombre.strip() != '' else fila[0]

    edad_input = simpledialog.askstring("Actualizar", f"Ingrese nueva edad [{fila[1]}]:")
    if edad_input and edad_input.isdigit():
        edad = int(edad_input)
    else:
        edad = fila[1]

    ciudad = simpledialog.askstring("Actualizar", f"Ingrese nueva ciudad [{fila[2]}]:")
    ciudad = ciudad if ciudad and ciudad.strip() != '' else fila[2]

    with sqlite3.connect('personas.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            UPDATE persona SET nombre = ?, edad = ?, ciudad = ? WHERE id = ?
        ''', (nombre, edad, ciudad, id_modificar))
        conexion.commit()
    messagebox.showinfo("Éxito", "Persona actualizada.")

# Busca a una persona por nombre o ciudad
def buscar_persona():
    campo = simpledialog.askstring("Buscar", "Buscar por (nombre/ciudad):")
    if not campo or campo not in ['nombre', 'ciudad']:
        messagebox.showerror("Error", "Valor incorrecto.")
        return
    
    valor = simpledialog.askstring("Buscar", f"Ingrese {campo} a buscar:")
    if not valor:
        return
    
    with sqlite3.connect('personas.db') as conexion:
        cursor = conexion.cursor()
        query = f"SELECT * FROM persona WHERE {campo} LIKE ?"
        cursor.execute(query, ('%' + valor + '%',))
        resultados = cursor.fetchall()

    if resultados:
        texto_resultados = ""
        for row in resultados:
            texto_resultados += f"ID:{row[0]} | Nombre:{row[1]} | Edad:{row[2]} | Ciudad:{row[3]}\n"
        messagebox.showinfo("Resultado de búsqueda", texto_resultados)
    else:
        messagebox.showinfo("Resultado de búsqueda", "Sin resultados.")
    

def main():
    """Función principal que configura GUI."""
    crear_tabla()

    root = tk.Tk()
    root.title("CRUD Personas")

    text = tk.Text(root, height=15, width=50)
    text.pack()

    frame = tk.Frame(root)
    frame.pack()

    btn_listar = tk.Button(frame, text="Listar", command=lambda: listar_personas(text))
    btn_listar.grid(row=0, column=0, padx=5, pady=5)

    btn_agregar = tk.Button(frame, text="Agregar", command=agregar_persona)
    btn_agregar.grid(row=0, column=1, padx=5, pady=5)

    btn_eliminar = tk.Button(frame, text="Eliminar", command=eliminar_persona)
    btn_eliminar.grid(row=0, column=2, padx=5, pady=5)

    btn_actualizar = tk.Button(frame, text="Actualizar", command=actualizar_persona)
    btn_actualizar.grid(row=0, column=3, padx=5, pady=5)

    btn_buscar = tk.Button(frame, text="Buscar", command=buscar_persona)
    btn_buscar.grid(row=0, column=4, padx=5, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()

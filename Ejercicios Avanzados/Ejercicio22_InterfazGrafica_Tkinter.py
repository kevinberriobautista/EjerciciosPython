# Ejercicio 22: Interfaz Gráfica con Tkinter

import sqlite3
import tkinter as tk
# messagebox y simpledialog --> módulos de tkinter para mostrar cuadros de diálogo y mensajes
from tkinter import messagebox, simpledialog

# Crear la tabla si no existe
def crear_tabla():
    with sqlite3.connect('personas.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS persona (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                edad INTEGER,
                ciudad TEXT
            )
        ''')

# Función para listar personas en el Text widget
def listar_personas(text_widget):
    with sqlite3.connect('personas.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM persona")
        filas = cursor.fetchall()
        # text_widget.delete('1.0', tk.END) --> borra todo el texto
        text_widget.delete('1.0', tk.END)
        # Inserta línea por línea la información de cada persona
        for fila in filas:
            text_widget.insert(tk.END, f"ID:{fila[0]} | Nombre:{fila[1]} | Edad:{fila[2]} | Ciudad:{fila[3]}\n")

# -------------------------------------------- Función para agregar persona ---------------------------------------------
def agregar_persona():
    # simpledialog.askstring --> usa cuadros de diálogo para pedir nombre, edad y ciudad
    # Si no escribe nombre o ciudad, cancela
    nombre = simpledialog.askstring("Nombre", "Ingrese nombre:")
    if not nombre:
        return
    try:
        # Pasa la edad a int
        edad = int(simpledialog.askstring("Edad", "Ingrese edad:"))
        # Si no puede convertir la edad a entero, muestra error
    except (ValueError, TypeError):
        messagebox.showerror("Error", "Edad inválida")
        return
    ciudad = simpledialog.askstring("Ciudad", "Ingrese ciudad:")
    if not ciudad:
        return

    # Realiza la conexión con la BBDD y inserta el nuevo usuario
    with sqlite3.connect('personas.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO persona (nombre, edad, ciudad) VALUES (?, ?, ?)", (nombre, edad, ciudad))
        conn.commit()
    messagebox.showinfo("Éxito", "Persona agregada")

# --------------------------------------------- Función para eliminar persona ---------------------------------------------
def eliminar_persona():
    try:
        id_eliminar = int(simpledialog.askstring("Eliminar", "Ingrese ID a eliminar:"))
    except (ValueError, TypeError):
        # Si el id no se puede pasar a int muestra error
        messagebox.showerror("Error", "ID inválido")
        return

    with sqlite3.connect('personas.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM persona WHERE id = ?", (id_eliminar,))
        fila = cursor.fetchone()

        # Compruebo si el usuario existe metiendo su informacion en fila, si esta vacio muestra error, si no, elimina la persona
        if fila is None:
            messagebox.showinfo("Información", "No existe persona con ese ID.")
            return

        cursor.execute("DELETE FROM persona WHERE id = ?", (id_eliminar,))
        conn.commit()
        messagebox.showinfo("Éxito", f"Persona con ID {id_eliminar} eliminada.")

# --------------------------------------------- Función para actualizar persona ---------------------------------------------
def actualizar_persona():
    try:
        id_modificar = int(simpledialog.askstring("Actualizar", "Ingrese ID a modificar:"))
    except (ValueError, TypeError):
        # Si el id no se puede pasar a int muestra error
        messagebox.showerror("Error", "ID inválido")
        return

    # En fila se guarda la información actual de usuario
    with sqlite3.connect('personas.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, edad, ciudad FROM persona WHERE id = ?", (id_modificar,))
        fila = cursor.fetchone()

        if fila is None:
            messagebox.showinfo("Información", "No existe persona con ese ID.")
            return

        # Paso a nombre_actual, edad_actual, ciudad_actual, la informacion de fila
        nombre_actual, edad_actual, ciudad_actual = fila

    # Pedir nuevos datos, con opción a dejar vacío para no cambiar
    messagebox.showinfo("Actualizar", "IMPORTANTE --> Los campos que se dejen en blanco se quedarán como esten.")
    nombre = simpledialog.askstring("Actualizar", f"Ingrese nuevo nombre [{nombre_actual}]:")
    edad_input = simpledialog.askstring("Actualizar", f"Ingrese nueva edad [{edad_actual}]:")
    ciudad = simpledialog.askstring("Actualizar", f"Ingrese nueva ciudad [{ciudad_actual}]:")
    
    # Si dejan vacío, mantienen valores actuales
    nombre = nombre if nombre and nombre.strip() != '' else nombre_actual

    if edad_input and edad_input.strip() != '':
        try:
            edad = int(edad_input)
        except ValueError:
            messagebox.showerror("Error", "Edad inválida, se mantendrá la actual.")
            edad = edad_actual
    else:
        edad = edad_actual

    ciudad = ciudad if ciudad and ciudad.strip() != '' else ciudad_actual

    with sqlite3.connect('personas.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE persona SET nombre = ?, edad = ?, ciudad = ? WHERE id = ?
        ''', (nombre, edad, ciudad, id_modificar))
        conn.commit()

    messagebox.showinfo("Éxito", f"Persona con ID {id_modificar} actualizada.")


# --------------------------------------------- Función para buscar persona ---------------------------------------------
def buscar_persona():
    # Busco por nombre o por ciudad
    campo = simpledialog.askstring("Buscar", "Buscar por (nombre/ciudad):")
    if campo is None:
        return
    campo = campo.strip().lower()
    if campo not in ['nombre', 'ciudad']:
        messagebox.showerror("Error", "Debe ser 'nombre' o 'ciudad'.")
        return

    # Ahora ingreso el nombre o la ciudad por la que quiero filtrar
    valor = simpledialog.askstring("Buscar", f"Ingrese el {campo} a buscar:")
    if valor is None or valor.strip() == '':
        return

    # Meto en resultados los usuarios filtrados
    with sqlite3.connect('personas.db') as conn:
        cursor = conn.cursor()
        query = f"SELECT * FROM persona WHERE {campo} LIKE ?"
        cursor.execute(query, ('%' + valor + '%',))
        resultados = cursor.fetchall()

    # Meto a los usuarios filtrados en texto_resultados para mostrarlos por pantalla
    if resultados:
        texto_resultados = ""
        for row in resultados:
            texto_resultados += f"ID:{row[0]} | Nombre:{row[1]} | Edad:{row[2]} | Ciudad:{row[3]}\n"
        messagebox.showinfo("Resultados de búsqueda", texto_resultados)
    else:
        messagebox.showinfo("Resultados de búsqueda", "No se encontraron resultados.")


# Interfaz principal
def main():
    crear_tabla()

    root = tk.Tk()
    root.title("CRUD Personas")

    # Cuadro de texto
    text = tk.Text(root, height=15, width=50)
    text.pack()

    # Tamaño de la interfaz
    frame = tk.Frame(root)
    frame.pack()

    # Botones
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

    # Ejecuta el loop principal para mostrar la ventana y esperar interacción
    root.mainloop()

if __name__ == "__main__":
    main()

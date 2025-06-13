# Haz un programa que:

# Cree una lista vacía.
# Pida al usuario 3 frutas para agregar a la lista.
# Imprima la lista completa.
# Pregunte si quiere eliminar alguna fruta y la elimine si está.
# Imprima la lista final.

# Creo una lista vacía
frutas = []

# ----------------- ESTO ESTA BIEN, PERO SE PUEDE HACER MÁS PRO ---------------------------

# Pido al usuario 3 frutas para añadir a la lista
# fruta1 = input("Ingresa la primera fruta: ")
# fruta2 = input("Ingresa la segunda fruta: ")
# fruta3 = input("Ingresa la tercera fruta: ")

# Añado las frutas a la lista
# frutas.append(fruta1)
# frutas.append(fruta2)
# frutas.append(fruta3)

# -----------------------------------------------------------------------------------------

# Pido las frutas y las añado con un for
for i in range(3):
    fruta = input("Ingresa una fruta: ")
    frutas.append(fruta)

# Muestro la lista
print("Lista completa: ", frutas)

# Pregunto al usuario si quiero borrar algún elemento
eliminar = input("¿Quieres eliminar alguna fruta? (si/no)")

# Si responde si, busco si esta la fruta escrita, y la borro
if eliminar.lower() == "si": # Pongo el .lower por si el usuario responde con mayusculas
    frutaBorrar = input("¿Que fruta quieres borrar: ? ")
    if frutaBorrar in frutas:
        frutas.remove(frutaBorrar)
        print(f"La fruta {frutaBorrar} se ha eliminado correctamente.")
    else: 
        print(f"La fruta {frutaBorrar} no está en la lista.")
else: 
    print("Okey, la lista se quedará como está.")

# Muestro la lista
print("Lista completa final: ", frutas)
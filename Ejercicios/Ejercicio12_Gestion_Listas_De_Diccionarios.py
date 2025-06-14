# Ejercicio 12: Funciones para gestionar una lista de diccionarios

# Agregar persona a una lista
def agregar_persona(personas, nombre, edad, ciudad):
    personas.append({"nombre": nombre, "edad": edad, "ciudad":ciudad})
    print(f"\nLa persona {nombre} ha sido agregada correctamente.")

# Buscar un persona por nombre en la lista
def buscar_persona(personas, nombre):
    print(f"\nBuscando a {nombre}: ")
    for persona in personas:
        if persona["nombre"] == nombre:
            print(f"\n{nombre} ha sido encontrad@ con exito.")
            return persona
    return None

# Actualizar la ciudad del usuario si existe
def actualizar_ciudad(personas, nombre, nueva_ciudad):
    for persona in personas:
        if persona["nombre"] == nombre:
            persona["ciudad"] = nueva_ciudad
            print(f"\nCiudad de {nombre} actualizada a {nueva_ciudad}.")
            return True
    return False

# Eliminar persona por nombre
def eliminar_persona(personas, nombre):
    for i, persona in enumerate(personas):
        if persona["nombre"] == nombre:
            del personas[i]
            print(f"\n{nombre} ha sido eliminad@ correctamente.")
            return True
    return False

# Mostrar lista
def mostrar_lista(personas):
    print("\nLista completa de personas: ")
    for persona in personas:
        print(persona)

# Uso de las funciones
personas = []

agregar_persona(personas, "Kevin", 23, "Almería")
agregar_persona(personas, "Manolo", 43, "Madrid")
agregar_persona(personas, "Luis", 32, "Cáceres")

mostrar_lista(personas)

buscar_persona(personas, "Kevin")

actualizar_ciudad(personas, "Manolo", "Burgos")

mostrar_lista(personas)

eliminar_persona(personas, "Luis")

mostrar_lista(personas)


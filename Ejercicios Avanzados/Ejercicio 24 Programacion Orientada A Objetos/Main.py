from Persona import Persona
from BaseDeDatos import BaseDeDatos

def menu():
    db = BaseDeDatos()

    while True:
        print("\n--- Menú ---")
        print("1. Listar personas")
        print("2. Agregar persona")
        print("3. Buscar persona")
        print("4. Actualizar persona")
        print("5. Eliminar persona")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            personas = db.listar_personas()
            if personas:
                for persona in personas:
                    print(f"ID: {persona[0]}, Nombre: {persona[1]}, Edad: {persona[2]}, Ciudad: {persona[3]}")
            else:
                print("No hay personas registradas.")

        elif opcion == "2":
            nombre = input("Nombre: ").strip()
            edad = input("Edad: ").strip()
            ciudad = input("Ciudad: ").strip()
            if nombre and edad.isdigit() and ciudad:
                persona = Persona(nombre, int(edad), ciudad)
                db.agregar_persona(persona)
                print(f"{nombre} agregad@ correctamente.")
            else:
                print("Datos inválidos.")

        elif opcion == "3":
            nombre = input("Nombre a buscar (deja vacío si no quieres buscar por nombre): ").strip()
            ciudad = input("Ciudad a buscar (deja vacío si no quieres buscar por ciudad): ").strip()
            resultados = db.buscar_personas(nombre=nombre if nombre else None,
                                            ciudad=ciudad if ciudad else None)
            if resultados:
                for persona in resultados:
                    print(f"ID: {persona[0]}, Nombre: {persona[1]}, Edad: {persona[2]}, Ciudad: {persona[3]}")
            else:
                print("No se encontraron resultados.")

        elif opcion == "4":
            id_str = input("ID de la persona a actualizar: ").strip()
            if not id_str.isdigit():
                print("ID inválido.")
                continue
            id_persona = int(id_str)

            print("Deja en blanco si no quieres modificar ese campo.")
            nombre = input("Nuevo nombre: ").strip()
            edad = input("Nueva edad: ").strip()
            ciudad = input("Nueva ciudad: ").strip()

            nombre = nombre if nombre != "" else None
            edad = int(edad) if edad.isdigit() else None
            ciudad = ciudad if ciudad != "" else None

            db.actualizar_persona(id_persona, nombre, edad, ciudad)
            print("Persona actualizada.")

        elif opcion == "5":
            id_str = input("ID de la persona a eliminar: ").strip()
            if id_str.isdigit():
                db.eliminar_persona(int(id_str))
                print("Persona eliminada.")
            else:
                print("ID inválido.")

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
1

# Ejercicio 6: Listas

# Defino una lista
frutas = ["manzana", "platano", "naranja"]

# Imprimo la lista completa
print("Lista completa: ", frutas)

# Imprimo solo la prima fruta, las listas empiezas en la posición 0
print("La primera fruta es: ", frutas[0])

# Agregar un nuevo elemento
frutas.append("pera")

# Imprimo la lista completa actualizada
print("Lista completa: ", frutas)

#Borro un elemento
frutas.remove("platano") # Tambien se puede hacer por indice con --> del frutas[posicion del elemento que quieor borrar]

# Recorrer la lista con un bucle for
print("Recorriendo la lista con un for: ")
for fruta in frutas:
    print(fruta)

# Buscar un elemento en la lista
if "naranja" in frutas:
    print("La naranja está en la lista.")
else: 
    print("La naranja no está en la lista.")
# Ejercicio 24: Clase Persona

class Persona:
    # Representa a una Persona con nombre, edad y ciudad
    # __init__ --> inicializa los atributos
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
    
    # __str__ --> funciona como el toString()
    def __str__(self):
        # Representa al objeto Persona como texto
        return (f"Nombre: {self.nombre}, Edad: {self.edad}, Ciudad: {self.ciudad}")
    
    # to_tuple --> devulve los datos en forma de tupla, listos para añadirlos a una base de datos
    def to_tuple(self): 
        # Prepara a la Persona para guardarla en la base de datos
        return (self.nombre, self.edad, self.ciudad)
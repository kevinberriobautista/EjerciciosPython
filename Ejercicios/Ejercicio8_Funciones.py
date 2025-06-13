# Ejercicio 8: Funciones

def saludar(nombre): # Esta función saluda a la persona que recibe como argumento
    print(f"Hola, {nombre}")

# Llamo a la funcion
saludar("Kevin")
saludar("Jorge")
saludar("Alex")

def sumar(numero1, numero2):
    return numero1 + numero2 

# Llamo a la funcion
resultado = sumar(5,2)
print("Resultado de la suma: ", resultado)
import csv
import StringHandling
import datetime

datos_lista = [
    ["paco", "42", 3],
    ["agu", "4", 2],
    ["messi", "420", 69]
]

with open("in.csv", "w", encoding="UTF-8", newline="") as archivo:
    writer = csv.writer(archivo, delimiter="|")
    # writer.writeheader()
    writer.writerows(datos_lista)

def saludar(nombre, apellido):
    print(f"Hola, {nombre} {apellido}!")

nombre_de_modulo = "StringHandling"
nombre_de_funcion = "left"
parametros = ["agu", 3]

func = getattr(StringHandling, nombre_de_funcion)
print(func("asdasd", 3))  # 👉️ 'abcd'


# Llamando a la función usando el string y pasando parámetros
"""if nombre_de_funcion in globals() and callable(globals()[nombre_de_funcion]):
    funcion = globals()[nombre_de_funcion]
    if hasattr(funcion, '__call__'):
        funcion(*parametros)
    else:
        print(f"{nombre_de_funcion} no es una función callable.")
else:
    print(f"No se encontró la función {nombre_de_funcion}")"""

def transformar(transformaciones):
    pass


esquema_entrada = ["nombre", "numero", "divisor"]

transformaciones = ["nombre_y_numero", "nombre", "StringHandling", "left"]
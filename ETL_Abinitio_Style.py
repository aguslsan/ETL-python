import csv
import datetime

def saludar(nombre, apellido):
    print(f"Hola, {nombre} {apellido}!")

# Nombre de la función como string
nombre_de_funcion = "saludar"

# Parámetros para la función
parametros = ["agu", "sanchez"]

# Llamando a la función usando el string y pasando parámetros
if nombre_de_funcion in globals() and callable(globals()[nombre_de_funcion]):
    funcion = globals()[nombre_de_funcion]
    if hasattr(funcion, '__call__'):
        funcion(*parametros)
    else:
        print(f"{nombre_de_funcion} no es una función callable.")
else:
    print(f"No se encontró la función {nombre_de_funcion}")

datos_lista = [
    ["paco", "42", 3],
    ["agu", "4", 2],
    ["messi", "420", 69]
]

with open("in.csv", "w", encoding="UTF-8", newline="") as archivo:
    writer = csv.writer(archivo, delimiter="|")
    # writer.writeheader()
    writer.writerows(datos_lista)


esquema_entrada = ["nombre", "numero", "divisor"]

transformaciones = ["nombre_y_numero", "nombre|numero"]
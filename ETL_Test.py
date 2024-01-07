import csv

# Escribir archivo de prueba

datos_lista = [
    ["paco", "42", 3],
    ["agu", "4", 2],
    ["messi", "420", 69]
]

with open("in.csv", "w", encoding="UTF-8", newline="") as archivo:
    writer = csv.writer(archivo, delimiter="|")
    # writer.writeheader()
    writer.writerows(datos_lista)

# Leer archivo y convertirlo en una lista de diccionarios, cada diccionario es un campo con su valor
with open("in.csv", "r", encoding="UTF-8") as archivo:
    reader = csv.reader(archivo, delimiter="|")
    lista_input = []
    for registro in reader:
        lista_input.append({"nombre": registro[0],
                            "numero": registro[1],
                            "divisor": registro[2]})

print(f"lista de input: {lista_input}")

# Hacer transformaciones creando una nueva lista de diccionarios

lista_output = []
for registro in lista_input:
    lista_output.append({"nombre_y_numero": registro.get("nombre")+registro.get("numero"),
                         "divido": float(registro.get("numero"))/float(registro.get("divisor"))})

print(f"lista de output: {lista_output}")

# Escribir lista de diccionarios en un archivo nuevo

with open("out.csv", "w", encoding="UTF-8", newline="") as archivo:
    writer = csv.DictWriter(archivo, fieldnames=lista_output[0].keys(), delimiter="|")
    writer.writeheader()
    writer.writerows(lista_output)

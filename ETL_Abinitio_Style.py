import csv
from builtins import map

import ETL_Abinitio_Stile_COMMON as COMMON
import yaml
import ETL_JOINS




def leer_archivo(archivo_path, campos, delimiter):
    with open(archivo_path, "r", encoding="UTF-8") as archivo:
        reader = csv.reader(archivo, delimiter=delimiter)
        lista_input = []
        for registro in reader:
            if len(registro) == len(campos):
                # Crear un diccionario con los campos y valores correspondientes
                registro_dict = {campo: valor for campo, valor in zip(campos, registro)}
                lista_input.append(registro_dict)
            else:
                print(f"Advertencia: Registro incompleto en línea {reader.line_num}. Ignorando.")

    return lista_input


def escribir_archivo(lista, path, delimitador):
    with open(path, "w", encoding="UTF-8", newline="") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=lista[0].keys(), delimiter=delimitador)
        writer.writeheader()
        writer.writerows(lista)


# ________________________________________________________

"""def load_config(transformations_file):
    with open(transformations_file, 'r') as f:
        transformations = yaml.safe_load(f)
    return transformations


def read_files(transformations):
    for x in transformations["files"]:
        globals()[x["variable_name"]] = leer_archivo(x["file_name"], x["schema"].split("|"), "|")"""


def execute_transformations(transformations):
    output_list = []
    for registro in globals()["main"]:
        output_list.append(transform(registro, transformations))
    return output_list


def transform(registro, transformations):
    output_record = {}
    for mapeo in transformations["mappings"]:
        if mapeo["type"] == "hardcode":
            output_record.update({mapeo["output_field_name"]: mapeo["parameters"]["value"]})

        if mapeo["type"] == "direct":
            output_record.update({mapeo["output_field_name"]: registro[mapeo["parameters"]["input_field_name"]]})

        if mapeo["type"] == "transformation":
            if mapeo["parameters"]["transformation_type"] == "manual":
                output_record.update({mapeo['output_field_name']: mapeo['parameters']['code']})

                exec("output_record.update({mapeo['output_field_name'] : " + mapeo['parameters']['code'] + "})")

    return output_record

# __________________________________________________________


mappings = COMMON.load_config("mappings.yaml")

COMMON.read_files(mappings)

print(globals()["main"])

lista_output = execute_transformations(mappings)

print(lista_output)

escribir_archivo(lista=lista_output, path="out.csv", delimitador="|")

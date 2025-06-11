"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from collections import defaultdict

def cargar_datos(ruta):
    with open(ruta, 'r') as f:
        return [line.strip().split('\t') for line in f.readlines()]
    
# Ruta absoluta 
ruta_archivo = "c:/Users/Alejandra Rojas/Documents/GitHub/LAB-01-python-basico-Aleja7R/files/input/data.csv"

datos = cargar_datos(ruta_archivo)


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    
    valores = defaultdict(list)
    for line in datos:
        letra, valor = line[0], int(line[1])
        valores[letra].append(valor)
    return sorted((letra, max(vals), min(vals)) for letra, vals in valores.items())


if __name__ == "__main__":
    print(pregunta_05())
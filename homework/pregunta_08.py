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

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    mapeo = defaultdict(set)
    for line in datos:
        numero = int(line[1])
        mapeo[numero].add(line[0])
    return sorted((k, sorted(v)) for k, v in mapeo.items())


if __name__ == "__main__":
    print(pregunta_08())
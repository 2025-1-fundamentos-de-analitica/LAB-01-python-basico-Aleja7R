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

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
        
    suma_por_letra = defaultdict(int)
    for line in datos:
        letra = line[0]
        suma = sum(int(par.split(':')[1]) for par in line[4].split(','))
        suma_por_letra[letra] += suma
    return dict(sorted(suma_por_letra.items()))


if __name__ == "__main__":
    print(pregunta_12())
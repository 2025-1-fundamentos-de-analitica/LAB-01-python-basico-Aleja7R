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

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
        
    suma_por_letra = defaultdict(int)
    for line in datos:
        valor = int(line[1])
        letras = line[3].split(',')
        for letra in letras:
            suma_por_letra[letra] += valor
    return dict(sorted(suma_por_letra.items()))

if __name__ == "__main__":
    print(pregunta_11())
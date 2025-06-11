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

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
        
    valores = defaultdict(list)
    for line in datos:
        pares = line[4].split(',')
        for par in pares:
            clave, valor = par.split(':')
            valores[clave].append(int(valor))
    return sorted((clave, min(vs), max(vs)) for clave, vs in valores.items())

if __name__ == "__main__":
    print(pregunta_06())
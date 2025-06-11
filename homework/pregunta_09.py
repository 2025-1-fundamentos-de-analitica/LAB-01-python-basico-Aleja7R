"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from collections import Counter

def cargar_datos(ruta):
    with open(ruta, 'r') as f:
        return [line.strip().split('\t') for line in f.readlines()]
    
# Ruta absoluta 
ruta_archivo = "files/input/data.csv"

datos = cargar_datos(ruta_archivo)

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    
    claves = []
    for line in datos:
        pares = line[4].split(',')
        claves.extend(par.split(':')[0] for par in pares)
    
    #ocurrencias de cada clave
    cuenta_claves = dict(Counter(claves))
    
    #diccionario ordenado 
    orden_claves = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj']
    
    resultado = {clave: cuenta_claves[clave] for clave in orden_claves}
    
    return resultado

if __name__ == "__main__":
    print(pregunta_09())
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def cargar_datos(ruta):
    with open(ruta, 'r') as f:
        return [line.strip().split('\t') for line in f.readlines()]

# Ruta absoluta 
ruta_archivo = "files/input/data.csv"

datos = cargar_datos(ruta_archivo)

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """
    return sum(int(line[1]) for line in datos)

if __name__ == "__main__":
    print(pregunta_01())

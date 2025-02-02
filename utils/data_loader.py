"""
Este módulo se ocupa de realizar la carga de datos para poder posteriormente analizar
datos de los ciclistas articipantes en la Orbea Monegros 2024. Se trata de un paso
imprescindible para responder a las preguntas de todos los ejercicios de la PEC4.
Si esta carga falla, no podrán ejecutarse los scripts de los ejercicios.
"""

import pandas as pd

def load_csv(file_name):
    """
    Carga un archivo CSV desde la carpeta 'data' y lo convierte en un DataFrame de pandas.

    Esta función toma el nombre de un archivo CSV, lo lee desde la carpeta 'data',
    y devuelve su contenido en forma de un DataFrame de pandas. El archivo se lee
    utilizando el separador ';' y la codificación 'utf-8'.

    Args:
        file_name (str): Nombre del archivo CSV (incluyendo extensión) a cargar.

    Returns:
        df (dataframe): El contenido del archivo CSV cargado como un DataFrame de pandas.
    """
    try:
        file_path = f"data/{file_name}"
        df = pd.read_csv(file_path, encoding='utf-8', sep=';', engine='python', header=0)
        return df
        # print(dataframe)
    except FileNotFoundError:
        print(f"Error: El archivo '{file_name}' no se encontró en la carpeta 'data'.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: El archivo '{file_name}' está vacío.")
        return None
    # except Exception as e:
    #     print(f"Se produjo un error inesperado al intentar cargar el archivo: {e}")
    #     return None

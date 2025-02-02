"""
Este módulo contiene funciones para analizar datos de ciclistas participantes
en la Orbea Monegros 2024. Proporciona operaciones para analizar la información
del dataframe. Ayuda a responder a las preguntas del ejercicio 1 de la PEC4.
"""

def ex1(df):
    """
    Muestra y analiza información básica del dataframe de ciclistas participantes en la 
    Orbea Monegros 2024.

    Operaciones:
    0. El dataframe ha sido importando en el script data_loader.py. Este script se puede encontrar
    en la sección "utils". En este ejercicio sólo se importa desde ahí pásandolo como
    parámetro a la función.
    1. Imprime las primeras 5 filas del dataframe.
    2. Calcula y muestra el número de ciclistas únicos, basándose en la columna 'dorsal',
       que participaron en la prueba
    3. Muestra una lista de las columnas presentes en el dataframe.

    Parámetros:
    df: Un dataframe de pandas que contiene los datos de los ciclistas.

    Retorna:
    tuple: Una tupla con tres elementos:
        - df (dataframe): El dataframe modificado.
        - numero_ciclistas_participantes (int): El número de ciclistas únicos según la columna
        'dorsal'.
        - columnas_dataframe (list): Lista de nombres de columnas del dataframe.

    Manejo de errores:
    - KeyError: Se imprime un mensaje de error si falta la columna 'dorsal'.
    - ValueError: Se imprime un mensaje si hay errores de valor en el dataframe.
    - Exception: Sirve para cualquier otro error inesperado e imprime un mensaje genérico.

    """
    print('''\n\n-------------
      MOSTRANDO RESULTADOS DEL EJERCICIO 1
      -------------\n''')
    try:
        # Imprimir las 5 primeras filas del dataset
        print(df.head(5))
        # Contar ciclistas sin tener en cuenta los duplicados
        # Decido contar números de dorsales porque hay bastantes nombres de ciclistas repetidos,
        # lo cual entiendo que es un error de preparación del dataset.
        numero_ciclistas_participantes = df['dorsal'].nunique()
        print(f"En la prueba participaron {numero_ciclistas_participantes} ciclistas.")
        # Mostrar las columnas del dataframe
        columnas_dataframe = list(df.columns)
        print(f"Las columnas que tiene el dataframe son las siguientes: {columnas_dataframe}")
        return df, numero_ciclistas_participantes, columnas_dataframe
    except KeyError as e:
        print(f"Error de clave: {e}")
        return None, None, None
    except ValueError as e:
        print(f"Error de valor: {e}")
        return None, None, None
    # Quito esta exception porque me salta en el linter, aunque yo la hubiera dejado.
    # except Exception as e:
    #     print(f"Error inesperado en la función ex1: {e}")
    #     return None, None, None

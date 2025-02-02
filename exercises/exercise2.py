"""
Este módulo contiene funciones para analizar datos de ciclistas participantes
en la Orbea Monegros 2024. Proporciona operaciones para analizar la información
del dataframe. Ayuda a responder a las preguntas del ejercicio 2 de la PEC4.
"""

def ex2(df):
    """
    Muestra y analiza información básica del dataframe de ciclistas participantes en la 
    Orbea Monegros 2024.

    Operaciones:
    0. Recibe el dataframe anonimizado en el script name_anonimization.py que se encuentra
    en la sección "utils".
    1. Elimina los ciclistas que no participaron en la carrera, identificados por un tiempo
       de '00:00:00'.
    2. Muestra las primeras 5 filas del dataframe después de eliminar las filas correspondientes
       a los ciclistas que no participaron.
    3. Imprime el número total de ciclistas únicos que participaron en la carrera.
    4. Recupera y muestra los datos del ciclista con el dorsal número 1000.
    5. Retorna el dataframe modificado para su uso en posteriores análisis.

    Parámetros:
    df: Un DataFrame de pandas que contiene los datos de los ciclistas, incluyendo 
    las columnas 'time' y 'dorsal'.

    Retorna:
    - El dataframe modificado sin los ciclistas que no participaron (tiempo '00:00:00').

    Manejo de errores:
    - KeyError: Se lanza si las columnas 'time' o 'dorsal' no se encuentran en el dataframe.
    - IndexError: Se lanza si se intenta acceder a índices fuera del rango permitido.
    - TypeError: Se lanza si el dataframe o sus columnas no tienen el tipo de dato esperado.
    """
    print('''\n\n-------------
      MOSTRANDO RESULTADOS DEL EJERCICIO 2
      -------------\n''')
    try:
        # print(f"El tipo de dato de la columna 'time' es: {df['time'].dtype}")
        # Elimino los ciclistas que no participaron en la carrera (tienen tiempos 00:00:00)
        df = df.drop(df[df['time'] == '00:00:00'].index)
        # Muestro los 5 primeras ciclistas del df que ya no tiene ciclistas con tiempos 00:00:00
        print(f"Los 5 primeros ciclistas que sí han participado en la prueba son: {df.head(5)}")
        # Cuántos ciclistas tenemos ahora en el dataset
        print(f"En la prueba participaron {df['dorsal'].nunique()} ciclistas.")
        # Recupero los datos del ciclista con el dorsal=1000
        print(f"El ciclista con el dorsal número 1000 es: {df.loc[df['dorsal']==1000]}")
        # Retorno el df con los nombres de la columna biker "anominizados" o falsificados
        # y sin los ciclistas que no participaron en la carrera para su utilización en el
        # ejecicio 3.
        return df
    except KeyError as e:
        print(f"Error de clave: {e}")
        return None
    except IndexError as e:
        print(f"Error de índice: {e}")
        return None
    except TypeError as e:
        print(f"Error de tipo: {e}")
        return None

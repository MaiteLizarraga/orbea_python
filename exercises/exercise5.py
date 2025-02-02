"""
Este módulo contiene funciones para analizar datos de ciclistas participantes
en la Orbea Monegros 2024. Proporciona operaciones para analizar la información
del dataframe. Ayuda a responder a las preguntas del ejercicio 5 de la PEC4.
"""
def analisis_ucsc(df):
    """
    Realiza un análisis de los ciclistas de la Unió Ciclista Sant Cugat (UCSC), 
    identificando al ciclista con el mejor tiempo y calculando su posición y porcentaje 
    sobre el total de ciclistas.

    Operaciones:
    1. Filtrar los ciclistas que pertenecen al club UCSC.
    2. Ordenar a los ciclistas por tiempo de forma ascendente (mejor tiempo primero).
    3. Mostrar el ciclista con el mejor tiempo y su posición respecto al total de ciclistas.
    4. Calcular el porcentaje que representa la posición del mejor ciclista respecto
    al total de participantes.

    Parámetros:
    df (dataframe): dataframe que contiene la información de los ciclistas, incluyendo
    al menos las columnas 'clean_club' (nombre del club) y 'time' (tiempo del ciclista).

    Excepciones manejadas:
    - KeyError: Si las columnas esperadas no están presentes en el dataframe.
    - IndexError: Si hay un problema al acceder a los índices del dataframe.

    Salida:
    Imprime en consola la información sobre los ciclistas de UCSC, su mejor tiempo,
    posición y porcentaje en relación al total de ciclistas.
    """
    try:
        print('''\n\n-------------
            MOSTRANDO RESULTADOS DEL EJERCICIO 5
            -------------\n''')
        # ¿Cuáles son los ciclistas de la UCSC (Unió Ciclista Sant Cugat)?
        # Los ordeno por tiempos ascendentes (mejor tiempo primero, es decir, tiempo más bajo,
        # primero) de cara al próximo ejercicio
        ciclistas_ucsc = df.loc[df['clean_club'].str.contains('UCSC')]
        ciclistas_ucsc = ciclistas_ucsc.sort_values(by='time', ascending=True)
        print(f"Los ciclistas de la Unió Ciclista de Sant Cugat son: {ciclistas_ucsc}\n")
        # ¿Qué ciclista de la UCSC ha hecho el mejor tiempo?
        mejor_tiempo_ucsc = ciclistas_ucsc.iloc[0]
        print(f"El ciclista de la UCSC que ha hecho el mejor tiempo es: {mejor_tiempo_ucsc}\n")
        # ¿En qué posición sobre el total ha quedado este ciclista,
        # y qué porcentaje sobre el total representa?
        # Posición sobre el total, le añado 1 para que no empiece a contar desde la posición 0
        mejor_tiempo_ucsc_primero_index = (mejor_tiempo_ucsc.name)+1
        # Posición del último ciclista, sumándole 1 ya que hemos empezado a contar
        # desde 1 y no desde 0
        total_index = (df.index)+1
        ultimo_ciclista_index = total_index[-1]
        print(f"El mejor ciclista del UCSC ha quedado en la posición "
                f"{mejor_tiempo_ucsc_primero_index} de {ultimo_ciclista_index}")
        # Qué porcentaje del total representa
        porcentaje_del_total = (mejor_tiempo_ucsc_primero_index * 100)/ultimo_ciclista_index
        print(f"Esta posición representa el porcentaje del "
                f"{round(porcentaje_del_total, 2)}% sobre el total de ciclistas.")
        return ciclistas_ucsc
    except KeyError as e:
        print(f"Error de clave: {e}")
        return None
    except IndexError as e:
        print(f"Error de índice: {e}")
        return None

"""
Este módulo contiene funciones para analizar datos de ciclistas participantes
en la Orbea Monegros 2024. Proporciona operaciones para analizar la información
del dataframe. Ayuda a responder a las preguntas del ejercicio 4 de la PEC4.
"""
import re
def clean_club(df):
    """
    Limpia los nombres de los clubes ciclistas y los guarda en una nueva columna
    llamada "clean_club".

    Esta función realiza varias operaciones de limpieza en la columna "club",
    incluyendo convertir los nombres a mayúsculas, eliminar prefijos comunes
    y aplicar expresiones regulares para eliminar patrones específicos tanto al
    inicio como al final de los nombres de los clubes.
    
    Después de la limpieza, agrupa los datos por la columna 'clean_club' y
    cuenta el número de ciclistas participantes por club, ordenando los resultados
    en orden descendente.

    Operaciones realizadas:
    1. Convierte los nombres de los clubes a mayúsculas.
    2. Elimina ciertos prefijos de los nombres de los clubes.
    3. Limpia espacios en blanco al inicio y al final de los nombres.
    4. Aplica expresiones regulares para eliminar patrones específicos.
    5. Agrupa los datos por la columna 'clean_club' y cuenta los ciclistas por club.

    Parámetros:
    df (dataframe): Un dataframe de pandas que contiene los datos de los ciclistas
    y sus clubes.

    Excepciones manejadas:
    - KeyError: Si las columnas esperadas no están presentes en el dataframe.
    - AttributeError: Si falla una referencia o asignación de atributo.

    Salida:
    Una tupla con dos elementos:
      - df (dataframe): El dataframe original con la columna 'clean_club' añadida.
      - lista_clubes (list): Una lista ordenada del número de ciclistas por club.

    Muestra:
    - Imprime los primeros 15 valores de la columna 'clean_club' después de la limpieza.
    - Imprime la lista de clubes con el número de ciclistas participantes, ordenada
    en orden descendente.
    """
    try:
        print('''\n\n-------------
          MOSTRANDO RESULTADOS DEL EJERCICIO 4
          -------------\n''')
        # Convierto todos los nombres de los clubes a mayúscula
        df['club'] = df['club'].str.upper()
        # print(df['club'].head(3))
        # Reemplozar por nada los siguientes valores
        df['clean_club'] = df['club'].replace(["PEÑA CICLISTA ", "PENYA CICLISTA ",
                                              "AGRUPACIÓN CICLISTA ","AGRUPACION CICLISTA ",
                                              "AGRUPACIÓ CICLISTA ","AGRUPACIO CICLISTA ",
                                              "CLUB CICLISTA ", "CLUB "], 
                                        ["", "", "", "", "", "", "", ""], regex=True)
        # print(df['clean_club'].unique())
        # Quito los espacios vacíos al inicio y al final de la cadena.
        # Esto no se me pide en el enunciado pero creo que es necesario hacerlo
        df['clean_club'] = df['clean_club'].str.strip()
        # Verifico que no haya valores nulos
        # nulos = df['club'].isnull()
        # print(nulos)
        # Creo la regex (regular expression) que va a reemplazar los valores dados en el enunciado
        # en el INICIO de los nombres de los clubes.
        # Tengo en cuenta los espacios en blanco al final de estos valores (\s)
        df['clean_club'] = df['clean_club'].apply(
          lambda x: re.sub(r"^[ACES]\.[CDE]\.\s|^[ACES]\.[CDE]\s|^[ACES][CDE]\s", "", x)
          )
        # print(df['clean_club'])
        # Ahora creo la regex para reemplazar los valores del enunciado en el FINAL
        # de los nombres de los clubes
        df['clean_club'] = df['clean_club'].apply(
          lambda x: re.sub(r"\s[ACT]\.[CDET]\.$|\s[ACT]\.[CDET]$|\s[ACT][CDET]$", "", x)
          )
        print(df['clean_club'].head(15))
        # Aquí decido eliminar los valores sin tener en cuenta el espacio ANTES (elimino \s) aunque
        # no se pide en el enunciado
        df['clean_club'] = df['clean_club'].apply(
          lambda x: re.sub(r"[ACT]\.[CDET]\.$|[ACT]\.[CDET]$|[ACT][CDET]$", "", x)
          )
        print(df['clean_club'].head(15))
        # Ahora ya puedo crear un nuevo dataframe con los datos agrupados a partir de la nueva
        # columna, donde se muestra el número de ciclistas participantes de cada club.
        # El dataframe está ordenado por el número de clubs con más participantes en orden
        # descendente.
        lista_clubes = df.groupby('clean_club')['dorsal'].count().sort_values(ascending=False)
        print(lista_clubes)
        return df, lista_clubes
    except KeyError as e:
        print(f"Error de clave: {e}")
        return None, None
    except AttributeError as e:
        print(f"Error de atributo: {e}")
        return None, None
    
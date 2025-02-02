"""
Este módulo se ocupa de anonimizar los nombres de los ciclistas presentes
en el dataset original. Se trata de un paso crítico para cumplir con las
obligaciones de la LGPD.
"""

from faker import Faker

def name_surname(df):
    """
    Anonimiza los nombres de los ciclistas en el dataframe.

    Esta función reemplaza los nombres reales de los ciclistas por nombres ficticios
    generados aleatoriamente utilizando la librería Faker. El dataframe original
    se modifica con estos nuevos nombres en la columna 'biker', y se muestra una vista
    previa con los primeros 5 registros.

    Args:
        df (dataframe): Un dataframe que contiene información sobre los ciclistas, 
                        incluyendo una columna llamada 'biker' que se actualizará
                        con nombres ficticios.

    Returns:
        dataframe: El dataframe actualizado con los nombres ficticios en la columna 'biker'.

    Excepciones:
        ModuleNotFoundError: Si no se encuentra el módulo necesario para generar
        los nombres ficticios.
        FileNotFoundError: Si el archivo de datos no se encuentra.
    """
    try:
        # Anonimizo los nombres de los corredores
        fake = Faker()
        df['biker'] = [fake.name() for biker in range(len(df))]
        # Muestro los primeros 5 valores del dataframe
        print(df.head(5))
        return df
    except ModuleNotFoundError as e:
        print(f"Módulo no encontrado: {e}")
        return None
    except FileNotFoundError as e:
        print(f"Archivo no encontrado: {e}")
        return None
    # Desactivo esta excepción porque me está dando error en el linter
    # except Exception as e:
    #     print(f"Error al cargar el archivo CSV: {e}")

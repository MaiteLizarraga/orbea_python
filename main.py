"""
Este módulo contiene el flujo principal de ejecución de los ejercicios.
Permite al usuario seleccionar qué ejercicio ejecutar desde un menú y 
realiza las acciones correspondientes.
"""

from datetime import timedelta
import pandas as pd
from utils.data_loader import load_csv
from utils.name_anonimization import name_surname
from exercises.exercise1 import ex1
from exercises.exercise2 import ex2
from exercises.exercise3 import ex3, minutes_002040, histograma_tiempo
from exercises.exercise4 import clean_club
from exercises.exercise5 import analisis_ucsc

def main():
    """
    Función principal que presenta un menú interactivo para que el usuario seleccione
    el ejercicio que desea ejecutar. Dependiendo de la opción seleccionada, se ejecuta el 
    código correspondiente al ejercicio seleccionado y, también, todos los ejercicios previos,
    ya que el dataframe inicial es modificado en cada etapa. Es decir, si se ejecutan los 
    ejercicios de manera aislada e individual sin tener en cuenta los ejercicios previos, el
    dataframe que empleará no será la última versión del mismo. 

    El menú incluye las siguientes opciones:
        - 0: Ejecutar todos los ejercicios.
        - 1: Ejecutar el ejercicio 1.
        - 2: Ejecutar el ejercicio 2.
        - 3: Ejecutar el ejercicio 3.
        - 4: Ejecutar el ejercicio 4.
        - 5: Ejecutar el ejercicio 5.

    En cada ejercicio, se carga un archivo CSV llamado 'dataset.csv' que procede del ejercicio
    anterior, no de la carga inicial mediante el data_loader (a excepción del ejercicio 1 que sí
    carga el dataset inicial). Este dataset, df, es modificado en cada ejercicio, por lo que
    es muy importante cargarlo adecuadamente.

    Si el usuario introduce un número de ejercicio fuera del rango de opciones o si ocurre
    un error durante la ejecución de cualquier ejercicio, se muestra un mensaje de error que
    permite introducir un nuevo número hasta que se seleccione una opción válida.

    Excepciones:
        - FileNotFoundError: Si no se encuentra el archivo 'dataset.csv'.
        - pd.errors.EmptyDataError: Si el archivo 'dataset.csv' está vacío.
        - ValueError: Si ocurre un error en la conversión de los datos.
        - KeyError: Si se hace referencia a una clave inexistente en el dataframe.

    """
    # Empiezo añadiendo un input para poder seleccionar si ejecutamos todo o si
    # seleccionamos un ejercicio concreto a ejecutar:
    print('''Seleccione el ejercicio que desea ejecutar:
            0: Ejecutar todos los ejercicios
            1: Ejercicio 1
            2: Ejercicio 2
            3: Ejercicio 3
            4: Ejercicio 4
            5: Ejercicio 5
            ''')
    while True:
        try:
            ejercicio_seleccionado = int(input("Ingrese el número del ejercicio: "))
            print("Introduzca un número de 1 a 5")
            df = load_csv('dataset.csv')
            if df is not None:
                df, _, _ = ex1(df)
                df = name_surname(df)
                if ejercicio_seleccionado == 1:
                    break
            if df is not None:
                df = ex2(df)
                if ejercicio_seleccionado == 2:
                    break
            if df is not None:
                df = ex3(df)
                df = minutes_002040(df, delta=timedelta(minutes=20))
                histograma_tiempo(df)
                if ejercicio_seleccionado == 3:
                    break
            if df is not None:
                df, _ = clean_club(df)
                if ejercicio_seleccionado == 4:
                    break
            if df is not None:
                analisis_ucsc(df)
                if ejercicio_seleccionado == 5:
                    break
            if ejercicio_seleccionado == 0:
                break
        except FileNotFoundError as e:
            print(f"Error: El archivo 'dataset.csv' no se encontró. {e}")
        except pd.errors.EmptyDataError as e:
            print(f"Error: El archivo 'dataset.csv' está vacío. {e}")
        except ValueError as e:
            print(f"Error en los datos: {e}")
        except KeyError as e:
            print(f"Error de clave: {e}")

if __name__ == "__main__":
    main()

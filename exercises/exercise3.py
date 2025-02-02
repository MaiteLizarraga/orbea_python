"""
Este módulo contiene funciones para analizar datos de ciclistas participantes
en la Orbea Monegros 2024. Proporciona operaciones para analizar la información
del dataframe. Ayuda a responder a las preguntas del ejercicio 3 de la PEC4.
"""
# Aquí no he puesto bloques try-except porque se me hacía muy largo.
from datetime import datetime, timedelta
import seaborn as sns
import matplotlib.pyplot as plt
def ex3(df):
    """
    Convierte la columna 'time' en un objeto de tiempo (datetime.time).

    Esta función realiza las siguientes operaciones:
    1. Elimina espacios en blanco adicionales de los valores en la columna 'time'.
    2. Convierte los valores de la columna 'time', que están en formato de cadena,
       a objetos de tipo 'datetime.time' utilizando el formato '%H:%M:%S'.

    Parámetros:
    df (dataframe): Un dataframe de pandas que contiene una columna 'time' con
    tiempos en formato de cadena.

    Retorna:
    dataframe: El dataframe modificado con la columna 'time' convertida a objetos
    'datetime.time'.
    """
    print('''\n\n-------------
      MOSTRANDO RESULTADOS DEL EJERCICIO 3
      -------------\n''')
    # Primero elimino posibles espacios extraños en los valores de 'time'
    df['time'] = df['time'].str.strip()
    # Sé desde el ejercicio 2 que el tiempo es de tipo object.
    # Para poder dividir el tiempo en franjas de 20 minutos, necesito convertirlo en datetime.
    time_format = '%H:%M:%S'
    # Para ello utilizo la función strptime, pasandole dos formatos, la hora en formato string
    # y la máscara para el formato que quiero que tenga ese string cuando se convierta en time
    df['time'] = [datetime.strptime(str_date, time_format).time() for str_date in df['time']]
    # print(df['time'].dtype)
    return df
# Creo la función que se me dice en el enunciado. Le paso el dataframe y el delta de tiempo
# que quiero que en este caso es de 20 minutos.
def minutes_002040(df, delta = timedelta(minutes=20)):
    """
    Contiene una función interior que redondea los tiempos al intervalo de 20 minutos más cercano
    (a la baja) y agrupa a los ciclistas según estos intervalos.

    Esta función realiza las siguientes operaciones:
    1. Redondea los tiempos en la columna 'time' del dataframe a intervalos de 20 minutos hacia
    abajo.
    2. Crea una nueva columna 'time_grouped' que contiene los tiempos redondeados.
    3. Muestra las primeras 15 filas del dataframe modificado.
    4. Agrupa los ciclistas por los tiempos redondeados y muestra el número de ciclistas en
    cada intervalo.

    Parámetros:
    df (dataframe): Un dataframe de pandas que contiene una columna 'time' con los tiempos de
    los ciclistas.
    delta (timedelta): Intervalo de tiempo para el redondeo. En este caso es de 20 minutos.

    Retorna:
    dataframe: El dataframe original modificado, con una nueva columna 'time_grouped' que contiene
    los tiempos redondeados a la franja de 20 minutos inferior más cercana.
    """
    def rounded_time(time):
        """
        Redondea un objeto de tiempo a la franja de tiempo más cercana en intervalos de 20 minutos.

        Esta función toma un objeto de tiempo y lo redondea hacia abajo al múltiplo más cercano
        de 20 minutos. Convierte el tiempo proporcionado en segundos totales, calcula la diferencia
        de segundos respecto al múltiplo de 20 minutos más cercano a la baja y retorna el tiempo
        redondeado en formato de horas y minutos (sin tener en cuenta los segundos).

        Parámetros:
        time (datetime.time): Un objeto de tiempo que representa la hora que se desea redondear.

        Retorna:
        str: Una cadena que representa el tiempo redondeado el intervalo de 20 minutos más cercano
        por abajo en formato 'HH:MM'.

        Otra información:
        - La función asume que `delta` es una variable global de tipo `timedelta`, configurada para 
        20 minutos (es decir, `delta = timedelta(minutes=20)`).
        """
        # Convierto todo el time que he convertido previamente del string a segundos
        total_segundos = time.hour * 3600 + time.minute * 60 + time.second
        # print(type(total_segundos))
        # Calculo los segundos del delta. Como le he pasado que delta sean 20 minutos
        # me dará un total de 1200 segundos. Estos son los segundos cuya diferencia con
        # los segundos reales utilizaré para realizar el redondeo.
        # total_seconds es una función de Timedelta que devuelve el número total de
        # segundos que contiene la duración
        delta_segundos = delta.total_seconds()
        # print(delta_segundos)
        # Ahora calculo la diferencia de segundos entre los segundos de cada tiempo
        # de cada ciclista y el módulo (o resto) del tiempo "redondeado". Es decir,
        # calculo el resto de dividir el total de segundos de cada ciclista por los
        # segundos que hay en 20 minutos, y, lo que sobra, se lo resto al total de
        # segundos para tener unos segundos múltiplos de los 20 minutos.
        diferencia_segundos = total_segundos - (total_segundos % delta_segundos)
        # print(diferencia_segundos)
        # Reconvierto los segundos a un timedelta que me da horas, minutos y segundos.
        # Ahora ya me salen por franjas de 20 en 20 minutos.
        diferencia_tiempo = timedelta(seconds=diferencia_segundos)
        # print(diferencia_tiempo)
        # Con esta diferencia de tiempo, retorno la nueva hora pero sin quitando los
        # segundos como se me pide en el enunciado. Sólo horas y minutos redondeados.
        # print((datetime.min + diferencia_tiempo).time().strftime('%H:%M'))
        # print(type((datetime.min + diferencia_tiempo).time().strftime('%H:%M')))
        return (datetime.min + diferencia_tiempo).time().strftime('%H:%M')
    # Aplico la función a cada tiempo en la columna "time" y almaceno el resultado en
    # una nueva columna llamada "time_grouped"
    df['time_grouped'] = df['time'].apply(rounded_time)
    print(f"A continuación muestro los 15 primeros valores del dataframe:\n{df.head(15)}")
    # En el enunciado se nos dice que agrupemos a los ciclistas según las horas redondeadas
    # aunque he visto que en mi caso no sería necesario ya que pasándole "time_grouped" a
    # Seaborn dibuja el histograma perfectamente. No utilizo esta parte del código.
    grouped = df.groupby('time_grouped').size().reset_index(name='num_ciclistas')
    print(f"\n\nA continuación muestro los valores del dataframe agrupado:\n{grouped}")
    return df
# Creo una nueva función para realizar el histograma.
# He decidido no mostrarlo por pantalla y guardarlo directamente en el directorio img.
def histograma_tiempo(df):
    """
    Crea y guarda un histograma de la columna 'time_grouped' del dataframe.

    Operaciones:
    1. Crea un histograma utilizando Seaborn para visualizar la distribución de la 
    columna 'time_grouped'.
    2. Guarda el histograma como una imagen en el path: '../pec4/img/histograma_ejercicio3.png'
    4. Cierra el plot para evitar conflictos con otros gráficos que puedan generarse 
    posteriormente.

    Parámetros:
    df (dataframe): Un DataFrame de pandas que contiene una columna 'time_grouped' con
    los tiempos agrupados.
    """
    # Realizo el histograma
    sns.histplot(data=df, x="time_grouped")
    # Cambio la orientación de las etiquetas del eje x para que se vean mejor
    plt.xticks(rotation='vertical')
    # Guardo la imagen en un nuevo directorio llamado img
    # Para ello no utilizo ningúna librería específica, aunque he visto que existen
    # Me decanto por usar la función savefig de matplolib
    path = '../pec4/img/histograma.png'
    plt.savefig(path)
    # Cierro el plot para que se sigan ejecutando el resto de ejercicios
    plt.close()

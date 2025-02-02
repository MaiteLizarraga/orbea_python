"""
Este módulo contiene los tests de las funciones del ejercicio 5 de la PEC4.
"""

import unittest
from utils import load_csv
from exercises.exercise1 import ex1
from exercises.exercise2 import ex2
from exercises.exercise3 import ex3, minutes_002040
from exercises.exercise4 import clean_club
from exercises.exercise5 import analisis_ucsc
# from exercises.exercise5 import analisis_ucsc
class TestEx5(unittest.TestCase):
    # Voy a verificar sólo que lo que recibe la función es un dataframe que no está vacío
    """
    Clase de pruebas para el ejercicio 5 de la PEC4.

    Esta clase contiene los tests para verificar el correcto funcionamiento
    de las funciones definidas en el ejercicio 5.

    Métodos:
    - setUpClass(cls): Carga y prepara el dataframe para ejecutar las pruebas.
    - test_ucsc_cyclists_filtered(self): verifica que existen ciclistas que pertenecen
    al club UCSC.
    - test_mejor_tiempo_ucsc(self): comprueba que el ciclista de UCSC con el mejor
    tiempo aparece el primero en la lista.
    """
    @classmethod
    def setUpClass(cls):
        """
        Método que asegura que el dataframe esté listo para las pruebas,
        realizando las modificaciones necesarias antes de ejecutar los casos de prueba.

        Operaciones:
        Carga el archivo 'dataset.csv' y:
        - Se aplican las funciones 'ex1', 'ex2' y 'ex3', modificando el DataFrame en cada paso.
        - Se realiza una transformación adicional con 'minutes_002040', otra transformación
        con 'clean_club' y una última con analisis_ucsc.
        
        Parámetros:
        cls (class): La clase del método.

        Salida:
        Ninguna. Modifica el atributo de clase 'cls._df' para ser utilizado en las pruebas.
        """
        cls._df = load_csv('dataset.csv')
        cls._df, _, _ = ex1(cls._df)  # Después de ex1, el df está modificado
        cls._df = ex2(cls._df)  # Después de ex2, el df está modificado
        cls._df = ex3(cls._df)  # Después de ex2, el df está modificado (probablemente haya
                                # una mejor manera de hacer esto pero no la he encontrado)
        cls._df = minutes_002040(cls._df) # Sigo actualizando el df de esta manera.
        cls._df, _ = clean_club(cls._df)
    def test_ucsc_cyclists_filtered(self):
        """
        Este test verifica que existen ciclistas que pertenecen al club UCSC.
        """
        df_ciclistas = analisis_ucsc(self._df)
        self.assertGreater(
            len(df_ciclistas), 0,
            "Se han filtrado correctamente los ciclistas de UCSC."
            )
    def test_mejor_tiempo_ucsc(self):
        """
        Este test comprueba que el ciclista de UCSC con el mejor tiempo
        aparece el primero en la lista.
        """
        df_ciclistas = analisis_ucsc(self._df)
        mejor_tiempo = df_ciclistas.iloc[0]['time']
        self.assertEqual(
            mejor_tiempo, df_ciclistas['time'].min(),
            "El mejor tiempo de UCSC es identificado correctamente."
            )

if __name__ == '__main__':
    unittest.main()
    
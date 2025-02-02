"""
Este módulo contiene los tests de las funciones del ejercicio 2 de la PEC4.
"""

import unittest
from utils import load_csv
from exercises.exercise1 import ex1
from exercises.exercise2 import ex2

class TestEx2(unittest.TestCase):
    """
    Clase de pruebas para el ejercicio 2 de la PEC4.

    Esta clase contiene los tests para verificar el correcto funcionamiento
    de las funciones definidas en el ejercicio 2.

    Métodos:
    - setUpClass(cls): Carga y prepara el dataframe para ejecutar las pruebas.
    - test_zero_times(self): Verifica que no haya registros con el tiempo
    '00:00:00' después de aplicar la función ex2.
    - test_unique_dorsal(self): Verifica que no haya dorsales duplicados
    en el dataset.
    - test_more_than_1000_cyclists(self): Verifica que el dataset contenga
    más de 1000 ciclistas.
    """
    @classmethod
    def setUpClass(cls):
        """
        Método que asegura que el dataframe esté listo para las pruebas,
        realizando las modificaciones necesarias antes de ejecutar los casos de prueba.
        Carga el archivo 'dataset.csv' y se aplica la función 'ex1' que modifica
        el dataframe.
        
        Parámetros:
        cls (class): La clase del método.

        Salida:
        Ninguna. Modifica el atributo de clase 'cls._df' para ser utilizado en las pruebas.
        """
        cls._df = load_csv('dataset.csv')
        cls._df, _, _ = ex1(cls._df)  # Después de ex1, el df está modificado
    # Verifico que no hay tiempos en 00:00:00 a la salida de esta función.
    def test_zero_times(self):
        """
        Verifica que no haya tiempos en '00:00:00' después de aplicar la función ex2.

        Llama a la función 'ex2' sobre el DataFrame modificado y comprueba que no haya valores 
        de tiempo iguales a '00:00:00' en la columna 'time'. Si se encuentra algún valor 
        igual a '00:00:00', el test falla.

        Salida:
        Ninguna. Si el test falla, lanza una excepción.
        """
        df = ex2(self._df)
        zero_times = (df['time'] == "00:00:00").any()
        self.assertFalse(zero_times, "Todavía hay tiempos en '00:00:00' después de ejecutar ex2.")
    # Ahora verifico que no hay dorsales duplicados, lo cual significaría
    # que hay ciclistas duplicados.
    def test_unique_dorsal(self):
        """
        Verifica que todos los dorsales en el dataframe son únicos.

        Llama a la función 'ex2' sobre el dataframe modificado y comprueba
        que no haya dorsales duplicados.
        Si encuentra dorsales repetidos, el test falla.

        Salida:
        Ninguna. Si el test falla, lanza una excepción.
        """
        df = ex2(self._df)
        unique_dorsals = (df['dorsal'].unique()).any()
        self.assertTrue(unique_dorsals, "Existen dorsales duplicados.")
    # Por último, verifico que hay más de 1000 ciclistas en el dataset.
    def test_more_than_1000_cyclists(self):
        """
        Verifica que el dataset contiene más de 1000 ciclistas.

        Llama a la función 'ex2' sobre el DataFrame modificado y comprueba que el número de
        ciclistas, es decir, el número de registros en la columna 'dorsal', sea superior a 1000.

        Salida:
        Ninguna. Si el test falla, lanza una excepción.
        """
        df=ex2(self._df)
        self.assertTrue(df['dorsal'].count() > 1000, "Hay más de 1000 ciclistas en el Dataset.")
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestEx2))
    unittest.TextTestRunner(verbosity=2).run(suite)

"""
Este módulo contiene los tests de las funciones del ejercicio 3 de la PEC4.
"""

import unittest
import os
from utils import load_csv
from exercises.exercise1 import ex1
from exercises.exercise2 import ex2
from exercises.exercise3 import ex3, minutes_002040

class TestEx3(unittest.TestCase):
    """
    Clase de pruebas para el ejercicio 3 de la PEC4.

    Esta clase contiene los tests para verificar el correcto funcionamiento
    de las funciones definidas en el ejercicio 3.

    Métodos:
    - setUpClass(cls): Carga y prepara el dataframe para ejecutar las pruebas.
    - test_input_time_format(self): Verifica que la columna 'time' sea de tipo string.
    - test_minutes_002040_output(self): Verifica que se haya añadido una nueva
    columna llamada 'time_grouped' al DataFrame.
    - test_time_grouped_column_type(self): Verifica que el gráfico generado se
    guarde correctamente en el directorio especificado.
    """
    @classmethod
    def setUpClass(cls):
        """
        Método que asegura que el dataframe esté listo para las pruebas,
        realizando las modificaciones necesarias antes de ejecutar los casos de prueba.

        Carga el archivo 'dataset.csv' y:
        - Se aplican las funciones 'ex1', 'ex2', 'ex3' y minutes_002040,
        modificando el DataFrame en cada paso.
        
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
        cls._df = minutes_002040(cls._df)
    # Verifico que el tiempo input es de tipo string (object)
    def test_input_time_format(self):
        """
        Verifica que la columna 'time' del DataFrame es de tipo string (object).

        Llama al DataFrame modificado y comprueba el tipo de datos de la columna 'time'.
        Verifica que sea de tipo `object`, que corresponde a los datos de tipo string en pandas.

        Salida:
        Ninguna. Si el test falla, lanza una excepción.
        """
        input_time_format = self._df['time'].dtype
        self.assertIsInstance(
            input_time_format, object, "El input time es de tipo string"
            )
    # Ahora verifico que el df incluye una nueva columna llamada time_grouped.
    def test_minutes_002040_output(self):
        """
        Verifica que el DataFrame incluye una nueva columna llamada 'time_grouped'.

        Llama al DataFrame modificado y valida que la columna 'time_grouped' esté presente,
        asegurándose de que la función 'minutes_002040' haya añadido correctamente esta columna.

        Salida:
        Ninguna. Si el test falla, lanza una excepción.
        """
        total_columns = self._df.columns.tolist()
        self.assertEqual(
            total_columns,
            ['dorsal','biker','club','time', 'time_grouped'],
            "El dataframe incluye la nueva columna time_grouped."
            )
    def test_time_grouped_column_type(self):
        """
        Verifica que el gráfico generado se guarda correctamente en el directorio especificado.

        Llama a la función que genera el gráfico y valida que el archivo de imagen se haya 
        guardado correctamente en el directorio 'img' con el nombre 'histograma_ejercicio3.png'.

        Salida:
        Ninguna. Si el test falla, lanza una excepción.
        """
        # Para terminar compruebo que el gráfico se ha generado correctamente.
        path_of_histogram = "img/histograma.png"
        self.assertTrue(
            os.path.exists(path_of_histogram),
            "El gráfico se está guardando correctamente en su path."
            )

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestEx3))
    unittest.TextTestRunner(verbosity=2).run(suite)

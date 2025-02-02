"""
Este módulo contiene los tests de las funciones del ejercicio 1 de la PEC4.
"""

import unittest
from utils import load_csv
from exercises.exercise1 import ex1

class TestEx1(unittest.TestCase):
    """
    Clase de pruebas para el ejercicio 1 de la PEC4.

    Esta clase contiene los tests para verificar el correcto funcionamiento
    de las funciones definidas en el ejercicio 1.

    Métodos:
    - setUpClass(cls): Carga y prepara el dataframe para ejecutar las pruebas.
    - test_cyclist_count_int(self): Verifica que el conteo de ciclistas es 
    un número entero positivo.
    - test_dataset_column_number(self): Verifica que el dataframe tiene
    el número y el orden correcto de columnas.
    """
    @classmethod
    def setUpClass(cls):
        """
        Método que asegura que el dataframe esté listo para las pruebas,
        realizando las modificaciones necesarias antes de ejecutar los casos de prueba.
        Carga el archivo 'dataset.csv'.
        
        Parámetros:
        cls (class): La clase del método.

        Salida:
        Ninguna. Modifica el atributo de clase 'cls._df' para ser utilizado en las pruebas.
        """
        cls._df = load_csv('dataset.csv')
    # Sí que voy a hacer un test que verifique que el conteo de ciclistas devuelve
    # un integer positivo
    def test_cyclist_count_int(self):
        """
        Verifica que el conteo de ciclistas participantes sea un número entero positivo.

        Llama a la función 'ex1' para obtener el número de ciclistas y comprueba que:
        1. El valor sea de tipo entero.
        2. El valor sea mayor que 0, es decir, positivo.

        Salida:
        Ninguna. La función ejecuta codigo que valida el tipo y valor del conteo de ciclistas.
        Si algún test falla se lanza una excepción.
        """
        # Llamo a la función ex1 pero sólo me interesa el número de ciclistas
        _, numero_ciclistas_participantes, _ = ex1(self._df)
        # Verifico que se trata de un número y no de un string u otro tipo de dato
        self.assertIsInstance(
            numero_ciclistas_participantes, int, "El conteo de ciclistas no es un número entero"
            )
        # Verifico que es mayor de 0, es decir, un número positivo
        self.assertGreater(
            numero_ciclistas_participantes, 0, "El conteo de ciclistas no es positivo"
            )
    # Ahora hago otro test para verificar que el dataset que le paso tiene 4 columnas
    # y no más ni menos
    def test_dataset_column_number(self):
        """
        Verifica que el dataframe tenga el número y el orden de columnas esperados.

        Llama a la función 'ex1' para obtener las columnas del dataframe y valida que
        el número de columnas y el orden coincidan con los esperados:
        ['dorsal', 'biker', 'club', 'time'].

        Salida:
        Ninguna. La función valida el número y el orden de las columnas.
        Si el test falla se lanza una excepción.
        """
        # De la función ex1 sólo me interesa el número de columnas
        _, _, columnas_dataframe = ex1(self._df)
        # Verifico que las columnas del dataset son lo que se espera en cuanto a su
        # número y orden de aparición
        self.assertEqual(
            columnas_dataframe,
            ['dorsal','biker','club','time'],
            "El dataframe las columnas adecuadas en el orden adecuado"
            )
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestEx1))
    unittest.TextTestRunner(verbosity=2).run(suite)

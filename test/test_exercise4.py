"""
Este módulo contiene los tests de las funciones del ejercicio 4 de la PEC4.
"""

import unittest
from utils import load_csv
from exercises.exercise1 import ex1
from exercises.exercise2 import ex2
from exercises.exercise3 import ex3, minutes_002040
from exercises.exercise4 import clean_club

class TestEx4(unittest.TestCase):
    """
    Clase de pruebas para el ejercicio 4 de la PEC4.

    Esta clase contiene los tests para verificar el correcto funcionamiento
    de las funciones definidas en el ejercicio 4.

    Métodos:
    - setUpClass(cls): Carga y prepara el dataframe para ejecutar las pruebas.
    - test_check_regex_application(self): Verifica que los patrones de expresión
    regular no coinciden con los datos.
    - test_check_decreasing_order(self): Verifica que los clubes están
    ordenados de manera descendente por el número de ciclistas.
    """
    @classmethod
    def setUpClass(cls):
        """
        Método que asegura que el dataframe esté listo para las pruebas,
        realizando las modificaciones necesarias antes de ejecutar los casos de prueba.

        Carga el archivo 'dataset.csv' y:
        - Se aplican las funciones 'ex1', 'ex2', 'ex3', 'minutes_002040 y clean_club
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
        cls._df, _ = clean_club(cls._df)
    # Verifico que los patrones de expresión regular se están aplicando correctamente
    def test_check_regex_application(self):
        """
        Verifica que los patrones de expresión regular no coincidan con los valores
        en la columna 'clean_club'.

        Se definen tres expresiones regulares y se verifica que no haya ningún valor
        en la columna 'clean_club' que coincida con estos patrones. Si algún valor
        coincide, se lanza una excepción.

        Salida:
        Ninguna. Si el test falla, lanza una excepción.
        """
        regex_1 = r"^[ACES]\.[CDE]\.\s|^[ACES]\.[CDE]\s|^[ACES][CDE]\s"
        regex_2 = r"\s[ACT]\.[CDET]\.$|\s[ACT]\.[CDET]$|\s[ACT][CDET]$"
        regex_3 = r"[ACT]\.[CDET]\.$|[ACT]\.[CDET]$|[ACT][CDET]$"
        matching_values = self._df['clean_club'].str.match(f"({regex_1}|{regex_2}|{regex_3})")
        self.assertFalse(
            matching_values.any(),
            "No se encuentran en el documento valores con los patrones dados."
            )
    # Y ahora chequeo que los datos del datagrame agrupado se muestran ordenados
    # descendentemente por número de ciclistas pertenencientes a cada club.
    def test_check_decreasing_order(self):
        """
        Verifica que los clubes en el DataFrame están ordenados de manera
        descendente por el número de ciclistas.

        Salida:
        Ninguna. Si el test falla, lanza una excepción.
        """
        _, lista_clubes = clean_club(self._df)
        self.assertTrue(
            (lista_clubes.reset_index(drop=True) ==
             lista_clubes.sort_values(ascending=False).reset_index(drop=True)).all,
            "El resultado está bien ordenado descendentemente, de mayor a menor."
            )

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestEx4))
    unittest.TextTestRunner(verbosity=2).run(suite)

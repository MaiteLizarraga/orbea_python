# Orbea Monegros 2024

## Descripción del proyecto

La Orbea Monegros es una prueba de ciclismo de montaña (BTT) no competitiva que se realiza en Sariñena (Huesca). Mediante este proyecto realizaremos un análisis en profundidad de los datos más relevantes extraídos de esta prueba.

* https://www.orbea.com/es-es/eventos/monegros-2024
* https://sportmaniacs.com/es/races/orbea-monegros-2024/662d72e2-07c8-4360-be3d-4072ac1f171c/results#rankings

<br>

## Componentes clave del proyecto

Los componentes principales del proyecto son:

### Directorios:
* **data:** contiene el dataset que constituye la fuente de los datos.

* **exercises:** contiene los scripts de los ejercicios.
    - Cada archivo representa un ejercicio y contiene las funciones específicas requeridas.
    - Las funciones deben estar bien documentadas con docstrings que expliquen los parámetros, el retorno y ejemplos de uso.

* **img:** contiene el png del histograma que se genera en el ejercicio 3.

* **test:** contiene los scripts de test de los ejercicios.
    - Los tests verifican que las funciones de cada ejercicio funcionan correctamente.
    - Usa un marco de pruebas unittest.
    - Los nombres de los archivos de prueba corresponden a los módulos de los ejercicios.

* **utils:** contiene funciones genéricas reutilizables, en ese caso para la carga de datos y para la anonimización de nombres. Sirven para responder parcialmente algunas de las preguntas de los ejercicios.

* **egg-info:** es un directorio situado junto al código y los recursos del proyecto que contiene los metadatos del proyecto. Se genera automáticamente cuando se ejecuta el script setup.py

### Archivos sueltos en el directorio principal:

* **License.txt:** MIT License que he copiado de mi Github.

* **main.py:** cuadro de mandos de la lógica de todo el proyecto. Desde aquí se ejecuta el proyecto. Este archivo:
    - Importa las funciones de los módulos de cada ejercicio.
    - Ejecuta todas las funciones de manera secuencial y mostrar los resultados.
    - Permite la ejecución individual de cada función mediante argumentos en la línea de comandos o un menú interactivo.

* **README.md:** archivo markdown donde se describe el proyecto, su organización y funcionamiento.

* **requirements.txt:** archivo de dependencias del proyecto, es decir, las librerías o paquetes que el proyecto necesita para funcionar correctamente.

* **setup.py:** archivo que sirve para configurar y gestionar la instalación y la distribución del paquete o aplicación de Python. En este caso, este fichero incluye e instala requirements.txt.

<br>

> **✨NOTA**  
> A lo largo de la ejecución de los diferentes comandos del proyecto, se irán generando otros directorios y archivos de metadatos y de caché que no se han listado en este apartado.

<br>

# Pasos para ejecutar el proyecto:

<br>

## PASO 1: Creación de un entorno virtual

Se recomienda ejecutar este programa en un entorno virtual. Para crear uno, lo más sencillo es:

### ➡ En Linux y Mac (bash y zsh):

Llamar a virtualenv con, como único argumento, el nombre del directorio donde queremos crear el entorno virtual:

    $ virtualenv venv

Esto creará una carpeta (en este caso, de nombre venv), que contendrá un archivo de configuración
y dos subcarpetas (bin y lib), que contendrán copias de la versión de Python que utilizará el
entorno, ficheros de interacción con el entorno, enlaces simbólicos a ciertos ficheros necesarios,
así como los ficheros que nos permitirán activar y desactivar el entorno (y que presentaremos a
continuación).

* Para crear el entorno virtual en Bash:

    python3 -m venv /path/to/new/virtual/environment

* Una vez creado el entorno virtual, hay que activarlo para poder usarlo. Para ello, ejecutamos:

    $ source venv/bin/activate

* A partir de este momento, nos encontraremos dentro del entorno virtual:

    (venv) nombre_usuario@nombre_del_pc:~$

### ➡ En Windows (CMD y PowerShell):

Para crear el entorno virtual:

    python -m venv C:\path\to\new\virtual\environment

Para activarlo en Windows:

> #### CMD:
    C:\> <venv>\Scripts\activate.bat

> #### PowerShell:
    PS C:\> <venv>\Scripts\Activate.ps1

<br>

## PASO 2: Instalación del package

Este programa se ha creado como paquete (package). Su configuración se encuentra en el script setup.py. Se puede instalar mediante los comandos:

> #### Bash/Zsh:
    pip install -e .

> #### Windows (mismo comando):
    pip install -e .

Esta instalación instalará todo lo contenido en el archivo setup.py incluido en el programa.

<br>

## PASO 3: Instalación de los requerimientos

Este programa se puede ejecutar con el IDE de elección del usuario.  
Si se ha instalado el package (paquete) tal y como se especifica en el paso anterior (Paso 2), no será necesario volver a instalar los requerimientos manualmente.  
No obstante, este comando puede ser de utilidad si, a lo largo del desarrollo del proyecto, se necesita actualizar la lista de requerimientos o si se quiere cambiar la versión de alguno de los módulos instalados.

> #### Bash/Zsh o Windows (mismo comando para todos los sistemas operativos):
    pip install -r requirements.txt

<br>

## PASO 4: Instrucciones para ejecutar el código:

Para ejecutar el programa completo o cada ejercicio por separado, se debe ejecutar el siguiente comando. Este comando abrirá un menú interactivo en el que el usuario podrá seleccionar el número de ejercicio que desea ejecutar o el cero (0) si desea ejecutar todos los ejercicios.
    el ejercicio que desea ejecutar.

> #### Bash/ZsH: 
    python3 main.py

> #### Windows: 
    python main.py

> **💡 TIP**  
> Tras la ejecución del comando, la consola muestra un prompt donde se pide al usuario que introduzca el número de ejercicio que quiere consultar.   
> Si introduce el 0 (cero), se ejecutará el programa entero.

> **✨NOTA**  
> Al introducir un número de ejercicio, también se ejecutan los ejercicios anteriores al ejercicio seleccionado para trabajar siempre con el dataframe más actual.

## PASO 4-B: Instrucciones para ejecutar el linter:

Con el fin de corregir los errores de estilo que pueda haber en el código, se puede ejecutar el linter mediante el siguiente comando:

    pylint nombre_archivo.py

Para ejecutar el linter de la pantalla de control de la lógica, main.py, se puede hacer con el siguiente comando:

    pylint main.py

Para pasar el linter a los scripts que se encuentran dentro de "utils":

    pylint utils/data_loader.py
    pylint utils/name_anonimization.py

Comandos de linter para los ejercicios:

    pylint exercises/exercise1.py
    pylint exercises/exercise2.py
    pylint exercises/exercise3.py
    pylint exercises/exercise4.py
    pylint exercises/exercise5.py


Y comandos de linter para los tests:

    pylint test/test_exercise1.py
    pylint test/test_exercise2.py
    pylint test/test_exercise3.py
    pylint test/test_exercise4.py
    pylint test/test_exercise5.py

> **✨NOTA**  
> Para utilizar Pylint con otros sistemas operativos u otras versiones de Python: https://pypi.org/project/pylint/

<br>

## PASO 5: Instrucciones para ejecutar los tests:

Para ejecutar todos los tests del proyecto:

    python3 -m unittest discover -v test/

Para ejecutar sólo los tests de cada ejercicio:

    python3 -m unittest -v test.test_exercise1   
    python3 -m unittest -v test.test_exercise2   
    python3 -m unittest -v test.test_exercise3   
    python3 -m unittest -v test.test_exercise4   
    python3 -m unittest -v test.test_exercise5   

Cambiando el nombre de ejercicio (exercise2, 3, 4 o 5) al final del comando se puede acceder a los tests individuales.  
Si se ejecutan todos los tests a la vez es necesario incluir la palabra "discover".

> **✨NOTA**  
> Los comandos son los mismos en Windows, sólo hay que reemplazar *python3* por *python* en el comando.

<br>

## PASO 6: Instrucciones para comprobar la cobertura de los tests:

Para comprobar la cobertura de todos los tests de todos los ejercicios con un sólo comando:

    pytest test/ --cov=exercises

Para comprobar la cobertura de los tests de cada ejercicio uno a uno hay que ejecutar los siguientes comandos:

    pytest --cov=exercises.exercise1 test/test_exercise1.py   
    pytest --cov=exercises.exercise2 test/test_exercise2.py   
    pytest --cov=exercises.exercise3 test/test_exercise3.py   
    pytest --cov=exercises.exercise4 test/test_exercise4.py   
    pytest --cov=exercises.exercise5 test/test_exercise5.py   

> **✨NOTA**  
> Los comandos son los mismos en Windows.

<br>

## FUENTES CONSULTADAS PARA LA REALIZACIÓN DE LOS EJERCICIOS:
Apuntes

https://cookiecutter-data-science.drivendata.org/

https://www.w3schools.com/python/pandas/ref_df_nunique.asp

https://www.reddit.com/r/learnpython/comments/13cqyau/difference_between_nunique_and_unique_please/?tl=es-es&rdt=33533

https://www.statology.org/pandas-nunique/

https://stackoverflow.com/questions/18172851/deleting-dataframe-row-in-pandas-based-on-column-value

https://stackoverflow.com/questions/67598478/drop-rows-in-a-dataframe-based-on-the-data-type-of-columns

https://www.freecodecamp.org/news/drop-list-of-rows-from-pandas-dataframe/

https://www.geeksforgeeks.org/select-rows-columns-by-name-or-index-in-pandas-dataframe-using-loc-iloc/

https://www.geeksforgeeks.org/how-to-get-rows-index-names-in-pandas-dataframe/

https://stackoverflow.com/questions/16096627/selecting-a-row-of-pandas-series-dataframe-by-integer-index

https://www.w3schools.com/python/ref_string_strip.asp

https://www.w3schools.com/python/ref_string_split.asp

https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/python-split/

https://www.programiz.com/python-programming/methods/string/strip

https://stackoverflow.com/questions/65303781/converting-date-into-y-m-d-using-strptime-and-strftime-using-python

https://www.datacamp.com/tutorial/converting-strings-datetime-objects

https://docs.python.org/3/library/unittest.html

https://seaborn.pydata.org/generated/seaborn.histplot.html

https://stackoverflow.com/questions/40755911/how-get-just-the-time-part-from-a-datetime-strptime-object-python

https://docs.python.org/3/library/datetime.html

https://docs.python.org/3/library/datetime.html#datetime.time.minute

https://stackoverflow.com/questions/3463930/how-to-round-the-minute-of-a-datetime-object

https://stackoverflow.com/questions/75112399/how-to-round-down-a-datetime-to-the-nearest-5-minutes

https://www.geeksforgeeks.org/pandas-dataframe-round/

https://stackoverflow.com/questions/22190638/python-round-time-to-the-nearest-second-and-minute

https://medium.com/@ernestasena/mastering-time-with-the-datetime-module-in-python-dcd81e2d4bc1#:~:text=Rounding%20Time,replace()%20method.&text=In%20this%20example%2C%20we%20use,seconds%20and%20microseconds%20to%20zero.

https://www.geeksforgeeks.org/floor-ceil-function-python/

https://stackoverflow.com/questions/19801727/convert-datetime-to-unix-timestamp-and-convert-it-back-in-python

https://www.geeksforgeeks.org/python-timedelta-total_seconds-method-with-example/

https://www.datacamp.com/tutorial/timedelta-python-time-intervals

http://www.tugurium.com/python/index.php?C=PYTHON.13_3

https://www.datacamp.com/es/tutorial/timedelta-python-time-intervals

https://stackoverflow.com/questions/64042859/timestamp-timedelta-and-conversion-in-python

https://stackoverflow.com/questions/12448592/how-to-add-delta-to-python-datetime-time

https://www.reddit.com/r/StableDiffusion/comments/177r3s1/how_to_save_an_image_in_python/?tl=es-es&rdt=33624

https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it

https://stackoverflow.com/questions/2241600/python-regex-r-prefix

https://www.w3schools.com/python/python_regex.asp

https://stackoverflow.com/questions/62767421/regular-expression-pattern-to-replace-in-python

https://www.freecodecamp.org/espanol/news/expresiones-lambda-en-python/

https://ellibrodepython.com/lambda-python

https://4geeks.com/es/how-to/pandas-apply

https://www.geeksforgeeks.org/applying-lambda-functions-to-pandas-dataframe/

https://stackoverflow.com/questions/73547102/creating-a-function-by-using-lambda-and-apply

https://stackoverflow.com/questions/74598438/extract-number-of-ranking-position-in-pandas-dataframe

https://es.stackoverflow.com/questions/508445/c%C3%B3mo-utilizar-groupby-en-python-para-hacer-un-promedio-por-fecha-que-incluya-to

https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/

https://stackoverflow.com/questions/74577980/how-to-sort-values-in-one-column-ascending-and-another-column-descending

https://realpython.com/python-sort/

https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method

https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.name.html

https://stackoverflow.com/questions/66788292/how-to-name-a-pandas-series-column-title

https://www.w3schools.com/python/pandas/ref_df_index.asp

https://es.stackoverflow.com/questions/515579/index-de-dataframe-no-me-permite-usarlo-para-visualizacion-de-datos-con-matplotl

https://docs.python.org/3/library/unittest.html

https://docs.python.org/3/library/unittest.html#organizing-test-code

https://docs.python.org/3/library/unittest.html#setupclass-and-teardownclass

https://docs.python.org/3/library/unittest.html#command-line-interface

https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual

https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue

https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertFalse

https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIs

https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNot

https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn

https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsInstancex

https://experienceleague.adobe.com/es/docs/contributor/contributor-guide/writing-essentials/markdown

https://www.atlassian.com/es/continuous-delivery/software-testing/code-coverage 

https://coverage-readthedocs-io.translate.goog/en/7.6.10/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=rq

https://pypi.org/project/pylint/

https://pypi.org/project/pytest-cov/

https://markdown.es/sintaxis-markdown/

https://stackoverflow.com/questions/66280468/how-can-i-use-pytest-cov-to-both-generate-a-coverage-report-and-also-print-to-te

https://github.com/orgs/community/discussions/16925

https://github.com/microsoft/vscode/issues/156957 

https://www.markdownguide.org/basic-syntax/ 

https://stackoverflow.com/questions/23667610/what-is-the-difference-between-setup-and-setupclass-in-python-unittest 

https://docs.python.org/es/3/library/unittest.html

https://stackoverflow.com/questions/4613000/difference-between-cls-and-self-in-python-classes 

https://peps.python.org/pep-0008/#function-and-method-arguments

https://stackoverflow.com/questions/24799403/what-does-cls-function-do-inside-a-class-method

https://realpython.com/inheritance-composition-python/

https://stackoverflow.com/questions/62444612/should-i-list-class-methods-in-the-class-docstring

https://stackoverflow.com/questions/37019744/is-there-a-consensus-on-what-should-be-documented-in-the-class-and-init-docs

https://www.geeksforgeeks.org/python-attributeerror/

https://docs.python.org/3/tutorial/errors.html

https://docs.python.org/3/tutorial/errors.html#exceptions

https://www.geeksforgeeks.org/python-exception-handling/

https://www.geeksforgeeks.org/python-list-index-out-of-range-indexerror/

https://www.geeksforgeeks.org/how-to-handle-keyerror-exception-in-python/

https://www.geeksforgeeks.org/how-to-fix-valueerror-exceptions-in-python/

https://www.geeksforgeeks.org/handling-typeerror-exception-in-python/

https://www.geeksforgeeks.org/python-attributeerror/


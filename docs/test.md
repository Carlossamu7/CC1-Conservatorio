## Tests ##

Los test del código resultan fundamentales en el desarrollo de proyectos actual por diferentes motivos. Por un lado, se ha de tener en cuenta el coste que supondría desplegar una aplicación con errores y por otro para asegurar la calidad del código mediante la comprobación de los requisitos planteados, como son las historias de usuario. Además, los test van a convertirse en un elemento esencial para la automatización de los ciclos de vida del software.

Las pruebas que se van a realizar por el momento son **unitarias** ya que las comprobaciones que se van a hacer son llamadas a una función con diferentes parámetros y asegurando que los resultados son los deseados. El diseño de software de este proyecto es usando **desarrollo basado en tests**, donde es preferible programar los test sabiendo qué se desea obtener y posteriormente el código.

### Librería de aserciones & Marco de pruebas ###

En mi caso, que estoy implementando el proyecto en `Python3` y encontré aquí algunos de los mejores *test frameworks* para este lenguaje como `Robot`, `unittest`, `pytest` y `Nose2`.
- `Nose2` es el sucesor de `Nose`. Está basado en `unittest` y tiene muchas dependencias debido a esta herencia y al uso de *plugins*.
- `Robot` tiene menos flexibilidad: sin funciones como etiqueta de autor, prueba de omisión, sin bucles anidados, etc.
- La opción de usar `pytest` está ampliamente aceptada y usada por programadores `Python`. Una desventaja es que no viene integrado y es necesaria su instalación y [documentándome](https://stackoverflow.com/questions/27954702/unittest-vs-pytest) me pareció más intuitivo usar `unittest`. Asimismo, evitar instalaciones nos aliviará mucho la imagen del contenedor que en el próximo hito se va a desplegar. Optimizar la futura imagen `docker` es beneficioso para el proyecto.

De este modo, el **marco de pruebas** que he elegido es `unittest`. Aunque puede llevar a confusión con que sea una biblioteca de aserciones, ya que posee ambas cosas, en la [documentación oficial](https://docs.python.org/3/library/unittest.html) se describe como un *test framework*. Buenos motivos para esta elección es que está integrado en `Python` y es todo un estándar por lo que hay bastante información al respecto. Resulta cómodo hacer TDD mediante esta biblioteca.

En `Python` encontramos diferenes **aserciones explícitas** con `assert`. Se pueden consultar [todas las aserciones](https://docs.python.org/3/library/unittest.html#assert-methods) pero resumo a continuación las que más he usado:
- `assertTrue`: fallará sólo si no devuelve `True`.
- `assertFalse`: fallará sólo si no devuelve `False`.
- `assertEqual`: fallará sólo si los dos argumentos no son iguales.
- `assertRaises`: fallará si no se lanza una excepción del tipo indicado. En este [link](https://ongspxm.gitlab.io/blog/2016/11/assertraises-testing-for-errors-in-unittest/) se muestras diferentes formas de usarlo y una de ellas muy elegante.

Personalmente la filosofía de  otras librerías como `doctest` no me gustan tanto porque llevan las ejecuciones y resultados comentados encima de cada método/función alargando mucho el código. Para mí es preferible que si ahí hay que poner algún comentario sea del método o función y por otro lado independientes los test. Por esto descarté `doctest`.

La combinación de usar `unittest` y las `assert` descritas resulta muy cómoda. Hace que el desarrollo basado en test sea una buena línea de trabajo y crecimiento del proyecto planteado. El uso de `fixtures` es totalmente necesario para automatizar lo máximo posible el código, eliminando repeticiones y construcciones análogas.

### Implementación test ###

He implementado tres clases `TestAlumno` ([ver](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/tests/testAlumno.py)), `TestAsignaturaConcepto` ([ver](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/tests/testAsignaturaConcepto.py)), `TestAsignatura` ([ver](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/tests/testAsignatura.py)) y `TestConservatorio` ([ver](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/tests/testConservatorio.py)) que son subclases de `unittest.TestCase`. He procurado seguir lo que considero que son buenos hábitos a la hora de programar tests. Dejo aquí anotados los más importantes:

- Cada test prueba una pequeña funcionalidad y demuestra que es correcta.
- Cada función test es independiente y se puede ejecutar por separado.
- Los tests se ejecutan rápidamente.
- Cada test unitario tiene un propósito claro y el nombre de la función es largo y descriptivo.

Los tests pueden ser numerosos y su configuración repetitiva. Afortunadamente, existen  `fixtures` que representan la preparación necesaria para realizar una o más pruebas y cualquier acción de limpieza asociada. Esto puede implicar, por ejemplo, crear bases de datos temporales o proxy, directorios o iniciar un proceso de servidor. En mi caso he implementando un método llamado `setUp()`, que el marco de prueba llamará automáticamente para cada prueba que ejecutemos.

*Nota*: Si el método `setUp()` genera una excepción mientras se ejecuta la prueba, el marco considerará que la prueba ha sufrido un error y el método de prueba no se ejecutará.

La ejecución de un test es como un programa en `Python`:

```
python3.8 tests/testAlumno.py
python3.8 tests/testAsignaturaConcepto.py
python3.8 tests/testAsignatura.py
python3.8 tests/testConservatorio.py
```

Para ejecutarlo en el entorno virtual sería a través de `pipenv`, documentación [aquí](https://pipenv-es.readthedocs.io/es/latest/). También he usado la herramienta `coverage` para medir qué zonas del código se han ejecutado y cuáles no. Esto me permite mantener un control más detallado ([fuente](https://coverage.readthedocs.io/en/coverage-5.3/)).


```
##########################  Test de Alumno  ##########################
pipenv run coverage run tests/testAlumno.py -v
pipenv run coverage report -m
########################  Test de AsignaturaConcepto  ########################
pipenv run coverage run tests/testAsignaturaConcepto.py -v
pipenv run coverage report -m
########################  Test de Asignatura  ########################
pipenv run coverage run tests/testAsignatura.py -v
pipenv run coverage report -m
#######################  Test de Conservatorio  ######################
pipenv run coverage run tests/testConservatorio.py -v
pipenv run coverage report -m
```

Veremos más adelante que esto se puede automatizar. Los resultados de las ejecuciones son los que vemos a continuación. Para la clase `Alumno`:

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_04_05/testAlumno.png)

Para la clase `Asignatura`:

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_04_05/testAsignatura.png)

Para la clase `AsignaturaConcepto`:

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_04_05/testAsignaturaConcepto.png)

Para la clase `Conservatorio`:

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_04_05/testConservatorio.png)

Observamos que los test barren el 100% del código de `Alumno.py`, de `AsignaturaConcepto.py`, de `Asignatura.py` y de `Conservatorio.py`. Asimismo se ha usado el parámetro `-v` u opción `verbose` para que informe qué test está ejecutando y posteriormente con `pipenv run coverage report -m` nos emite el informe de las zonas de código ejecutadas.

### Gestor de tareas ###

Los gestores de tareas más populares para `Python` a día de hoy son `invoke`, `poetry` y `Makefile`. A continuación voy a explicar algunos detalles de estos así como posibles ventajas y desventajas.

Algunos de los inconvenientes de `Invoke` para mi gusto es que es dirigido por código, por tanto tiene sintaxis Python y los errores se muestran como tal. Los comandos del shell se ejecutan usando `run('orden')`. Al fin y al cabo [hereda de Make](http://www.pyinvoke.org/) y para eso prefiero elegir `Makefile` como gestor de tareas.

`Poetry` es u  gestor de tareas y dependencias más moderno con muchos puntos fuertes. Sin embargo, en este [enlace](https://news.ycombinator.com/item?id=24081125) encontré algunos motivos por los cuales no usar `Poetry` o fallos que han tenido algunos desarrolladores. A mí personalmente me pareció un tanto **complejo de usar y configurar correctamente**, y más aún después de observar los fallos que otros desarrolladores han tenido con las dependencias de esta herramienta.
-  `Poetry` todavía tiene que luchar contra los errores.
- La resolución de dependencias puede ser un problema difícil de resolver al mismo tiempo, pero sería genial, si `Poetry` no solo usara un solo núcleo, para acelerar el proceso.
- Problemas y fallos de CI aleatorias que ocurren cuando `Poetry` resuelve las dependencias: https://github.com/actions/virtual-environments/issues/1343
- Otra opinión: "Soy un gran fanático de `Poetry` pero no está exento de inconvenientes. Hace al menos unos meses, necesitaba instalar una suite de compilación completa si deseaba instalar una distribución de código fuente de `Python` puro (`sdist`) que se creó con `Poetry` en *Alpine*".

Aquí otro ejemplo en donde `Poetry` coge la versión incorrecta de `Python`: [enlace](https://github.com/python-poetry/poetry/issues/655).

El **gestor de tareas** que he elegido para el proyecto es `Makefile`. No es perfecto y tiene algunas carencias pero para las tareas que voy a necesitar y por su sencillez creo que es una opción idónea. En él se pueden ejecutar los test unitarios rápidamente con la orden `make test`.

```
test:
	# Tests unitarios e informe a través de report -m
	##########################  Test de Alumno  ##########################
	pipenv run coverage run tests/testAlumno.py -v
	pipenv run coverage report -m
	########################  Test de AsignaturaConcepto  ########################
	pipenv run coverage run tests/testAsignaturaConcepto.py -v
	pipenv run coverage report -m
	########################  Test de Asignatura  ########################
	pipenv run coverage run tests/testAsignatura.py -v
	pipenv run coverage report -m
	#######################  Test de Conservatorio  ######################
	pipenv run coverage run tests/testConservatorio.py -v
	pipenv run coverage report -m
```

Además con `make sintaxis` se puede comprobar la sintaxis de las clases implementadas.

```
sintaxis:
	pipenv run python3.8 src/Alumno.py
	pipenv run python3.8 src/AsignaturaConcepto.py
	pipenv run python3.8 src/Asignatura.py
	pipenv run python3.8 src/Conservatorio.py
```

Para borrar los ficheros generados y que no queremos se dispone de la tarea `clean`:

```
clean:
	#rm -r ./src/__pycache__
	rm .coverage
	rm Pipfile*
```

### Avances en el código ###

Los avances en el código en este entrega son los siguientes. No obstante en durante el desarrollo de contenerización de han mejorado algunas prácticas de `Python` según lo que se indicó. [Consultar avances contenerización](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/docker.md#avance-del-proyecto).

- Avance notable de prácticamente todas las HU.
- Implementación de `listaAsignaturas()`, `matriculaAsignatura()` y `desmatriculaAsignatura()`. Nuevo formateado para las asignaturas como string.
- Conforme avanza el proyecto se demandan nuevas necesidades para el conservatorio mediante historias de usuario. Creación de las [[HU6]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/39), [[HU10]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/43), [[HU11]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/44), [[HU12]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/45), [[HU13]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/46) y [[HU14]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/47).
- Implementación de una clase controladora `Conservatorio` disponible [aquí](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Conservatorio.py). Esta clase maneja coleccionables (listas) de `Asignatura` y `Alumno` del Conservatorio ayudando a su gestión. De esta manera se consiguen avanzar algunas de las HU.
- Tratamiento de nuevas excepciones de la clase `Conservatorio`.

*Nota*: las funciones implementadas de rastreo de aulas que ha pisado un alumno/profesor correspondientes a la [[HU14]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/47) son de gran utilidad para periodos como el actual debido a la COVID-19, en donde rastrear el virus es muy importante.

#### Nuevos avances ####

- [Cambiar a notación `snake_case`](https://github.com/Carlossamu7/CC1-Conservatorio/issues/62).

- [Se deben justificar todas las modificaciones de un objeto](https://github.com/Carlossamu7/CC1-Conservatorio/issues/58). No había ninguna HU indicando que se puedan modificar todas las asignaturas a la vez a través `set_asignaturas` por lo que es eliminado.

- [Se debe almacenar la asignaturas de la forma más adecuada para las HUs](https://github.com/Carlossamu7/CC1-Conservatorio/issues/59). Almacenar las asignaturas en una lista. Usar la clase asignatura.

- [Usar fixtures en los tests de Python](https://github.com/Carlossamu7/CC1-Conservatorio/issues/63)

- Se ha relacionado el *issue* [Cambio en el tratamiento de asignaturas dentro de Alumno](https://github.com/Carlossamu7/CC1-Conservatorio/issues/42) con las HU correspondientes.

- [Como desarrollador quiero comprobar la validez de un email para [HU7]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/64)

- [Como desarrollador, voy a distinguir entre AsignaturaConcepto (concepto, material, curso) y la Asignatura (profesor, aula, horario)](https://github.com/Carlossamu7/CC1-Conservatorio/issues/65)

- [Se debe almacenar la asignaturas de la forma más adecuada para las HUs](https://github.com/Carlossamu7/CC1-Conservatorio/issues/59). Efectivamente, no es lo más eficiente guardar las asignaturas como un único *string* separado por comas y espacios. Se ha valorado la opción de usar la clase `Asignatura` pero no parece lo más correcto porque dicha clase tiene el aula, horario, profesor y otros campos que no son de interés para el alumno. Es más, es posible que en el momento de la matriculación esto no se sepa (en la Universidad normalmente sí se sabe en el momento de la matriculación pero no es así en los Conservatorios) y la asignatura no esté dada de alta. Por eso me parece lo más correcto cambiar a usar una lista de *strings* lo cual elimina el método `lista_asignaturas` y simplifica y hace más eficiente algunas cosas.

- [Añadir comprobación de tipos](https://github.com/Carlossamu7/CC1-Conservatorio/issues/68)

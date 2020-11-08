## Herramientas y tecnologías del proyecto

##### Lenguaje

Los servicios de la aplicación van a estar implementados en `Python3`. Se puede consultar la [documentación de las versiones](https://www.python.org/doc/versions/).

##### Entorno vitual

El entorno virtual que se va a usar para las versiones mencionadas es el conocido `virtualenv` para `Python`.

##### Herramienta de construcción

Se va a usar la herramienta clásica `Makefile`. Las tareas que nuestro `Makefile` puede hacer por el momento son:

- `make install`: instala las versiones de los paquetes que el proyecto necesita. Básicamente lanzará la orden `pip3 install -r requirements.txt`, en donde las dependencias están en `requirements.txt`.

- `make test`: ejecuta los tests. Se usará `unittest` disponible en las distribuciones de `Python`. En el directorio `tests` de este repositorio se irán situando los diferentes programas de test.

- `make clean`: limpieza de archivos generados

##### Integración continua

La herramienta de integración continua del proyecto va a ser [Travis CI](https://travis-ci.org/getting_started). Travis comprueba que los tests se ejecuten correctamente para las versiones especificadas en el fichero `.travis.yml`.

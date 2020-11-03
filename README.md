# Proyecto de Cloud Computing

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Repositorio para el proyecto (con propósito educativo) de Cloud Computing: Fundamentos e Infraestructuras (2020-21) del Máster en Ingeniería Informática UGR.

El ambiente de trabajo necesario para la asignatura y en el cual se va a implementar dicho proyecto se puede consultar en este [link](https://github.com/Carlossamu7/CC1-Proyecto/blob/master/docs/set-up.md).

## Descripción del problema

Una escuela de música o conservatorio privado tiene todo su registro de alumnos, profesores, horarios y otros en papel. Dicho conservatorio quiere actualizarse de modo puedan hacer eso computacionalmente lo cual les ahorraría mucho trabajo y evitaría que la pérdida de un papel suponga un fallo grave para la empresa.

##### Descripción de la solución

Este proyecto esta dirigido a dar una solución *cloud* a este problema. La solución consistiría en mantener el registro de alumnos y su matriculación a asignaturas del centro. Para ello se usaría una plataforma donde los administradores puedan dar de alta una asignatura y los alumnos que lo deseen matricularse en ella y poder informarse de aspectos como el horario o el aula.

## Arquitectura

En primer lugar hay que analizar muy bien el proyecto que estamos tratando de resolver. En dicho proyecto reconocemos perfectamente dos entidades fundamentales, por un lado las **asignaturas** que son dadas de alta por un Administrador del Conservatorio por ejemplo y por otro lado tenemos a los **alumnos** que se matriculan de asignaturas y hacen diversas consultas o cambios en su matrícula.

Después de estudiar las diferentes arquitecturas y teniendo en cuenta el proyecto que se va a desarrollar la arquitectura que mejor se adecúa es una **arquitectura basada en microservicios**. La justificación de esta elección se debe a las numerosas ventajas que esta arquitectura ofrece a nuestro problema. La más importante es la independencia entre los microservicios en su desarrollo, en su manejo, en su mantenimiento o en su actualización. Por otro lado hay que tener en cuenta la robustez frente a fallos: la caída de un servicio no implica la del otro.

Otra razón para esta elección es la posibilidad de una gestión descentralizada de datos, cada microservicio tiene su base de datos y la comunicación la van realizar mediante una API. Un problema de estas arquitecturas es cuando el número de microservicios es grande y por consiguiente la tarea de gestión se hace más pesada pero en nuestro caso sólo vamos a tener dos grandes microservicios que dirigen cada una de las funcionalidades ya introducidas:

- **Gestión del conservatorio**. Llevada a cabo por un Administrador del Conservatorio. Se encarga de dar de alta, borrar y modificar asignaturas. Cada asignatura tiene un horario, un aula y profesor asociado.

- **Gestión de alumnos**. Cada alumno tiene la posibilidad de darse de alta en el conservatorio mediante la matricula en las asignaturas deseadas. También puede matricular y desmatricular asignaturas así como hacer consultas.

Es posible que conforme avance el proyecto surja la necesidad de desarrollar un nuevo microservicio. Esta arquitectura resulta idónea para la integración del mismo.

## Aspectos del proyecto

##### Lenguaje

Los servicios de la aplicación van a estar implementados en `Python3`. En concreto se va a dar mantenibilidad de las versiones `3.6`, `3.7` y `3.8` ([documentación de las versiones](https://www.python.org/doc/versions/)). El framework de comunicación que se va a usar para desarrollar las `API REST` es `Flask`.

##### Entorno vitual

El entorno virtual que se va a usar para las versiones mencionadas es el conocido `virtualenv` para `Python`.

##### Base de datos

Se usará la base de datos relacional PostgreSQL. Su uso en Python se hará a través de `peewee`.

##### Herramienta de construcción

Se ha valorado la opción de usar `Invoke` pero la opción final ha sido la herramienta clásica `Makefile`.

```
buildtool: Makefile
```

Con la siguiente orden se instalan las versiones de los paquetes que el proyecto necesita

```
make install
```

Básicamente lanzará la orden `pip3 install -r requirements.txt`, en donde las dependencias están en `requirements.txt`.

Para ejecutar los test se usará `unittest` disponible en las distribuciones de `Python`. En el directorio `tests` de este repositorio se irán situando los diferentes programas de test y los podremos lanzar con

```
make test
```

Más adelante, cuando sea necesaria la limpieza de archivos generados podremos automatizarla llevándola acabo con:

```
make clean
```

##### Integración continua

La herramienta de integración continua del proyecto va a ser [Travis CI](https://travis-ci.org/getting_started). Travis comprueba que los tests se ejecuten correctamente para las versiones especificadas en `.travis.yml`.

##### Sistema de logging

La gestión de logs se realizará usando la libreria `logging` de `Python`.

## *Roadmap*

Para consultar exclusivamente los *milestone* con sus *issues* entrar [aquí](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/milestones_hu.md). La planificación del desarrollo del proyecto es la siguiente:

**Fase 1**. Desarrollar un producto mínimamente viable (MVP) de [Administrador](https://github.com/Carlossamu7/CC1-Conservatorio/milestone/4) y de [Alumno](https://github.com/Carlossamu7/CC1-Conservatorio/milestone/3).

- [[HU1] Como administrador quiero dar de alta una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/12)

> Se ha implementado la clase `Asignatura.py` [aquí](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Asignatura.py).

- [[HU4] Como alumno quiero matricularme de ciertas asignaturas.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/15)

> Se ha implementado la clase `Alumno.py` [aquí](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Alumno.py). Gestionada la comprobación de DNIs, no se dará de alta a ningún alumno con un DNI no válido en el sistema.

**Fase 2**. Avanzar esos MVP con nuevas historias de usuario que los hacen más funcionales.

- [[HU2] Como administrador quiero modificar una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/13)
- [[HU3] Como administrador quiero borrar una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/14)
- [[HU5] Como alumno quiero desmatricularme de ciertas asignaturas.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/16)
- [[HU6] Como alumno quiero modificar la dirección de correo con la que el centro se pone en contacto conmigo.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/17)

**Fase 3**. Introducir tests que comprueben y aseguren la calidad del código ya implementado ya que nuestro objetivos es desplegar la aplicación en la nube y estas pruebas confirmarán que el código hace lo que se espera que haga.

- [Tests para Alumno](https://github.com/Carlossamu7/CC1-Conservatorio/issues/24)
- [Tests para Asignatura](https://github.com/Carlossamu7/CC1-Conservatorio/issues/25)

**Fase 4**. Continuar con el desarrollo de la aplicación avanzando historias de usuario que necesitan de la comunicación de ambos microservicios.

- [[HU7] Como alumno quiero consultar el horario de una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/18)
- [[HU8] Como alumno quiero consultar el aula de una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/19)

**Fase 5**. Crear contenedores en donde almacenar la aplicación para permitir el despliegue de la misma en la nube.

## Clases

En primer lugar la **estructura del proyecto** es sencilla con dos clases:

```bash
src
├── Alumno.py
└── Asignatura.py

```

- Clase [Asignatura](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Asignatura.py). Tiene los siguientes atributos:
    - asignatura (`getter`)
    - profesor (`getter` y `setter`)
    - horario (`getter` y `setter`)
    - aula (`getter` y `setter`)

  Y los siguientes métodos:
    - `toString()`

- Clase [Alumno](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Alumno.py). Tiene los siguientes atributos:
    - nombre (`getter` y `setter`)
    - email (`getter` y `setter`)
    - dni (`getter`)
    - asignaturas (`getter` y `setter`)

  Y lo siguientes métodos:
    - `listaAsignaturas()`
    - `matriculaAsignatura()`
    - `desmatriculaAsignatura()`
    - `toString()`

#### Comprobación de la sintaxis:

Ejecutando las órdenes

```
python3.8 src/Alumno.py
python3.8 src/Asignatura.py
```

observamos que la sintaxis es correcta.

![](./docs/images/sem_02_03/sintaxis.png)

#### Tratamiento de errores

Los errores tratados por el sistema son los siguientes (todos de la clase Alumno):

- Crear un alumno con un DNI no válido. Se lanza una excepción de tipo `ValueError` que informa diciendo: ``El DNI no es válido.``

- Matricular una asignatura ya matriculada. Se lanza una excepción de tipo `ValueError` que informa diciendo: ``Asignatura ya matriculada.``

- Desmatricular una asignatura no matriculada. Se lanza una excepción de tipo `ValueError` que informa diciendo: ``No existe tal asignatura.``

## Licencia

Este proyecto está desarrollado bajo licencia [GNU General Public License v3.0](https://es.wikipedia.org/wiki/GNU_General_Public_License).

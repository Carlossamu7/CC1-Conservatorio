# Proyecto de Cloud Computing

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Repositorio para el proyecto (con propósito educativo) de Cloud Computing: Fundamentos e Infraestructuras (2020-21) del Máster en Ingeniería Informática UGR.

El ambiente de trabajo necesario para la asignatura y en el cual se va a implementar dicho proyecto se puede consultar en este [link](https://github.com/Carlossamu7/CC1-Proyecto/blob/master/docs/set-up.md).

## Descripción del problema

Una escuela de música o conservatorio privado tiene todo su registro de alumnos, profesores, horarios y otros en papel. Dicho conservatorio quiere actualizarse de modo puedan hacer eso computacionalmente lo cual les ahorraría mucho trabajo y evitaría que la pérdida de un papel suponga un fallo grave para la empresa.

## Descripción de la solución

Este proyecto esta dirigido a dar una solución cloud a este problema. La solución consistiría en mantener el registro de alumnos y su matriculación a asignaturas del centro. Para ello se usaría una plataforma donde los administradores puedan dar de alta una asignatura y los alumnos que lo deseen matricularse en ella y poder informarse de aspectos como el horario o el aula.

## Arquitectura

Después de estudiar las diferentes arquitecturas e indagar las ventajas e inconvenientes de cada una he elegido una arquitectura basada en **microservicios**.
Las ventajas de esta arquitectura son numerosas, de ahí la popularidad en su uso. Por ejemplo la independencia de cada uno de los microservicios e incluso poder implementarlos en lenguajes distintos consiguiendo una mayor eficiencia. Esto ayuda al mantenimiento y desarrollo de los mismos así como la robustez frente a fallos: la caída de un servicio no implica la del otro.

En este proyecto hay dos grandes microservicios:

- **Gestión del conservatorio**. Dar de alta, borrar y modificar asignaturas. Cada asignatura tiene un horario, un aula y profesor asociado.

- **Gestión de alumnos**. Darse de alta en el conservatorio mediante la matricula en las asignaturas deseadas.

![](./docs/images/sem_02_03/CC-Arch.png)

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

## Roadmap

La organización del proyecto es la siguiente (actualmente el desarrollo va por el punto 3):

1. Descripción del proyecto y establecer el ambiente de trabajo.
2. Definir la arquitectura del proyecto así como el lenguaje y otros detalles como los gestores de tareas y versiones.
3. Implementar las clases `Alumno.py` y `Asignatura.py` con sus interfaces. Aquí se dará una solución computacional a las historias de usuario de cada uno de estos MVP. Las historias de usuario se han intentado ordenar en el modo en el que se van a llevar a cabo cronológicamente.
4. Desarrollo de `tests` para estas clases de manera que se tenga un producto mínimamente viable (MVP).
5. Se seguirá avanzando según lo pedido con el objetivo de desplegar el proyecto en la nube.

## *Milestones*

En este apartado se van a exponer los diferentes *milestone* del proyecto y los issues que siguen su traza.

*Milestone* 1 - [Descripción del proyecto usando correctamente git y GitHub](https://github.com/Carlossamu7/CC1-Conservatorio/milestone/1)

- [Crear `README`](https://github.com/Carlossamu7/CC1-Conservatorio/issues/1)
- [Añadir licencia](https://github.com/Carlossamu7/CC1-Conservatorio/issues/2)
- [Crear `.gitignore`](https://github.com/Carlossamu7/CC1-Conservatorio/issues/3)
- [Crear `docs` y establecer el set-up del proyecto](https://github.com/Carlossamu7/CC1-Conservatorio/issues/4)
- [Descripción del proyecto](https://github.com/Carlossamu7/CC1-Conservatorio/issues/5)


*Milestone* 2 - [Concretando y planificando el proyecto](https://github.com/Carlossamu7/CC1-Conservatorio/milestone/2)

- [Elegir arquitectura adecuada](https://github.com/Carlossamu7/CC1-Conservatorio/issues/7)
- [Elegir lenguaje, gestor de tareas, versiones y otros](https://github.com/Carlossamu7/CC1-Conservatorio/issues/8)
- [Crear `.travis.yml`](https://github.com/Carlossamu7/CC1-Conservatorio/issues/9)
- [Crear `Makefile`](https://github.com/Carlossamu7/CC1-Conservatorio/issues/10)
- [Definir y explicar las HU](https://github.com/Carlossamu7/CC1-Conservatorio/issues/11)
- [Crear `cc.yaml`](https://github.com/Carlossamu7/CC1-Conservatorio/issues/20)
- [Introducir Roadmap y Milestones](https://github.com/Carlossamu7/CC1-Conservatorio/issues/21)

#### Historias de usuario

Para cada microservicio se ha definido un *milestone*. Cuando alguno de estos *milestone* esté acabado obtendremos un MVP. El primer *milestone* es para el [Administrador](https://github.com/Carlossamu7/CC1-Conservatorio/milestone/4) (de las asignaturas).
- [[HU1] Como administrador quiero dar de alta una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/12)

> Se ha implementado la clase `Asignatura.py` [aquí](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Asignatura.py).

- [[HU2] Como administrador quiero modificar una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/13)
- [[HU3] Como administrador quiero borrar una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/14)


El segundo *milestone* es para los [Alumnos](https://github.com/Carlossamu7/CC1-Conservatorio/milestone/3).
- [[HU4] Como alumno quiero matricularme de ciertas asignaturas.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/15)

> Se ha implementado la clase `Alumno.py` [aquí](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Alumno.py).

- [[HU5] Como alumno quiero desmatricularme de ciertas asignaturas.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/16)
- [[HU6] Como alumno quiero modificar la dirección de correo con la que el centro se pone en contacto conmigo.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/17)
- [[HU7] Como alumno quiero consultar el horario de una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/18)
- [[HU8] Como alumno quiero consultar el aula de una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/19)

## Licencia

Este proyecto está desarrollado bajo licencia [GNU General Public License v3.0](https://es.wikipedia.org/wiki/GNU_General_Public_License).

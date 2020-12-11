# *MiConservatorio*

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![TravisCI](https://travis-ci.org/Carlossamu7/CC1-Conservatorio.svg?branch=master)](https://travis-ci.org/github/Carlossamu7/CC1-Conservatorio)
[![CircleCI](https://circleci.com/gh/Carlossamu7/CC1-Conservatorio.svg?style=svg)](https://app.circleci.com/pipelines/github/Carlossamu7/CC1-Conservatorio)

Repositorio para el proyecto (con propósito educativo) de **Cloud Computing**: Fundamentos e Infraestructuras (2020-21) del Máster en Ingeniería Informática de la Universidad de Granada.

## Información ##

Este proyecto es para la aplicación de gestión de un Conservatorio privado.

- [Descripción del problema](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/descripcion.md)
- [Arquitectura elegida](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/arquitectura.md)
- [Roadmap](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/roadmap.md)
- [Clases y estructura del proyecto](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/clasessindetalle.md)

## Test ##

Los test del código resultan fundamentales en el desarrollo de proyectos actual por diferentes motivos. Por un lado, se ha de tener en cuenta el coste que supondría desplegar una aplicación con errores y por otro para asegurar la calidad del código mediante la comprobación de los requisitos planteados, como son las historias de usuario. Además, los test van a convertirse en un elemento esencial para la automatización de los ciclos de vida del software.

[Documentación de test](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/test.md)

## Docker ##

El principal objetivo del uso de [Docker]((https://www.docker.com/)) u otra infraestructura de contenedores es aislar la ejecución de una aplicación de forma que sea mucho más fácil desplegarla, incluyendo los datos y el estado en el que se encuentre en un momento determinado. Usar dockers facilita el hecho de mantener un entorno de pruebas consistente y obtener una mayor consistencia entre los entornos de prueba y los entornos de producción.

[Documentación de contenerización](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/docker.md)

## Integración continua ##

En sistemas de desarrollo ágil quien desarrolle tiene que asegurar que el código pasa todos los tests antes de ser desplegado o simplemente incorporado a la rama principal, porque los tests son la especificación de los requisitos. Para ello se escriben una serie de tests que se ejecutan automáticamente al añadir o modificar código. Estos tests tienen el fin obvio de asegurar la calidad del mismo, pero también en un entorno de desarrollo colaborativo permiten integrar código fácilmente asegurándose de que no se rompa nada. Se va a configurar el repositorio del proyecto para que se pasen los tests, en diferentes ambientes, automáticamente. Para ello han elegido varios sistemas de integración continua, [Travis-CI](https://travis-ci.com/) y [Circle-CI](https://circleci.com/) en donde se ha hecho uso del contenedor docker.

[Documentación de integración continua](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/ci.md)

## Licencia

Este proyecto está desarrollado bajo licencia [GNU General Public License v3.0](https://es.wikipedia.org/wiki/GNU_General_Public_License).

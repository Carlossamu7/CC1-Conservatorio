# *MiConservatorio*

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![TravisCI](https://travis-ci.com/Carlossamu7/CC1-Conservatorio.svg?branch=master)](https://travis-ci.com/github/Carlossamu7/CC1-Conservatorio)
[![CircleCI](https://circleci.com/gh/Carlossamu7/CC1-Conservatorio.svg?style=svg)](https://app.circleci.com/pipelines/github/Carlossamu7/CC1-Conservatorio)

Repositorio para el proyecto (con propósito educativo) de **Cloud Computing**: Fundamentos e Infraestructuras (2020-21) del Máster en Ingeniería Informática de la Universidad de Granada.

## Información ##

Este proyecto es para la aplicación de gestión de un Conservatorio privado.

- [Descripción del problema](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/descripcion.md)
- [Arquitectura elegida](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/arquitectura.md)
- [Roadmap](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/roadmap.md)
- [Clases y estructura del proyecto](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/clasessindetalle.md)

## Puesta en marcha del proyecto ##

En primer lugar descarga el repo desde GitHub:

```
git clone https://github.com/Carlossamu7/CC1-Conservatorio.git
```

En segundo lugar has de tener una versión de `Python3` instalada, entre la `3.6` y la `latest`. Asimismo debes de tener instalado en tu sistema operativo el paquete `build-essentials` para poder usar el gestor de tareas.

Una vez hecho esto desde la carpeta raíz del proyecto ejecuta la siguiente orden para instalar las dependencias:

```
make install
```

Alternativamente se puede comprobar la sintaxis de las clases del proyecto así como lanzar los test con las respectivas ordenes:

```
make check
make test
```

Por último para limpiar los ficheros generados:
```
make clean
```

## Microservicios ##

Sobre la base de la clase hecha se va a diseñar una API consistente en una serie de rutas (API REST) y testearlo. También se va a crear la infraestructura necesaria para comenzar a ejecutarlo. Para ello, se va de usar el mismo fichero de construcción que hasta ahora, añadiendo las nuevas tareas. Esto también permite, por ejemplo, usar uno de los sistemas de integración continua creados para hacer una ejecución de prueba, en vez de ejecutar los tests.

[Documentación de microservicios](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/microservices.md)

## Licencia

Este proyecto está desarrollado bajo licencia [GNU General Public License v3.0](https://es.wikipedia.org/wiki/GNU_General_Public_License).

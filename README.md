# *MiConservatorio*

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![TravisCI](https://travis-ci.com/Carlossamu7/CC1-Conservatorio.svg?branch=master)](https://travis-ci.com/github/Carlossamu7/CC1-Conservatorio)
[![CircleCI](https://circleci.com/gh/Carlossamu7/CC1-Conservatorio.svg?style=svg)](https://app.circleci.com/pipelines/github/Carlossamu7/CC1-Conservatorio)

![docker-compose](https://github.com/Carlossamu7/CC1-Conservatorio/workflows/Comprobar%20docker%20compose/badge.svg)
![YAML](https://github.com/Carlossamu7/CC1-Conservatorio/workflows/Comprobar%20YAML/badge.svg)

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

Para limpiar los ficheros generados:
```
make clean
```

Y por último para ejecutar el servidor de la API:
```
make execute
```

## Composición de servicios ##

Cuando una aplicación no cabe en un solo contenedor por la existencia de varios tier, o simplemente nodos que sirven para almacenar datos, es necesario usar Docker compose para describir de forma repetible la forma como se van a conectar tales contenedores. Se va a diseñar, usando Docker compose y describiendo la infraestructura mediante un fichero docker-compose.yml, un servicio que incluya varios contenedores, incluyendo uno cuyo contenido exclusivo sea almacenar datos.

[Documentación de composición de servicios](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/docker_compose.md)

## Enlaces relevantes ##

- [Test](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/test.md)
- [Contenerización](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/docker.md)
- [Integración continua](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/ci.md)
- [Microservicios](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/microservices.md)

## Licencia

Este proyecto está desarrollado bajo licencia [GNU General Public License v3.0](https://es.wikipedia.org/wiki/GNU_General_Public_License).

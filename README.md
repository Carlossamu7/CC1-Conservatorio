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

## Licencia

Este proyecto está desarrollado bajo licencia [GNU General Public License v3.0](https://es.wikipedia.org/wiki/GNU_General_Public_License).

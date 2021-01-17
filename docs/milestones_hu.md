## *Milestones*

En este apartado se van a exponer los diferentes *milestone* del proyecto y los *issues* (importantes) que siguen su traza.

***Milestone*** 0 - [Descripción del proyecto usando correctamente git y GitHub](https://github.com/Carlossamu7/CC1-Conservatorio/milestone/1)

- [Crear `README`](https://github.com/Carlossamu7/CC1-Conservatorio/issues/1)
- [Añadir licencia](https://github.com/Carlossamu7/CC1-Conservatorio/issues/2)
- [Crear `.gitignore`](https://github.com/Carlossamu7/CC1-Conservatorio/issues/3)
- [Crear `docs` y establecer el set-up del proyecto](https://github.com/Carlossamu7/CC1-Conservatorio/issues/4)
- [Descripción del proyecto](https://github.com/Carlossamu7/CC1-Conservatorio/issues/5)


***Milestone*** 1 - [Concretando y planificando el proyecto](https://github.com/Carlossamu7/CC1-Conservatorio/milestone/2)

- [Elegir arquitectura adecuada](https://github.com/Carlossamu7/CC1-Conservatorio/issues/7)
- [Elegir lenguaje, gestor de tareas, versiones y otros](https://github.com/Carlossamu7/CC1-Conservatorio/issues/8)
- [Crear `.travis.yml`](https://github.com/Carlossamu7/CC1-Conservatorio/issues/9)
- [Crear `Makefile`](https://github.com/Carlossamu7/CC1-Conservatorio/issues/10)
- [Definir y explicar las HU](https://github.com/Carlossamu7/CC1-Conservatorio/issues/11)
- [Crear `cc.yaml`](https://github.com/Carlossamu7/CC1-Conservatorio/issues/20)
- [Introducir Roadmap y Milestones](https://github.com/Carlossamu7/CC1-Conservatorio/issues/21)

#### Historias de usuario

Para cada microservicio se ha definido un *milestone*. Cuando alguno de estos *milestone* esté acabado obtendremos un MVP.

***Milestone*** - [Administrador](https://github.com/Carlossamu7/CC1-Conservatorio/milestone/4) (de las asignaturas)

- [[HU1] Como administrador quiero dar de alta una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/12)

> Se ha implementado la clase `Asignatura.py` [aquí](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Asignatura.py).

- [[HU2] Como administrador quiero modificar una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/13)
- [[HU3] Como administrador quiero borrar una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/14)
- [[HU11] Como administrador quiero saber en el número de alumnos y asignaturas del conservatorio.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/44)

> Se ha implementado la clase `Conservatorio.py` [aquí](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Conservatorio.py).

- [[HU12] Como administrador quiero saber las asignaturas que imparte un profesor.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/45)
- [[HU13] Como administrador quiero saber el horario completo de un  profesor.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/46)
- [[HU14] Como administrador quiero saber las aulas que usa un profesor/alumno.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/47)
- [[HU15] Como administrador quiero dar de alta un alumno.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/57)
- [[HU16] Como administrador quiero obtener un listado de los alumnos y su información.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/77)
- [[HU17] [HU17] Como administrador quiero obtener un listado de las asignaturas y su información.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/78)


***Milestone*** - [Alumnos](https://github.com/Carlossamu7/CC1-Conservatorio/milestone/3)

- [[HU4] Como alumno quiero matricularme de ciertas asignaturas.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/15)

> Se ha implementado la clase `Alumno.py` [aquí](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Alumno.py). Gestionada la comprobación de DNIs, no se dará de alta a ningún alumno con un DNI no válido en el sistema.

- [[HU5] Como alumno quiero desmatricularme de ciertas asignaturas.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/16)
- [[HU6] Como alumno quiero consultar mis asignaturas matriculadas.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/39)
- [[HU7] Como alumno quiero modificar la dirección de correo con la que el centro se pone en contacto conmigo.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/17)
- [[HU8] Como alumno quiero consultar el horario de una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/18)
- [[HU9] Como alumno quiero consultar el aula de una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/19)
- [[HU10] Como alumno quiero saber mi horario completo.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/43)

***Milestone*** 2 - [Tests](https://github.com/Carlossamu7/CC1-Conservatorio/milestone/5)

- [Actualizar `Makefile` (`test` y `clean`)](https://github.com/Carlossamu7/CC1-Conservatorio/issues/26)
- [Actualizar ``.travis.yml` para tests](https://github.com/Carlossamu7/CC1-Conservatorio/issues/30)
- [Incluir clase `Conservatorio` en `Makefile`](https://github.com/Carlossamu7/CC1-Conservatorio/issues/48)
- [Actualizar `requirements.txt`](https://github.com/Carlossamu7/CC1-Conservatorio/issues/34)
- [Actualizar `cc.yaml`](https://github.com/Carlossamu7/CC1-Conservatorio/issues/33)
- [Documentación para *milestone* 2](https://github.com/Carlossamu7/CC1-Conservatorio/issues/31)

***Milestone*** 3 - [Dockers](https://github.com/Carlossamu7/CC1-Conservatorio/milestone/6)

- [Documentación para *milestone* 3](https://github.com/Carlossamu7/CC1-Conservatorio/issues/52)
- [`Dockerfile`](https://github.com/Carlossamu7/CC1-Conservatorio/issues/53).

Otros:

- [Uso de atributos privados en Python](https://github.com/Carlossamu7/CC1-Conservatorio/issues/54)
- [Eliminar métodos innecesarios en Conservatorio.py](https://github.com/Carlossamu7/CC1-Conservatorio/issues/55)
- [Cambiar a estructura de datos de tipo diccionario en Conservatorio](https://github.com/Carlossamu7/CC1-Conservatorio/issues/56)

***Milestone*** 4 - [Integración continua](https://github.com/Carlossamu7/CC1-Conservatorio/milestone/7)

- [Documentación para milestone 4 (CI)](https://github.com/Carlossamu7/CC1-Conservatorio/issues/60)
- [Fichero de Travis-CI](https://github.com/Carlossamu7/CC1-Conservatorio/issues/61)
- [Fichero de Circle-CI](https://github.com/Carlossamu7/CC1-Conservatorio/issues/69)

***Milestone*** 5 - [Microservicios](https://github.com/Carlossamu7/CC1-Conservatorio/milestone/8)

- [Documentación para milestone 5 (Microservicios)](https://github.com/Carlossamu7/CC1-Conservatorio/issues/74)
- [Implementación de microservicios](https://github.com/Carlossamu7/CC1-Conservatorio/issues/75)
- [Actualizar `cc.yaml`](https://github.com/Carlossamu7/CC1-Conservatorio/issues/76)
- [Actualizar el gestor de tareas](https://github.com/Carlossamu7/CC1-Conservatorio/issues/79)

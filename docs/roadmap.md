## *Roadmap*

Para consultar exclusivamente los *milestone* con sus *historias de usuario* entrar [aquí](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/milestones_hu.md). La planificación del desarrollo del proyecto es la siguiente:

**Fase 1**. La primera fase está dedicada a la administración de asignaturas del Conservatorio tal relacionado con el *milestone* [Administrador](https://github.com/Carlossamu7/CC1-Conservatorio/milestone/4).

- [[HU1] Como administrador quiero dar de alta una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/12)

> Se ha implementado la clase `Asignatura.py` [aquí](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Asignatura.py).

- [[HU2] Como administrador quiero modificar una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/13)
- [[HU3] Como administrador quiero borrar una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/14)

**Fase 2**. En esta segunda fase, tras haber gestionado la administración de asignaturas podemos empezar a gestionar los alumnos del Centro y permitir su matriculación o desmatriculación de las mismas. Esta fase se enmarca en el *milestones* [Alumno](https://github.com/Carlossamu7/CC1-Conservatorio/milestone/3).

- [[HU4] Como alumno quiero matricularme de ciertas asignaturas.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/15)

> Se ha implementado la clase `Alumno.py` [aquí](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Alumno.py). Gestionada la comprobación de DNIs, no se dará de alta a ningún alumno con un DNI no válido en el sistema.

- [[HU5] Como alumno quiero desmatricularme de ciertas asignaturas.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/16)
- [[HU6] Como alumno quiero consultar mis asignaturas matriculadas.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/39)
- [[HU7] Como alumno quiero modificar la dirección de correo con la que el centro se pone en contacto conmigo.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/17)

**Fase 3**. Se añaden las funcionalidades relativas a las acciones que pueden realizar los alumnos en el sistema y cómo se relacionan con sus horarios o aulas de las asignaturas en las que están matriculados. Para realizar esto previamente se necesita haber desarrollado una administración correcta de las asignaturas, ya que no se podría acceder a esta información si no se gestiona correctamente la matriculación de asignaturas.

- [[HU8] Como alumno quiero consultar el horario de una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/18)
- [[HU9] Como alumno quiero consultar el aula de una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/19)
- [[HU10] Como alumno quiero saber mi horario completo.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/43)

> Se ha implementado la clase `Conservatorio.py` [aquí](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Conservatorio.py).

**Fase 4**. Se añaden funcionalidades relativas a la administración del Centro como saber el número de alumnos y asignaturas que en ese curso se están llevando a cabo. En esta fase se avanza la lógica de negocio del problema ya que se va a poder obtener información de qué asignaturas imparte un profesor o extraer los horarios completos de un profesor o las aulas a las que acuden semanalmente alumnos y profesores. Para ello es necesario que previamente se gestione bien la matriculación y gestión de asignaturas.

- [[HU11] Como administrador quiero saber en el número de alumnos y asignaturas del conservatorio.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/44)
- [[HU12] Como administrador quiero saber las asignaturas que imparte un profesor.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/45)
- [[HU13] Como administrador quiero saber el horario completo de un  profesor.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/46)
- [[HU14] Como administrador quiero saber las aulas que usa un profesor/alumno.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/47)

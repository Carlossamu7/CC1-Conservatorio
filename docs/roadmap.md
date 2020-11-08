## *Roadmap*

Para consultar exclusivamente los *milestone* con sus *issues* entrar [aquí](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/milestones_hu.md). La planificación del desarrollo del proyecto es la siguiente:

**Fase 1**. Comenzar el desarrollo de los *milestones* de [Administrador](https://github.com/Carlossamu7/CC1-Conservatorio/milestone/4) y de [Alumno](https://github.com/Carlossamu7/CC1-Conservatorio/milestone/3). Cuando dichos *milestone* se hayan alcanzado se dispondrá de un producto mínimamente viable (MVP).

- [[HU1] Como administrador quiero dar de alta una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/12)

> Se ha implementado la clase `Asignatura.py` [aquí](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Asignatura.py).

- [[HU4] Como alumno quiero matricularme de ciertas asignaturas.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/15)

> Se ha implementado la clase `Alumno.py` [aquí](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Alumno.py). Gestionada la comprobación de DNIs, no se dará de alta a ningún alumno con un DNI no válido en el sistema.

**Fase 2**. Avanzar esos MVP con nuevas historias de usuario que los hacen más funcionales.

- [[HU2] Como administrador quiero modificar una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/13)
- [[HU3] Como administrador quiero borrar una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/14)
- [[HU5] Como alumno quiero desmatricularme de ciertas asignaturas.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/16)
- [[HU6] Como alumno quiero consultar mis asignaturas matriculadas.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/39)
- [[HU7] Como alumno quiero modificar la dirección de correo con la que el centro se pone en contacto conmigo.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/17)

**Fase 3**. Introducir tests que comprueben y aseguren la calidad del código ya implementado ya que nuestro objetivo es desplegar la aplicación en la nube y estas pruebas confirmarán que el código hace lo que se espera que haga. Los tests comprobarán las HU de alumno y las de administrador.

**Fase 4**. Continuar con el desarrollo de la aplicación avanzando historias de usuario que necesitan de la comunicación de ambos microservicios.

- [[HU8] Como alumno quiero consultar el horario de una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/18)
- [[HU9] Como alumno quiero consultar el aula de una asignatura.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/19)
- [[HU10] Como alumno quiero saber mi horario completo.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/43)

> Se ha implementado la clase `Conservatorio.py` [aquí](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Conservatorio.py).

- [[HU11] Como administrador quiero saber en el número de alumnos y asignaturas del conservatorio.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/44)
- [[HU12] Como administrador quiero saber las asignaturas que imparte un profesor.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/45)
- [[HU13] Como administrador quiero saber el horario completo de un  profesor.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/46)
- [[HU14] Como administrador quiero saber las aulas que usa un profesor/alumno.](https://github.com/Carlossamu7/CC1-Conservatorio/issues/47)

**Fase 5**. Crear contenedores en donde almacenar la aplicación para permitir el despliegue de la misma en la nube.

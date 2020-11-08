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

  Y los siguientes métodos (además de `validoDNI()`):
    - `listaAsignaturas()`
    - `matriculaAsignatura()`
    - `desmatriculaAsignatura()`
    - `toString()`

- Clase [Conservatorio](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Conservatorio.py). Tiene los siguientes atributos:
    - `nombreConservatorio` (que es `MiConservatorio`, tiene `getter`)
    - `listaAlum` (`getter`)
    - `listaAsig` (`getter`)

  Y los siguientes métodos:
    - `getNumeroAlumnos()`
    - `getNumeroAsignaturas()`
    - `toString()`

  algunos más relacionados con los alumnos
    - `existAlumno()`
    - `darAltaAlumno()`
    - `getAlumno()`
    - `getEmail()`
    - `getAsignaturas()`
    - `getAlumnos()`
    - `getHorarioAlumno()`
    - `getAulasAlumno()`

  y otros más relacionados con las asignaturas
    - `existAsignatura()`
    - `darAltaAsignatura()`
    - `getAsignatura()`
    - `getProfesor()`
    - `getHorario()`
    - `getAula()`
    - `getListaAsignaturasProfesor()`
    - `getNombreAsignaturasProfesor()`
    - `getHorarioProfesor()`
    - `getAulasProfesor()`

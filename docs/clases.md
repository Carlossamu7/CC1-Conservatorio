- Clase [Alumno](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Alumno.py). Tiene los siguientes atributos:
    - nombre (`getter` y `setter`)
    - email (`getter` y `setter`)
    - dni (`getter`)
    - asignaturas (`getter` y `setter`)

  Y los siguientes métodos (además de `valido_dni()` y `valido_email`):
    - `matricula_asignatura()`
    - `desmatricula_asignatura()`
    - `to_string()`

- Clase [AsignaturaConcepto](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/AsignaturaConcepto.py). Tiene los siguientes atributos:
    - id (`getter`)
    - nombre_asignatura (`getter`)
    - curso (`getter`)
    - concepto (`getter`)

  Y los siguientes métodos:
    - `to_string()`

- Clase [Asignatura](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Asignatura.py). Tiene los siguientes atributos:
    - Hereda de AsignaturaConcepto
    - profesor (`getter` y `setter`)
    - horario (`getter` y `setter`)
    - aula (`getter` y `setter`)

  Y los siguientes métodos:
    - `to_String()`

- Clase [Conservatorio](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Conservatorio.py). Tiene los siguientes atributos:
    - `nombre_conservatorio` (que es `MiConservatorio`, tiene `getter`)
    - `dic_alumnos` (`getter`)
    - `dic_alumnos` (`getter`)

  Y los siguientes métodos:
    - `get_nombre_conservatorio()`
    - `get_diccionario_alumnos()`
    - `get_numero_alumnos()`
    - `get_diccionario_asignaturas()`
    - `get_numero_asignaturas()`
    - `to_string()`

  algunos más relacionados con los alumnos
    - `exist_alumno()`
    - `dar_alta_alumno()`
    - `get_alumno()`
    - `get_alumnos_nombre()`
    - `get_horario_asignatura_alumno()`
    - `get_horario_alumno()`
    - `get_aulas_alumno()`

  y otros más relacionados con las asignaturas
    - `exist_asignatura()`
    - `dar_alta_asignatura()`
    - `borrar_asignatura()`
    - `get_asignatura()`
    - `get_lista_asignaturas_profesor()`
    - `get_nombre_asignaturas_profesor()`
    - `get_horario_profesor()`
    - `get_aulas_profesor()`

## Clases

En primer lugar la **estructura del proyecto** es sencilla con dos clases:

```bash
src
├── Alumno.py
└── Asignatura.py
```

- Clase [Asignatura](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Asignatura.py). Tiene los siguientes atributos:
    - asignatura (`getter`)
    - profesor (`getter` y `setter`)
    - horario (`getter` y `setter`)
    - aula (`getter` y `setter`)

- Clase [Alumno](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Alumno.py). Tiene los siguientes atributos:
    - nombre (`getter` y `setter`)
    - email (`getter` y `setter`)
    - dni (`getter`)
    - asignaturas (`getter` y `setter`)

- Clase [Conservatorio](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Conservatorio.py). Tiene los siguientes atributos:
    - `nombreConservatorio` (que es `MiConservatorio`, tiene `getter`)
    - `listaAlum` (`getter`)
    - `listaAsig` (`getter`)

[Consultar con más detalle los métodos de estas clases.](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/clases.md)

#### Comprobación de la sintaxis:

Ejecutando las órdenes

```
python3.8 src/Alumno.py
python3.8 src/Asignatura.py
python3.8 src/Conservatorio.py
```

observamos que la sintaxis es correcta.

![](./docs/images/sem_02_03/sintaxis.png)

#### Tratamiento de errores

Los errores tratados por el sistema son los siguientes:

- En la clase `Alumno`:

    - Crear un alumno con un DNI no válido. Se lanza una excepción de tipo `ValueError` que informa diciendo: ``El DNI no es válido.``
    - Matricular una asignatura ya matriculada. Se lanza una excepción de tipo `ValueError` que informa diciendo: ``Asignatura ya matriculada.``
    - Desmatricular una asignatura no matriculada. Se lanza una excepción de tipo `ValueError` que informa diciendo: ``No existe tal asignatura.``

- En la clase `Conservatorio`:
    - Dar de alta un alumno que ya está dado de alta. Se lanza una excepción de tipo `ValueError` que informa diciendo: ``Ya existe un alumno con este DNI.``
    - Dar de alta una asignatura que ya está dada de alta. Se lanza una excepción de tipo `ValueError` que informa diciendo: ``Ya existe esta asignatura.``

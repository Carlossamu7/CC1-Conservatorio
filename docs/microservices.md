## Microservicios ##

Sobre la base de la clase hecha se va a diseñar una API consistente en una serie de rutas (API REST) y testearlo. También se va a crear la infraestructura necesaria para comenzar a ejecutarlo. Para ello, se va de usar el mismo fichero de construcción que hasta ahora, añadiendo las nuevas tareas. Esto también permite, por ejemplo, usar uno de los sistemas de integración continua creados para hacer una ejecución de prueba, en vez de ejecutar los tests.

### Framework ###

El primer paso es elegir el Framework que se va a usar para el desarrollo de la API. Tras una primera etapa de información acerca de las variantes más conocidas para `Python` podemos centrar el estudio en: `Hug`, `Flask`, `Django` y otros dos menos populares como `Pyramid`, y `Bottle`. Analizamos las ventajas y desventajas que nos ofrecen teniendo en cuenta nuestro proyecto. Enlaces relevantes del estudio: [enlace1](https://programacion.net/articulo/los_4_frameworks_web_mas_populares_para_python_1069), [enlace2](https://openwebinars.net/blog/los-4-mejores-frameworks-para-aplicaciones-de-python/) y [enlace3](https://blog.thedojo.mx/2019/03/12/tres-formas-de-crear-api-s-con-python.html).

- `Hug`. Es una pequeña biblioteca para crear API’s muy fáciles de entender y mantener. Provee un serie de herramientas que permiten hacer el API rápidamente, con poco código y siguiendo las mejores prácticas.

    El *holamundo* de `Hug` es así:
    ```
    import hug

    @hug.get()
    def hola_apis():
    return {"mensaje": "Hola API's"}
    ```

    Ventajas:
    - Documentación automática
    - Verificación y validación de parámetros (con *type hinting* de `Python3`)
    - Versionamiento de API´s.
    - Múltiples tipos de salida con sólo cambiar la configuración.
    - Extensibilidad y flexibilidad.

- `Flask`. Es una herramienta flexible para programar proyectos web en `Python`. Provee una capa mínima de ruteo y compatibilidad con WSGI, así como funcionalidades y helpers comunes para las tareas más comunes en desarrollo web. Entre las características de `Flask` están:
    - Integración por defecto con Jinja2
    - Soporte de cookies de sesión seguras
    - Servidor web para desarrollo y debuggeo
    - Sencillo, flexible y ligero.

    Debido a la sencillez también se mostrará el *holamundo* de `Flask`:
    ```
    from flask import Flask, jsonify
    app = Flask(__name__)
    @app.route("/")
    def hello():
        return jsonify({"message": "Hello World!"})
    ```

  Además `Flask` resulta ideal para los desarrolladores que:
    - aprender a programar.
    - preocuparse por las buenas prácticas y el código "elegante".
    - que quieran crear prototipos de forma rápida.
    - que necesitan una aplicación independiente.

- `Django`. Es un framework MVT (*Model-View-Template*, su propia variante del MVC) para desarrollar proyectos web robustos de manera rápida. Provee:

    - Un sistema de *templating* propio.
    - Un ORM (*Object Relational Mapper* - una capa de abstracción de la base de datos).
    - Ruteo robusto.
    - Sistema de configuración robusto y adaptable.
    - Interfaz de administración automática.
    - Administración de usuarios.
    - Ideal para desarrolladores que deseen construir algo rápidamente con potentes herramientas integradas.
    -  Es uno de los mayores framework web basado en `Python`.
    - Trabaja con PostgreSQL, MySQL, SQLite y Oracle pero esto nos es indiferente porque en el proyecto no hay bases de datos.

Sin embargo si se necesita algo para lo que `Django` no esté preparado éste requiere más experiencia técnica para modificarlo.
Por lo que he visto en esta [introducción](https://www.paradigmadigital.com/dev/introduccion-django-rest-framework/) resulta más técnico y complejo que los anteriores.

- `Pyramid`. Nació de una fusión entre *Pylons 1.0* y *repoze.bfg*. Este framework viene con *pilas incluidas*, pero no hace ninguna suposición acerca de los componentes del sitio web. Algunos detalles:
    - Su comunidad está creciendo rápidamente y cada día son más los desarrolladores que se suman al uso del framework.
    - La documentación es excelente y permite a los desarrolladores avanzar sin tener que contar con el apoyo de la comunidad.
    - Se esfuerza por ser minimalista, rápido y fiable.
    - Fue uno de los primeros frameworks web que fue compatible con `Python3`.

  Asimismo es ideal para:
    - Inicio rápido
    - Desarrolladores que trabajan en proyectos con la API
    - Prototipar un concepto
    - Desarrollo de aplicaciones web grandes, como un CMS o un KMS

- `Bottle`. Es un microframework muy simple que proporciona un mínimo de herramientas al desarrollador (enrutamiento, plantillas y una pequeña abstracción sobre WSGI). Se puede ejecutar en Python 3. Es ideal para:
    - Desarrolladores que buscan flexibilidad.
    - Crear una API web.
    - Personas que quieren desarrollar algo realmente simple.

Tras el estudio realizado la opción que mejor se adapta es `Flask`. Sus puntos a favor son que sea ideal para aprender a programar, que ayude a seguir buenas prácticas, que tenga un código elegante, la inmensa bibliografía y ejemplos que hay detrás de este framework y su posibilidad de usarlo con `ùnittest` que es el módulo que se usa en este proyecto para los tests.

Para el aprendizaje del microframework `Flask` se puede consultar este [video tutorial](https://www.youtube.com/watch?v=Esdj9wlBOaI).

[Documentación de Flask](https://flask.palletsprojects.com/en/1.1.x/).

### Diseño del API ###

En primer lugar es necesario conocer las buenas prácticas a la hora del diseño de una API Restful e intentar seguirlas lo máximo posible, esto nos ayudará a acercarnos a un código de calidad. En este [enlace](https://hackernoon.com/restful-api-designing-guidelines-the-best-practices-60e1d954e7c9) se encuentran algunas de ellas.

Durante el diseño de la API se han tomado las siguientes decisiones:
- Indicar el tipo en la ruta y en el argumento. Ejemplo:
```
# [HU10] Como alumno quiero saber mi horario completo
@app.route('/alumno/<string:id_alumno>/horario')
def get_horario_alumno(id_alumno: str):
    content = conser.get_horario_alumno(id_alumno)
    if(content=="No existe ningún alumno con ese DNI."):
        return jsonify({"Mensaje": content}), 404
    else:
        return jsonify({'Horario completo': content}), 200
```

- La petición `GET` es la que hay por defecto así que cuando no se indique nada se está usando esa.
- Los datos que se devuelven están en formato JSON.

Para tener algunas instancias en el Conservatorio se ha preparado el JSON [`conservatorio.json`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/data/conservatorio.json) el cual se leerá y permitirá la creación de los objetos pertinentes en la clase controladora. Comenzamos explicando el diseño de las rutas y los [códigos de estado](https://developer.mozilla.org/es/docs/Web/HTTP/Status).

#### Ruta `/`

Por elegancia se ha querido dar la bienvenida:

```
@app.route('/')
def hello_conser():
    return jsonify({'mensaje': "Bienvenido a MiConservatorio!"}), 200
```

#### Ruta `/asignatura`

| HU | Comando y ruta | Código de estado |
|--------|--------|---------|
| [[HU1]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/12) | `POST /asignatura` | 200, 400 |
| [[HU2]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/13) | `PUT /asignatura/<id_asignatura>` | 200, 400 |
| [[HU3]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/14) | `DELETE /asignatura/<id_asignatura>` | 200, 400 |
| [[HU17]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/78) | `GET /asignatura` | 200 |

#### Ruta `/alumno`

| HU | Comando y ruta | Código de estado |
|--------|--------|---------|
| [[HU4]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/15) | `POST /alumno/<id_alumno>/asignatura` | 200, 400, 404 |
| [[HU5]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/16) | `DELETE /alumno/<id_alumno>/asignatura/<nombre_asignatura>` | 200, 400, 404 |
| [[HU6]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/39) | `GET /alumno/<id_alumno>/asignatura` | 200, 404 |
| [[HU7]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/17) | `PUT /alumno/<id_alumno>` | 200, 400, 404 |
| [[HU8]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/18) | `GET /alumno/<id_alumno>/asignatura/<nombre_asignatura>/horario` | 200, 404 |
| [[HU9]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/19) | `GET /alumno/<id_alumno>/asignatura/<nombre_asignatura>/aula` | 200, 404 |
| [[HU10]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/43) | `GET /alumno/<id_alumno>/horario` | 200, 404 |
| [[HU11]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/44) | `GET /alumno/num` y `GET /asignatura/num` | 200 |
| [[HU15]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/57) | `POST /alumno` | 200, 400 |
| [[HU16]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/77) | `GET /alumno` | 200 |

#### Ruta `/profesor`

| HU | Comando y ruta | Código de estado |
|--------|--------|---------|
| [[HU12]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/45) | `GET /profesor/<nombre_profesor>/asignatura` | 200, 404 |
| [[HU13]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/46) | `GET /profesor/<nombre_profesor>/horario` | 200, 404 |
| [[HU14]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/47) | `GET /profesor/<nombre_profesor>/aula` y `GET /alumno/<id_alumno>/aula` | 200, 404 |

[Consultar `app.py`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/app.py).

### Configuración distribuida: `logs` ###

### Tests ###

Uno de los motivos de la elección de `Flask` es su fácil uso con `unittest`. A continuación vamos a comprobar que efectivamente es relativamente cómodo e intuitivo. No obstante antes de ello me gustaría introducir un programa que me ayudó a comprobar las peticiones HTTP por ejemplo en el caso de que haya que enviar un formulario. Dicho programa es [insomnia.rest](https://insomnia.rest/) disponible también en linux.

En él puedo crear `requests` que se quedan guardados, almacenan el tipo de petición, la ruta e inclusive el contenido JSON que hay que enviar. Es una herramienta excelente para el desarrollo del API. Personalmente he creado al menos un `request` por cada HU. Dejo una captura del mismo:

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_10_11_12/insomnia.png)

- Arranco la app en `setUp()`

```
import unittest
import json
import sys
sys.path.append('src')

from app import app, lee_json

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
```

- Cuando tengo que incluir nuevos alumnos o asignaturas en el Conservatorio para un test lo leo de del JSON [`conservatorio_test.json`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/data/conservatorio_test.json).

- Tengo cuidado con los `DELETE` ya que los cambios en la aplicación cliente persisten entre diferentes test  por lo que habitualmente volveré a dejar la instancia tal y como estaba.

- Siempre se testea el código de estado:

  ```
  self.assertEqual(response.status_code, 200)
  ```

- Siempre se testea el contenido, o una parte del mismo para asegurar el buen funcionamiento:

  ```
  self.assertIn(b'Asignaturas', response.data)
  ```

- En caso de que una función pueda devolver varias salidas en función de la existencia de un determinado objeto u otro se realizará una petición para cada posible caso.

[Consultar `testApp.py`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/tests/testApp.py).

### Avance del proyecto ###

- Mejoras en la descripción de todas las historias de usuario. Asimismo se ha tenido en cuanta la aportación realizada en la [úndecima sesión](https://github.com/JJ/CC-20-21/blob/master/sesiones/11-semana.md). Se ha dado un formato común a todas, añadiendo notas técnicas e indicando las rutas de la API específicas de dicha HU.

    [Consultar HUs](https://github.com/Carlossamu7/CC1-Conservatorio/issues).

- Nuevas historias de usuario:
    - [[HU16] Como administrador quiero obtener un listado de los alumnos y su información](https://github.com/Carlossamu7/CC1-Conservatorio/issues/77)
    - [[HU17] Como administrador quiero obtener un listado de las asignaturas y su información](https://github.com/Carlossamu7/CC1-Conservatorio/issues/78).

- [Documentación de HUs y milestones actualizada](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/milestones_hu.md).

- Trabajo futuro: comprobar los tipos devueltos en el `request.json` de las peticiones HTTP.

##### Gestor de tareas #####

Se han añadido dos nuevas tareas al gestor: `build` que realmente no hace nada y `execute` y que ejecuta la API en `http://127.0.0.1:4000/`.

```
# Construcción
build:
	echo 'No es necesario realizar build'

# Ejecuta la app
execute:
	python3 src/app.py
```

##### Dockerfile de despliegue #####

Se ha cambiado la ejecución final respecto del `Dockerfile` normal:
```
# Ejecutamos la API
CMD ["make", "execute"]
```

[Dockerfile_execute](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/Dockerfile_execute)

La hacemos disponible en [DockerHub](https://hub.docker.com/repository/docker/carlossamu7/cc1-conservatorio_exec).

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_10_11_12/docker_run.png)

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_10_11_12/docker_push.png)

Uno el repo de DockerHub creado al de GitHub.

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_10_11_12/docker_hub.png)

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

### Configuración distribuida: `logs` ###

### Tests ###

### Avance del proyecto ###

- Mejoras en la descripción de todas las historias de usuario. Asimismo se ha tenido en cuanta la aportación realizada en la [úndecima sesión](https://github.com/JJ/CC-20-21/blob/master/sesiones/11-semana.md). Se ha dado un formato común a todas, añadiendo notas técnicas e indicando las rutas de la API específicas de dicha HU.

    [Consultar HUs](https://github.com/Carlossamu7/CC1-Conservatorio/issues).

- Nuevas historias de usuario:
    - [[HU16] Como administrador quiero obtener un listado de los alumnos y su información](https://github.com/Carlossamu7/CC1-Conservatorio/issues/77)
    - [[HU17] Como administrador quiero obtener un listado de las asignaturas y su información](https://github.com/Carlossamu7/CC1-Conservatorio/issues/78).

- [Documentación de HUs y milestones actualizada](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/milestones_hu.md).

- Trabajo futuro: comprobar los tipos devueltos en el `request.json` de las peticiones HTTP.

#### Gestor de tareas ####

## Integración continua

En sistemas de desarrollo ágil quien desarrolle tiene que asegurar que el código pasa todos los tests antes de ser desplegado o simplemente incorporado a la rama principal, porque los tests son la especificación de los requisitos. Para ello se escriben una serie de tests que se ejecutan automáticamente al añadir o modificar código.

Estos tests tienen el fin obvio de asegurar la calidad del mismo, pero también en un entorno de desarrollo colaborativo permiten integrar código fácilmente asegurándose de que no se rompa nada. En cada incorporación de código la ejecución automática de los tests asegura que el código sigue cumpliendo las especificaciones. Se va a configurar el repositorio del proyecto para que se pasen los tests, en diferentes ambientes, automáticamente.

Para ello se van a elegir varios sistemas de integración continua, se va a dar de alta el usuario y posteriormente vincularlos con la cuenta de *GitHub* conectando con el repositorio del proyecto. Del mismo modo se va a aprovechar el contenedor docker en alguno de los sistemas de integración continua.

#### Justificación de la elección de los sistemas de CI ####

Las sistemas de integración continua que se van a valorar son *Travis-CI*, *Circle-CI*, *Jenkins* y *Shippable*. Se han consultado algunos enlaces: [enlace principal](https://www.altexsoft.com/blog/engineering/comparison-of-most-popular-continuous-integration-tools-jenkins-teamcity-bamboo-travis-ci-and-more/) y [enlace complementario](https://www.trustradius.com/products/jfrog-pipelines/reviews).

***Travis-CI***

- Ventajas:
    - Lleva mucho tiempo y es una herramienta muy popular.
    - Fácil instalación y configuración.
    - Conectividad directa con *GitHub*.
    - Copia de seguridad de la compilación reciente. Siempre que ejecuta una nueva compilación, *Travis-CI* clona su repositorio de GitHub en un nuevo entorno virtual.

- Desventajas:
    - No tiene CD (distribución continua).
    - Alojamiento solo de GitHub. Solo ofrece soporte para proyectos alojados en *GitHub*, los equipos que usan *GitLab* o cualquier otra alternativa, se ven obligados a confiar en otra herramienta de CI.

***Circle-CI***

- Ventajas:
    - Interfa de usuario simple.
    - Atención al cliente de alta calidad. Los miembros de la comunidad de *StackShare* destacan el rápido soporte de *Circle-CI*: responden a las solicitudes en 12 horas.
    - *Circle-CI* ejecuta todo tipo de pruebas de software, incluidos entornos web, móviles y de contenedores.
    - Almacenamiento en caché de la instalación de requisitos y dependencias de terceros.
    - Sin necesidad de depuración manual. *Circle-CI* tiene la función de depuración *Debug* a través de SSH.
    - Permite usar imágenes docker.

- Desventajas:
    - Automatización excesiva: cambia el entorno sin previo aviso, lo que puede ser un problema.
    - Sin almacenamiento en caché de imágenes de Docker.

***Jenkins***

- Ventajas:
    - Es gratuita.
    - Integraciones ilimitadas. Jenkins puede integrarse con casi cualquier programa externo utilizado para desarrollar aplicaciones. Le permite utilizar tecnología de contenedores como *Docker* y *Kubernetes*. Tiene muchos plugins.
    - Distribución de compilaciones y cargas de prueba en varias máquinas.

- Desventajas:
    - La documentación no es suficiente.
    - Tiene una interfaz de usuario muy pobre.

***Shippable***

- Ventajas:
    - Usa docker. Esto le da una buena velocidad de compilación.
    - Usa una sintaxis de superconjunto para *Travis-CI* y, por lo tanto, su configuración de compilación de *Travis-CI* funcionará.

- Desventajas:
    - A veces, las compilaciones se cuelgan en el paso de aprovisionamiento del nodo y, por lo general, lleva mucho tiempo completar este paso.
    - Hubo tiempos de inactividad del servicio intermitentes.
    - Solía tener problemas frecuentes con la autenticación y solía evitar que inicie sesión y esto sucedió varias veces, pero su equipo de soporte resuelve la mayoría de los problemas rápidamente.

Finalmente, tras este análisis, se ha decidido usar *Travis-CI* porque es la herramienta mejor valorada cuando se trabaja con *GitHub* como es el caso. Las buenas prácticas aconsejan usar una herramienta de integración continua adicional. La segunda elección llevada a cabo es *Circle-CI* ya que sus ventajas son numerosas y permite usar imágenes docker, lo cual nos permitirá experimentar un poco.

### Integración continua: `Travis CI`

El primer sistema de integración continua que se va a usar es [Travis-CI](https://travis-ci.com/). A continuación se enumeran los pasos seguidos para darse de alta, activar el repositorio y configurar correctamente la integración continua:

1. En primer lugar hay que darse de alta en Travis.

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_08_09/travis_init.png)

2. A continuación hay que conectar con la cuenta de GitHub. Para activar el repositorio que deseemos, en este caso el del proyecto, vamos a *Perfil-Settings-Migrate*. Escogiendo la opción *Only selected repositories* seleccionamos aquellos que deseamos. En mi caso ya lo tenía hecho. Veamos:

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_08_09/migrate.png)

3. Ahora hay que configurar el archivo [`.travis.yml`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/.travis.yml).

- No es conveniente poner excesivas versiones del lenguaje. En mi caso no tengo excesiva dependencia de bibliotecas y por tanto de versiones del lenguaje así que he elegido tres: `3.6`, `3.7` y `3.8`.

- Para instalar las dependencias del proyecto encontramos `install` esto lanzará la orden `make install` que instala aquellas librerías que se encuentran en [`requirements.txt`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/requirements.txt).

- Finalmente se lanzan los test, que es el objetivo de la integración continua.

```
#Lenguaje de programación
language: python

# Versiones
python:
  - "3.6"
  - "3.7"
  - "3.8"
  - "nightly"

# Instala dependencias
install:
  - make install

# Ejecuta los tests
script:
  - make test
```

*Travis* permite saber cuál es la versión mínima de tu lenguaje y también saber si funciona con la versión *latest*. En esta [documentación](https://docs.travis-ci.com/user/languages/python/) encontramos que podemos ejecutar la última versión de `Python` con `nightly`. Básicamente apunta a una versión de desarrollo reciente de la compilación de `Python`. Como versión mínima he elegido la `3.6` porque con la `3.5` no funciona porque dicha versión realiza un ordenamiento sobre algunas estructuras de datos como el las listas haciendo que los test fallen. [Aquí se puede consultar el error](https://travis-ci.com/github/Carlossamu7/CC1-Conservatorio/jobs/460798577).

En la página web de *Travis-CI* encontramos un *badget* de este repositorio, el cual situaremos en el `README` del proyecto y que nos indica si se ha pasado el *build*.

[![TravisCI](https://travis-ci.com/Carlossamu7/CC1-Conservatorio.svg?branch=master)](https://travis-ci.com/github/Carlossamu7/CC1-Conservatorio)

### Integración continua adicional: `Circle CI`

El sistema de integración continua adicional que se va a usar es [Circle-CI](https://circleci.com/) A continuación se enumeran los pasos seguidos para darse de alta, activar el repositorio y configurar correctamente la integración continua:

1. En primer lugar hay que darse de alta. Entramos en *Sign Up* y a continuación *Sign Up with GitHub*. Autorizamos el acceso. Le indicamos la organización a usar, que va a ser nuestra cuenta de *GitHub*.

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_08_09/circle_init.png)

2. Una vez registrados indicamos el repositorio y hacemos click en *Set Up Project*.

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_08_09/set_up_project.png)

3. Nos propone un fichero de configuración y yo he elegido la opcióon *Use Existing Config*.

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_08_09/configyml.png)

Como aún no está disponible el fichero no lo encuentra.

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_08_09/noconfigyml.png)

4. Por último es momento de configurar [`config.yml`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/.circleci/config.yml) en el directorio `.circleci`.

- Se va a usar la imagen docker disponible en *Docker Hub*. En un apartado posterior se comentarán más detalles acerca de esto.

- Utilizando el gestor de tareas se ejecutan los tests implementados.

```
---
version: 2.1

jobs:
    test:
        docker:
            - image: carlossamu7/my_docker:latest
        steps:
            - checkout
            - run: make tests

workflows:
    build_test:
        jobs:
            - test
```

Por úlitmo se incluye el *badget* de *Circle CI* en este repositorio, el cual situaremos en el `README` del proyecto y que nos indica si se ha pasado el *build*.

[![CircleCI](https://circleci.com/gh/Carlossamu7/CC1-Conservatorio.svg?style=svg)](https://app.circleci.com/pipelines/github/Carlossamu7/CC1-Conservatorio)

### Gestor de tareas

El gestor de tareas automatiza los cometidos de cualquier proyecto software. Hasta ahora siempre nos ha simplificado las tareas de instalación, comprobación de sintaxis, ejecución de tests, etc. En la integración continua también juega un papel fundamental haciendo que la tarea de instalación de dependencias y ejecución de tests sea sencilla.

El gestor que se eligió para este proyecto fue [`Makefile`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/Makefile). Veamos el papel que juega en cada uno de los sistemas de CI usados:

- *Travis CI*. Realiza dos tareas. La primera es `install` en donde se instalan las dependencias mediante `make install` que básicamente instala los paquetes contenidos en [`requirements.txt`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/requirements.txt). La segunda es `script` en donde se lanzan todos los tests unitarios mediante `make test`.

- *Circle CI*. En el trabajo `test` el paso fundamental, una vez descargada la imagen, es ejecutar `make test` lo cual comprueba los tests unitarios del código del proyecto.

### Uso del contenedor de Docker en CI

Algunos sitemas de integración continua permiten aprovechar la imagen generada para el proyecto lo cual resulta muy útil. Este es el caso del sistema de integración continua *Circle CI* por lo que se ha aprovechado el docker generado para el proyecto.

En el fichero de configuración se indica la imagen a usar, en donde indicamos que se use la subida en *Docker Hub*: `carlossamu7/my_docker:latest`. Veamos:

```
docker:
    - image: carlossamu7/my_docker:latest
```

La ventaja es que este entorno ya está preparado para la ejecución de los tests. Tiene todas las dependencias instaladas así como el paquete `build-essentials` en donde está gestor de tareas *GNU Make*.

### Avance del proyecto

- [Sobrescribir el método `__eq__` de `Python` para las clases Alumno y Asignatura](https://github.com/Carlossamu7/CC1-Conservatorio/issues/70).
    - Para hacerlo en Asignatura va a ser conveniente hacerlo en AsignaturaConcepto.
    - Es necesario hacer tests para cada uno de estos métodos `__eq__`.
    - Una vez implementados usarlos en los tests de la clase Conservatorio. Esta era el objetivo primordial.

#### Otros avances del proyecto ####

Mejorando la entrega correspondiente al *Desarrollo basado en tests* se han hecho muchas mejoras y modificaciones del proyecto, las cuales recuerdo que son las siguientes:

- [Cambiar a notación `snake_case`](https://github.com/Carlossamu7/CC1-Conservatorio/issues/62).

- [Se deben justificar todas las modificaciones de un objeto](https://github.com/Carlossamu7/CC1-Conservatorio/issues/58). No había ninguna HU indicando que se puedan modificar todas las asignaturas a la vez a través `set_asignaturas` por lo que es eliminado.

- [Se debe almacenar la asignaturas de la forma más adecuada para las HUs](https://github.com/Carlossamu7/CC1-Conservatorio/issues/59). Almacenar las asignaturas en una lista. Usar la clase asignatura.

- [Usar fixtures en los tests de Python](https://github.com/Carlossamu7/CC1-Conservatorio/issues/63)

- Se ha relacionado el *issue* [Cambio en el tratamiento de asignaturas dentro de Alumno](https://github.com/Carlossamu7/CC1-Conservatorio/issues/42) con las HU correspondientes.

- [Como desarrollador quiero comprobar la validez de un email para [HU7]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/64)

- [Como desarrollador, voy a distinguir entre AsignaturaConcepto (concepto, material, curso) y la Asignatura (profesor, aula, horario)](https://github.com/Carlossamu7/CC1-Conservatorio/issues/65)

- [Se debe almacenar la asignaturas de la forma más adecuada para las HUs](https://github.com/Carlossamu7/CC1-Conservatorio/issues/59). Efectivamente, no es lo más eficiente guardar las asignaturas como un único *string* separado por comas y espacios. Se ha valorado la opción de usar la clase `Asignatura` pero no parece lo más correcto porque dicha clase tiene el aula, horario, profesor y otros campos que no son de interés para el alumno. Es más, es posible que en el momento de la matriculación esto no se sepa (en la Universidad normalmente sí se sabe en el momento de la matriculación pero no es así en los Conservatorios) y la asignatura no esté dada de alta. Por eso me parece lo más correcto cambiar a usar una lista de *strings* lo cual elimina el método `lista_asignaturas` y simplifica y hace más eficiente algunas cosas.

- [Añadir comprobación de tipos](https://github.com/Carlossamu7/CC1-Conservatorio/issues/68)

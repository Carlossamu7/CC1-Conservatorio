## Integración continua

En sistemas de desarrollo ágil quien desarrolle tiene que asegurar que el código pasa todos los tests antes de ser desplegado o simplemente incorporado a la rama principal, porque los tests son la especificación de los requisitos. Para ello se escriben una serie de tests que se ejecutan automáticamente al añadir o modificar código.

Estos tests tienen el fin obvio de asegurar la calidad del mismo, pero también en un entorno de desarrollo colaborativo permiten integrar código fácilmente asegurándose de que no se rompa nada. En cada incorporación de código la ejecución automática de los tests asegura que el código sigue cumpliendo las especificaciones. Se va a configurar el repositorio del proyecto para que se pasen los tests, en diferentes ambientes, automáticamente.

Para ello se van a elegir varios sistemas de integración continua, se va a dar de alta el usuario y posteriormente vincularlos con la cuenta de *GitHub* conectando con el repositorio del proyecto. Del mismo modo se va a aprovechar el contenedor docker en alguno de los sisstemas de integración continua.

Las elecciones que se van a valorar son *Travis-CI*, *Circle-CI*, *Jenkins* y *Shippable*.

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

# Versiones (de momento)
python:
  - "3.6"
  - "3.7"
  - "3.8"

# Instala dependencias
install:
  - make install

# Ejecuta los tests
script:
  - make test
```

En la página web de travis encontramos un *badget* de este repositorio, el cual situaremos en el `README` del proyecto y que nos indica si se ha pasado el *build*.

[![Build Test](https://travis-ci.org/Carlossamu7/CC1-Conservatorio.svg?branch=master)](https://travis-ci.org/github/Carlossamu7/CC1-Conservatorio)

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
```

Por úlitmo se incluye el *badget* de *Circle CI* en este repositorio, el cual situaremos en el `README` del proyecto y que nos indica si se ha pasado el *build*.

[![Build Test](https://circleci.com/gh/Carlossamu7/CC1-Conservatorio.svg?style=svg)](https://github.com/Carlossamu7/CC1-Conservatorio)

### Gestor de tareas

### Uso del contenedor de Docker en CI

### Avance del proyecto

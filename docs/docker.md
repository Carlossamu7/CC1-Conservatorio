## Docker

El principal objetivo del uso de [Docker]((https://www.docker.com/)) u otra infraestructura de contenedores es aislar la ejecución de una aplicación de forma que sea mucho más fácil desplegarla, incluyendo los datos y el estado en el que se encuentre en un momento determinado.

### Elección del contenedor base

El primer paso en la contenerización es elegir la imagen base que se va a usar. Para tomar una elección adecuada hay que conocer bien las necesidades del proyecto, lenguaje de programación que necesita, versiones que soporta, paquetes necesarios, etc.

Este proyecto está siendo desarrollado en `Python3` y se pretende que tenga soporte para distintas versiones del lenguaje, incluida la última estable `Python3.9`. Del mismo modo, se va a necesitar instalar algunos paquetes mediante `pip3` por lo que hay que instalarlo también en caso de la imagen base no lo tenga. Se puede consultar información de [python en Docker Hub](https://hub.docker.com/_/python?tab=tags).

En esta sección de va a construir un contenedor básico para este lenguaje con la instalación (en caso de que sea necesario) de `pip3`. Se va a valorar el tamaño que ocupa el contenedor y también el tiempo necesario en su ejecución. Tras un primer estudio e investigación las imágenes base que se van a testear son: *Fedora*, *Alpine*, *Ubuntu 18.04*, *Ubuntu 20.04*, *Python3.8-slim* y *Python3.9-slim*.

Necesitaremos de las siguientes órdenes en este proceso.

```
docker build --no-cache -t nombre_imagen -f Dockerfile .
docker run --rm nombre_imagen
```

- **Fedora**. En *Fedora* es necesario instalar `python3` y `pip3`, lo cual aumentará el tamaño de la imagen base. El [`Dockerfile`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/Dockerfiles/Fedora/Dockerfile) es el siguiente:

```
FROM fedora:latest
WORKDIR /home/CC1-Conservatorio
RUN dnf install -y python3-setuptools python3-devel redhat-rpm-config
COPY hola.py ./
CMD python3 hola.py
```

Peso: 389 MB.
Tiempo: Medio.

- **Alpine-Python**. Trae instalado `Python3` pero no `pip3`, el cual podemos instalar con `apk add py3-pip`. El [`Dockerfile`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/Dockerfiles/Alpine/Dockerfile) es:

```
FROM python:alpine
WORKDIR /home/CC1-Conservatorio
RUN apk add py3-pip
COPY hola.py ./
CMD python hola.py
```

Peso: 96.6 MB.
Tiempo: Bajo.

- **Ubuntu 18.04**. No tiene sentido valorar una imagen anterior a esta porque queremos que nuestro proyecto tenga LTS *Long Term Support*. Esta imagen tiene LTS hasta 2023. Es necesario instalar `pip` pues no viene por defecto. El [`Dockerfile`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/Dockerfiles/Ubuntu18/Dockerfile) es:

```
FROM ubuntu:18.04
WORKDIR /home/CC1-Conservatorio
RUN apt update \
  && apt -y upgrade \
  && apt install -y python3-pip

COPY hola.py ./
CMD python3 hola.py
```

Peso: 401 MB.
Tiempo: Alto.

- **Ubuntu 20.04**. Esta es la versión *Focal Fossa*, la última estable de *Ubuntu* y tiene LTS hasta abril de 2025. Al igual que antes es necesario instalar `pip`. El [`Dockerfile`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/Dockerfiles/Ubuntu20/Dockerfile) es:

```
FROM ubuntu:20.04
WORKDIR /home/CC1-Conservatorio
RUN apt update \
  && apt -y upgrade \
  && apt install -y python3-pip
COPY hola.py ./
CMD python3 hola.py
```

Peso: 500 MB.
Tiempo: Alto.

- **Python 3.8-slim**. Esta versión *slim* es una de las grandes candidatas pues está optimizada para ello. El [`Dockerfile`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/Dockerfiles/Slim3.8/Dockerfile) es:

```
FROM python:3.8-slim
WORKDIR /home/CC1-Conservatorio
COPY hola.py ./
CMD python3 hola.py
```

Peso: 113 MB.
Tiempo: Bajo.

- **Python 3.9-slim**. Esta versión *slim* de `Python3.9` es una de las grandes candidatas pues está optimizada para ello. El [`Dockerfile`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/Dockerfiles/Slim3.9/Dockerfile) es:

```
FROM python:3.9-slim
WORKDIR /home/CC1-Conservatorio
COPY hola.py ./
CMD python3 hola.py
```

Peso: 115 MB.
Tiempo: Bajo.

---

Observamos las imágenes creadas localmente con `docker images`. Los resultados son los siguientes:

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_06_07/image_base.png)

Las imágenes de *Fedora*, *Ubuntu 18.04* y *Ubuntu 20.04* son demasiado pesadas y han tomado un tiempo considerable en su construcción. Es cierto que podríamos tratar de borrar algún fichero o funcionalidad con el objetivo de optimizar lo máximo posible los respectivos contenedores. Sin embargo, estamos demasiado lejos de las otras tres opciones.

La opción de *Alpine* es muy ligera pero después de leer este [artículo](https://pythonspeed.com/articles/alpine-docker-python/) en donde se exponen las razones por la que usar *Alpine* para `Python` puede hacer que sea más lento descarto esta opción. El artículo expone que puede hacer:
1. Las construcciones más lentas.
2. Las imágenes más grandes.
3. Desperdicia tiempo.
4. En ocasiones introduce algunos errores en tiempo de ejecución.

Finalmente la imagen base escogida es **Python 3.8-slim** por ser 2MB más ligera que la otra y por la buena crítica y estudio que recibe en [este artículo de Abril de 2020](https://pythonspeed.com/articles/base-image-python-docker-images/). Es importante saber que esta imagen base tiene por debajo *debian-buster*.

### `Dockerfile`

Queremos que la creación del entorno de pruebas sea reproducible, por lo que se va a diseñar un `Dockerfile`. El `Dockerfile` final está disponible [aquí](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/Dockerfile) pero lo observamos a continuación:

```
# Imagen base
FROM python:3.8-slim

# Etiqueta que indica el mantenedor
LABEL maintainer="carlossamu7@gmail.com"

# Creación de un usuario sin permisos, carpeta y actualización de pip
RUN useradd -m -s /bin/bash nonrootuser \
    && mkdir -p app/test \
    && python3 -m pip install --upgrade pip \
    && apt-get update \
    && apt-get install -y build-essential

# Directorio de trabajo
WORKDIR /app/test

# Fichero con los paquetes necesarios
COPY requirements.txt .

# Instalación de paquetes
RUN pip install -r requirements.txt \
    && rm requirements.txt

# Usamos el usuario creado
USER nonrootuser

# Ejecutamos los tests
CMD ["make", "test"]
```

Se ha diseñado siguiendo buenas prácticas como las disponibles en este [primer enlace](https://www.atareao.es/tutorial/docker/buenas-practicas-con-docker/) y este [segundo enlace](https://medium.com/@serrodcal/buenas-pr%C3%A1cticas-construyendo-im%C3%A1genes-docker-8a4f14f7ad1d):

- Por supuesto, uso de mayúsculas en las instrucciones.

- Según [esta información oficial](https://docs.docker.com/engine/reference/builder/) el uso de `MAINTEINER` está deprecado y es conveniente indicarlo en `LABEL`.

- Seguridad: es importante que siempre que sea posible se ejecute la aplicación como un usuario no privilegiado. Creación de usuario [así](https://stackoverflow.com/questions/39855304/how-to-add-user-with-dockerfile). Es preferible usar `useradd`, y le indicamos que cree una carpeta en el home (`-m`) y cuál va a ser el shell (`-s`)

    > `useradd` es un comando que ejecuta un binario del sistema, mientras que `adduser` es un script en perl que utiliza el binario `useradd`.

- En mi caso uso `Makefile` que no viene por defecto. Es necesario instalar el paquete `build-essential`.

- Del mismo modo copio el fichero `requirements.txt`, instalo las dependencias y lo elimino.

- El docker va a ser testeado con `docker run -t -v pwd:/app/test nick-estudiante/nombre-del-repo` por lo que establezco como `WORKDIR` el directorio `/app/test`. Para ejecutar los tests en el docker, incluyo finalmente `CMD ["make", "test"]`.

Con la orden `docker inspect ID | jq` vemos información acerca del contenedor indicado en ID. En este caso el contenedor tiene 8 capas.

### Docker Hub y actualización automática

[Docker Hub](https://hub.docker.com/) es un repositorio público en la nube, similar a Github, para distribuir los contenidos. Es el sitio oficial y gratuito (de momento) en donde la comunidad informática puede subir o usar contenedores. En este apartado se va a explicar cómo subir el docker y como sincronizar dicho docker con GitHub para automatizar las actualizaciones.

#### Subiendo el docker

En primer lugar nos damos de alta utilizando preferentemente el mismo *nickname* que en GitHub. Posteriormente podremos subir contenedores. Para ello nos identificamos, asignamos una etiqueta al docker y finalmente lo subimos. Se muestran las órdenes para realizar cada una de estas acciones:

```
docker login --username=carlossamu7
docker tag ce61eb646e2c carlossamu7/my_docker:latest
docker push carlossamu7/my_docker
```

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_06_07/docker_login.png)

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_06_07/docker_tag_push.png)

Se puede observar el docker subido correctamente en la plataforma.

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_06_07/my_docker_hub.png)

[Enlace al contenedor en Docker Hub](https://hub.docker.com/r/carlossamu7/my_docker).

#### Actualización automática

La plataforma Docker Hub permite automatizar la construcción de nuestro docker de manera que cuando pusheemos al repositorio del proyecto en GitHub se reconstruya también en Docker Hub si es necesario. Para ello tenemos que establecer la siguiente configuración:

1. Vamos al docker y en la opción *Manage Repository* hay una pestaña *Builds*. Encontramos la posibilidad de conectarlo a un repositorio y que se automatice la construcción.

2. Elegimos la opción de GitHub en mi caso y conectamos la cuenta de Docker Hub con la de GitHub.

3. Una vez conectada la cuenta volvemos al docker y le indicamos la cuenta y el repositorio con el que se va a automatizar. Dejo el resto de opciones a como vienen por defecto. Veamos:

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_06_07/connecting.png)

4. Finalmente seleccionamos *Save and Build*. Finalmente ya tenemos automatizada la construcción:

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_06_07/autobuild.png)

### Uso de registros alternativos

Este es el [tutorial](https://docs.github.com/es/free-pro-team@latest/packages/using-github-packages-with-your-projects-ecosystem/configuring-docker-for-use-with-github-packages) que he seguido.

1. El primer paso es [crear un token de acceso personal](https://docs.github.com/es/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token). Ir a *Settings* - *Developer settings* - *Personal access tokens* y hacer click en *Generate new token*. Le damos un nombre y seleccionamos los accesos del token, es importante copiar el token generado porque después ya no tendremos oportunidad.

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_06_07/personal_token.png)

2. A continuación vamos a *Feature preview* y habilitamos haciendo click en `Enable` el soporte mejorado de contenedores. Esto permite compartir más fácilmente los contenedores, establecer permisos de acceso granularmente y acceso anónimo a imágenes de contenedores públicos.

3. Para loguearnos hemos guardado el token en un fichero `TOKEN.txt` en el `home` y ejecutamos `cat ~/TOKEN.txt | docker login ghcr.io -u carlossamu7 --password-stdin`.

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_06_07/github_login.png)

4. Asignamos el `tag` indicando el nombre de la imagen y la versión y pusheamos.

```
docker tag <ID> ghcr.io/carlossamu7/my_docker:0.1.0
docker push ghcr.io/carlossamu7/my_docker:0.1.0
```

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_06_07/github_tag_push.png)

Observamos el resultado en la sección *Packages* de GitHub.

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_06_07/github_docker.png)

5. Finalmente, dentro del paquete GitHub nos indica que podemos conectar el docker a un repositorio. Hacemos esta configuración eligiendo el repositorio del proyecto. Veamos:

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_06_07/github_docker_conectado.png)

### Avance del proyecto

Siguiendo las indicaciones dadas en entregas anteriores del proyecto el avance en esta fase se ha centrado en:

- [Atributos privados para las clases implementadas](https://github.com/Carlossamu7/CC1-Conservatorio/issues/54).

- [Eliminar algunos métodos innecesarios](https://github.com/Carlossamu7/CC1-Conservatorio/issues/55).
    - Es mejor devolver el objeto Alumno y que éste se manipule. Eliminados por tanto métodos de la clase Conservatorio como `getNombreAlumno`, `getEmail` y `getAsignaturas`.
    - Ídem con las Asignaturas. Eliminados los métodos de la clase Conservatorio `getProfesor`, `getHorario` y `getAula`.

- Devolver una estructura de datos manejable en vez de concatenar strings.
    - [[HU10]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/43), método `getHorarioAlumno`.
    - [[HU14]](https://github.com/Carlossamu7/CC1-Conservatorio/issues/47), método `getAulasProfesor` y `getAulasAlumno`.

- [Optimizar la búsqueda de alumnos mediante el uso de diccionarios](https://github.com/Carlossamu7/CC1-Conservatorio/issues/56) en [`Conservatorio.py`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/Conservatorio.py). Esto mejora la implementación de casi todas las HUs relacionadas con el Administrador del Conservatorio.

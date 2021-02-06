## Composición de servicios ##

Cuando una aplicación no cabe en un solo contenedor por la existencia de varios *tier*, o simplemente nodos que sirven para almacenar datos, es necesario usar `docker-compose` para describir de forma repetible la forma como se van a conectar tales contenedores. Se va a diseñar, usando `docker-compose` y describiendo la infraestructura mediante un fichero `docker-compose.yml`, un servicio que incluya varios contenedores.

### Estructura del clúster ###

Este proyecto admite diversas composiciones de servicios. Tras adentrarme en el mundo de la composición de servicios, las inmensas posibilidades que ofrece así como las ventajas y utilidades de las mismas parece razonable realizar una orquestación de la aplicación desarrollada con una base de datos y un cliente.

Después de indagar estudios y desarrollos parecidos a esta idea en el lenguaje en cuestión, Python, se encuentran ejemplos como esta [orquestación de servicios con docker-compose](https://www.atareao.es/tutorial/docker/orquestar-contenedores-con-docker-compose/). Por un lado se levanta un contenedor con la aplicación y por otro un contenedor con la base de datos. En caso de querer cambiar la versión de la app o del servidor de la base de datos solo habría que parar el contenedor y levantar otro. Este ejemplo es cuanto menos interesante, todo el código esta disponible en este [repo](https://github.com/atareao/chiquito-compose).

Respecto al cliente, consiste en una aplicación implementada en Python que haga peticiones HTTP a la API desde la composición de los contenedores. Dichas peticiones deben cubrir las diferentes historias de usuario del proyecto.

Por cuestiones de tiempo lamentablemente sólo se va a realizar la composición de contenedores con el cliente, dejando como un **trabajo futuro** para este proyecto la comunicación con la base de datos.

### Configuración de cada uno de los contenedores de la composición ###

En esta sección se van a explicar los diferentes contenedores del clúster. El primero de ellos es el **servidor**. El código de la API REST está en [`app.py`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/app.py). Básicamente lanza el servicio al puerto y host indicados en el dichero de configuración [.env](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/.env).

```
if __name__ == '__main__':
    # Ejecutamos la app
    app.run(debug=True, host=HOST, port=PORT)
```

El `Dockerfile` del servidor copia los ficheros necesarios para la ejecución y expone el puerto 80 que es el que usa la API para recibir peticiones HTTP. Después de este proceso lanza la ejecución.

```
# Imagen base
FROM python:3.8-slim

# Etiqueta que indica el mantenedor
LABEL maintainer="carlossamu7@gmail.com"

# Creación de un usuario sin permisos, carpeta y actualización de pip
RUN useradd -m -s /bin/bash nonrootuser \
    && mkdir -p app/ \
    && python3 -m pip install --upgrade pip \
    && apt-get update \
    && apt-get install -y build-essential

# Directorio de trabajo
WORKDIR /app/

# Fichero con los paquetes necesarios
COPY ./src /app/src/
COPY ./data /app/data/
COPY .env /app/
COPY requirements.txt /app/
COPY Makefile /app/

# Instalación de paquetes
RUN pip install -r /app/requirements.txt \
    && rm /app/requirements.txt

# Usamos el usuario creado
USER nonrootuser

# Expongo el puerto 80
EXPOSE 80

# Ejecutamos la API
CMD ["make", "execute"]
```

[Consultar `execute.Dockerfile`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/execute.Dockerfile)

Observemos un ejemplo de dicha ejecución mediante la orden `docker run --rm -p 80:80 cc1-conservatorio_server`:

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_13_14_15/soloserver.png)

A continuación pasamos a hablar del **cliente**. Para este comenzamos construyendo la ruta donde realizar las peticiones así como algunas variables que se usarán continuamente.

```
# Variables de entorno
load_dotenv()
PORT = os.getenv('PORT')
CLIENT_HOST = os.getenv('CLIENT_HOST')

# Variables globales
RUTA = "http://" + CLIENT_HOST + ":" + str(PORT)
PARAM = {'content-type': 'application/json'}
```

Las peticiones se van a hacer mediante [`requests`](https://pypi.org/project/requests/) que admiten los diferentes verbos HTTP. Para mostrar resultados al cliente de dichas peticiones se ha implementado la siguiente función sencilla, que devuelve tanto el estado HTTP como el contenido JSON de la respueta.

```
def print_request(response):
    print("Código de estado: {}".format(response.status_code))
    print(response.text)
```

Ahora ya se pueden realizar todas las peticiones que se deseen. En mi caso voy a cubrir la totalidad de las historias de usuario. El código está en [`client.py`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/src/client.py). Para la primera sería:

```
# [HU1] Como administrador quiero dar de alta una asignatura
print("[HU1] Como administrador quiero dar de alta una asignatura")
print_request(requests.post(RUTA + "/asignaturas", json.dumps(asignatura), headers=PARAM))
```

Vamos a realizar la contenerización del cliente. Esta es aún más sencilla que el anterior. El objetivo es lanzar la ejecución del cliente.

```
# Imagen base
FROM python:3.8-slim

# Etiqueta que indica el mantenedor
LABEL maintainer="carlossamu7@gmail.com"

# Creación de un usuario sin permisos, carpeta y actualización de pip
RUN useradd -m -s /bin/bash nonrootuser \
    && python3 -m pip install --upgrade pip \
    && apt-get update

# Directorio de trabajo
WORKDIR .

# Fichero con los paquetes necesarios
COPY ./src/client.py requirements_client.txt .env ./

# Instalación de paquetes
RUN pip install -r requirements_client.txt \
    && rm requirements_client.txt

# Usamos el usuario creado
USER nonrootuser

# Abrir puerto 8001
EXPOSE 8001

CMD ["python3", "client.py"]
```

[Consultar `client.Dockerfile`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/client.Dockerfile)

### Fichero de composición ###

Para aprender cómo construir el fichero de composición `docker-compose.yml` he comenzado revisando algunas [guías](https://www.linode.com/docs/guides/how-to-use-docker-compose/) así como [documentación oficial](https://docs.docker.com/compose/gettingstarted/). El `docker-compose.yml` de esta composición queda así:

```
version: '3'
services:
  server:
    build:
      context: .
      dockerfile: execute.Dockerfile
    restart: always
    ports:
    - "80:80"

  client:
    build:
      context: .
      dockerfile: client.Dockerfile
    depends_on:
      - server
    ports:
    - "8001:8001"
```

A continuación se comentan y explican algunos aspectos de dicho fichero:

- Observamos claramente los dos servicios, cliente y servidor. En ambos se usa el parámetro `build` en vez de `image` para que se construya el contenedor. Consultando [aquí](https://docs.docker.com/compose/compose-file/compose-file-v3/#build) descubrimos parámetros disponibles para la opción `build` en la versión `3`. En concreto yo voy a indicarle dónde están los respectivos archivos `Dockerfile` y el contexto.

- Por otro lado se usa [`restart`](https://docs.docker.com/compose/compose-file/compose-file-v3/#restart) cuyos posibles valores son: `"no"` (por defecto), `always`, `on-failure` y `unless-stopped`. En mi caso establezco este parámetro en `always`.

- La clave `ports` indica el mapeo de puertos.

- En el cliente se usa `depends_on` para indicar las dependencias y como es lógico necesitamos primero la construcción y lanzamiento del servidor para poder levantar el cliente.

*Nota:* Otro parámetro relevante que se puede usar es [`container_name`](https://docs.docker.com/compose/compose-file/compose-file-v3/#container_name) para indicar el nombre que se le debe asignar al contenedor después de la construcción. En mi caso no lo he usado porque me gusta el que genera por defecto:

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_13_14_15/images.png)

[Consultar `docker-compose.yml`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docker-compose.yml)

Ejecutando `docker-compose up --build` en el directorio donde se encuentra el `docker-compose.yml` realizamos la composición. En primer lugar el servidor:

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_13_14_15/server.png)

Y a continuación la parte del cliente:

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_13_14_15/client.png)

### Test ###

Una vez realizada la composición y estando el contenedor levantado se pueden realizar peticiones desde fuera del mismo. De hecho, podríamos volver a ejecutar el cliente, con todas las historias de usuario, pero desde fuera de la composición.

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_13_14_15/compose.png)

En el [material de la asignatura](http://jj.github.io/CC/documentos/temas/Composicion_de_contenedores) encontramos un ejemplo de *GitHub Actions* que testea la composición. A partir de él voy se ha construido un test para este proyecto. Se lanzará en los push y en los PR.

```
name: Comprobar que docker compose funciona
on: [push,pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Construye el cluster
    run: docker-compose up -d
    - name: Testea el cluster
    run: wget http://localhost:80/ || exit 1
    - name: Testea asignaturas
    run: wget http://localhost:80/asignaturas || exit 1
    - name: Testea alumnos
    run: wget http://localhost:80/alumnos || exit 1
```

[Consultar `test-docker-compose.yml`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/.github/workflows/test-docker-compose.yml)

Comprobamos el correcto funcionamiento del *workflow*:

![](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/images/sem_13_14_15/testcompose.png)

![docker-compose](https://github.com/Carlossamu7/CC1-Conservatorio/workflows/Comprobar%20que%20docker%20compose%20funciona/badge.svg)

### Avance ###

Mejoras indicadas en microservicios:
- [La definición de rutas no debe contener ninguna lógica de negocio](https://github.com/Carlossamu7/CC1-Conservatorio/issues/84)
- [No se pueden poner números mágicos en el código](https://github.com/Carlossamu7/CC1-Conservatorio/issues/85)
- [Renombrar rutas a plural](https://github.com/Carlossamu7/CC1-Conservatorio/issues/86)

Otros avances:
- Tras crear mi primera *GitHub Actions* he sentido la necesidad de realizar más pruebas. Normalmente uso yamllint en mi local después de modificar alguno de los ficheros que tienen dicha extensión. He creado una sencilla acción para ello en [.github/workflows/yaml.yml](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/.github/workflows/yaml.yml).

![YAML](https://github.com/Carlossamu7/CC1-Conservatorio/workflows/Comprobando%YAML/badge.svg)

[Consultar issues relevantes](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docs/milestones_hu.md).

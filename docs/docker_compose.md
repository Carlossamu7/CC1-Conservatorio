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

[`execute.Dockerfile`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/execute.Dockerfile)

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

[`client.Dockerfile`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/client.Dockerfile)

### Fichero de composición ###

Para aprender cómo construir el fichero de composición `docker-compose.yml` he comenzado revisando algunas [guías](https://www.linode.com/docs/guides/how-to-use-docker-compose/) y [documentación oficial](https://docs.docker.com/compose/gettingstarted/)

Otros valores son: no (por defecto), always y on-failure.

Consultando [aquí](https://docs.docker.com/compose/compose-file/compose-file-v3/#build) descubrimos parámetros disponibles para la opción `build` en la versión `3`. En concreto yo voy a indicarle el archivo `Dockerfile` y el contexto.

[`docker-compose.yml`](https://github.com/Carlossamu7/CC1-Conservatorio/blob/master/docker-compose.yml)

### Test ###

### Avance ###

Mejoras indicadas en microservicios:
- [La definición de rutas no debe contener ninguna lógica de negocio](https://github.com/Carlossamu7/CC1-Conservatorio/issues/84)
- [No se pueden poner números mágicos en el código](https://github.com/Carlossamu7/CC1-Conservatorio/issues/85)
- [Renombrar rutas a plural](https://github.com/Carlossamu7/CC1-Conservatorio/issues/86)

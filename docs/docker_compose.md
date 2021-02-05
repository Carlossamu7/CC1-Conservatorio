## Composición de servicios ##

Cuando una aplicación no cabe en un solo contenedor por la existencia de varios tier, o simplemente nodos que sirven para almacenar datos, es necesario usar `docker-compose` para describir de forma repetible la forma como se van a conectar tales contenedores. Se va a diseñar, usando `docker-compose` y describiendo la infraestructura mediante un fichero `docker-compose.yml`, un servicio que incluya varios contenedores, incluyendo uno cuyo contenido exclusivo sea almacenar datos.

### Estructura del clúster ###

Este proyecto admite diversas composiciones de servicios. Tras adentrarme en el mundo de la composición de servicios, las inmensas posibilidades que ofrece así como las ventajas y utilidades de las mismas parece razonable realizar una orquestación de la aplicación desarrollada con una base de datos y un cliente.

Después de indagar estudios y desarrollos parecidos a esta idea en el lenguaje en cuestión, Python, se encuentran ejemplos como esta [orquestación de servicios con docker-compose](https://www.atareao.es/tutorial/docker/orquestar-contenedores-con-docker-compose/). Por un lado se levanta un contenedor con la aplicación y por otro un contenedor con la base de datos. En caso de querer cambiar la versión de la app o del servidor de la base de datos solo habría que parar el contenedor y levantar otro. Este ejemplo es cuanto menos interesante, todo el código esta disponible en este [repo](https://github.com/atareao/chiquito-compose).

Respecto al cliente, consiste en una aplicación implementada en Python que haga peticiones HTTP a la API desde la composición de los contenedores.

Por cuestiones de tiempo sólo se va a realizar la composición de contenedores con cliente, dejando como un trabajo futuro para este proyecto la comunicación con la base de datos.

### Configuración de cada uno de los contenedores de la composición ###

### Fichero de composición ###

Para aprender cómo construir el fichero de composición `docker-compose.yml` he comenzado revisando algunas [guías](https://www.linode.com/docs/guides/how-to-use-docker-compose/) y [documentación oficial](https://docs.docker.com/compose/gettingstarted/)

Otros valores son: no (por defecto), always y on-failure.

Consultando [aquí](https://docs.docker.com/compose/compose-file/compose-file-v3/#build) descubrimos parámetros disponibles para la opción `build` en la versión `3`. En concreto yo voy a indicarle el archivo `Dockerfile` y el contexto.

### Test ###

### Avance ###

Mejoras indicadas:
- [La definición de rutas no debe contener ninguna lógica de negocio](https://github.com/Carlossamu7/CC1-Conservatorio/issues/84)
- [No se pueden poner números mágicos en el código](https://github.com/Carlossamu7/CC1-Conservatorio/issues/85)
- [Renombrar rutas a plural](https://github.com/Carlossamu7/CC1-Conservatorio/issues/86)

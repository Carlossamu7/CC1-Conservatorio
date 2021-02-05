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

# Expongo el puerto 8000
EXPOSE 8000

# Ejecutamos la API
CMD ["make", "execute"]

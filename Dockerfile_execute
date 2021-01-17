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

# Ejecutamos la API
CMD ["make", "execute"]

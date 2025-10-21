Estos son los comandos dia a dia que utilizo para interactuar con Docker desde la línea de comandos.

## Comandos Básicos de Docker
- `docker ps`: Lista los contenedores Docker en ejecución.
- `docker ps -a`: Lista todos los contenedores Docker, incluyendo los que no están en ejecución.
- `docker images`: Muestra todas las imágenes Docker disponibles localmente.
- `docker pull [nombre_imagen]`: Descarga una imagen Docker desde un repositorio (por ejemplo, Docker Hub).
  - `docker pull [nombre_imagen]:[tag]`: Descarga una imagen Docker específica con la etiqueta (tag) indicada.
- `docker exec -it [nombre_contenedor o ID] /bin/bash`: Abre una terminal interactiva dentro de un contenedor en ejecución.
- `docker logs [nombre_contenedor o ID]`: Muestra los logs de un contenedor específico.
- `docker stop [nombre_contenedor o ID]`: Detiene un contenedor en ejecución.
- `docker start [nombre_contenedor o ID]`: Inicia un contenedor detenido.
- `docker update [nombre_contenedor o ID] --restart=always`: Configura un contenedor para que se reinicie automáticamente.
- `docker inspect [nombre_contenedor o ID]`: Muestra detalles técnicos y configuración de un contenedor.
  - `docker inspect [nombre_imagen]`: Muestra detalles técnicos y configuración de una imagen.
  - `docker inspect -f '{{.NetworkSettings.IPAddress}}' [nombre_contenedor o ID]`: Obtiene la dirección IP de un contenedor.
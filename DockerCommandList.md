Estos son los comandos dia a dia que utilizo para interactuar con Docker desde la línea de comandos.

## Comandos Básicos de Docker
- `docker ps`: Lista los contenedores Docker en ejecución.
- `docker ps -a`: Lista todos los contenedores Docker, incluyendo los que no están en ejecución.
- `docker images`: Muestra todas las imágenes Docker disponibles localmente.
- `docker pull [nombre_imagen]`: Descarga una imagen Docker desde un repositorio (por ejemplo, Docker Hub).
  - `docker pull [nombre_imagen]:[tag]`: Descarga una imagen Docker específica con la etiqueta (tag) indicada.
- `docker exec -it [nombre_contenedor o ID] /bin/bash`: Abre una terminal interactiva dentro de un contenedor en ejecución.
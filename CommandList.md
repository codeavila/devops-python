En este documento se describen algunos comandos que son utiles para interactuar con el sistema operativo desde la línea de comandos.
Normalmente son estos los que utilizo en mi dia a día, pero hay muchos más disponibles dependiendo del sistema operativo y las herramientas instaladas.

## Comandos Básicos del Sistema

- `ls`: Lista los archivos y directorios en el directorio actual.
- `cd [directorio]`: Cambia el directorio actual al especificado.
- `pwd`: Muestra la ruta del directorio actual.
- `mkdir [nombre_directorio]`: Crea un nuevo directorio con el nombre especificado.
- `mkdir -p [ruta_directorio]`: Crea un nuevo directorio y todos los directorios padres necesarios en la ruta especificada.
- `mv [origen] [destino]`: Mueve o renombra un archivo o directorio.
- `rm [archivo]`: Elimina el archivo especificado.
- `rm -rf [directorio]`: Elimina un directorio y todo su contenido de forma recursiva.
- `cp [origen] [destino]`: Copia un archivo o directorio al destino especificado.
- `touch [archivo]`: Crea un nuevo archivo vacío o actualiza la fecha de modificación de un archivo existente.
- `cat [archivo]`: Muestra el contenido de un archivo en la terminal.
- `cat [archivo] | grep [texto]`: Busca y muestra las líneas que contienen el texto especificado en un archivo.
- `tail -f [archivo]`: Muestra las últimas líneas de un archivo y sigue mostrando nuevas líneas a medida que se agregan.
- `df -h`: Muestra el uso del espacio en disco de todos los sistemas de archivos montados en un formato legible.
- `watch -n [segundos] [comando]`: Ejecuta un comando repetidamente cada cierto número de segundos y muestra su salida.
- `grep -r [texto] [directorio]`: Busca recursivamente el texto especificado en todos los archivos dentro del directorio dado.
- `kill -9 [PID]`: Fuerza la terminación de un proceso utilizando su ID de proceso (PID).
- `top`: Muestra una lista dinámica de los procesos en ejecución y su uso de recursos del sistema.
- `!$`: Ejecuta el último comando utilizado en la terminal.
- `ping [dirección_ip o dominio]`: Envía paquetes ICMP a una dirección IP o dominio para verificar la conectividad de red.
- `curl [url]`: Descarga el contenido de la URL especificada o realiza solicitudes HTTP.
- `ifconfig` o `ip addr`: Muestra la configuración de red y las interfaces de red del sistema.
- `find [directorio] -name [nombre_archivo]`: Busca un archivo con el nombre especificado dentro del directorio dado y sus subdirectorios.
  - `find [directorio] *.[extensión]`: Busca todos los archivos con la extensión especificada dentro del directorio dado y sus subdirectorios.
- `history`: Muestra el historial de comandos utilizados en la terminal.
  - `history | grep [texto]`: Busca en el historial de comandos aquellos que contienen el texto especificado.
  - `history [number]`: Muestra los últimos 'número' de comandos del historial.

- `cron`: Permite programar tareas para que se ejecuten automáticamente en intervalos regulares.
- `crontab -e`: Edita las tareas programadas.
- `crontab -r`: Elimina todas las tareas programadas del usuario actual.

``` Estructura de una línea en crontab:
* * * * *
| | | | |- Día de la semana (0 - 7) (Domingo=0 o 7)
| | | |- Mes (1 - 12)
| | |- Día del mes (1 - 31)
| |- Hora (0 - 23)
|- Minuto (0 - 59)
```
Ejemplo: `0 2 * * 1 /ruta/al/script.sh` ejecuta el script todos los lunes a las 2:00 AM.

- `journalctl -u [nombre_servicio]`: Muestra los logs de un servicio gestionado por systemd.
- `systemctl status [nombre_servicio]`: Muestra el estado actual de un servicio gestionado por systemd.
- `systemctl start [nombre_servicio]`: Inicia un servicio gestionado por systemd.
- `systemctl stop [nombre_servicio]`: Detiene un servicio gestionado por systemd.
- `systemctl restart [nombre_servicio]`: Reinicia un servicio gestionado por systemd.
- `ps aux | grep [nombre_proceso]`: Muestra información sobre todos los procesos en ejecución.
- `lsof -i :[puerto]`: Muestra los procesos que están utilizando el puerto especificado.
- `chmod +x [archivo]`: Otorga permisos de ejecución a un archivo.
- `iptables -L`: Muestra las reglas actuales del firewall configurado con iptables.
- `tar -cvf [archivo.tar.gz] [directorio o archivo]`: Crea un archivo comprimido en formato tar.gz del directorio o archivo especificado.
- `tar -xvf [archivo.tar.gz]`: Extrae el contenido de un archivo comprimido en formato tar.gz.
  - `z flag`: Indica que el archivo está comprimido con gzip, pero es mejor que "tar" lo detecte automáticamente, asi que no es "necesario" usarla. Ejemplo: `tar -xzvf [archivo.tar.gz]`.
- `unzip [archivo.zip]`: Extrae el contenido de un archivo comprimido en formato zip.
- `ssh [usuario]@[dirección_ip o dominio]`: Establece una conexión SSH con un servidor remoto.
- `scp [archivo] [usuario]@[dirección_ip o dominio]:[ruta_destino]`: Copia un archivo a un servidor remoto utilizando SCP.
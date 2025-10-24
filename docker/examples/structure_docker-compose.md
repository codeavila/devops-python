# Estructura de un archivo docker-compose.yml para apps Python Flask
```yaml
version: "3.9"
```
> Históricamente declaraba el formato del archivo. Con Compose v2 y la Compose Specification ya no es necesario (puedes omitirlo); el CLI moderno entiende el spec actual sin version. Mantenerlo no rompe, pero la recomendación hoy es omitido. 


```yaml
services:
```
Todo lo que corre como contenedor se define aquí como servicios. 
<img width="2480" height="3508" alt="DevOps-Python_2_1761317101716" src="https://github.com/user-attachments/assets/811a742b-1b19-4576-b553-d6dfd319b5c9" />


```yaml
  web:
```
Nombre lógico del servicio. Se usa para el hostname interno y para componer nombres de contenedor/red. 
Docker Documentation

```yaml
    build:
      context: .
      dockerfile: Dockerfile
```
build indica que Compose construirá la imagen desde tu Dockerfile.
context: . = envía el directorio actual como contexto de build (respeta tu .dockerignore).
dockerfile te deja especificar un nombre alterno si no es Dockerfile.

Best practice: mantener el contexto chico (usa .dockerignore) para builds más rápidos. 
Docker Documentation
<img width="2480" height="3508" alt="DevOps-Python_3_1761320570248" src="https://github.com/user-attachments/assets/d0d182b9-4cb4-4fb6-9cc9-50595acc10ea" />

```yaml
    image: flask-hello:prod
```
Nombre/etiqueta de la imagen resultante. Útil para versionar (p.ej. flask-hello:2025.10.23) y “promover” entre entornos. 

```yaml
    container_name: flask_hello
```
Nombre fijo del contenedor. Tip: en entornos multi-proyecto, suele preferirse no fijarlo para evitar colisiones; deja que Compose nombre directorio_servicio_1. Úsalo solo si lo necesitas de verdad. 
Docker Documentation

```yaml
    ports:
      - "5000:5000"
```
Publica el puerto 5000 del host → 5000 del contenedor.

La app Flask (o Gunicorn según tu Dockerfile) escucha en 0.0.0.0:5000.
Tip: en dev puedes mapear a otro puerto host (8080:5000) si 5000 está ocupado. 
Docker Documentation

```yaml
    environment:
      # Variables que tu app necesite
      # APP_ENV: production
      # SECRET_KEY: "change_me"
```
Variables de entorno para configuración 12-factor (no secretos en la imagen).

```yaml
    volumes:
      - .:/app:rw
```
(dev-style) Monta el código del host dentro del contenedor (hot reload con --reload).

Best practice: en producción evita montar el código desde el host; usa imagen inmutable. Mantén este volumen solo para desarrollo. 


```yaml
    restart: unless-stopped
```
Política de reinicio: reanuda el contenedor si se cae, excepto si lo detuviste manualmente. Para reboots persistentes podrías evaluar always, pero unless-stopped suele ser lo correcto para servicios largos. 

```yaml
    healthcheck:
      test: ["CMD-SHELL", "curl -fsS http://localhost:5000/health > /dev/null || exit 1"]
      interval: 15s
      timeout: 5s
      retries: 3
```
Healthcheck: Compose puede monitorear la salud del servicio. Usa una ruta /health en tu app que devuelva 200 OK si todo está bien.
Por qué estos flags

```
-f, --fail → hace que curl retorne código ≠ 0 en HTTP 4xx/5xx (sin esto, puede devolver 0 aunque haya 404/500).

-s, --silent y -S, --show-error → silencio normal pero muestra el error si falla (útil en logs).
```

Redirijo la salida a /dev/null para no ensuciar logs del contenedor.
CMD-SHELL permite usar tuberías/|| exit 1 para forzar estado no saludable si curl falla.

```yaml
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```
Rotación de logs del driver json-file: evita llenar disco en VPS (el default no rota).

max-size y max-file son opciones oficiales del driver. Alternativa: driver local (rotación con compresión por defecto). 

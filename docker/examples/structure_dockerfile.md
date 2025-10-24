# Estructura recomendada de Dockerfile para apps Python Flask
```
FROM python:3.11-slim AS base
```
Por qué: imagen oficial ligera (slim) → menor superficie y tiempo de build. Las Official Images siguen procesos de revisión/seguridad y son buena base. 
<img width="2480" height="3508" alt="DevOps-Python_1_1761283686555" src="https://github.com/user-attachments/assets/e58be8ff-5b50-4105-b06f-74c5c2e46a64" />

```
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
```

PYTHONDONTWRITEBYTECODE=1 evita generar *.pyc → menos I/O y menos archivos en la imagen.

PYTHONUNBUFFERED=1 fuerza salida no bufferizada → logs inmediatos en contenedor (evitas “se cayó y no logueó”).

Ambas variables están recomendadas en la guía oficial de Docker para Python. 

```
RUN useradd -m appuser
```

No-root por defecto. Reducís privilegios: si alguien compromete el proceso, el daño se limita. Es best practice explícita: usa USER con un usuario dedicado. 

```
RUN apt-get update && apt-get install -y --no-install-recommends ...
    && rm -rf /var/lib/apt/lists/*
```

Paquetes del sistema solo si son necesarios y con --no-install-recommends para evitar “bloat”.

Limpieza de apt para no dejar cachés y reducir la imagen. (Patrón general de best practices en Docker). 

```
WORKDIR /app
```

Define el directorio de trabajo para las instrucciones siguientes (RUN, CMD, COPY, etc.). Si no existe, se crea. 

```
COPY requirements.txt /app/requirements.txt
```

Capa de caché inteligente: copiar primero requirements.txt permite que Docker reutilice la capa de dependencias si el código cambia pero los requisitos no. Acelera builds. (Patrón clásico de cacheo por orden). 

```
RUN pip install --no-cache-dir -r requirements.txt
```

Instalar sin cache → imágenes más pequeñas (no guardás ruedas/artefactos descargados). Recomendado en guías de seguridad y buenas prácticas. 

```
COPY --chown=appuser:appuser . /app
```

Copiás el código ya con propietario correcto → evitás archivos root:root que luego den problemas de escritura en runtime al correr como no-root. (Alineado a principio de menor privilegio). 

```
EXPOSE 5000
```

Documenta que el contenedor escucha en ese puerto (no publica). Sirve para tooling/orquestadores; para exponer fuera se usa -p/--publish. 
Docker Documentation

```
USER appuser
```

A partir de acá, todo corre sin root (runtime). Recomendación explícita de Docker para endurecer contenedores. 

```
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]
```

Gunicorn es el WSGI server recomendado para producción; flask run es para desarrollo. -w 2 → dos workers básicos; -b bind en 0.0.0.0. (Flask docs y práctica común en producción). 

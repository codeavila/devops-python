# Example of Dockerfile for a simple Flask application (production-ready baseline)
FROM python:3.11-slim AS base

# 1) Configuración de entorno
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 2) Crea usuario no-root por seguridad
RUN useradd -m appuser

# 3) Instala dependencias del sistema mínimas (si las necesitas)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential \
#  && rm -rf /var/lib/apt/lists/*

# 4) Carpeta de trabajo
WORKDIR /app

# 5) Copia solo requirements primero para aprovechar la cache de Docker
COPY requirements.txt /app/requirements.txt

# 6) Instala dependencias de Python sin cache
RUN pip install --no-cache-dir -r requirements.txt

# 7) Copia el código (ajusta propietario para evitar archivos root:root)
COPY --chown=appuser:appuser . /app

# 8) Expone el puerto de la app
EXPOSE 5000

# 9) Cambia a usuario no-root
USER appuser

# 10) Comando de arranque: Gunicorn (más robusto que 'flask run')
#     -w: workers; -b: bind address
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]

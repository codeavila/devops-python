# Construir y correr en desarrollo
docker compose -f docker-compose.yml up --build

# Construir y correr en “producción local”
docker compose up --build -d
docker compose ps
docker compose logs -f web

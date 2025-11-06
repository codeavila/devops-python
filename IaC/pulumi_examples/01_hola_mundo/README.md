# Pulumi + Docker: Hola Mundo

Pequeño ejemplo para desplegar un contenedor Flask usando Pulumi con Python y Docker local. Ideal para probar IaC sin credenciales en la nube.

## Requisitos
- Docker en ejecución.
- Python 3.8+ con `pip`.
- Pulumi CLI instalado y autenticado (puedes usar almacenamiento local con `pulumi login file://$HOME/.pulumi-local`).

## Estructura del proyecto
```
IaC/pulumi_examples/01_hola_mundo/
├── Pulumi.yaml
├── Pulumi.dev.yaml
├── README.md
├── __main__.py
├── requirements.txt
└── hello_app/
    ├── Dockerfile
    ├── app.py
    └── requirements.txt
```

`hello_app/` contiene la app Flask “Hola mundo”; Pulumi se encarga de construir la imagen y levantar el contenedor.

## Preparar entorno Python
```bash
cd IaC/pulumi_examples/01_hola_mundo
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecutar con Pulumi
1. Asegúrate de estar en un stack (el template trae `dev`):
   ```bash
   pulumi stack select dev
   ```
2. Previsualiza los cambios:
   ```bash
   pulumi preview
   ```
3. Aplica y levanta el contenedor:
   ```bash
   pulumi up
   ```
4. Abre <http://localhost:5000>; deberías ver el mensaje “Hola desde Pulumi + Docker”.

## Limpiar recursos
```bash
pulumi destroy
pulumi stack rm dev   # opcional, elimina el stack
```

## Personalizar
- Ajusta `pulumi-docker-hello:hostPort` en `Pulumi.dev.yaml` (o con `pulumi config set pulumi-docker-hello:hostPort 5001`) para mapear otro puerto.
- Modifica `hello_app/app.py` para devolver contenido distinto o añadir rutas.
- Usa `pulumi config` para crear más stacks (ej. `pulumi stack init qa`) manteniendo el mismo código.

Con este ejemplo tendrás tu primer flujo de IaC declarando contenedores Docker desde Python. A partir de aquí puedes extenderlo con redes, volúmenes, o conectarlo a proveedores cloud.

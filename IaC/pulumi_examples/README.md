# Pulumi con Python: Guía Rápida

Pulumi es una herramienta de Infraestructura como Código que permite describir y gestionar recursos de nube usando lenguajes de programación comunes. Con Python puedes usar librerías, clases, pruebas y reutilizar código para modelar infraestructura igual que modelas aplicaciones.

## ¿Por qué Pulumi?
- **Lenguajes conocidos**: escribe IaC con Python, TypeScript, Go, C#, Java o YAML.
- **Estado administrado**: Pulumi guarda el estado de tus recursos (Stack State) en su servicio gestionado o en backends auto hospedados como S3, Azure Blob, GCS, etc.
- **Infra multi-nube**: soporta AWS, Azure, GCP, Kubernetes, Docker y más de 100 proveedores.
- **Reutilizable**: usa funciones, clases o componentes para compartir patrones dentro del equipo.

## Conceptos clave
- **Project**: carpeta con tu código Pulumi (`Pulumi.yaml` + código Python en `__main__.py` u otros módulos).
- **Stack**: instancia de un proyecto (por ejemplo `dev`, `qa`, `prod`). Cada stack mantiene su propio estado y variables de configuración.
- **State**: archivo JSON que Pulumi usa para saber qué recursos administras. Puede vivir en Pulumi Service (por defecto) o en backends como S3, Azure Blob, GCS, etc.
- **Providers**: plugins que permiten crear recursos específicos (AWS, Azure, Docker...). Deben instalarse con `pulumi plugin install` o se descargan automáticamente al usar `pulumi up`.

## Requisitos
- Python 3.8 o superior (recomendado 3.10+).
- `pip` y `virtualenv` o `pipenv` para manejar dependencias.
- [Pulumi CLI](https://www.pulumi.com/docs/install/) instalada y autenticada (`pulumi login`).
- Credenciales del proveedor que vayas a usar (por ejemplo variables de AWS).

## Crear un proyecto nuevo
```bash
mkdir 01_api
cd 01_api
pulumi new python
```
Pulumi te pedirá:
1. Nombre del proyecto (por defecto toma el nombre de la carpeta).
2. Descripción breve.
3. Nombre del stack inicial (ej. `dev`).

El template genera:
- `Pulumi.yaml`: metadatos del proyecto.
- `Pulumi.dev.yaml`: archivo de configuración para el stack `dev`.
- `requirements.txt`: dependencias de Python para Pulumi.
- `__main__.py`: punto de entrada donde defines recursos.

## Entorno virtual y dependencias
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Flujo de trabajo básico
1. **Define recursos** en `__main__.py`. Por ejemplo:
   ```python
   import pulumi
   from pulumi_aws import s3

   bucket = s3.Bucket("demo-bucket")
   pulumi.export("bucket_name", bucket.id)
   ```
2. **Previsualiza** los cambios:
   ```bash
   pulumi preview
   ```
3. **Aplica** los cambios reales:
   ```bash
   pulumi up
   ```
4. **Mira el estado** y salidas:
   ```bash
   pulumi stack output
   pulumi stack
   ```
5. **Elimina** la infraestructura cuando no la necesites:
   ```bash
   pulumi destroy
   ```

## Configuración por stack
Pulumi permite variables por stack:
```bash
pulumi config set aws:region us-east-1
pulumi config set api:replicas 3 --stack dev
```
En código las lees con:
```python
config = pulumi.Config("api")
replicas = config.get_int("replicas") or 1
```

## Buenas prácticas
- Guarda los archivos del stack (ej. `Pulumi.dev.yaml`) en el repositorio.
- Protege credenciales usando `pulumi config set --secret clave valor`.
- Usa `pulumi preview` en CI/CD antes de aplicar.
- Crea componentes reutilizables para redes, bases de datos, etc.
- Versiona tus scripts igual que cualquier repositorio de código.

## Documentación y recursos
- Documentación oficial: <https://www.pulumi.com/docs/>
- Referencia de paquetes Python de Pulumi: <https://www.pulumi.com/registry/>
- Ejemplos en Python: <https://github.com/pulumi/examples/tree/master/python>

Con esta base puedes empezar a modelar la API Docker del repositorio, o cualquier otro recurso de infraestructura, directamente desde Python.

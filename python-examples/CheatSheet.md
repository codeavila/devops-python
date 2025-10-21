# Shebang y permisos de ejecución
El shebang es una línea especial al inicio de un script que indica al sistema operativo qué intérprete usar para ejecutar el archivo. En Python, se usa comúnmente para permitir que los scripts se ejecuten directamente desde la línea de comandos sin necesidad de invocar explícitamente el intérprete de Python.
## 1) primera línea del archivo:
#!/usr/bin/env python3

## 2) permisos de ejecución
chmod +x script.py

## 3) ejecutarlo
./script.py

# Crear un entorno virtual
Un entorno virtual en Python es un entorno aislado que permite gestionar dependencias específicas para un proyecto sin afectar al resto del sistema o a otros proyectos. Esto es especialmente útil para evitar conflictos entre diferentes versiones de paquetes.
```bash
python -m venv nombre_del_entorno
source nombre_del_entorno/bin/activate  # En Linux/Mac
nombre_del_entorno\Scripts\activate  # En Windows
```

# Modo estricto en Visual Studio Code para tipos de datos
Para habilitar el modo estricto en Visual Studio Code y mejorar la verificación de tipos en Python, puedes configurar las opciones de Pylance en el archivo `settings.json` de tu proyecto. Esto ayuda a detectar errores relacionados con los tipos de datos durante el desarrollo.

Esto es solo visual en el editor y no afecta la ejecución del código.

```json
{
    "python.analysis.typeCheckingMode": "strict"
}
```
Hay tres niveles de verificación de tipos:
- off: No se realiza verificación de tipos. 
- basic: Verificación de tipos básica.
- strict: Verificación de tipos estricta.

# Redondear números
Python proporciona varias funciones integradas para redondear números:
- round(): Redondea un número al entero más cercano o a un número específico de decimales.
- math.floor(): Redondea hacia abajo al entero más cercano.
- math.ceil(): Redondea hacia arriba al entero más cercano.

```python
import math

# Ejemplos de redondeo
print(round(3.5))      # Salida: 4
print(math.floor(3.5))  # Salida: 3
print(math.ceil(3.5))   # Salida: 4
```



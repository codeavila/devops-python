# Infraestructura como Código (IaC)

```
TL;DR

IaC ayuda a tratar la infraestructura con las mismas reglas del desarrollo de software:
versionado, pruebas, revisiones y despliegues automatizados.
Adoptarla simplifica la operación diaria, reduce errores y 
acelera la entrega de valor en los equipos DevOps.
```

---

Infraestructura como Código (Infrastructure as Code) es la práctica de definir la infraestructura de una plataforma (servidores, redes, bases de datos, balanceadores) utilizando archivos de texto versionables. En lugar de crear recursos manualmente desde una consola, describimos el estado deseado y dejamos que las herramientas creen, cambien o eliminen los componentes necesarios.

## ¿Por qué es útil?
- Permite recrear entornos completos en cuestión de minutos.
- Reduce errores humanos al automatizar configuraciones repetitivas.
- Mejora la colaboración: los archivos se versionan igual que el código de la aplicación.
- Facilita auditorías y cumplimiento, porque todo cambio queda registrado.

## Enfoques comunes
- **Declarativo**: Describe el estado objetivo y la herramienta se encarga de alcanzarlo. Ej.: Terraform, CloudFormation.
- **Imperativo**: Indica paso a paso cómo construir la infraestructura. Ej.: Ansible, scripts de Bash o Python.

## Herramientas populares
- `Terraform`: Declarativa y multi-nube. Usa archivos `.tf` y un plan de ejecución antes de aplicar.
- `Ansible`: Imperativa, ideal para configurar servidores y aplicaciones. Usa playbooks YAML.
- `AWS CloudFormation` / `Azure ARM`: Plantillas declarativas específicas de cada nube.
- `Pulumi`: Permite definir infraestructura usando lenguajes como Python, TypeScript o Go.

## Buenas prácticas
- Controlar versiones y mantener ramas claras para cada cambio de infraestructura.
- Probar en entornos de staging antes de tocar producción.
- Mantener módulos reutilizables para redes, bases de datos, políticas, etc.
- Usar variables y archivos de configuración por entorno (dev, qa, prod).
- Integrar validaciones automáticas (lint, pruebas estáticas) en pipelines CI/CD.


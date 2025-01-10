# Proyecto de Automatización con Selenium y Python

Este proyecto utiliza Selenium y Python para automatizar tareas relacionadas con la generación de CURP y RFC. Además, integra un pipeline de CI/CD con GitHub Actions para garantizar la calidad y el correcto funcionamiento del código de manera automática.

## Tecnologías utilizadas

1. Python 3.13.1: Lenguaje principal del proyecto.
2. Selenium: Biblioteca para la automatización de navegadores web.
3. GitHub Actions: Plataforma de automatización para CI/CD.
4. Pytest: Herramienta para escribir y ejecutar pruebas.
5. Firefox: Navegador utilizado para la ejecución de pruebas automatizadas.


## Resultados del Pipeline

Puedes verificar el estado de las ejecuciones del pipeline en la sección Actions de este repositorio. Cada ejecución muestra:
1. Logs de instalación y configuración.
2. Resultados de las pruebas automatizadas.

El archivo de configuración se encuentra en `.github\workflows\pipeline.yml`.

## Ejemplo del pipeline en acción

![Pipeline](imagenes\captura-del-test.png)



## Configuración del entorno

Para ejecutar el proyecto localmente, sigue estos pasos:
1. Clona este repositorio:
   ```bash
   git clone https://github.com/SofiaMeroni/devops.git

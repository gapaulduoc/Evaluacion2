# Evaluacion2 - GraphHopper Mejorado-ESP

![Python](https://img.shields.io/badge/python-3670A0?style-for-the-badge&logo=python&logoColor=ffdd54)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style-for-the-badge&logo=github&logoColor=white)

Este repositorio contiene el script de Python mejorado para el proyecto con la **Biblioteca Nacional**. El programa calcula una ruta optimizada, mostrando la distancia, duración e instrucciones de viaje en español.

---

## Características Principales

* **Traducción Completa**: Toda la interacción con el usuario está en español.
* **Formato Preciso**: Los datos numéricos se muestran con un máximo de dos decimales.
* **Navegación Intuitiva**: Incluye una opción para salir del programa fácilmente (`s` o `salir`).
* **Instrucciones Claras**: La narrativa del viaje se obtiene y muestra en español.

---

## Cómo Empezar

Sigue estos pasos para poner en marcha el script.

### Prerrequisitos

* **Asegúrate de tener Python 3 instalado.** Para verificar si lo tienes, abre una terminal y ejecuta:
    ```bash
    python3 --version
    ```
    Si el comando devuelve una versión (ej. `Python 3.8.10`), ya está instalado. Si recibes un error, puedes instalarlo con el siguiente comando en sistemas Debian/Ubuntu:
    ```bash
    sudo apt update && sudo apt install python3
    ```
* Necesitarás la librería `requests`.

### Instalación y Configuración

1.  **Clona este repositorio:**
    ```bash
    git clone [https://github.com/gapaulduoc/Evaluacion2.git](https://github.com/gapaulduoc/Evaluacion2.git)
    cd Evaluacion2
    ```

2.  **Instala las dependencias:**
    ```bash
    pip install requests
    ```

3.  **Configura tu API Key:**
    * Abre el archivo `.py` en un editor de código.
    * Busca la línea: `GRAPHHOPPER_API_KEY = "TU_API_KEY_DE_GRAPHHOPPER"`
    * Reemplaza el texto `"TU_API_KEY_DE_GRAPHHOPPER"` con tu clave (token) de la API de Graphhopper.

---

## Ejecución

1.  Abre una terminal en la carpeta del proyecto.
2.  Ejecuta el script con el siguiente comando:
    ```bash
    python3 nombre_del_script.py
    ```
    *(Reemplaza `nombre_del_script.py` con el nombre real de tu archivo)*.

3.  ¡Listo! El programa te pedirá que introduzcas una dirección de origen para comenzar.

---

## Realizado por

* Gabriel Paul
* Vicente Medel

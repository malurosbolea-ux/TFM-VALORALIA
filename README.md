# 🏙️ Valoralia TFM: Sistema de Valoración Inmobiliaria Inteligente (SaaS)

> **Autora:** María Luisa Ros Bolea  
> **Proyecto:** Trabajo Fin de Máster (TFM) - Ingeniería de Datos e IA

Bienvenido al repositorio de despliegue de **Valoralia**. Este proyecto no es solo un modelo académico; es una arquitectura **Microservicios** completa lista para producción en la nube (AWS), diseñada para ofrecer tasaciones inmobiliarias precisas en Madrid mediante un enfoque híbrido (Deep Learning + Reglas de Negocio Expertas).

---

## 📂 Estructura del Repositorio (Mi "Kit de Despliegue")

Esta carpeta contiene todos los artefactos necesarios para levantar el servicio SaaS desde cero. Aquí explico qué es cada pieza de mi arquitectura:

### 1. 🎨 El Frontend (`app.py`)
Es la cara visible del producto. Desarrollado en **Streamlit**, ofrece una interfaz de usuario (UI) profesional y reactiva.
* **Función:** Recoge los datos del inmueble (superficie, zona, estado) y muestra la tasación final.
* **Lógica de Negocio:** Implementa *Guardrails* (filtros lógicos) que desarrollé para evitar "alucinaciones" del modelo en casos extremos (ej: impedir 5 baños en 30m²).
* **Ejecución:** `streamlit run app.py`

### 2. 🧠 El Backend (`main.py`)
El motor oculto. Una API RESTful de alto rendimiento construida con **FastAPI**.
* **Función:** Expone el modelo de IA al mundo exterior mediante endpoints seguros.
* **Escalabilidad:** Diseñado para soportar múltiples peticiones concurrentes, separando la lógica de cálculo de la interfaz visual.

### 3. 🐳 La Infraestructura (`Dockerfile`)
La receta de mi "máquina virtual".
* **Función:** Este archivo le dice a Amazon AWS (o cualquier nube) cómo construir el entorno exacto para que mi código funcione. Define el sistema operativo (Linux), instala Python y configura los puertos. ¡Es lo que hace que el proyecto sea "Cloud Native"!

### 4. 📦 Las Dependencias (`requirements.txt`)
La lista de ingredientes.
* **Contenido:** Todas las librerías necesarias (`pandas`, `numpy`, `scikit-learn`, `fastapi`, `uvicorn`, etc.) para que el entorno se replique sin errores en cualquier servidor del mundo.

### 5. 🤖 Los Cerebros (`.pkl`)
* **`modelo_valoralia_final.pkl`**: El modelo predictivo entrenado y serializado.
* **`scaler_X.pkl`**: El escalador matemático que normaliza los datos de entrada para que la red neuronal los entienda.

### 6. 📊 Los Datos (`dataset_INMOBILIARIO_FINAL.csv`)
* **Transparencia:** Adjunto el dataset procesado (anonimizado) que utilicé para validar las reglas de mercado, demostrando la base empírica de mi TFM.

---

## 🚀 Cómo Desplegar este Proyecto (Guía Rápida)

Para levantar el sistema completo en un entorno local o servidor:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/malurosbolea-ux/TFM-VALORALIA.git](https://github.com/malurosbolea-ux/TFM-VALORALIA.git)
    cd TFM-VALORALIA
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Lanzar la Aplicación (Frontend + Lógica Híbrida):**
    ```bash
    streamlit run app.py
    ```
    *El sistema abrirá automáticamente el navegador en `http://localhost:8501`.*

---

## 🏆 Puntos Clave para el Tribunal

* **Arquitectura Híbrida:** No confío ciegamente en la IA. He implementado una capa de **Reglas de Negocio** (Business Logic Layer) que valida la coherencia arquitectónica de los inputs antes de tasar.
* **Ready for Cloud:** Gracias a Docker y FastAPI, este proyecto es agnóstico de la infraestructura. Puede correr en AWS EC2, Google Cloud Run o Azure sin cambios en el código.
* **UX/UI Centric:** El diseño no es un añadido, es core. La interfaz está pensada para generar confianza en el usuario final (agentes inmobiliarios).

---
*Hecho con ❤️ y mucho código en Madrid.*

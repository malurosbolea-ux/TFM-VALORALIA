# 🏢 VALORALIA ENTERPRISE | TFM 2026

**Plataforma SaaS de Valoración Inmobiliaria Inteligente desplegada en AWS.**

Este repositorio contiene el código fuente de producción del TFM "Valoralia". El sistema utiliza modelos de Machine Learning (Random Forest) enriquecidos con lógica de negocio para tasar activos en Madrid y simular escenarios macroeconómicos (Crisis, Burbuja, Recesión).

## 🚀 Despliegue en Producción
El sistema se encuentra desplegado y operativo en una instancia **AWS EC2 (t3.micro)** bajo arquitectura Dockerizada.

- **URL Producción:** `http://13.62.247.160`
- **Tecnología:** Python 3.10, Streamlit, Scikit-Learn.
- **Infraestructura:** Amazon Web Services (Región eu-north-1).

## 🧠 Características Técnicas
1.  **Algoritmo Híbrido:** Random Forest Regressor calibrado con precios de mercado 2026.
2.  **Lógica Anti-Alucinación:** Capa de reglas de negocio que impide inputs incoherentes (ej. 5 habitaciones en 40m²).
3.  **Stress Testing:** Módulo de simulación financiera que aplica factores de corrección por escenarios de riesgo (-20% Crash).

## 📂 Estructura del Repositorio
- `/APP_DEPLOY`: Código fuente de la aplicación SaaS (Backend + Frontend).
- `/Notebooks`: Cuadernos de Jupyter con el análisis exploratorio (EDA) y pruebas de concepto.
- `/DATA`: Datasets crudos y procesados.

---
*Autor: María Luisa Ros Bolea | TFM Máster Big Data & AI*

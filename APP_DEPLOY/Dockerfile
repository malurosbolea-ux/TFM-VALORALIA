# Imagen base oficial de Python (Ligera)
FROM python:3.9-slim

# Directorio de trabajo
WORKDIR /app

# Copiar archivos de requisitos e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . .

# Ejecutar el entrenamiento del modelo al construir (para que el contenedor nazca "aprendido")
RUN python generar_modelo.py

# Exponer el puerto de Streamlit
EXPOSE 8501

# Comando de arranque
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

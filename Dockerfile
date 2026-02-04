FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
COPY main.py .
COPY modelo_valoralia_final.pkl .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

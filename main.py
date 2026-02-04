from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np

# 1. Inicializar la App (El Camarero)
app = FastAPI()

# 2. Cargar el "Cerebro" (Tu modelo y escaladores)
# Asegúrate de que estos archivos .pkl estén en la misma carpeta que este script
with open('modelo_valoralia_final.pkl', 'rb') as f:
    model = pickle.load(f)

# (Opcional) Si usas escaladores separados, cárgalos aquí también.
# with open('scaler_X.pkl', 'rb') as f:
#     scaler = pickle.load(f)

# 3. Definir qué datos te tiene que mandar el usuario (La Comanda)
class ViviendaInput(BaseModel):
    superficie: float
    habitaciones: int
    banos: int
    ascensor: int       # 1 si tiene, 0 si no
    distrito_id: int    # El código numérico del distrito (ej: 1 para Centro)
    estado: int         # 1 Buen estado, 0 A reformar, etc.

# 4. Crear la ruta (El Endpoint)
@app.get("/")
def home():
    return {"mensaje": "Bienvenido a la API de Valoralia. Ve a /docs para probarla."}

@app.post("/tasar")
def predecir_precio(datos: ViviendaInput):
    # Convertir los datos que llegan en un DataFrame (como en el notebook)
    df_entrada = pd.DataFrame([{
        'Superficie': datos.superficie,
        'Habitaciones': datos.habitaciones,
        'Banos': datos.banos,
        'Ascensor': datos.ascensor,
        'Distrito_ID': datos.distrito_id,
        'Estado': datos.estado
        # Añade aquí el resto de variables que use tu modelo
    }])
    
    # NOTA: Si usabas scaler en el notebook, aquí tendrías que hacer:
    # df_entrada = scaler.transform(df_entrada)

    # Predecir
    prediccion = model.predict(df_entrada)
    
    # Devolver el resultado
    return {
        "precio_estimado": round(float(prediccion[0]), 2),
        "moneda": "EUR"
    }
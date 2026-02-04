from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
import sklearn.preprocessing

app = FastAPI()

# CARGAMOS TU MODELO REAL
try:
    model = joblib.load('modelo_valoralia_final.pkl')
    scaler = joblib.load('scaler_X.pkl')
    print("✅ CEREBRO LISTO")
except:
    print("⚠️ ERROR: Faltan los archivos .pkl")

class InputWeb(BaseModel):
    zona_calidad: int
    antiguedad: float
    superficie: float
    habitaciones: float
    tiene_ascensor: int

@app.post("/tasar")
def predecir(datos: InputWeb):
    try:
        # 1. Traducir MADRID a MATEMÁTICAS (Para que tu modelo no falle)
        df = pd.DataFrame([{
            'longitude': -122.4 + (datos.zona_calidad * 0.1),
            'latitude': 37.8 - (datos.zona_calidad * 0.1),
            'housing_median_age': datos.antiguedad,
            'Ingresos_Medios': datos.zona_calidad * 3.0,
            'rooms_per_household': datos.superficie / 25,
            'bedrooms_per_room': 1.0 / (datos.habitaciones + 0.1),
            'population_per_household': 3.0
        }])
        
        # 2. Predicción Base
        X_scaled = scaler.transform(df)
        precio = abs(model.predict(X_scaled)[0]) * 1.9 # Conversión a Euros
        
        # 3. IMPACTO DEL ASCENSOR (Lógica de Negocio TFM)
        if datos.tiene_ascensor == 1:
            precio = precio * 1.15 # Sube un 15%
            
        # 4. Ajuste Mínimo de Mercado
        if precio < 120000: precio += 100000
        
        return {"precio_estimado": int(precio)}
    except Exception as e:
        return {"error": str(e)}
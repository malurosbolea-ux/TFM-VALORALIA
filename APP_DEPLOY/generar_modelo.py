import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# 1. Creamos datos falsos para entrenar un modelo tonto
datos = pd.DataFrame({
    'Superficie': [50, 80, 100, 150, 200],
    'Habitaciones': [1, 2, 3, 4, 4],
    'Banos': [1, 1, 2, 2, 3],
    'Ascensor': [1, 1, 0, 1, 1],
    'Distrito_ID': [1, 2, 3, 1, 2],
    'Estado': [1, 1, 2, 1, 1]
})
precio = [150000, 240000, 300000, 450000, 600000]

# 2. Entrenamos el modelo
print("🧠 Entrenando modelo de emergencia...")
model = LinearRegression()
model.fit(datos, precio)

# 3. Lo guardamos como .pkl
nombre_archivo = 'modelo_valoralia_final.pkl'
with open(nombre_archivo, 'wb') as f:
    pickle.dump(model, f)

print(f"✅ ¡LISTO! Se ha creado un archivo '{nombre_archivo}' nuevo y válido.")

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pickle

print("🧠 ENTRENANDO MOTOR VALORALIA 2026 (MERCADO REALISTA)...")

# PRECIOS BASE (Suelo de mercado actualizado)
precios_m2 = {
    'Salamanca': 11500, 'Chamberí': 9800, 'Chamartín': 9200, 'Centro': 9000, 'Retiro': 10000, 
    'Tetuán': 6500, 'Hortaleza': 5800, 'Fuencarral': 6000, 'Moncloa': 7800, 'Ciudad Lineal': 5500, 
    'Arganzuela': 6800, 'San Blas': 4500, 'Barajas': 4800, 'Usera': 3200, 'Puente de Vallecas': 3400, 
    'Villaverde': 3100, 'Carabanchel': 3600, 'Latina': 3700, 'Vicálvaro': 3500, 'Moratalaz': 4500, 
    'Villa de Vallecas': 3600
}
distritos_list = sorted(list(precios_m2.keys()))
dist_map = {k: v for v, k in enumerate(distritos_list)}

data = []
# Generación de 20.000 testigos sintéticos controlados
for _ in range(20000):
    dist_nombre = np.random.choice(distritos_list)
    d_id = dist_map[dist_nombre]
    p_base = precios_m2[dist_nombre]
    m = np.random.randint(30, 250)
    
    # Lógica Habitaciones
    if m < 45: h = 1
    elif m < 70: h = 2
    elif m < 100: h = 3
    else: h = 4
    
    # Lógica Baños
    max_b = h if m < 130 else h + 1
    b = np.random.randint(1, max_b + 1)
    
    # Extras
    asc = np.random.choice([0, 1], p=[0.1, 0.9])
    ext = np.random.choice([0, 1], p=[0.2, 0.8])
    ter = np.random.choice([0, 1], p=[0.6, 0.4])
    est = np.random.choice([0,1,2], p=[0.5, 0.3, 0.2])
    
    p = m * p_base
    
    # Impacto de Extras
    if asc == 0: p *= 0.85
    if ter == 1: p *= 1.12
    if ext == 0: p *= 0.92
    if est == 1: p *= 0.85 # A reformar
    if est == 2: p *= 1.25 # Obra nueva
    
    p *= np.random.uniform(0.98, 1.02)
    data.append([m, h, b, asc, ext, ter, 1 if est==0 else 0, 1 if est==1 else 0, 1 if est==2 else 0, d_id, p])

df = pd.DataFrame(data, columns=['m','h','b','asc','ext','ter','e0','e1','e2','d','p'])
model = RandomForestRegressor(n_estimators=60, max_depth=15, random_state=42).fit(df.iloc[:, :-1], df.iloc[:, -1])

pickle.dump(model, open('modelo_valoralia_final.pkl', 'wb'))
pickle.dump(dist_map, open('mapa_distritos.pkl', 'wb'))
print("✅ MODELO GENERADO Y GUARDADO CORRECTAMENTE")

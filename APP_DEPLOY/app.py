import streamlit as st
import pickle
import numpy as np
import os

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Valoralia Systems", layout="wide")

# ESTILOS CSS PROFESIONALES
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@500;700&display=swap');
    .stApp { background: linear-gradient(rgba(255,255,255,0.92), rgba(255,255,255,0.95)), url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=2670'); background-size: cover; background-attachment: fixed; }
    h1, h2, h3 { font-family: 'Oswald'; color: #0F172A !important; text-transform: uppercase; }
    .stSelectbox label p, .stNumberInput label p, .stSlider label p, .stCheckbox label p { color: #B91C1C !important; font-weight: 800; font-size: 14px; }
    section[data-testid='stSidebar'] { background-color: #0F172A; }
    section[data-testid='stSidebar'] * { color: white !important; }
    .stButton>button { background: #2563EB; color: white !important; font-weight: bold; width: 100%; padding: 15px; border: none; font-size: 18px; }
    .resultado-final { background-color: white; color: black; padding: 30px; border: 2px solid #0F172A; border-radius: 10px; box-shadow: 0 10px 30px rgba(0,0,0,0.15); margin-top: 20px; }
</style>
""", unsafe_allow_html=True)

# CARGA DE MODELOS (Con gestión de errores)
try:
    model = pickle.load(open('modelo_valoralia_final.pkl', 'rb'))
    dist_map = pickle.load(open('mapa_distritos.pkl', 'rb'))
except:
    st.error("Error crítico: No se encuentran los modelos 'modelo_valoralia_final.pkl' o 'mapa_distritos.pkl'. Ejecuta generar_modelo.py primero.")
    st.stop()

# SIDEBAR: PARAMETRIZACIÓN MACRO
st.sidebar.title("PARAMETRIZACIÓN")
esc = st.sidebar.radio("ESCENARIO MACRO:", ["ESTABILIDAD (Base)", "RECESIÓN (-10%)", "CRASH (-20%)", "BURBUJA (+15%)"])

# TÍTULO PRINCIPAL
st.markdown("<h1 style='font-size:55px; margin-bottom:0;'>VALORALIA <span style='color:#2563EB'>SYSTEMS</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#64748B; font-weight:bold; letter-spacing:2px; margin-top:-15px;'>REAL ESTATE INTELLIGENCE UNIT</p><hr>", unsafe_allow_html=True)

# COLUMNAS DE ENTRADA
c1, c2 = st.columns(2, gap="large")

with c1:
    dist = st.selectbox("DISTRITO", sorted(dist_map.keys()))
    m2 = st.number_input("METROS CUADRADOS", 30, 600, 90)
    
    # LÓGICA DE NEGOCIO (ANTI-ALUCINACIÓN)
    max_h = 1 if m2 < 45 else (2 if m2 < 70 else (3 if m2 < 100 else 5))
    if max_h > 1:
        hab = st.slider(f"HABITACIONES (Máx por m²: {max_h})", 1, max_h, min(3, max_h))
    else:
        st.info(f"HABITACIONES: 1 (Limitado por {m2}m²)")
        hab = 1
        
    max_b = hab if m2 < 130 else hab + 1
    if max_b > 1:
        ban = st.slider(f"BAÑOS (Máx lógico: {max_b})", 1, max_b, 1)
    else:
        st.info("BAÑOS: 1 (Limitado por lógica)")
        ban = 1

with c2:
    est_v = st.selectbox("ESTADO", ["Buen estado", "A reformar", "Obra Nueva"])
    st.markdown("<br>", unsafe_allow_html=True)
    k1, k2, k3 = st.columns(3)
    asc = k1.checkbox("ASCENSOR", True)
    ext = k2.checkbox("EXTERIOR", True)
    ter = k3.checkbox("TERRAZA", False)

# BOTÓN DE CÁLCULO
if st.button("CALCULAR TASACIÓN IA"):
    # Encoding variables categóricas
    e0 = 1 if est_v=="Buen estado" else 0
    e1 = 1 if est_v=="A reformar" else 0
    e2 = 1 if est_v=="Obra Nueva" else 0
    
    # Vector de características
    features = [[m2, hab, ban, 1 if asc else 0, 1 if ext else 0, 1 if ter else 0, e0, e1, e2, dist_map[dist]]]
    
    # Predicción base
    res = model.predict(features)[0]
    
    # Ajuste por Escenario Macro
    factor = 1.0
    if "RECESIÓN" in esc: factor = 0.90
    if "CRASH" in esc: factor = 0.80
    if "BURBUJA" in esc: factor = 1.15
    final = res * factor
    
    # VISUALIZACIÓN DE RESULTADOS
    st.markdown(f'''<div class="resultado-final">
    <div style="display:flex; justify-content:space-between; align-items:center;">
        <div><p style="color:#B91C1C; font-weight:900; margin:0;">VALORACIÓN IA</p><h1 style="font-size:60px; margin:0;">{final:,.0f} €</h1></div>
        <div style="text-align:right;"><p style="color:#B91C1C; font-weight:900; margin:0;">PRECIO m²</p><h3 style="font-size:28px;">{final/m2:,.0f} €/m²</h3></div>
    </div>
    <div style="margin-top:15px; border-top:1px solid #EEE; padding-top:10px; display:flex; justify-content:space-between;">
        <span style="font-weight:bold; color:#555;">MADRID 2026 | MODELO TFM</span>
        <span style="font-weight:bold; color:#000;">ESCENARIO: {esc.split('(')[0]}</span>
    </div></div>''', unsafe_allow_html=True)


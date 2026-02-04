import subprocess
import time
import sys

print("🚀 INICIANDO VALORALIA (CANAL 8008)...")

# 1. LIMPIEZA TOTAL DE PROCESOS (Matar todo lo que sea Python)
import os
if os.name == 'posix':
    os.system("pkill -f uvicorn")
    os.system("pkill -f streamlit")
    time.sleep(1)

# 2. INSTALAR LIBRERÍAS (Para asegurar)
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scikit-learn", "pandas", "joblib", "fastapi", "uvicorn", "streamlit"])
except:
    pass

# 3. ENCENDER CEREBRO EN PUERTO 8008 (NUEVO CANAL)
print("🧠 Encendiendo Cerebro (Puerto 8008)...")
backend = subprocess.Popen([sys.executable, "-m", "uvicorn", "main:app", "--reload", "--port", "8008"])

# 4. ESPERAR A QUE ARRANQUE
print("⏳ Esperando 5 segundos...")
time.sleep(5)

# 5. ABRIR WEB
print("💻 Abriendo Web...")
frontend = subprocess.Popen([sys.executable, "-m", "streamlit", "run", "app.py"])

print("✅ SISTEMA ONLINE EN PUERTO 8008.")
print("⚠️ NO CIERRES ESTA VENTANA NEGRA.")

try:
    backend.wait()
    frontend.wait()
except KeyboardInterrupt:
    backend.terminate()
    frontend.terminate()
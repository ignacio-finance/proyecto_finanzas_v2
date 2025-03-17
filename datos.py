import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Descargar datos de tasas de interés de EE.UU. desde Yahoo Finance
ticker = "^IRX"  # Treasury Bill 13 semanas (ejemplo)
data = yf.download(ticker, period="6mo", interval="1wk")

# Verificar los datos descargados
print(data.head())

# Guardar en un CSV para futuras referencias
data.to_csv("tasas_interes_api.csv")

# Graficar la evolución de la tasa de interés
plt.figure(figsize=(8,5))
plt.plot(data.index, data["Adj Close"], marker="o", linestyle="-", label="Tasa de interés")
plt.xlabel("Fecha")
plt.ylabel("Tasa de interés (%)")
plt.title("Evolución de la Tasa de Interés (Datos en Tiempo Real)")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()

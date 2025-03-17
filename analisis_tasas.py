
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Definir el ticker (símbolo financiero)
ticker = "^IRX"  # Treasury Bill 13 semanas

# Descargar los datos en tiempo real (últimos 6 meses, intervalos semanales)
data = yf.download(ticker, period="6mo", interval="1wk")

# Ver las columnas disponibles
print("📊 Columnas disponibles:", data.columns)
print(data.head())

# Graficar los datos
plt.plot(data.index, data["Close"], marker="o", linestyle="-", label="Tasa de interés")
plt.xlabel("Fecha")
plt.ylabel("Tasa de Interés (%)")
plt.title("Evolución de la Tasa de Interés (Datos en Tiempo Real)")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()

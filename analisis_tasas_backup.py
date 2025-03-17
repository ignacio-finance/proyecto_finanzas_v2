import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Descargar datos de tasas de interés
ticker = "^IRX"  # Treasury Bill 13 semanas
data = yf.download(ticker, period="6mo", interval="1wk")

# Seleccionar la columna correcta del MultiIndex
tasas_interes = data[("Close", "^IRX")]

# Graficar la evolución de la tasa de interés
plt.figure(figsize=(10, 5))
plt.plot(tasas_interes.index, tasas_interes, marker='o', linestyle='-', label="Tasa de interés")

# Formato del gráfico
plt.xlabel("Fecha")
plt.ylabel("Tasa de Interés (%)")
plt.title("Evolución de la Tasa de Interés (Datos en Tiempo Real)")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

# Mostrar gráfico
plt.show()

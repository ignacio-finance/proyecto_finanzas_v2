import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1️⃣ Descargar datos financieros
ticker = "^IRX"  # Treasury Bill 13 semanas (puedes cambiarlo por otro)
data = yf.download(ticker, period="6mo", interval="1wk")

# 2️⃣ Preprocesar datos
data = data.reset_index()
data["Date"] = data["Date"].map(lambda x: x.toordinal())  # Convertir fechas a números

X = data["Date"].values.reshape(-1, 1)  # Variable independiente (Fecha)
y = data["Close"].values  # Variable dependiente (Precio de cierre)

# 3️⃣ Aplicar Regresión Lineal
modelo = LinearRegression()
modelo.fit(X, y)

# 4️⃣ Hacer predicciones futuras
future_dates = np.array([X[-1] + i * 7 for i in range(1, 5)]).reshape(-1, 1)
predictions = modelo.predict(future_dates)

# 5️⃣ Graficar los resultados
plt.scatter(X, y, color="blue", label="Datos reales")
plt.plot(future_dates, predictions, "r--", label="Predicción")
plt.xlabel("Fecha (Ordinal)")
plt.ylabel("Valor")
plt.title("Regresión Lineal - Predicción Financiera")
plt.legend()
plt.show()

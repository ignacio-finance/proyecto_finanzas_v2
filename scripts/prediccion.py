import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos de ejemplo
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 6, 8, 10])

# Modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X, y)

# Predicción
X_pred = np.array([6, 7, 8]).reshape(-1, 1)
y_pred = modelo.predict(X_pred)

# Graficar resultados
plt.scatter(X, y, color='blue', label="Datos reales")
plt.plot(X_pred, y_pred, color='red', linestyle="dashed", label="Predicción")
plt.legend()
plt.xlabel("X")
plt.ylabel("y")
plt.title("Regresión Lineal - Predicción")
plt.show()

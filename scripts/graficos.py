import matplotlib.pyplot as plt
import seaborn as sns
from obtener_datos import obtener_datos

def graficar_datos(api_key, symbol):
    df = obtener_datos(api_key, symbol)

    # Configurar gráfico
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=df.index, y=df["4. close"], label="Precio de Cierre", color="blue")
    plt.title(f"Evolución del precio de {symbol}")
    plt.xlabel("Fecha")
    plt.ylabel("Precio")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    api_key = "TU_API_KEY"  # Reemplaza con tu API Key
    symbol = "AAPL"  # Cambia el símbolo si quieres otra empresa
    graficar_datos(api_key, symbol)

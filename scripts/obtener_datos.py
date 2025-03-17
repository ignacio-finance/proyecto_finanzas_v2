import requests
import pandas as pd

def obtener_datos(api_key, symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&outputsize=compact"
    response = requests.get(url)
    data = response.json()
    
    # Convertir a DataFrame
    df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient="index")
    df = df.astype(float)
    df.index = pd.to_datetime(df.index)

    return df

if __name__ == "__main__":
    api_key = "TU_API_KEY"
    symbol = "AAPL"
    df = obtener_datos(api_key, symbol)
    print(df.head())

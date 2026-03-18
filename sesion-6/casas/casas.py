import pandas as pd

df = pd.read_csv('casas.csv', skip_blank_lines=False)

cantidad_nulos = df["precios"].isnull().sum()

print(f"Cantidad de valores nulos en la columna 'precios': {cantidad_nulos}")

print(df.describe())
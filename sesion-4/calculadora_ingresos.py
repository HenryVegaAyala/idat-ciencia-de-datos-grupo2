import pandas as pd

df = pd.read_csv("compras.csv")

df["ingreso_total"] = df["cantidad"] * df["precio_unitario"]

df_ordenado = df.sort_values("ingreso_total", ascending=False)

print(df_ordenado)
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv("compras.csv")

df.rename(columns={"ciudad": "Provincia"}, inplace=True)

df.drop("total", axis=1, inplace=True)
df.drop("fecha", axis=1, inplace=True)
df.drop(["Provincia", "id_compra"], axis=1, inplace=True)

print(df)
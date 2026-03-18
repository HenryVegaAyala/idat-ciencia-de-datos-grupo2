import pandas as pd

df = pd.read_csv('mascotas.csv')

print(df["categoria"].mode().values[0])
print(df["precio"].mean())
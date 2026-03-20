import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("clientes.csv")

x = df[['gasto_anual', 'visitas_mes']]

kmeas = KMeans(n_clusters=2)
kmeas.fit(x)

grupo_1 = kmeas.predict(pd.DataFrame([[50, 1]], columns=['gasto_anual', 'visitas_mes']))
grupo_2 = kmeas.predict(pd.DataFrame([[10, 5]], columns=['gasto_anual', 'visitas_mes']))

print(f"Cliente bajo gasto asignado al grupo: {grupo_1[0]}")
print(f"Cliente vip gasto asignado al grupo: {grupo_2[0]}")
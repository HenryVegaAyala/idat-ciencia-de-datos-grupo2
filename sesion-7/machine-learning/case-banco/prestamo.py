import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("dato_credito.csv")

x = df[["ingreso", "morosidad"]]

y = df["aprobado"]

modelo = DecisionTreeClassifier()
modelo.fit(x, y)

prediccion_data = pd.DataFrame([[2800, 1]], columns=["ingreso", "morosidad"])
resultado = modelo.predict(prediccion_data)

if resultado[0] == 1:
    print("El crédito ha sido aprobado")
else:
    print("El crédito ha sido rechazado")

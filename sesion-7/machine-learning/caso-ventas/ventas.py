import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("regresion_logistica.csv")

x = df[["antiguedad", "cuota_mensual"]]

y = df["fuga"]

modelo = LogisticRegression()
modelo.fit(x, y)

prediccion_data = pd.DataFrame([[1, 30]], columns=["antiguedad", "cuota_mensual"])
resultado = modelo.predict(prediccion_data)

if resultado[0] == 1:
    print("El cliente va hacer churn")
else:
    print("El cliente se va a quedar con el servicio")

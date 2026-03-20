import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("regresion_multiple.csv")

x = df[['experiencia', 'estudios']]

y = df['salario']

modelo = LinearRegression()
modelo.fit(x, y)

# Hacemos las preguntas
prediccion_6 = pd.DataFrame([[4, 5]], columns=["experiencia", "estudios"])

resultado = modelo.predict(prediccion_6)
print(f"Salario sugerido: {resultado[0]:.2f}")

import pandas as pd
from sklearn.linear_model import LinearRegression

# 2. Leer archivo CSV
data = pd.read_csv("marketing.csv")

# Seleccionamos la columna Marketing como un dataFrame en lugar de una Serie "para que sea compatible con LinearRegression"
x = data[['marketing']]

# Seleccionamos la columna ventas como una serie
y = data['ventas']

# Comenzar a entrenar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(x, y) # Se entrena el modelo de datos con los resultados de Marketing (x) y ventas (y)

# Creamos el registro de predicción para el nuevo gasto en marketing
nueva_fila = pd.DataFrame([[6000]], columns=["marketing"])
prediccion = modelo.predict(nueva_fila)
print(f"La predicción de ventas para una nueva inversión de $6000 en marketing es: {prediccion[0]:.2f}")

# Creamos el registro de predicción para el nuevo gasto en marketing
nueva_fila = pd.DataFrame([[10000]], columns=["marketing"])
prediccion = modelo.predict(nueva_fila)
print(f"La predicción de ventas para una nueva inversión de $10000 en marketing es: {prediccion[0]:.2f}")
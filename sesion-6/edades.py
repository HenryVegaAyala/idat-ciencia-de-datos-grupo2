import pandas as pd

edades = pd.Series([10, 12, 10, 11, None, 85, 11])

mediana = edades.median()
print(f"La mediana de las edades es: {mediana}")

edades = edades.fillna(mediana)
print("Edades después de reemplazar los valores faltantes con la mediana:")
print(edades)

resultado = edades[edades <= 18]

print("Resultado faltantes:")
print(resultado)
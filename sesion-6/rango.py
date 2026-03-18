import pandas as pd

edades = pd.Series([15, 16, 17, 18, 19, 20])

rango = edades.max() - edades.min()

print("Rango de edades:", rango)
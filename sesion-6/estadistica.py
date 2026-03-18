import pandas as pd

edades = pd.Series([10, 15, 16, 17, 18, 19, 20])

mean = edades.mean()
median = edades.median()
mode = edades.mode()

print("Media:", mean)
print("Mediana:", median)
print("Moda:", mode.values[0])
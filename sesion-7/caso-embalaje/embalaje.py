import pandas as pd
import scipy.stats as st

df = pd.read_csv("puntaje.csv")

grupo_a = df[df["embalaje"] == "A"]["puntuacion"] # Cajas con embalaje Antiguo
grupo_b = df[df["embalaje"] == "B"]["puntuacion"] # Cajas con embalaje Nuevo

resultado = st.ttest_ind(grupo_a, grupo_b)

print(f"Resultado de la prueba t: {resultado.pvalue:.4f}")
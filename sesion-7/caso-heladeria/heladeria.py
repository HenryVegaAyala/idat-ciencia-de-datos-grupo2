import pandas as pd
import numpy as np
import scipy.stats as st

df = pd.read_csv("gastos.csv")
datos_gasto = df["gasto"]

# 2. Calcular el intervalo de confianza

intervalo = st.t.interval(
    confidence=0.95, # porcentaje de intervalo de confianza
    df=len(datos_gasto) - 1, # Ajuste de cantidad de datos
    loc=np.mean(datos_gasto), # El promedio
    scale=st.sem(datos_gasto) # escala
)

print(f"El cliente promedio gastará entre S/.{intervalo[0]} y S/.{intervalo[1]}")
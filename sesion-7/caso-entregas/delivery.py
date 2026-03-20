import pandas as pd
import numpy as np
import scipy.stats as st

df = pd.read_csv("tiempos.csv")

vehiculo_tradicional = df[df["vehiculo"] == "Tradicional"]["minutos"]
vehiculo_electrico = df[df["vehiculo"] == "Electrica"]["minutos"]

# Intervalo de confianza
ic = st.t.interval(
    confidence=0.95, # Porcentaje de intervalo de confianza 95%
    df=len(vehiculo_tradicional) - 1, # Cantidad de registros
    loc=np.mean(vehiculo_tradicional), # Promedio
    scale=st.sem(vehiculo_tradicional) # Escala
)

print(f"El tiempo promedio de entrega con vehículo tradicional es entre {ic[0]:.2f} y {ic[1]:.2f} minutos") # 28.2 minutos

ic = st.t.interval(
    confidence=0.95, # Porcentaje de intervalo de confianza
    df=len(vehiculo_electrico) - 1, # Cantidad de registros
    loc=np.mean(vehiculo_electrico), # Promedio
    scale=st.sem(vehiculo_electrico) # Escala
)

print(f"El tiempo promedio de entrega con vehículo electrico es entre {ic[0]:.2f} y {ic[1]:.2f} minutos") # 20 minutos

# 2 Pruebas de Test A/B
test = st.ttest_ind(vehiculo_tradicional, vehiculo_electrico)
print(f"El valor p de la prueba A/B es: {test.pvalue:.4f}")
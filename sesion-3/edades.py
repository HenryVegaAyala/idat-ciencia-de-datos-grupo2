import numpy as np

edades = [10, 25, 30, 18, 19, 60]

# Aplicar filtro con numpy
edades_array = np.array(edades)

filtrar_edades = edades_array >= 18
print(f"Edades filtradas (>= 18): {filtrar_edades}")

resultad = edades_array[filtrar_edades]
print(f"Edades resultantes: {resultad}")
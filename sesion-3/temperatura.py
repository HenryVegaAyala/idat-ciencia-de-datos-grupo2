import numpy as np

temperatura = [22, 21, 23, 90, 22, 20, 105, 21]
temp_array = np.array(temperatura)
filtro_temp = temp_array > 50

print(filtro_temp)

resultado = temp_array[filtro_temp]
print(resultado)

cantidad = resultado.size
print(f"Cantidad de temperaturas mayores a 50: {cantidad}")
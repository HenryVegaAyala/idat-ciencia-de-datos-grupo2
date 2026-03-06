import numpy as np

# Convetir de una lista a un array de numpy
lista = [10, 20, 30]
print(f"Lista original: {lista}")

array = np.array(lista)
print(f"Lista convertida: {array}")

# Generadores automáticos de números aleatorios
ceros = np.zeros(6)
print(f"Array de ceros: {ceros}")

unos = np.ones(7)
print(f"Array de unos: {unos}")

rangos = np.arange(0, 11, 2)
print(f"Array con rango: {rangos}")
import pandas as pd

datos = {
    "Nombres": ["Alice", "Bob", "Charlie"],
    "Edades": [25, 30, 35],
}

table = pd.DataFrame(datos)
print(table)
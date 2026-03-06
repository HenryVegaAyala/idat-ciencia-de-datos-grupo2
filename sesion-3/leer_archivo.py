import pandas as pd

df_csv = pd.read_csv("ventas_enero.csv")
print(df_csv["producto"])

df_txt = pd.read_csv("ventas_enero.txt", sep=";")
print(df_txt)

validar_si_cargo_bien = pd.read_csv("ventas_enero.csv")
print(validar_si_cargo_bien.head(2))

print("")

data_info = pd.read_csv("ventas_enero.csv")
print(data_info.info())

print("")

data_describe = pd.read_csv("ventas_enero.csv")
print(data_info.describe())
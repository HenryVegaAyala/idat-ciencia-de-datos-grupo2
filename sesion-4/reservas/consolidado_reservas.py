import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

reservas = pd.read_csv("reservas_enero.csv")
alojamientos = pd.read_csv("alojamineto_julio.csv")
tours = pd.read_csv("city_tours.csv")

reservas["tipo"] = "reserva"
alojamientos["tipo"] = "alojamiento"
tours["tipo"] = "tour"

consolidad = pd.concat([reservas, alojamientos, tours])

print(consolidad)
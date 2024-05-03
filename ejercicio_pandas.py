import pandas as pd

# Corrección de la estructura de la lista ventas_mensuales
ventas_mensuales = [
    {"mes": "Enero", "total_ventas": 15000, "año": 2023},
    {"mes": "Febrero", "total_ventas": 18000, "año": 2023},
    {"mes": "Marzo", "total_ventas": 22000, "año": 2023},
    {"mes": "Abril", "total_ventas": 19000, "año": 2023},
    {"mes": "Mayo", "total_ventas": 25000, "año": 2023},
    {"mes": "Junio", "total_ventas": 28000, "año": 2023},
    {"mes": "Julio", "total_ventas": 32000, "año": 2023},
    {"mes": "Agosto", "total_ventas": 30000, "año": 2023},
    {"mes": "Septiembre", "total_ventas": 28000, "año": 2023},
    {"mes": "Octubre", "total_ventas": 31000, "año": 2023},
    {"mes": "Noviembre", "total_ventas": 33000, "año": 2023},
    {"mes": "Diciembre", "total_ventas": 36000, "año": 2023},
    {"mes": "Enero 2", "total_ventas": 37000, "año": 2024},
    {"mes": "Febrero 2", "total_ventas": 38000, "año": 2024},
    {"mes": "Marzo 2", "total_ventas": 42000, "año": 2024},
    {"mes": "Abril 2", "total_ventas": 39000, "año": 2024},
    {"mes": "Mayo 2", "total_ventas": 45000, "año": 2024},
    {"mes": "Junio 2", "total_ventas": 48000, "año": 2024},
    {"mes": "Julio 2", "total_ventas": 52000, "año": 2024},
    {"mes": "Agosto 2", "total_ventas": 50000, "año": 2024},
    {"mes": "Septiembre 2", "total_ventas": 48000, "año": 2024},
    {"mes": "Octubre 2", "total_ventas": 51000, "año": 2024},
    {"mes": "Noviembre 2", "total_ventas": 55000, "año": 2024},
    {"mes": "Diciembre 2", "total_ventas": 58000, "año": 2024}
]

# Crea un DataFrame con los datos.
df = pd.DataFrame(ventas_mensuales)

# Agrega una columna para el trimestre.
trimestres = {"Primero": ["Enero", "Febrero", "Marzo"],
              "Segundo": ["Abril", "Mayo", "Junio"],
              "Tercero": ["Julio", "Agosto", "Septiembre"],
              "Cuarto": ["Octubre", "Noviembre", "Diciembre"]}

def asignar_trimestre(mes):
    for key, value in trimestres.items():
        if mes in value:
            return key

df["trimestre"] = df["mes"].apply(asignar_trimestre)

# Calcular el total de ventas por trimestre
ventas_trimestrales = df.groupby("trimestre")["total_ventas"].sum()

# Imprimir los totales de ventas por trimestre
print(ventas_trimestrales)














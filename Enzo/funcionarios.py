import pandas as pd

df = pd.read_excel('dados_funcionarios.xlsx')



# agrupar por registros e nome
resultado = df.groupby(["Registro", "Nome"])["Horas"].sum()

# Mostrando os resultados

for (registro, nome), horas in resultado.items():
    print(f"{registro} - {nome} - {horas} horas")
    
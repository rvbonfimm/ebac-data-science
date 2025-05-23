import pandas as pd
import numpy as np
from scipy import stats


pd.set_option('display.width', None)

df = pd.read_csv("data/clientes-v2-tratados.csv")

print(df.head())

# Transformação logarítmica (não entendi muito bem)
df["salario_log1p"] = np.log1p(df["salario"]) # log1p é usado p/ evitar problemas com valores zerados

# print(df["salario"].min())
# print(df["salario_log1p"].min())
print("\nDF after:\n", df.tail(15))

# Transformação Box-Cox
df["salario_boxbox"], _ = stats.boxcox(df["salario"] + 1) # + 1 caso tenha algum valor negativo

print("\nDF after Box-Cox:\n", df.head())

# Codificação de frequência para 'estado'
estado_freq = df["estado"].value_counts() / len(df)
df["estado_fre"] = df["estado"].map(estado_freq)

print("\nDF after frequency:\n", df.head())

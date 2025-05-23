"""
    Script for data normalization and standardization
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler


pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv("data/clientes-v2-tratados.csv")

# print(df.head())

# Filter columns
df = df[["idade", "salario"]]
# Could be df = df.drop([...], axis=1)

# Normalização - MinMaxScaler
scaler = MinMaxScaler()
df["idade_scaler"] = scaler.fit_transform(df[["idade"]])
df["salario_scaler"] = scaler.fit_transform(df[["salario"]])

scaler_featured = MinMaxScaler(feature_range=(-1, 1))
df["idade_scaler_featured"] = scaler_featured.fit_transform(df[["idade"]])
df["salario_scaler_featured"] = scaler_featured.fit_transform(df[["salario"]])

# print(df.head())

# Padronização
scaler = StandardScaler()
df["idade_std_scaler"] = scaler.fit_transform(df[["idade"]])
df["salario_std_scaler"] = scaler.fit_transform(df[["salario"]])

# Padronização - RobustScaler
scaler = RobustScaler()
df["idade_robust_scaler"] = scaler.fit_transform(df[["idade"]])
df["salario_robust_scaler"] = scaler.fit_transform(df[["salario"]])

# print(df.head(15))

print("\nMinMaxScaler (De 0 a 1:")
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(df["idade_scaler"].min(), df["idade_scaler"].max(), df["idade_scaler"].mean(), df["idade_scaler"].std()))
print("Salário - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(df["salario_scaler"].min(), df["salario_scaler"].max(), df["salario_scaler"].mean(), df["salario_scaler"].std()))

print("\nStandardScaler (Ajuste a Média a 0 e Desvio Padrão a 1")
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.18f} Std: {:.4f}".format(df["idade_std_scaler"].min(), df["idade_std_scaler"].max(), df["idade_std_scaler"].mean(), df["idade_std_scaler"].std()))
print("Salário - Min: {:.4f} Max: {:.4f} Mean: {:.18f} Std: {:.4f}".format(df["salario_std_scaler"].min(), df["salario_std_scaler"].max(), df["salario_std_scaler"].mean(), df["salario_std_scaler"].std()))

print("\nRobustScaler (Ajuste a Mediana e IQR")
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(df["idade_robust_scaler"].min(), df["idade_robust_scaler"].max(), df["idade_robust_scaler"].mean(), df["idade_robust_scaler"].std()))
print("Salário - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(df["salario_robust_scaler"].min(), df["salario_robust_scaler"].max(), df["salario_robust_scaler"].mean(), df["salario_robust_scaler"].std()))

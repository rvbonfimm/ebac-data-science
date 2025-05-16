import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)

df = pd.read_csv("data/clientes-v2-tratados.csv")

print(df.head(), "\n")

# Codificação one-hot para o estado civil
df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix="estado_civil")], axis=1)

print("\nDF após codificação one-hot para 'estado_civil':\n", df.head())

# Codificação ordinal para 'nivel_educacao'
educacao_ordem = {"Ensino Fundamental": 1, "Ensino Médio": 2, "Ensino Superior": 3, "Pós-graduação": 4}
df["nivel_educacao_ordinal"] = df["nivel_educacao"].map(educacao_ordem)

print(df.head(), "\n")

# Gera automaticamente os códigos correspondentes para cada item de uma categoria
# Sem a necessidade de atuar manualmente como na linha 16, 17
df["area_atuacao_cod"] = df["area_atuacao"].astype("category").cat.codes

# labelEncoder para 'estado'
# Converte cada valor único em números de 0 a n_classes-1
label_encoder = LabelEncoder()
df["estado_cod"] = label_encoder.fit_transform(df["estado"])

print("\nDF final:\n", df.head(), "\n")

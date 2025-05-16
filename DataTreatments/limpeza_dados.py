import pandas as pd
#import sys


df = pd.read_csv("clientes.csv")

pd.set_option("display.width", None)
pd.set_option("display.max_columns", None)
print(df.head())
print(df.shape)

# Remover dados
df.drop("country", axis=1, inplace=True) # Remover Coluna
df.drop(2, axis=0, inplace=True) # Remover Linha

# Normalizar campos de texto
df["name"] = df["name"].str.strip().str.title() # Capitalize
df["address"] = df["address"].str.lower()
df["state"] = df["state"].str.strip().str.upper()

# Converter tipo de dados
df["age"] = df["age"].astype(int)

print("Normalizar textos", df.head())

# Tratar valores nulos (ausentes)
df_fillna = df.fillna('') # Substituir valores nulos por vazio
df_dropna = df.dropna() # Remover registros com valores nulos (coluna a coluna, não toda a linha)

# Keep only the rows with at least X non-NA values
# Uma estratégia pode ser de removermos o registro caso 50% das colunas sejam nulas
fifth_percent_columns = (df.shape[1] * 50) / 100
df_dropna_thresh = df.dropna(thresh=fifth_percent_columns)
df = df.dropna(subset=["cpf"]) # Remover registros com CPF nulos

print("\nNull values: ", df.isnull().sum())
print("Fillna Null values: ", df_fillna.isnull().sum().sum())
print("Dropna Null values: ", df_dropna.isnull().sum().sum())
print("Thresh Dropna Null values: ", df_dropna_thresh.isnull().sum().sum())
print("Null CPFs: ", df.isnull().sum().sum())

# Fulfill null data
df.fillna({ "state": "Desconhecido"}, inplace=True)
df["address"] = df["address"].fillna("Endereço não informado")

df["age_fixed"] = df["age"].fillna(df["age"].mean()) # Set the average age
df["birthday_fixed"] = pd.to_datetime(df["birthday"], format="%Y-%m-%d", errors="coerce")

# Tratar dados duplicados
print("Rows: ", df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset=['cpf'], inplace=True)
print("After Drop Duplicates Rows: ", len(df))

print("Cleaned dataframe:\n", df)

# Save new data frame
df["birthday"] = df["birthday_fixed"]
df["age"] = df["age_fixed"]

df_salvar = df[["name", "cpf", "age", "birthday", "address", "state"]]
df_salvar.to_csv("clientes-cleaned.csv", index=False)

export_filename = "clientes-cleaned.csv"
print("New data frame: \n", pd.read_csv(export_filename))
print(f"CSV Exported Successfully: {export_filename}")

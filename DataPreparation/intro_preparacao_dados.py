import pandas as pd


df = pd.read_csv("data/clientes-v2.csv")

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

print(df.head().to_string() + "\n")
print(df.tail().to_string())

df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y", errors="coerce")

print("Verificação inicial: ")
print(df.info())

print("\nDados nulos:\n", df.isnull().sum())
print("% de dados nulos:\n", df.isnull().mean() * 100) # also could be df.isnull().sum() / len(df) * 100
df.dropna(inplace=True)
print("DF after dropna:", df.isnull().sum().sum())

print("\nAnalise de dados duplicados:\n", df.duplicated().sum())
print("\nAnalise de dados únicos:\n", df.nunique())
print("\nEstatística dos dados:\n", df.describe())

# Filter only needed fields to the data analysis
df = df[["idade", "data", "estado", "salario", "nivel_educacao", "numero_filhos", "estado_civil", "area_atuacao"]]
print("\nDF final:\n", df.head().to_string() + "\n")
df.to_csv("data/clientes-v2-tratados.csv", index=False)
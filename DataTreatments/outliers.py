import pandas as pd
from scipy import stats


pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv("dados/clientes-cleaned.csv")
df_filtered = df[df["age"] > 100]

print("Basic filter: ", df_filtered[["name", "age"]])

# identify outliers with statistics lib, the Z-score
z_scores = stats.zscore(df["age"].dropna())

# Identify outliers with IQR
# Interquartile Range, ou Amplitude Interquartil
# É uma medida estatística que representa a dispersão dos 50% centrais de um conjunto de dados
Q1 = df["age"].quantile(q=0.25)
Q3 = df["age"].quantile(q=0.75)
IQR = Q3 - Q1

low_limit = Q1 - 1.5 * IQR
high_limit = Q3 + 1.5 * IQR

print("IQR Limit: ", low_limit, high_limit)

outliers_iqr = df[(df["age"] < low_limit) | (df["age"] > high_limit)]
print("Outliers by IQR: ", outliers_iqr)

# Filter outliers with IQR
df_iqr = df[(df["age"] >= low_limit ) & (df["age"] <= high_limit)]
print("Outliers by IQR: ", df_iqr)

# Filter outliers manually
low_limit = 1
high_limit = 100
df = df[(df["age"] >= low_limit ) & (df["age"] <= high_limit)]
print("Outliers manually: ", df_iqr)

# Filter by invalid addresses
df["address"] = df["address"].apply(lambda x: "Endereço inválido" if len(x.split("\n")) < 3 else x)
print("Invalid addresses: ", (df["address"] == "Endereço inválido").sum())

# Treat text fields
df["name"] = df["name"].apply(lambda x: "Nome inválido" if isinstance(x, str) and len(x) > 50 else x)
print("Invalid names: ", (df["name"] == "Nome inválido").sum())

print("Treated Outliers dataframe: ", df)

export_filename = "dados/clientes-out-of-outliers.csv"
print(f"CSV Exported Successfully: {export_filename}")
df.to_csv(export_filename, index=False)

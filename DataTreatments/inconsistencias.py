import pandas as pd
import numpy as np
import json
import os

from gera_base_clientes import export_filename

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv("clientes-out-of-outliers.csv")

# To mask personal data
df["cpf_masked"] = df["cpf"].apply(lambda cpf: f"{cpf[:3]}.***.***-{cpf[-2:]}")

# print(df.head())
# Fix dates
df["birthday"] = pd.to_datetime(df["birthday"], format="%Y-%m-%d", errors="coerce")

actual_date = pd.to_datetime("today")
minimal_base_datetime = "1900-01-01"
df["date_updated"] = df["birthday"].where(df["birthday"] <= actual_date, pd.to_datetime(minimal_base_datetime))
df["age_adjusted"] = actual_date.year - df["date_updated"].dt.year # Year adjust
df["age_adjusted"] -= ((actual_date.month <= df["date_updated"].dt.month) & (actual_date.day < df["date_updated"].dt.day)).astype(int) # Day adjust
df.loc[df["age_adjusted"] > 100, "age_adjusted"] = np.nan # Set age > 100 to NaN

# print(df.head())
df["address_only"] = df["address"].apply(lambda address: address.split("\n")[0].strip())
df["neighborhood"] = df["address"].apply(lambda address: address.split("\n")[1].strip() if len(address.split("\n")) > 1 else "Desconhecido")
df["state_abbreviation"] = df["address"].apply(lambda address: address.split(" / ")[-1].strip() if len(address.split("\n")) > 1 else "Desconhecido")

# Check address data format
df["address_only"] = df["address_only"].apply(lambda address: "Endereço inválido" if len(address) > 50 or len(address) < 5 else address)

# Fix wrong data
df["cpf"] = df["cpf"].apply(lambda cpf: cpf if len(cpf) == 14 else "CPF inválido")

json_file = "./utils/brazil-states-list.json"
abs_path = os.path.abspath(json_file)
json_data = None
with open(abs_path, encoding="utf-8", mode="r") as json_file:
    json_data = json.load(json_file)

only_state_abbreviations = list(json_data.keys())
df["state_abbreviation"] = df["state_abbreviation"].str.upper().apply(lambda state: state if state in only_state_abbreviations else "Desconhecido")

print("Dados tratados: ", df.head())

# Replace formated fields
df["cpf"] = df["cpf_masked"]
df["age"] = df["age_adjusted"]
df["address"] = df["address_only"]
df["state"] = df["state_abbreviation"]
df_salvar = df[["name", "cpf", "age", "birthday", "address", "neighborhood", "state"]]

# df.info()
print(df.dtypes)

# export_filename = "clientes-tratados.csv"
# df_salvar.to_csv(export_filename, index=False)
# print("Novo DataFrame: \n", pd.read_csv(export_filename))
# print("CSV Exported Successfully", export_filename)

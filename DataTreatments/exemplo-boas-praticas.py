import pandas as pd

# Carregar dados de um arquivo CSV
df = pd.read_csv('dados.csv')

# Visualizar os primeiros registros
print(df.head())

# Verificar a quantidade de linhas e colunas
print(df.shape)

# Verificar tipos de dados e valores nulos
print(df.info())

# Remover colunas desnecessárias
df = df.drop(columns=['coluna_desnecessaria'])

# Padronizar campos de texto
df['nome'] = df['nome'].str.title()

# Tratar valores nulos
df['idade'] = df['idade'].fillna(df['idade'].mean())

# Converter tipos de dados
df['data'] = pd.to_datetime(df['data'])

# Salvar o dataset limpo em um novo arquivo CSV
df.to_csv('dados_limpos.csv', index=False)

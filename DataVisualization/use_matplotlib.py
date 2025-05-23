import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("data/clientes-v3-preparado.csv")
print(df.head(20).to_string())

# Gráfico de barras
plt.figure(figsize=(10, 6))
df["nivel_educacao"].value_counts().plot(kind="bar", color="#90ee70")
plt.title("Divisão de Escolaridade")
plt.xlabel("Nível de Educação")
plt.ylabel("Quantidade")
plt.xticks(rotation=0)
plt.show()

x = df["nivel_educacao"].value_counts().index
y = df["nivel_educacao"].value_counts().values

plt.figure(figsize=(10, 6))
plt.bar(x, y, color="#60aa65")
plt.title("Gráfico 2 - Divisão de Escolaridade")
plt.xlabel("Nível de Educacao")
plt.ylabel("Quantidade")

# Gráfico de Pizza
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct="%.1f%%", startangle=90)
plt.title("Distribuição de Nível de Educação")
plt.show()

# Gráfico de Dispersão
plt.hexbin(df["idade"], df["salario"], gridsize=40, cmap="Blues")
plt.colorbar(label="Contagem dentro do bin")
plt.xlabel("Idade")
plt.ylabel("Salário")
plt.title("Dispersão de Idade e Salário")
plt.show()

# Criar o gráfico de pizza
plt.figure(figsize=(8, 8))
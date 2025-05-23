import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv("data/clientes-v3-preparado.csv")
print(df.head(20).to_string())

# Dispersão
sns.jointplot(x="idade", y="salario", data=df, kind="scatter")
plt.show()

# Densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df.salario, fill=True, color="#863e9c", )
plt.title("Densidade de Salários")
plt.xlabel("Salário")
plt.ylabel("Densidade")
plt.show()

# Gráfico de Pairplot - Dispersão e Histograma
# Exibe apenas números, logo, filtra o nivel_educacao por ser texto
sns.pairplot(df[["idade", "salario", "anos_experiencia", "nivel_educacao"]])
plt.show()

# Gráfico de regressão
sns.regplot(x="idade", y="salario", data=df, color="#278f65", scatter_kws={"alpha": 0.5, "color": "#34c289"})
plt.title("Regressão de Salário por Idade")
plt.xlabel("Idade")
plt.ylabel("Salário")
plt.show()

# Gráfico countplot com hue
sns.countplot(x="estado_civil", hue="nivel_educacao", data=df, palette="pastel")
plt.legend(title="Nível de Educação")
plt.xlabel("Estado Civil")
plt.ylabel("Quantidade de Clientes")
plt.show()

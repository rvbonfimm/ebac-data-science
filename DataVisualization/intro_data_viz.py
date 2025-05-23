import matplotlib.pyplot as plot
import pandas as pd
import seaborn as sns

df = pd.read_csv("data/clientes-v3-preparado.csv")
print(df.head().to_string())

# plot.hist(df["salario"])
# plot.show()

# First graph
plot.figure(figsize=(10, 6))
plot.hist(df["salario"], bins=100, color="green", alpha=0.8)
plot.title("Histograma - Distribuição de Salários")
plot.xlabel("Salario")
plot.xticks(ticks=range(0, int(df["salario"].max()) + 2000, 2000)) # De 0 até o máximo + 2k, andando de 2 em 2k
plot.ylabel("Frequência")
plot.grid(True)
plot.show()

# Múltiplos gráficos
plot.figure(figsize=(10, 6))
plot.subplot(2, 2, 1)

# Gráfico de Dispersão
plot.scatter(x=df["salario"], y=df["salario"])
plot.title("Dispersão - Salário e Salário")
plot.xlabel("Salario")
plot.ylabel("Salario")
plot.show()

plot.subplot(2, 2, 2) # 1 Linha, 2 Colunas, 2º gráfico

# colors="#5883a8"
plot.scatter(x=df["salario"], y=df["anos_experiencia"], alpha=0.6, s=30)
plot.title("Dispersão - Idade e Anos de XP")
plot.xlabel("Salario")
plot.ylabel("Anos de XP")
plot.show()

# Mapa de calor
corr = df[["salario", "anos_experiencia"]].corr()
plot.subplot(2, 2, 3) # 1 Linha, 2 Colunas, 3º gráfico
sns.heatmap(corr, annot=True, cmap="coolwarm")
plot.title("Correlação Salário e Idade")

plot.tight_layout()
plot.show()

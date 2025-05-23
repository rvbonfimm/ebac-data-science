import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


df = pd.read_csv("data/clientes-v3-preparado.csv")
print(df.head(20).to_string())

df_corr = df[["salario", "idade", "anos_experiencia", "numero_filhos", "nivel_educacao_cod", "area_atuacao_cod", "estado_cod"]].corr()

# Heatmap de correlação
plt.figure(figsize=[10,8])
sns.heatmap(df_corr, annot=True, cmap="Greens", fmt=".2f")
plt.title("Mapa de Calor - Correlação entre Variáveis")
plt.show()

# Countplot
sns.countplot(x="estado_civil", data=df)
plt.title("Distribuição do Estado Civil")
plt.xlabel("Estado Civil")
plt.ylabel("Contagem")
plt.show()

# Countplot com Legenda
sns.countplot(x="estado_civil", hue="nivel_educacao", data=df)
plt.title("Distribuição do Estado Civil")
plt.xlabel("Estado Civil")
plt.ylabel("Contagem")
plt.legend(loc="upper right", title="Nível de Educação")
plt.show()

x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)

plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar()  # Adiciona uma barra de cores para referência
plt.title('Gráfico de Dispersão com cmap')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.show()

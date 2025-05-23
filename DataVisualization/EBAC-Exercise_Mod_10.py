import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""
  Adicionando alguns campos para o data frame
"""


def normalize_data(input_df: pd.DataFrame):
    # Filtrar campos desnecessários
    input_df.drop(labels=["Unnamed: 0", "Review1", "Review2", "Review3"], axis=1, inplace=True)

    # Gerar o campo Gênero Código automático
    input_df["Gênero_Cod"] = df["Gênero"].astype("category").cat.codes

    # Criar o campo Total_Vendas
    input_df["Total_Vendas"] = df["Preço"] * df["Qtd_Vendidos_Cod"]

    # Preencher o campo Total_Vendas nulo com 0
    input_df["Total_Vendas"].fillna(0)

    # Filtrar campos
    input_df.drop(labels=["Qtd_Vendidos"], axis=1, inplace=True)

    return input_df


"""
  Gráficos
  - Vendas por produto/marca/material/temporada
  - Notas por produto/marca/material
  - Nº avaliações por produto/marca/material
"""


def show_graphs():
    """
      Gráfico de Histograma ✅
      Gráfico de Dispersão ✅
      Mapa de calor (Heatmap) ✅
      Gráfico de Barra
      Gráfico de Pizza ✅
      Gráfico de Densidade ✅
      Gráfico de Regressão ✅
    """

    # Create multiple graphs
    fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(16, 16))

    plt.subplots_adjust(left=0.1,
                        bottom=0.1,
                        right=0.7,
                        top=0.9,
                        wspace=0.5,
                        hspace=0.5)

    # Gráfico de Histograma (# Preço dos produtos)
    # print("Histograma >>>: ", int(df["Preço"].max()))
    axes[0, 0].hist(df["Preço"], bins=10, color="green", alpha=0.8)
    axes[0, 0].set_title("Histograma - Distribuição de Preço dos produtos")
    axes[0, 0].set_xlabel("Preço")
    axes[0, 0].set_xticks(ticks=range(0, int(df["Preço"].max()) + 100, 50))
    axes[0, 0].set_ylabel("Frequência")
    axes[0, 0].grid(True)

    # Gráfico de Dispersão - Matplotlib (# Preço por Preço)
    axes[0, 1].scatter(x=df["Preço"], y=df["Preço"], alpha=0.6, s=30)
    axes[0, 1].set_title("Dispersão de Preço dos produtos")
    axes[0, 1].set_xlabel("Preço")
    axes[0, 1].set_ylabel("Preço")
    axes[0, 1].grid(True)

    # Gráfico de Calor - Heatmap (# Preço X Desconto)
    corr = df[["Preço", "Desconto"]].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=axes[1, 0])
    axes[1, 0].set_title("Correlação de Preço e Desconto")

    # Gráfico de Calor - Heatmap (# Qtd_Vendidos_Cod X Marca_Freq)
    corr = df[["Qtd_Vendidos_Cod", "Marca_Freq"]].corr()
    sns.heatmap(corr, annot=True, cmap="Reds", ax=axes[1, 1])
    axes[1, 1].set_title("Correlação de Itens Vendidos com a Marca")

    # Gráfico de barras (# Top 5 vendas por produto)
    df_filtered = df.sort_values(by="Total_Vendas", ascending=False)[:10]

    x_axis = df["Marca_Cod"].value_counts().index
    y_axis = df["Marca_Cod"].value_counts().values
    axes[2, 0].bar(x_axis, y_axis, color="#60aa65")
    axes[2, 0].set_title("Marca_Cod")
    axes[2, 0].set_xlabel("Marca_Cod")
    axes[2, 0].set_ylabel("Quantidade")

    # Gráfico de pizza (# Notas)
    notas_axis_x = df["Nota"].value_counts().index
    notas_axis_y = df["Nota"].value_counts().values
    axes[2, 1].pie(notas_axis_y, labels=notas_axis_x, autopct="%.1f%%", startangle=45, pctdistance=1.15, labeldistance=.5)
    axes[2, 1].set_title("Gráfico Pizza / Distribuição de Notas por produto")

    # Gráfico de Densidade (sns.kdeplot)
    sns.kdeplot(data=df, x="Preço", fill=True, color="#863e9c", ax=axes[3, 0])
    axes[3, 0].set_title("Densidade de Preços")
    axes[3, 0].set_xlabel("Preço")
    axes[3, 0].set_xlabel("Densidade")

    # Gráfico de regressão
    sns.regplot(x="Qtd_Vendidos_Cod", y="Gênero_Cod", data=df, ax=axes[3, 1])
    axes[3, 1].set_title("Regressão de Itens vendidos por Gênero")
    axes[3, 1].set_xlabel("Itens vendidos")
    axes[3, 1].set_ylabel("Gênero")

    plt.tight_layout()
    plt.show()


def data_exploration():
    print(df.info())
    print(df.head(20))

    titulos = df["Título"].unique()
    qtd_titulos = len(titulos)
    print(f"'{qtd_titulos}' produtos vendidos")

    generos = df["Gênero"].unique()
    qtd_generos = len(generos)
    print(f"'{qtd_generos}' gêneros")

    marcas = df["Marca"].unique()
    qtd_marcas = len(marcas)
    print(f"'{qtd_marcas}' marcas vendidas")

    materiais = df["Material"].unique()
    qtd_materiais = len(materiais)
    print(f"'{qtd_materiais}' materiais vendidas")

    temporadas = df["Temporada"].unique()
    qtd_temporadas = len(temporadas)
    print(f"'{qtd_temporadas}' temporadas vendidas")

    notas = df["Nota"].value_counts()  # Frequência das notas de 0 a 5.0
    print(f"{notas}")

    n_avaliacoes = df["N_Avaliações"].value_counts().sort_index()  # Avaliações
    print(f"{n_avaliacoes}")


pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv("data/ecommerce_preparados.csv")
df = normalize_data(df)

show_graphs()
# data_exploration()

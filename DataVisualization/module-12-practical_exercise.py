import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

data = {
    'Nome': ['Alice', 'Joao', 'Charlie', 'David', 'Eva', 'Diego', 'Denize', 'Claudio'],
    'Idade': [25, 30, 35, 40, 45, 60, 22, 24],
    'Profissão': ['Engenheiro', 'Médico', 'Professor', 'Advogado', 'Médico','Engenheiro', 'Estudante','Estudante'],
    'Salário': ['4500', '8000', '5000', '10000', '12000','15000', '1200','1500'],
    'Limite_Credito': ['2500', '4000', '4000', '1000', '10000','2000', '500','250'],
    'Historico_Inadimplencia': ['0', '0', '0', '1', '0','1', '0','1'],
    'Estado_Civil': ['Casamento', 'Casamento', 'Solteiro', 'Solteiro', 'Casamento','Solteiro', 'Solteiro','Solteiro'],
    'Imovel_Proprio': ['0', '0', '0', '1', '1','1', '0','0']
}

df = pd.DataFrame(data)

df['Salário'] = df['Salário'].astype(int)
df['Limite_Credito'] = df['Limite_Credito'].astype(int)
df['Historico_Inadimplencia'] = df['Historico_Inadimplencia'].astype(int)
df['Imovel_Proprio'] = df['Imovel_Proprio'].astype(int)

df.head(10)

# Gráfico de Pizza (pie)

profissao_por_hist_inadimplencia = (
    df
    .groupby(['Profissão', 'Historico_Inadimplencia'])['Limite_Credito']
    .mean()
    .reset_index()
    .sort_values(by='Limite_Credito', ascending=True)
)

fig1 = px.pie(profissao_por_hist_inadimplencia, names='Historico_Inadimplencia', values='Limite_Credito', title='Limite de Crédito por Hist. Inadimplência',
            labels={'Limite_Credito': 'Limite de Crédito', 'Historico_Inadimplencia': 'Hist. Inadimplência'},
            color='Limite_Credito')

fig1.update_traces(texttemplate='Limite Créd.: %{value:0.2f} <br>(%{percent})')
fig1.update_layout(legend_traceorder="reversed")
fig1.update_traces(textposition='inside')
fig1.update_layout(legend=dict(
    yanchor="top",
    y=1,
    xanchor="left",
    x=0.25
))
fig1.update_layout(font_size=15)

fig1.show()

# Gráfico de Dispersão (Scatter)
fig2 = px.scatter(df, x='Limite_Credito', y='Salário', title='Limite de Crédito por Salário',
                 size='Limite_Credito',
                 labels={'Limite_Credito': 'Limite de Crédito', 'Salário': 'Salário'})

fig2.show()

# Pairplot
sns.pairplot(df[["Salário", "Limite_Credito", "Historico_Inadimplencia", "Imovel_Proprio"]])

plt.show()
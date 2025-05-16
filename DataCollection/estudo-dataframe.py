import pandas

dados = [
    {'nome': 'Roger', 'email': 'roger@gmail.com'},
    {'nome': 'Frederick', 'email': 'fred@live.com'},
    {'nome': 'Ana', 'email': 'ana-sazack@hotmail.com'},
]
df = pandas.DataFrame(dados)
print(df)
import pandas as pd


df = pd.DataFrame({
    'numeros': [1,2,3,4,5,10]
})
df['valor_ao_cubo'] = df['numeros'].apply(lambda x : x**3)
print(df)

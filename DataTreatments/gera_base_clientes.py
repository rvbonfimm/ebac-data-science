from faker import Faker
import pandas as pd
import random


fake = Faker(locale="pt_BR")

rows = []
for _ in range(1027):
    name = fake.name()
    cpf = fake.cpf()
    age = random.randint(18, 60)
    birthday = fake.date_of_birth(minimum_age=18, maximum_age=60)
    address = fake.address()
    state = fake.state()
    country = fake.country()
    rows.append({
        "name": name,
        "cpf": cpf,
        "age": age,
        "birthday": birthday,
        "address": address,
        "state": state,
        "country": country
    })

df = pd.DataFrame(rows)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.width', None)
#print(df.head())

export_filename = "clientes.csv"
df.to_csv(export_filename, index=False)
print(f"File exported successfully - {export_filename}")

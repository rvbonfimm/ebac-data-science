import requests
from bs4 import BeautifulSoup
import pandas

# Requests

# url = "https://finance.yahoo.com/quote/%5EBVSP/history/"
url = "https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/"
response = requests.get(url)
# print(response.text)

# BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

# Pandas
pandas_html = pandas.read_html(url)
print(pandas_html[0].head(5))
